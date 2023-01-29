from datetime import datetime
import enum
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
from abc import ABC, abstractmethod

from selenium.webdriver.common.by import By

from . import constants as const


class TicketClassEnum(enum.Enum):
    ECONMY = (1, "Economy")
    PREMIUM = (2, "Premium (Buisness/First)")


class BaseBot(ABC, webdriver.Firefox):
    def __init__(self, home_page_url, driver_path=const.DRIVER_PATH):
        self.driver_path = driver_path
        self.home_page_url = home_page_url
        os.environ['PATH'] += self.driver_path
        super(BaseBot, self).__init__()

    @abstractmethod
    def _first_page_cleanup(self):
        pass

    def land_first_page(self):
        self.get(self.home_page_url)
        self._first_page_cleanup()

    @abstractmethod
    def select_start_date(self, date: datetime):
        pass

    @abstractmethod
    def select_end_date(self, date: datetime):
        pass

    @abstractmethod
    def select_departure_country(self, country_name: str):
        pass

    @abstractmethod
    def select_departure_city(self, city_name: str):
        pass

    @abstractmethod
    def select_landing_country(self, country_name: str):
        pass

    @abstractmethod
    def select_landing_city(self, city_name: str):
        pass

    @abstractmethod
    def select_passengers(self, adult: int = 1, teen: int = 0, child: int = 0, infant: int = 0):
        pass

    @abstractmethod
    def select_ticket_class(self, ticket_class: TicketClassEnum):
        pass

    @abstractmethod
    def get_tickets(self):
        pass

    def __exit__(self, exception_type, exception_value, traceback):
        self.quit()


class RoyalAirMarocBot(BaseBot):

    def __init__(self, home_page_url=const.ROYAL_AIR_MAROC_URL, driver_path=const.DRIVER_PATH):
        super().__init__(home_page_url=home_page_url, driver_path=driver_path)

    def _first_page_cleanup(self):
        try:
            close_button = self.find_element(
                By.CSS_SELECTOR, const.ROYAL_AIR_MAROC_FP_CLEANUP["CLOSE_BUTTON"]
            )
        except NoSuchElementException:
            pass
        else:
            close_button.click()

    def select_start_date(self, date: datetime):
        raise NotImplementedError

    def select_end_date(self, date: datetime):
        raise NotImplementedError

    def select_departure_country(self, country_name: str):
        raise NotImplementedError

    def select_departure_city(self, city_name: str):
        raise NotImplementedError

    def select_landing_country(self, country_name: str):
        raise NotImplementedError

    def select_landing_city(self, city_name: str):
        raise NotImplementedError

    def select_passengers(self, adult: int = 1, teen: int = 1, child: int = 0, infant: int = 0):
        raise NotImplementedError

    def select_ticket_class(self, ticket_class: TicketClassEnum):
        raise NotImplementedError

    def get_tickets(self):
        raise NotImplementedError


class RyanairBot(BaseBot):

    def __init__(self, home_page_url=const.RYANAIR_URL, driver_path=const.DRIVER_PATH):
        super().__init__(home_page_url=home_page_url, driver_path=driver_path)

    def select_start_date(self, date: datetime):
        raise NotImplementedError

    def select_end_date(self, date: datetime):
        raise NotImplementedError

    def select_departure_country(self, country_name: str):
        raise NotImplementedError

    def select_departure_city(self, city_name: str):
        raise NotImplementedError

    def select_landing_country(self, country_name: str):
        raise NotImplementedError

    def select_landing_city(self, city_name: str):
        raise NotImplementedError

    def select_passengers(self, adult: int = 1, teen: int = 1, child: int = 0, infant: int = 0):
        raise NotImplementedError

    def select_ticket_class(self, ticket_class: TicketClassEnum):
        raise NotImplementedError

    def get_tickets(self):
        raise NotImplementedError


class QatarAirwaysBot(BaseBot):

    def __init__(self, home_page_url=const.QATAR_AIRWAYS_URL, driver_path=const.DRIVER_PATH):
        super().__init__(home_page_url=home_page_url, driver_path=driver_path)

    def select_start_date(self, date: datetime):
        raise NotImplementedError

    def select_end_date(self, date: datetime):
        raise NotImplementedError

    def select_departure_country(self, country_name: str):
        raise NotImplementedError

    def select_departure_city(self, city_name: str):
        raise NotImplementedError

    def select_landing_country(self, country_name: str):
        raise NotImplementedError

    def select_landing_city(self, city_name: str):
        raise NotImplementedError

    def select_passengers(self, adult: int = 1, teen: int = 0, child: int = 0, infant: int = 0):
        raise NotImplementedError

    def select_ticket_class(self, ticket_class: TicketClassEnum):
        raise NotImplementedError

    def get_tickets(self):
        raise NotImplementedError
