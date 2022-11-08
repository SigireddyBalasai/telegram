from App import content
class MessageAutoDeleteTimerChanged:
    def __init__(self):
        self.message_auto_delete_time: int=None
    def set_data(self, context):
        self.message_auto_delete_time: int = content(context, 'message_auto_delete_')