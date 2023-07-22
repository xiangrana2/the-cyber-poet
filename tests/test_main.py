import unittest
from unittest.mock import patch, MagicMock
from the_cyber_poet import main

class TestMain(unittest.TestCase):

    @patch('the_cyber_poet.main.os.getenv')
    @patch('the_cyber_poet.main.wordpress.create_post')
    @patch('the_cyber_poet.main.wordpress.setup_wordpress')
    @patch('the_cyber_poet.main.chatgpt.generate_blog_post')
    @patch('the_cyber_poet.main.chatgpt.setup_gpt')
    def test_main(self, mock_setup_gpt, mock_generate_blog_post, mock_setup_wordpress, mock_create_post, mock_getenv):
        # Arrange
        mock_getenv.return_value = 'mock_value'
        mock_generate_blog_post.return_value = 'mock_post_data'
        mock_setup_wordpress.return_value = 'mock_auth_token'
        mock_create_post.return_value = {'link': 'mock_link'}

        # Act
        main.main()

        # Assert
        mock_setup_gpt.assert_called_once_with('mock_value')
        mock_generate_blog_post.assert_called_once_with("Poetry writen by a Cyber Poet about an event of his live as a Robot")
        mock_setup_wordpress.assert_called_once_with('mock_value', 'mock_value', 'mock_value')
        mock_create_post.assert_called_once_with('mock_value', 'mock_auth_token', 'mock_post_data')

if __name__ == "__main__":
    unittest.main()
