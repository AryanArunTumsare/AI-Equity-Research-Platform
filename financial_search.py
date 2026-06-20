from pypdf import PdfReader

reader = PdfReader("annual_reports/TCS.pdf")

keywords = [
    "revenue",
    "profit",
    "dividend",
    "risk",
    "cash flow"
]

for keyword in keywords:
    print(f"\n\n### {keyword.upper()} ###")

    for i, page in enumerate(reader.pages):
        text = page.extract_text()

        if text and keyword in text.lower():

            print(f"\nFound '{keyword}' on page {i+1}")

            position = text.lower().find(keyword)

            start = max(0, position - 100)
            end = min(len(text), position + 300)

            print("-" * 50)
            print(text[start:end])
            print("-" * 50)