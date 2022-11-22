import typing
from dataclasses import dataclass

@dataclass
class BaseChatPhoto:
    small_file_id : typing.Union[None,str]
    small_file_unique_id : typing.Union[None,str]
    big_file_id : typing.Union[None,str]
    big_file_unique_id : typing.Union[None,str]