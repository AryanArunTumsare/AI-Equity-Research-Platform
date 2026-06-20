from pypdf import PdfReader

reader = PdfReader("annual_reports/TCS.pdf")

pages_to_extract = [35, 36, 58]

with open("financial_summary.txt", "w", encoding="utf-8") as output:

    for page_num in pages_to_extract:

        page = reader.pages[page_num - 1]

        text = page.extract_text()

        output.write(f"\n\nPAGE {page_num}\n")
        output.write("="*50 + "\n")

        if text:
            output.write(text)