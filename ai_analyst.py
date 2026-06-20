from google import genai

client = genai.Client(
        api_key="YOUR_GEMINI_API_KEY")

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="What is equity research?"
)

print(response.text)


    