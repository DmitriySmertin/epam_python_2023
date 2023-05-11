import pytest
import logging as logger

from src.hw15.config.Data import TEST_NAME, TEST_ABV, TEST_BEER_ENDPOINT
from src.hw15.helpers.BeerHelper import BeerHelper


@pytest.mark.tcid29
def test_get_beer_info_positive():
    logger.info("TEST: Get Beer Info (Positive)")

    beer_obj = BeerHelper()
    beer_api_info = beer_obj.getBeerInfo()

    assert beer_api_info[0]["name"] == TEST_NAME, \
        f'User name doesnt exist in response: {TEST_NAME}, Actual: {beer_api_info[0]["name"]}'

    assert beer_api_info[0]["abv"] == TEST_ABV, \
        f'abv doesnt exist in response: {TEST_ABV}, Actual: {beer_api_info[0]["name"]}'


def test_delete_beer_negative():
    logger.info("TEST: Delete Beer Info (Negative)")

    beer_obj = BeerHelper()
    resp = beer_obj.deleteBeerInfo()

    assert resp["statusCode"] == 404, \
        f'The actual status code: {resp["statusCode"]} does not match the expected: {404}'

    assert resp["message"] == "No endpoint found that matches " + f"'{TEST_BEER_ENDPOINT}'"
