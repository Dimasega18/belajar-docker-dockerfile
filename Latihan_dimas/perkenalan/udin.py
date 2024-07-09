x = '*'

while True:
    y = 9
    for i in range (1,11,2):
        print(" "*y+i*x)
        y-=1
    if i == 9 :
        break