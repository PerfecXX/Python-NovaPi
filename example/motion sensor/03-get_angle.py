import novapi
from time import sleep

print("Get Angle!")

while True:
    x_degree = novapi.get_pitch()
    y_degree = novapi.get_roll()
    z_degree = novapi.get_yaw()
    print("X: ",x_degree,"Y: ",y_degree,"Z: ",z_degree)
    sleep(0.5)
