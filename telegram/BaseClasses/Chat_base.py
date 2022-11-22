import typing
from dataclasses import dataclass
from .ChatPermissions_base import BaseChatPermissions
from .ChatPhoto_base import BaseChatPhoto
from .Location_base import BaseLocation


@dataclass
class BaseChat:
    """Base class for Chat"""
    chat_id: typing.Union[int, None]
    type: typing.Union[str, None]
    title: typing.Union[str, None]
    username: typing.Union[str, None]
    linked_chat_id = typing.Union[int, None]
    first_name = typing.Union[str, None]
    last_name: typing.Union[str, None]
    is_forum: typing.Union[None, bool]
    photo: typing.Union[None, BaseChatPhoto]
    location: typing.Union[None, BaseLocation]
    permissions: typing.Union[None, BaseChatPermissions]
    active_usernames: list[str]
    emoji_status_custom_emoji_id: typing.Union[str, None]
    bio: typing.Union[str, None]
    has_private_forwards: typing.Union[bool, None]
    has_restricted_voice_and_video_messages: typing.Union[bool, None]
    join_to_send_messages: typing.Union[bool, None]
    join_by_request: typing.Union[bool, None]
    description: typing.Union[str, None]
    invite_link: typing.Union[str, None]
    slow_mode_delay: typing.Union[int, None]
    message_auto_delete_time: typing.Union[int, None]
    has_protected_content: typing.Union[bool, None]
    sticker_set_name: typing.Union[str, None]
    can_set_sticker_set: typing.Union[bool, None]
