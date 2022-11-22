from .PhotoSize_base import BasePhotoSize
import typing


class BaseAnimation:
    """This is the base Animation class"""
    file_id: typing.Union[None, str]
    file_unique_id: typing.Union[None, str]
    width: typing.Union[None, int]
    height: typing.Union[None, int]
    duration: typing.Union[None, int]
    thumb: typing.Union[None, type(BasePhotoSize)]
    file_name: typing.Union[None, str]
    mime_type: typing.Union[None, str]
    file_size: typing.Union[None, int]
