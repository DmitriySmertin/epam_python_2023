from src.hw15.config.Data import TEST_BEER_ENDPOINT
from src.hw15.util.RequestUtil import RequestUtil


class BeerHelper:
    def __init__(self):
        self.req_util = RequestUtil()

    def getBeerInfo(self):
        resp = self.req_util.get(TEST_BEER_ENDPOINT, expected_status_code=200)
        return resp

    def deleteBeerInfo(self):
        resp = self.req_util.delete(TEST_BEER_ENDPOINT)
        return resp
