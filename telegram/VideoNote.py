from PhotoSize import PhotoSize
from App import content


class VideoNote:

    def __init__(self):
        self.file_id: str = None
        self.file_unique_id: str = None
        self.duration: int = None
        self.length: int = None
        self.file_size: int = None
        self.thumb: PhotoSize = None

    def set(self, context):
        self.file_id: str = content(context, "file_id")
        self.file_unique_id: str = content(context, "file_unique_id")
        self.duration: int = content(context, "duration")
        self.length: int = content(context, 'length')
        self.file_size: int = content(context, 'file_size')
        self.thumb: PhotoSize = PhotoSize().set(context['thumb'])
