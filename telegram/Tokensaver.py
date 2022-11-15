class TokenSaver:
    token: str
    base_url = "https://api.telegram.org/bot"
    command_prefix : str

    def __init__(self, token, prefix):
        TokenSaver.token = token
        TokenSaver.command_prefix = prefix
