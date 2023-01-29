import pytest
from bot.bot import QatarAirwaysBot, RoyalAirMarocBot, RyanairBot

from bot import constants as const
import enum


class BotEnum(enum.Enum):
    ROYAL_AIR_MAROC = (1, "Royal Air Maroc")
    RYANAIR = (2, "Ryanair")
    QATAR_AIR_WAYS = (3, "Qatar Airways")

    def __str__(self):
        return self.value[1]


@pytest.fixture
def bot_factory():
    def build_bot(bot_type: BotEnum, driver_path=const.DRIVER_PATH):
        bot = None

        if bot_type == BotEnum.ROYAL_AIR_MAROC:
            bot = RoyalAirMarocBot(driver_path=driver_path)
        elif bot_type == BotEnum.RYANAIR:
            bot = RyanairBot(driver_path=driver_path)
        elif bot_type == BotEnum.QATAR_AIR_WAYS:
            bot = QatarAirwaysBot(driver_path=driver_path)

        return bot

    return build_bot


@pytest.fixture
def royal_air_maroc_bot(bot_factory):
    return bot_factory(bot_type=BotEnum.ROYAL_AIR_MAROC)


@pytest.fixture
def ryanair_bot(bot_factory):
    return bot_factory(bot_type=BotEnum.RYANAIR)


@pytest.fixture
def qatar_airways_bot(bot_factory):
    return bot_factory(bot_type=BotEnum.QATAR_AIR_WAYS)
