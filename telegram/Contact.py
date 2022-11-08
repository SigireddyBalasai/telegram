from content import content


def Contact():
    def __init__(self):
        self.phone_number: str = None
        self.first_name: str = None
        self.last_name: str = None
        self.user_id: int = None
        self.vcard: int = None

    def set_data(self, context):
        self.phone_number: str = content(context, "phone_number")
        self.first_name: str = content(context, "first_name")
        self.last_name: str = content(context, "last_name")
        self.user_id: int = content(context, "user_id")
        self.vcard: int = content(context, "vcard")
