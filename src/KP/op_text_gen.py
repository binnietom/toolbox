import openai
response = openai. ChatCompletion. create(
    model="gpt-4",
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Can you say something to inspire the audience of Microsoft BUILD 2023?"},
        ]
)
print(response ["choices"] [0] ["message"] ["content"])
