import typing
from dataclasses import dataclass
from .ChatPermissions_base import BaseChatPermissions
from .ChatPhoto_base import BaseChatPhoto
from .Location_base import BaseLocation


@dataclass
class BaseChat:
    """Base class for Chat"""
    chat_id: typing.Union[int, None] = None
    type: typing.Union[str, None] = None
    title: typing.Union[str, None] = None
    username: typing.Union[str, None] = None
    linked_chat_id = typing.Union[int, None] = None
    first_name = typing.Union[str, None] = None
    last_name: typing.Union[str, None] = None
    is_forum: typing.Union[None, bool] = None
    photo: typing.Union[None, BaseChatPhoto] = None
    location: typing.Union[None, BaseLocation] = None
    permissions: typing.Union[None, BaseChatPermissions] = None
    active_usernames: list[str] = None
    emoji_status_custom_emoji_id: typing.Union[str, None] = None
    bio: typing.Union[str, None] = None
    has_private_forwards: typing.Union[bool, None] = None
    has_restricted_voice_and_video_messages: typing.Union[bool, None] = None
    join_to_send_messages: typing.Union[bool, None] = None
    join_by_request: typing.Union[bool, None] = None
    description: typing.Union[str, None] = None
    invite_link: typing.Union[str, None] = None
    slow_mode_delay: typing.Union[int, None] = None
    message_auto_delete_time: typing.Union[int, None] = None
    has_protected_content: typing.Union[bool, None] = None
    sticker_set_name: typing.Union[str, None] = None
    can_set_sticker_set: typing.Union[bool, None] = None
