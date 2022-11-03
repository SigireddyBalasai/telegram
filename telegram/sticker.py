from PhotoSize import PhotoSize
from App import content
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
        self.premium_animation: File=None
        self.mask_position: MaskPosition=None
        self.custom_emoji: str=None
        self.file_size: int=None

    def set(self, context):
        self.file_id: str = content(context, 'file_id')
        self.file_unique_id: str = content(context, 'file_unique_id')
        self.type: str = content(context,'type')
        self.width: int =content(context, 'width')
        self.height: int = content(context, 'height')
        self.is_animated: bool = content(context, 'is_animated')
        self.is_video: bool = content(context, 'is_video')
        self.thumb: PhotoSize = PhotoSize().set(context['thumb'])
        self.emoji: str = content(context, 'emoji')
        self.set_name: str = content(context, 'set_name')
        self.premium_animation: File = File().set(context['premium_animation'])
        self.mask_position: MaskPosition = MaskPostion().set(context['mask_position'])
        self.custom_emoji: str = content(context, 'custom_emoji')
        self.file_size: int = content(context, 'file_size')
