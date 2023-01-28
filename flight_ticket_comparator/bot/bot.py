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

    @abstractmethod
    def land_first_page(self):
        pass

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
