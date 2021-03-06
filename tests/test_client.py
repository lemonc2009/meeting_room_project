import pytest
from app import create_app


class TestCase():
    def setup(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        assert response.status_code == 200
        assert ('GDS Meeting Room Availablity' in response.get_data(as_text=True))
