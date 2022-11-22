from dataclasses import dataclass
import typing


@dataclass
class BasePhotoSize:
    """This is a base photo size"""
    file_id: typing.Union[str, None]
    file_unique_id: typing.Union[str, None]
    width: typing.Union[int, None]
    height: typing.Union[int, None]
    file_size: typing.Union[int, None]
