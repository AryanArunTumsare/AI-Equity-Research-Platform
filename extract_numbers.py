from pypdf import PdfReader
import re

reader = PdfReader("annual_reports/TCS.pdf")

patterns = [
    "revenue",
    "profit",
    "dividend"
]

for page_num, page in enumerate(reader.pages):

    text = page.extract_text()

    if not text:
        continue

    for pattern in patterns:

        if pattern in text.lower():

            print("\n" + "=" * 60)
            print(f"PAGE {page_num + 1}")
            print("=" * 60)

            numbers = re.findall(r'[\d,]+\.\d+|[\d,]+', text)

            print("Numbers found:")
            print(numbers[:20])

            break
        import re