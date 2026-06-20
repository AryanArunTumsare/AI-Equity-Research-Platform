from google import genai

client = genai.Client(
    api_key="YOUR_GEMINI_API_KEY"
)

company = input("Enter company name: ")
print(f"Selected company: {company}")

with open(f"{company}_report.txt", "r", encoding="utf-8") as f:
    report_text = f.read()

prompt = f"""
You are a senior equity research analyst.

Analyze this annual report and return:

COMPANY NAME:
INDUSTRY:

BUSINESS OVERVIEW:

REVENUE DRIVERS:

KEY RISKS:

COMPETITIVE ADVANTAGES:

MANAGEMENT COMMENTARY:

LONG TERM OUTLOOK:

INVESTMENT THESIS:

RATING:
(Buy/Hold/Sell)

Annual Report:
{report_text[:50000]}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
)

with open("research_report.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Research report saved.")