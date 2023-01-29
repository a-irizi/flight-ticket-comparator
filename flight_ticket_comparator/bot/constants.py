import os

DRIVER_PATH = os.path.join(os.environ['HOME'], 'Downloads')

ROYAL_AIR_MAROC_URL = "https://www.royalairmaroc.com/us-en"
RYANAIR_URL = "https://www.ryanair.com/us/en"
QATAR_AIRWAYS_URL = "https://www.qatarairways.com/en-us/homepage.html"

ROYAL_AIR_MAROC_FP_CLEANUP = {
    "CLOSE_BUTTON": "button.onetrust-close-btn-handler",
    "FILTER_INPUT": "/html/body/div[1]/div/div/div/div[2]/section/div[2]/div/div/app-booking-engine-root/div/app-booking-menu/div/app-tab/div/div[2]/div[2]/app-flight-search/div/div[2]/div[1]/div[2]/app-location-picker/div/input",
    "LOCATION_LIST":  "/html/body/div[1]/div/div/div/div[2]/section/div[2]/div/div/app-booking-engine-root/div/app-booking-menu/div[1]/app-tab/div/div[2]/div[2]/app-flight-search/div/div[3]/div[1]/div[2]/app-location-picker/div/div[2]",
    "LOCATION": "div.location-picker-list-option",
}
