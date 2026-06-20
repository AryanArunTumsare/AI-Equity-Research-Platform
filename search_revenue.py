from pypdf import PdfReader

reader = PdfReader("annual_reports/TCS.pdf")

for i, page in enumerate(reader.pages):
    text = page.extract_text()

    if text and "revenue" in text.lower():
        print(f"\nFOUND ON PAGE {i+1}\n")
        print(text[:1000])
        break