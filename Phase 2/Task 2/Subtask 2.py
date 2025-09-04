from time import time
from rich.console import Console

console = Console()

def send_Msg(msg):
    if isinstance(msg, BaseMsg):
        console.print(msg, style = msg.style)
    else:
        print(msg)


class BaseMsg:
    def __init__(self, data: str):
        self._data = data

    @property
    def style(self):
        return ''
    
    @property
    def data(self) -> str:
        return self._data
    
    def __str__(self) -> str:
        return self._data
    
    def __len__(self) -> int:
        return len(self._data)
    
    def __eq__(self, other: object) -> bool:
        if str(self) == str(other):
            return True
        else:
            return False
        
    def __add__(self, other) -> object:
        if isinstance(self, WarnMsg):
            sum = WarnMsg(self.data + other.data)
            return sum
        elif isinstance(self, LogMsg):
            sum = LogMsg(str(self) + other.data)
            return sum
        else:
            sum = BaseMsg(str(self) + other.data)
            return sum
    
class LogMsg(BaseMsg):
    def __init__(self, data: str):
        super().__init__(data)  
        self._timestamp = time()

    @property
    def style(self):
        return 'default on yellow'

    def __str__(self) -> str:
        return f'[{self._timestamp}] {super().__str__()}'
    
class WarnMsg(LogMsg):
    @property
    def style(self):
        return 'white on red'
    
    def __str__(self) -> str:
        return f'[WARN!]{super().__str__()}'
    

if __name__ == '__main__':
    m1 = BaseMsg('Normal message')
    m2 = LogMsg('Log')
    m3 = WarnMsg('Warning')
    send_Msg(m1)
    send_Msg(m2)
    send_Msg(m3)