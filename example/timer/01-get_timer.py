import novapi

print("Timer Start!")
while not novapi.timer() == 10:
    print('Timer: ',novapi.timer())

print("Timer end with ",novapi.timer()," second")



