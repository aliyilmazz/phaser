from phaser import Phaser
import time



p1 = Phaser(1, "stage one")
p1.start()
time.sleep(3) # do some work
p1.end()


p2 = Phaser(2, "stage two")
p2.start()
time.sleep(5) # do some other work
p2.end()


p3 = Phaser(3, "final boss")
p3.start()
try:
    time.sleep(5) # throw some desperate punches
    raise Exception("boss is too strong")
except Exception as e:
    p3.end(error=e)
