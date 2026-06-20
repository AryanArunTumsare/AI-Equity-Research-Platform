from google import genai

client = genai.Client(
    api_key="YOUR_GEMINI_API_KEY"
)

companies = ["TCS", "Infosys"]

all_metrics = ""

for company in companies:

    print(f"Processing {company}...")

    with open(f"{company}_report.txt", "r", encoding="utf-8") as f:
        report_text = f.read()

    prompt = f"""
You are a professional equity research analyst.

Extract the following financial metrics from the annual report.

Return ONLY in this format:

Company: {company}

Revenue:
Net Profit:
EPS:
Operating Margin:
ROE:
Free Cash Flow:
Total Assets:
Total Debt:
Dividend Per Share:

Annual Report:

{report_text[:50000]}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    all_metrics += response.text + "\n\n"
    all_metrics += "=" * 60 + "\n\n"

    print(f"{company} completed.")

with open("financial_metrics.txt", "w", encoding="utf-8") as f:
    f.write(all_metrics)

print("\nFinancial metrics saved successfully.")