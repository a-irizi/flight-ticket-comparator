from datetime import datetime
import enum
from selenium import webdriver
import os
from abc import ABC, abstractmethod

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

    def land_first_page(self):
        self.get(self.home_page_url)

    @abstractmethod
    def select_start_date(self, date: datetime):
        pass

    @abstractmethod
    def select_end_date(self, date: datetime):
        pass

    @abstractmethod
    def select_country(self):
        pass

    @abstractmethod
    def select_city(self):
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

    def select_start_date(self, date: datetime):
        raise NotImplementedError

    def select_end_date(self, date: datetime):
        raise NotImplementedError

    def select_country(self):
        raise NotImplementedError

    def select_city(self):
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

    def select_country(self):
        raise NotImplementedError

    def select_city(self):
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

    def select_country(self):
        raise NotImplementedError

    def select_city(self):
        raise NotImplementedError

    def select_passengers(self, adult: int = 1, teen: int = 0, child: int = 0, infant: int = 0):
        raise NotImplementedError

    def select_ticket_class(self, ticket_class: TicketClassEnum):
        raise NotImplementedError

    def get_tickets(self):
        raise NotImplementedError
