from PhotoSize import PhotoSize
from App import content
from typing import Union
from content import content

class VideoNote:

    def __init__(self):
        self.file_id: Union[str, None] = None
        self.file_unique_id: Union[str, None] = None
        self.duration: Union[int, None] = None
        self.length: Union[int, None] = None
        self.file_size: Union[int, None] = None
        self.thumb: Union[PhotoSize, None] = None

    def set_data(self, context):
        self.file_id: str = content(context, "file_id")
        self.file_unique_id: str = content(context, "file_unique_id")
        self.duration: int = content(context, "duration")
        self.length: int = content(context, 'length')
        self.file_size: int = content(context, 'file_size')
        self.thumb: PhotoSize = PhotoSize().set_data(context['thumb'])
