from .PhotoSize import PhotoSize
from .App import content


class Animation:
    def __init__(self):
        self.file_id: str = None
        self.file_unique_id: str = None
        self.width: int = None
        self.height: int = None
        self.duration: int = None
        self.thumb: PhotoSize = None
        self.file_name: str = None
        self.mime_type: str = None
        self.file_size: int = None

    def set_data(self, context):
        self.file_id: str = content(context, 'file_id')
        self.file_unique_id: str = content(context, 'file_unique_id')
        self.width: int = content(context, 'width')
        self.height: int = content(context, 'height')
        self.duration: int = content(context, 'duration')
        self.thumb: PhotoSize = PhotoSize().set_data('thumb')
        self.file_name: str = content(context, 'file_name')
        self.mime_type: str = content(context, 'mime_type')
        self.file_size: int = content(context, 'file_size')
