import pytest

from bot import constants as const


def test_GIVEN_bot_WHEN_instantiating_THEN_assert_bot_driver_path_equals_DIRVER_PATH(ryanair_bot):
    bot = ryanair_bot

    print(f"bot.driver_path = {bot.driver_path}")

    assert bot.driver_path == const.DRIVER_PATH


def test_GIVEN_bot_WHEN_instantiating_THEN_assert_bot_home_page_url_equals_RYANAIR_URL(ryanair_bot):
    bot = ryanair_bot

    print(f"bot.home_page_url = {bot.home_page_url}")

    assert bot.home_page_url == const.RYANAIR_URL


def test_GIVEN_bot_WHEN_land_first_page_THEN_assert_bot_current_page_url_equals_home_page_url(ryanair_bot):
    bot = ryanair_bot

    bot.land_first_page()

    print(f"bot.current_url = {bot.current_url}")
    print(f"bot.home_page_url = {bot.home_page_url}")

    assert bot.current_url == bot.home_page_url
