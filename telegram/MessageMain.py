from .BaseClasses.Message_base import Base_Message, MessageSending


class Message(Base_Message):
    def __init__(self, context: dict):
        self.from_user = context.pop("from")

        super().__init__(**context)

    async def replay(self,object : MessageSending):
        object.chat_id = self.from_user['id']
        print(object.__dict__)
        await Message.send_message(object)
