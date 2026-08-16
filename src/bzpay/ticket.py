from dataclasses import dataclass
from typing import Callable

@dataclass
class Ticket:
    player: str
    payment: int
    description: str
    payment_id: str
    callback: Callable[[str, int, str], None]