from MessageEntity import MessageEntity
from content import content


class Poll:
    def __init__(self):
        self.id: str = None
        self.question: str = None
        self.options: PollOption = none
        self.total_voter_count: int = None
        self.is_closed: bool = None
        self.is_anonymous: bool = None
        self.type: str = None
        self.allows_multiple_answers: bool = None
        self.correct_option_id: int = None
        self.explanation: str = None
        self.explanation_entities: MessageEntity = None
        self.open_period: int = None
        self.close_date: int = None

    def set(self, context):
        self.id: str = content(context, 'id')
        self.question: str = content(context, 'question')
        self.options: PollOption = PollOption().set_data(context['options'])
        self.total_voter_count: int = content(context, 'total_voter_count')
        self.is_closed: bool = content(context, 'is_closed')
        self.is_anonymous: bool = content(context, 'is_anonymous')
        self.type: str = content(context, 'type')
        self.allows_multiple_answers: bool = content(context, 'allows_multiple_answers')
        self.correct_option_id: int = content(context, 'correct_options_id')
        self.explanation: str = content(context, 'explanation')
        self.explanation_entities: MessageEntity = MessageEntity().set_data(context['explanation_entities'])
        self.open_period: int = content(context, 'open_period')
        self.close_date: int = content(context, 'close_date')
