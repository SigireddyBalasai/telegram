from dataclasses import dataclass
import typing


@dataclass
class BaseChatPermissions:
    """Chat Permissions Base"""
    can_send_messages: typing.Union[None, bool]
    can_send_media_messages: typing.Union[None, bool]
    can_send_polls: typing.Union[None, bool]
    can_send_other_messages: typing.Union[None, bool]
    can_add_web_page_previews: typing.Union[None, bool]
    can_change_info: typing.Union[None, bool]
    can_invite_users: typing.Union[None, bool]
    can_pin_messages: typing.Union[None, bool]
