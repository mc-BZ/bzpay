from .config import BZAUTH_URL, BANGXIBOT_URL
from .ticket import Ticket
import requests
from flask.app import Flask
import flask

class Pay:
    def __init__(self, bot_name="bzpay_bot", password="Bbzpay"):
        requests.get(BANGXIBOT_URL + f"/login?player={bot_name}&password={password}")
        self.app = Flask(__name__)
        self.tickets: dict[str, Ticket] = {} # uuid: Ticket
        self.gotpay_callbacks: dict[str, list[str]] # player: queue[uuid]