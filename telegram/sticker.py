from PhotoSize import PhotoSize
from typing import Union
class Sticker:
    def __init__(self):
        self.file_id: Union[str,None]=None
        self.file_unique_id: Union[str,None]=None
        self.type: Union[str,None]=None
        self.width: Union[int,None]=None
        self.height: Union[int,None]=None
        self.is_animated: Union[bool,None]=None
        self.is_video: Union[bool,None]=None
        self.thumb: Union[PhotoSize,None]=None
        self.emoji: Union[str,None]=None
        self.set_name: Union[str,None]=None
        #self.premium_animation: Union[File,None] =None