from pynput.keyboard import Key, Controller
import random
import time

keyboard = Controller()
waitX = random.randint(2,10)
waitY = random.randint(2,10)
waitZ = random.randint(2,10)
count = 1
print('------------------------------------------------------')
print('--------Please open tinder web page and wait :)-------')
print('----------------github.com/hasretozkan----------------')
print('--------------------hasretozkan.me--------------------')
print('------------------------------------------------------')

print('Starting in 5 seconds.')
time.sleep(1)
print('Starting in 4 seconds.')
time.sleep(1)
print('Starting in 3 seconds.')
time.sleep(1)
print('Starting in 2 seconds.')
time.sleep(1)
print('Starting in 1 seconds.')
time.sleep(1)
print('STARTING')

while True:
    if count % waitX == 0 and count % waitY == 0:
            zzz = random.uniform(5,10)
            print('Short Delay %.2f seconds'% zzz)
            time.sleep(zzz)
    elif count % waitY == 0 and count % waitZ == 0:
        zzz = random.uniform(5,10)
        print('Short Delay %.2f seconds'% zzz)
        time.sleep(zzz)
    elif count % waitX == 0 and count % waitY == 0 and count % waitZ == 0:
        zzz = random.uniform(10,15)
        print('Short Delay %.2f seconds'% zzz)
        time.sleep(zzz)
    else:
        luck = random.random()
        zzz = random.uniform(1,4)
        print('Sleeping %.2f seconds'% zzz)
        time.sleep(zzz)

        if luck <= 0.85:
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            print('Liked')
        else:
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            print('Disliked')
    
    count += 1
