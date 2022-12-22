from telegram.BaseClasses.Animation_base import BaseAnimation


class Animation(BaseAnimation):
    def __init__(self,context:dict):
        self.animation = super(**context)

