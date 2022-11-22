import typing
from dataclasses import dataclass


@dataclass
class BaseUser:
    """THis is the base User Class"""
    added_to_attachment_menu: typing.Union[bool, None]
    is_premium: typing.Union[bool, None]
    username: typing.Union[str, None]
    last_name: typing.Union[str, None]
    can_join_groups: typing.Union[bool, None]
    supports_inline_queries: typing.Union[bool, None]
    can_read_all_group_messages: typing.Union[bool, None]
    language_code: typing.Union[str, None]
    first_name: typing.Union[str, None]
    is_bot: typing.Union[bool, None]
    user_id: typing.Union[int, None]

