def delchar(s,c):
    if len(c)==1:
        for i in s:
            if c!=i:
                print(i,end="")
    else:
        print(s)
s=str(input("enter the string= "))
c=str(input("which word have to romove= "))
delchar(s,c)
