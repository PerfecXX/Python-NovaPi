import novapi
from time import sleep

novapi.set_shake_threshold(50)

while True:
    if novapi.is_shaked():
        print('Shake Detected!')
    else:
        print('No Shake Detected!')
    time.sleep(0.5)
