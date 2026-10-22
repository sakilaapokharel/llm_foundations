from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def ask(messages):
    response = client.chat.completions.create(
        model="llama3.2",
        messages=messages,
        temperature=0,
        max_tokens=100,
    )
    return response.choices[0].message.content

# Call 1: tell the model a fact
print("Call 1:", ask([{"role": "user", "content": "My favorite fruit is mango. Remember that."}]))

# Call 2: a NEW call with no history
print("Call 2:", ask([{"role": "user", "content": "What is my favorite fruit?"}]))