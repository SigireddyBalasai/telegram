from .content import content


class PhotoSize:
    def __init__(self):
        self.file_id: str = None
        self.file_unique_id: str = None
        self.width: int = None
        self.height: int = None
        self.file_size: int = None

    def set_data(self, context):
        self.file_id: str = content(context, "file_id")
        self.file_unique_id: str = content(context, "file_unique_id")
        self.width: int = content(context, "width")
        self.height: int = content(context, "height")
        self.file_size: int = content(context, "file_size")
