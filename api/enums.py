from enum import Enum
class TimeInterval(Enum):    
    ONE = '1min'
    FIVE =  '5min'
    FIFTEEN = '15min'
    HALF = '30min'
    HOUR = '60min'

class SetupStatus(Enum):    
    active = 'Active'    
    disabled = 'Disabled'