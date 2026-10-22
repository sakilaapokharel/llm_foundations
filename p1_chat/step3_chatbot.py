from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

messages = [
    {"role": "system", "content": "You are a helpful assistant. Keep answers short."}
]

print("Chat started. Type 'quit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in {"quit", "exit"}:
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama3.2",
        messages=messages,
        temperature=0.7,
        max_tokens=300,
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(messages)
    print(f"Bot: {reply}")
    print(f"  [prompt_tokens={response.usage.prompt_tokens}, messages_sent={len(messages)}]\n")