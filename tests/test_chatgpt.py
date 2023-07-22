# tests/test_chatgpt.py

import unittest
from unittest.mock import patch, MagicMock
from the_cyber_poet.api import chatgpt

class TestChatGPT(unittest.TestCase):

    @patch('the_cyber_poet.api.chatgpt.openai')
    def test_setup_gpt(self, mock_openai):
        # Arrange
        api_key = 'mock_openai_key'

        # Act
        chatgpt.setup_gpt(api_key)

        # Assert
        self.assertEqual(mock_openai.api_key, 'mock_openai_key')

    @patch('the_cyber_poet.api.chatgpt.openai.Completion.create')
    def test_send_prompt(self, mock_create):
        # Arrange
        prompt = 'mock_prompt'
        mock_create.return_value = MagicMock(choices=[MagicMock(text='mock_text')])

        # Act
        result = chatgpt.send_prompt(prompt)

        # Assert
        self.assertEqual(result, 'mock_text')
        mock_create.assert_called_once_with(engine="text-davinci-004", prompt=prompt, max_tokens=100)

    @patch('the_cyber_poet.api.chatgpt.send_prompt')
    def test_generate_blog_post(self, mock_send_prompt):
        # Arrange
        topic = 'mock_topic'
        mock_send_prompt.side_effect = ['mock_title', 'mock_introduction', 'mock_body']

        # Act
        result = chatgpt.generate_blog_post(topic)

        # Assert
        self.assertEqual(result, {"title": 'mock_title', "content": 'mock_introduction\n\nmock_body'})
        mock_send_prompt.assert_any_call(f"Create a catchy blog title about {topic}", max_tokens=10)
        mock_send_prompt.assert_any_call(f"Write an engaging introduction for a blog post about {topic}", max_tokens=100)
        mock_send_prompt.assert_any_call(f"Write the body of a blog post about {topic}", max_tokens=500)

if __name__ == "__main__":
    unittest.main()
