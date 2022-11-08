from content import content
from typing import Union


class Audio:
    def __init__(self):
        self.file_id: Union[str, None] = None
        self.file_unique_id: Union[str, None] = None
        self.duration: Union[int, None] = None
        self.mime_type: Union[str, None] = None
        self.file_size: Union[int, None] = None

    def set_data(self, context):
        self.file_id: str = content(context, "file_id")
        self.file_unique_id: str = content(context, "file_unique_id")
        self.duration: int = content(context, "duration")
        self.mime_type: str = content(context, "mime_type")
        self.file_size: int = content(context, 'file_size')
