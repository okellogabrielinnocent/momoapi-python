import unittest
import pytest
from momoapi.client import MomoApi
try:
    from unittest import mock
except ImportError:
    import mock

from .utils import mocked_requests_get, mocked_requests_post


class TestClient(unittest.TestCase):
    def setUp(self):
        pass
        #self.widget = Widget('The widget')

    def tearDown(self):
        pass
        # self.widget.dispose()
        #self.widget = None

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_client_instantiate(self, mock_get):
        client = MomoApi("APIKEY", "USERID", "APISECRET")

        #request_mock.assert_requested("post", "/v1/accounts")
        assert isinstance(client, MomoApi)

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_request_to_pay(self, mock_get):
        client = MomoApi("APIKEY", "USERID", "APISECRET")
        ref = client.requestToPay("256772123456", "600", "123456789", note="dd",
                                  message="dd", currency="EUR", environment="sandbox")
