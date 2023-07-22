from .api import chatgpt

def main():
    # Get the OpenAI key from environment variables
    api_key = os.getenv('OPENAI_KEY')

    # Substitute 'your-api-key' with your actual OpenAI API key
    chatgpt.setup_gpt(api_key)

    prompt = "Once upon a time"
    print(chatgpt.send_prompt(prompt))

if __name__ == "__main__":
    main()