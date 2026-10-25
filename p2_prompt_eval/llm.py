from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")


def chat(prompt, system=None, temperature=0, max_tokens=50, model="llama3.2"):
    """Send one prompt, return the model's text reply."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content.strip()