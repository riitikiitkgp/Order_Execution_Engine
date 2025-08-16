import time
from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel

@dataclass
class Order:
    id: str
    token_in: str
    token_out: str
    amount: float
    order_type: str = "market"
    status: str = "pending"
    tx_hash: Optional[str] = None
    executed_price: Optional[float] = None
    last_error: Optional[str] = None

class ExecuteOrderRequest(BaseModel):
    token_in: str
    token_out: str
    amount: float
    order_type: Optional[str] = "market"
