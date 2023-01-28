import pytest

from bot import constants as const


def test_GIVEN_bot_WHEN_instantiating_THEN_assert_bot_driver_path_equals_DIRVER_PATH(royal_air_maroc_bot):
    bot = royal_air_maroc_bot

    print(f"bot.driver_path = {bot.driver_path}")

    assert bot.driver_path == const.DRIVER_PATH


def test_GIVEN_bot_WHEN_instantiating_THEN_assert_bot_home_page_url_equals_ROYAL_AIR_MAROC_URL(royal_air_maroc_bot):
    bot = royal_air_maroc_bot

    print(f"bot.home_page_url = {bot.home_page_url}")

    assert bot.home_page_url == const.ROYAL_AIR_MAROC_URL
