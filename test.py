import time
import webbrowser

take_breake = 3
break_count = 0

while break_count< take_breake:
    print(time.ctime())
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=cbIE1x8aJe8&list=RDMMS3Wimxxq7xc&index=5")
    break_count = break_count+1