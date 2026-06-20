from pypdf import PdfReader

reader = PdfReader("annual_reports/TCS.pdf")

keywords = [
    "revenue from operations",
    "net profit",
    "dividend",
    "cash flow"
]

with open("analysis_report.txt", "w") as output:

    for keyword in keywords:

        output.write(f"\n{'='*50}\n")
        output.write(f"{keyword.upper()}\n")
        output.write(f"{'='*50}\n")

        for i, page in enumerate(reader.pages):

            text = page.extract_text()

            if text and keyword in text.lower():

                position = text.lower().find(keyword)

start = max(0, position - 150)
end = min(len(text), position + 500)

output.write(f"\nFound on page {i+1}\n")
output.write("-" * 50 + "\n")
output.write(text[start:end])
output.write("\n" + "-" * 50 + "\n")