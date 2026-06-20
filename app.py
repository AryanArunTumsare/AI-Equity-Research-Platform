import streamlit as st
import pandas as pd
import yfinance as yf
from google import genai
from pypdf import PdfReader
from io import BytesIO
import os

# =========================
# CONFIG
# =========================

st.set_page_config(
    page_title="AI Equity Research Platform",
    layout="wide"
)

client = genai.Client(
    api_key="YOUR_GEMINI_API_KEY"
)

# =========================
# FUNCTIONS
# =========================

@st.cache_data
def extract_pdf_text(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        try:
            page_text = page.extract_text()

            if page_text:
                text += page_text

        except:
            pass

    return text


def ask_gemini(prompt):

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text


def create_excel(metrics_text):

    df = pd.DataFrame({
        "Results": [metrics_text]
    })

    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

    return output.getvalue()

# =========================
# TITLE
# =========================

st.title("📈 AI Equity Research Platform")

# =========================
# LIVE MARKET DATA
# =========================

st.header("Live Market Data")

ticker = st.text_input(
    "Stock Ticker (Example: TCS.NS, INFY.NS)"
)

if ticker:

    try:

        stock = yf.Ticker(ticker)

        info = stock.info

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Current Price",
            f"₹{info.get('currentPrice', 'N/A')}"
        )

        col2.metric(
            "PE Ratio",
            info.get("trailingPE", "N/A")
        )

        col3.metric(
            "Market Cap",
            f"₹{info.get('marketCap', 0):,}"
        )

        hist = stock.history(period="1y")

        st.line_chart(hist["Close"])

    except Exception as e:

        st.warning("Unable to fetch stock data")

# =========================
# LOGOS
# =========================

company_logo = {
    "TCS":
    "https://upload.wikimedia.org/wikipedia/commons/b/b1/Tata_Consultancy_Services_Logo.svg",

    "Infosys":
    "https://upload.wikimedia.org/wikipedia/commons/9/95/Infosys_logo.svg"
}

# =========================
# FILE UPLOADS
# =========================

st.header("Annual Report Analysis")

pdf1 = st.file_uploader(
    "Upload Company 1 Annual Report",
    type=["pdf"]
)

pdf2 = st.file_uploader(
    "Upload Company 2 Annual Report (Optional)",
    type=["pdf"]
)

company_name = st.text_input(
    "Company Name"
)

if company_name in company_logo:

    st.image(
        company_logo[company_name],
        width=250
    )

# =========================
# ANALYSIS
# =========================

if st.button("Analyze"):

    if pdf1 is None:

        st.error("Upload at least one PDF")

        st.stop()

    with st.spinner("Reading Annual Reports..."):

        report1 = extract_pdf_text(pdf1)

        report2 = ""

        if pdf2:
            report2 = extract_pdf_text(pdf2)

    tab1, tab2, tab3, tab4 = st.tabs([
        "Research Report",
        "Financial Metrics",
        "Comparison",
        "Recommendation"
    ])

    # =====================
    # TAB 1
    # =====================

    with tab1:

        prompt = f"""
        You are a senior equity research analyst.

        Analyze this annual report.

        Provide:

        1. Business Overview
        2. Revenue Drivers
        3. Key Risks
        4. Competitive Advantages
        5. Management Commentary
        6. Long Term Outlook
        7. Buy/Hold/Sell Rating

        Report:

        {report1[:50000]}
        """

        research = ask_gemini(prompt)

        st.markdown(research)

    # =====================
    # TAB 2
    # =====================

    with tab2:

        metrics_prompt = f"""
        Extract:

        Revenue
        Net Profit
        EPS
        Operating Margin
        ROE
        Free Cash Flow

        Return in clean table format.

        Annual Report:

        {report1[:50000]}
        """

        metrics = ask_gemini(metrics_prompt)

        st.markdown(metrics)

        excel_file = create_excel(metrics)

        st.download_button(
            "📊 Download Excel Report",
            data=excel_file,
            file_name="research_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    # =====================
    # TAB 3
    # =====================

    with tab3:

        if pdf2:

            compare_prompt = f"""
            Compare Company 1 and Company 2.

            Company 1:

            {report1[:25000]}

            Company 2:

            {report2[:25000]}

            Compare:

            - Revenue
            - Profitability
            - Growth
            - Risks
            - Valuation
            - Competitive Position
            """

            comparison = ask_gemini(compare_prompt)

            st.markdown(comparison)

        else:

            st.info(
                "Upload second company report for comparison."
            )

    # =====================
    # TAB 4
    # =====================

    with tab4:

        if pdf2:

            recommendation_prompt = f"""
            Based on both annual reports:

            Give:

            Winner

            Confidence Score

            Reasons

            Investment Recommendation

            Company 1:

            {report1[:25000]}

            Company 2:

            {report2[:25000]}
            """

            recommendation = ask_gemini(
                recommendation_prompt
            )

            st.markdown(recommendation)

        else:

            st.info(
                "Upload second company report for recommendation engine."
            )