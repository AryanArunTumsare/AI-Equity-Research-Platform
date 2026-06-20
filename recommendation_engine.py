from google import genai

client = genai.Client(
    api_key="YOUR_GEMINI_API_KEY"
)

with open("comparison_report.txt", "r", encoding="utf-8") as f:
    comparison = f.read()

with open("financial_metrics.txt", "r", encoding="utf-8") as f:
    metrics = f.read()

prompt = f"""
You are a senior equity research analyst.

Based on the comparison report and financial metrics,
determine the better investment.

Return in this format:

WINNER:

CONFIDENCE:
(Low/Medium/High)

REASONS:
- Reason 1
- Reason 2
- Reason 3

INVESTMENT RECOMMENDATION:
(Buy/Hold/Sell)

Comparison Report:
{comparison}

Financial Metrics:
{metrics}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
)

print(response.text)

with open("final_recommendation.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Final recommendation saved.")