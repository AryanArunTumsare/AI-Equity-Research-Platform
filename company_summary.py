from pypdf import PdfReader

reader = PdfReader("annual_reports/TCS.pdf")

all_text = ""

for page in reader.pages:
    text = page.extract_text()

    if text:
        all_text += text + "\n"

# Save complete report text
with open("full_report.txt", "w", encoding="utf-8") as file:
    file.write(all_text)

print("Report extracted successfully")