from App import content


class File:
    def __init__(self):
        self.file_id: str = None
        self.file_unique_id: str = None
        self.file_size: int = None
        self.file_path: str = None

    def set(self, context):
        self.file_id: str = content(context, 'file_id')
        self.file_unique_id: str = content(context, 'file_unique_id')
        self.file_size: int = content(context, 'file_size')
        self.file_path: str = content(context, 'file1_path')
