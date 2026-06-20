from google import genai

client = genai.Client(
    api_key="YOUR_GEMINI_API_KEY"
)

company1 = input("First company: ")
company2 = input("Second company: ")

with open(f"{company1}_report.txt", "r", encoding="utf-8") as f:
    report1 = f.read()

with open(f"{company2}_report.txt", "r", encoding="utf-8") as f:
    report2 = f.read()

prompt = f"""
You are a senior equity research analyst.

Compare these two companies.

Provide:

1. Business Comparison
2. Revenue Comparison
3. Profitability Comparison
4. Growth Comparison
5. Risk Comparison
6. Competitive Advantages
7. Which company is a better long-term investment and why

Company 1 ({company1}):
{report1[:25000]}

Company 2 ({company2}):
{report2[:25000]}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
)

with open("comparison_report.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print(response.text)
print("\nComparison report saved.")