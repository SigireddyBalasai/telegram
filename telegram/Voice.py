from PhotoSize import PhotoSize
from App import content


class Audio:
    def __init__(self):
        self.file_id: str = None
        self.file_unique_id: str = None
        self.duration: int = None
        self.mime_type: str = None
        self.file_size: int = None

    def set(self, context):
        self.file_id: str = content(context, "file_id")
        self.file_unique_id: str = content(context, "file_unique_id")
        self.duration: int = content(context, "duration")
        self.mime_type: str = content(context, "mime_type")
        self.file_size: int = content(context, 'file_size')
