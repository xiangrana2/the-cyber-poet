import openai

def setup_gpt(api_key):
    openai.api_key = api_key

def send_prompt(prompt, max_tokens=100):
    response = openai.Completion.create(engine="text-davinci-004", prompt=prompt, max_tokens=max_tokens)
    return response.choices[0].text.strip()

def generate_blog_post(topic):
    # Create a blog post using the GPT-3 API
    title_prompt = f"Create a catchy blog title about {topic}"
    title = send_prompt(title_prompt, max_tokens=10)
    
    intro_prompt = f"Write an engaging introduction for a blog post about {topic}"
    introduction = send_prompt(intro_prompt, max_tokens=100)

    body_prompt = f"Write the body of a blog post about {topic}"
    body = send_prompt(body_prompt, max_tokens=500)
    return {
        "title": title,
        "content": f"{introduction}\n\n{body}"
    }
