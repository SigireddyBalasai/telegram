from PhotoSize import PhotoSize
class Sticker:
    def __init__(self):
        self.file_id: str=None
        self.file_unique_id: str=None
        self.type: str=None
        self.width: int=None
        self.height: int=None
        self.is_animated: bool=None
        self.is_video: bool=None
        self.thumb: PhotoSize=None
        self.emoji: str=None
        self.set_name: str=None
        self.premium_animation: File =None