from pypdf import PdfReader

reader = PdfReader("annual_reports/TCS.pdf")

keywords = [
    "revenue from operations",
    "net profit",
    "dividend",
    "earnings per share",
    "cash and cash equivalents"
]

for keyword in keywords:

    print("\n" + "="*60)
    print(keyword.upper())
    print("="*60)

    for i, page in enumerate(reader.pages):

        text = page.extract_text()

        if text and keyword in text.lower():

            print(f"Found on page {i+1}")
            break