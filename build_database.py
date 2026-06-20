from pypdf import PdfReader

reader = PdfReader("annual_reports/TCS.pdf")

company_data = {
    "company": "TCS",
    "revenue_pages": [],
    "profit_pages": [],
    "risk_pages": []
}

for i, page in enumerate(reader.pages):

    text = page.extract_text()

    if not text:
        continue

    text = text.lower()

    if "revenue" in text:
        company_data["revenue_pages"].append(i + 1)

    if "profit" in text:
        company_data["profit_pages"].append(i + 1)

    if "risk" in text:
        company_data["risk_pages"].append(i + 1)

print(company_data)