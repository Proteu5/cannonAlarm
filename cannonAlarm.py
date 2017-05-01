from datetime import datetime
from threading import Timer
import webbrowser

### day+0 to test now
### day+1 for tomorrow
### Military Time for Hours

x=datetime.today()
y=x.replace(day=x.day+1, hour=5, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    print ("hello world")
    webbrowser.open('https://www.youtube.com/watch?v=Qvbm23xcFMo')
    #...

t = Timer(secs, hello_world)
t.start()
