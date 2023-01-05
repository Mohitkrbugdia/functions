def back():
    '''to come back'''
            
    print("1= right angle")
    print("2= table")

    a=int(input("enter: "))
    if a==1:
        for i in range(1,11):
            for j in range(1,i):
                print("*",end='')
            print()
    else:
        a=int(input("enter: "))
        for i in range(1,11):
            print(a,'*',i,'=',a*i)
back()
print()
for i in range(11):
    back()
