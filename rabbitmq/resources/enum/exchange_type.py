from enum import Enum

class ExchangeType(Enum):
    Direct = 'direct'
    Fanout = 'fanout'
    Headers = 'headers'
    Topic = 'topic'

