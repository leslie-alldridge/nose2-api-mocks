import unittest
from users import get_users
from unittest.mock import patch


class BasicTests(unittest.TestCase):
    @patch('users.requests.get')  # Mock 'requests' module 'get' method.
    def test_request_response_with_decorator(self, mock_get):

        mockuser = [{
            "id": 0,
            "first_name": "Dell",
            "last_name": "Norval",
            "phone": "994-979-3976"
        }]

        # Mock status code of response.
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mockuser
        response = get_users()

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), mockuser)


if __name__ == "__main__":
    unittest.main()
