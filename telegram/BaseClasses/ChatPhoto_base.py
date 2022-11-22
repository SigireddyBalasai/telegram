import typing
from dataclasses import dataclass


@dataclass
class BaseChatPhoto:
    """This is baseChat photo"""
    small_file_id: typing.Union[None, str]
    small_file_unique_id: typing.Union[None, str]
    big_file_id: typing.Union[None, str]
    big_file_unique_id: typing.Union[None, str]
