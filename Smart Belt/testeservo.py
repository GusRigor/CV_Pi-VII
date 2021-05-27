from servo import servo

servo1 = servo()
while True:
    servo1.to0()
    print('0')
    servo1.to45()
    print('45')
servo1.stop()