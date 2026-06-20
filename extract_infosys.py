from pypdf import PdfReader

reader = PdfReader("annual_reports/Infosys.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

with open("Infosys_report.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Infosys report extracted.")