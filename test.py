from main import App
from User import User
from Message import Message
import asyncio
ok = App()
hello = asyncio.run(ok.run(token="5764436314:AAHqvTxI4LLfkK6ilKC2Y4hEo-OW9-oM0g0"))
asyncio.run(Message.copy_message()