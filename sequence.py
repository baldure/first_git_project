number= int(input("input an integer: "))
a= 1
b= 2
c= 3
d = a + b + c
teljari=1
while teljari < number+1:
    if teljari == 1:
        print(a)
    elif teljari == 2:
        print (b)
    elif teljari == 3:
        print (c)
    elif teljari == 4:
        print (d)
    else:
        a = b
        b = c
        c = d
        d = a + b + c
        print(d)

    teljari += 1


#0+1+2 = 3

#1+2+3 = 6

#2+3+6 = 11

#3+6+11 = 20

#6+11+20 = 37
