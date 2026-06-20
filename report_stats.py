with open("full_report.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = len(text.split())

print("Total words:", words)
