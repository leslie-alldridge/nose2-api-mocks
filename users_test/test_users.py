import unittest

from users import get_users, get_user, get_api
from unittest.mock import patch


class BasicTests(unittest.TestCase):
    @patch('users.requests.get')  # Mock 'requests' module 'get' method.
    def test_request_response_with_decorator(self, mock_get):

        mockuser = [
            {'phone': '514-794-6957', 'first_name': 'Brant',
                'last_name': 'Mekhi', 'id': 0},
            {'phone': '772-370-0117', 'first_name': 'Thalia',
                'last_name': 'Kenyatta', 'id': 1},
            {'phone': '176-290-7637', 'first_name': 'Destin',
                'last_name': 'Soledad', 'id': 2}
        ]

        # Mock status code of response.
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mockuser
        response = get_users()

        # filter to find user 2
        user = get_user(2)

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), mockuser)
        self.assertEqual(user, mockuser[2])

    @patch('users.requests.get')  # Mock 'requests' module 'get' method.
    def test_request_response_with_decorator(self, mock_get):

        mockresponse = {"weather": [
            {
                "id": 803,
                "main": "Clouds",
                "description": "broken clouds",
                "icon": "04n"
            }
        ]}

        # Mock status code of response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mockresponse
        response = get_api()

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), mockresponse)


if __name__ == "__main__":
    unittest.main()
