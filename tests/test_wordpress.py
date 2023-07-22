import unittest
from unittest.mock import patch, MagicMock
from the_cyber_poet.api import wordpress

class TestWordPress(unittest.TestCase):

    @patch('the_cyber_poet.api.wordpress.requests.post')
    def test_setup_wordpress(self, mock_post):
        # Arrange
        api_url = 'mock_api_url'
        username = 'mock_username'
        password = 'mock_password'
        mock_post.return_value = MagicMock(json=MagicMock(return_value={"token": 'mock_token'}))

        # Act
        result = wordpress.setup_wordpress(api_url, username, password)

        # Assert
        self.assertEqual(result, 'mock_token')
        mock_post.assert_called_once_with(f"{api_url}/jwt-auth/v1/token", data={"username": username, "password": password})

    @patch('the_cyber_poet.api.wordpress.requests.post')
    def test_create_post(self, mock_post):
        # Arrange
        api_url = 'mock_api_url'
        auth_token = 'mock_auth_token'
        post_data = {'content': 'mock_content'}
        mock_post.return_value = MagicMock(json=MagicMock(return_value='mock_response'))

        # Act
        result = wordpress.create_post(api_url, auth_token, post_data)

        # Assert
        self.assertEqual(result, 'mock_response')
        mock_post.assert_called_once_with(f"{api_url}/wp/v2/posts", headers={"Authorization": f"Bearer {auth_token}"}, json=post_data)

if __name__ == "__main__":
    unittest.main()
