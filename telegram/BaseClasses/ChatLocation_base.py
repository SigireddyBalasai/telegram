from dataclasses import dataclass
from typing import Union
from .Location_base import BaseLocation


@dataclass
class BaseChatLocation:
    """This is base Chat Location"""
    location: Union[BaseLocation, None]
    address: Union[str, None]
