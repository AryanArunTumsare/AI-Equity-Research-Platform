import google.generativeai as genai

genai.configure(api_key="AIzaSyAXPn8iZKHli6OV8PQsqITLBWIfAZPqi0U")

for model in genai.list_models():
    print(model.name)