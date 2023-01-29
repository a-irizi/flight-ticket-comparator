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


def test_GIVEN_bot_WHEN_land_first_page_THEN_assert_bot_current_page_url_equals_home_page_url(royal_air_maroc_bot):
    bot = royal_air_maroc_bot

    bot.land_first_page()

    print(f"bot.current_url = {bot.current_url}")
    print(f"bot.home_page_url = {bot.home_page_url}")

    assert bot.current_url == bot.home_page_url

def test_GIVEN_bot_and_city_WHEN_select_city_and_city_is_correct_THEN_assert_select_city_does_not_raise_exception(royal_air_maroc_bot):
    bot = royal_air_maroc_bot

    try:
        bot.land_first_page()
    except Exception as exc:
        assert False, f'land_first_page raised an exception {exc}'

    try:
        bot.select_city(city_name="casablanca")
    except Exception as exc:
        assert False, f'select_city raised an exception {exc}'
