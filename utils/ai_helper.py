import openai
openai.api_key = "your-api-key"

def generate_response(thought):
    prompt = f"A user just shared a negative thought: '{thought}'. Use CBT techniques to gently challenge it and provide a helpful response."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response["choices"][0]["message"]["content"]
