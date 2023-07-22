import os
from dotenv import load_dotenv
from .api import chatgpt, wordpress

# Load environment variables from .env file
load_dotenv()

def main():
    # Get the OpenAI key from environment variables
    gpt_key = os.getenv('OPENAI_KEY')
    chatgpt.setup_gpt(gpt_key)

    # Generate a blog post
    topic = "Poetry writen by a Cyber Poet about an event of his live as a Robot"
    post_data = chatgpt.generate_blog_post(topic)

    # Get the WordPress details from environment variables
    wp_api_url = os.getenv('WP_API_URL')
    wp_username = os.getenv('WP_USERNAME')
    wp_password = os.getenv('WP_PASSWORD')

    # Setup WordPress API and create a new post
    auth_token = wordpress.setup_wordpress(wp_api_url, wp_username, wp_password)
    new_post = wordpress.create_post(wp_api_url, auth_token, post_data)

    print(f"Created a new post: {new_post['link']}")

if __name__ == "__main__":
    main()