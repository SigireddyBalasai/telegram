import asyncio
from .Tokensaver import TokenSaver
from .prase import Praser


class Commands:
    ok = Praser()
    commands_list = dict()

    def __init__(self, content):
        self.prased_command = Commands.ok.prase(content)
        self.call()

    def call(self):
        loop = asyncio.get_running_loop()
        if(self.prased_command.message.text != None):
            ok = self.prased_command.message.text.replace(" ","_")
            print(ok)
            if (ok[1:] in Commands.commands_list.keys()) and (ok[0] == TokenSaver.command_prefix):
                print("command_running")
                loop.create_task(Commands.commands_list[self.prased_command.message.text[1:].replace(" ","_")](self.prased_command))
        else:
            print(Commands.commands_list)
            loop.create_task(Commands.commands_list["Audio"](self.prased_command))

    @classmethod
    def add_command(cls, func):
        cls.commands_list[func.__name__] = func
