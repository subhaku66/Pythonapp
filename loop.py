#For Loop

#print 1 to 10
i=1

for i in range(1,100):
     print(i)

for i in range(1,100):
    if (i%2)==0:
        print("even")
        print(i)
    else:
        print('odd number')
        print(i)

print ('------')
a1=100
a2=200
for j in range(a1,a2):
    print(j)
    if j==110:
        break
'''
#while loop
a=10
while(True):
    a=a+1
    print(a)
    if(a==100):
        break
'''

print('------------------------------')
a="bangalore"
for i in a:
    #print(i)
    if(i=="a"):
        print(i)
    elif(i=="e"):
        print(i)
    elif(i=="i"):
        print(i)
    elif(i=="o"):
        print(i)
    elif(i=="u"):
        print(i)
    else:
        print("not a vwoel")

for i in range(100,120):
    if(i%2==0):
        print("%s is a Even number "%(i))

    else:
       pass