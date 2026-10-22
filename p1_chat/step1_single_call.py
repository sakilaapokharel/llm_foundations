from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",  # where Ollama listens
    api_key="ollama",                      # ignored by Ollama, but the library requires something
)

response = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Keep answers short."},
        # {"role": "system", "content": "Answer like a pirate"},
        {"role": "user", "content": "Why is the sky blue?"},
    ],
    temperature=0.7,
    max_tokens=111,
)

print(response.choices[0].message.content)
print("\n--- usage ---")
print(response.usage)