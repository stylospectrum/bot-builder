import enum


class BotResponseType(str, enum.Enum):
    Text = ("Text",)
    RandomText = ("RandomText",)
    Image = "Image"
    Gallery = "Gallery"
    QuickReply = "QuickReply"
