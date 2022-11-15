from PhotoSize import PhotoSize
from App import content
from typing import Union
from content import content

class Video:
    def __init__(self):
        self.file_id: Union[str, None] = None
        self.file_unique_id: Union[str, None] = None
        self.duration: Union[int, None] = None
        self.width: Union[int, None] = None
        self.height: Union[int, None] = None
        self.title: Union[str, None] = None
        self.file_name: Union[str, None] = None
        self.mime_type: Union[str, None] = None
        self.file_size: Union[int, None] = None
        self.thumb: Union[PhotoSize, None] = None

    def set_data(self, context):
        self.file_id: str = content(context, "file_id")
        self.file_unique_id: str = content(context, "file_unique_id")
        self.duration: int = content(context, "duration")
        self.width: str = content(context, "width")
        self.height: int = content(context, "height")
        self.title: str = content(context, "title")
        self.file_name: str = content(context, "file_name")
        self.mime_type: str = content(context, "mime_type")
        self.file_size: int = content(context, 'file_size')
        self.thumb: PhotoSize = PhotoSize().set_data(context['thumb'])
