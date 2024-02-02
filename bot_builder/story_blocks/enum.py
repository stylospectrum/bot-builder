import enum


class StoryBlockType(str, enum.Enum):
    UserInput = 'UserInput'
    BotResponse = 'BotResponse'
    StartPoint = 'StartPoint'
    DefaultFallback = 'DefaultFallback'
