from google import genai

client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

with open("financial_summary.txt", "r", encoding="utf-8") as f:
    report_text = f.read()

prompt = f"""
Analyze this annual report data and provide:

1. Company overview
2. Revenue analysis
3. Risks
4. Growth opportunities
5. Investment recommendation

Data:
{report_text[:15000]}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)