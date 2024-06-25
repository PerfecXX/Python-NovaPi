import novapi
from time import sleep

print("Get Acceleration!")

while True:
    x_acc = novapi.get_acceleration("x")
    y_acc = novapi.get_acceleration("y")
    z_acc = novapi.get_acceleration("z")
    print("X: ",x_acc," Y: ",y_acc," Z: ",z_acc)
    sleep(0.5)
