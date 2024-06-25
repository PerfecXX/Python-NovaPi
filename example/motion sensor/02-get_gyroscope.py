import novapi
from time import sleep

print("Get Gyroscope!")

while True:
    x_gyro = novapi.get_gyroscope("x")
    y_gyro = novapi.get_gyroscope("y")
    z_gyro = novapi.get_gyroscope("z")
    print("X: ",x_gyro," Y: ",y_gyro," Z: ",z_gyro)
    sleep(0.5)
