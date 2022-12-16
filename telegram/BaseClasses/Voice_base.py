import typing
from dataclasses import dataclass


@dataclass
class Voice:
    """THis is the base User Class"""
    file_id: typing.Union[str, None]
    file_unique_id: typing.Union[str, None]
    duration: typing.Union[int, None]
    mime_type: typing.Union[str, None]
    file_size: typing.Union[int, None]