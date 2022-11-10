def se():
    s1={5,8,9,10}
    s2={8,9,7,6}
    s1.add(6)
    print(s1)
    s1.remove(9)
    print(s1)
    print(s1|s2)
    print(s1&s2)
    return
def tup():
    t1=(8,9,7,1,2)
    t2=(5,4,2,1,7,6)
    print(t1*2)
    print(t1+t2)
    print(t1[0])
    print(t2[1:3])
    return
def li():
    l1=[8,97,5,10]
    l1.append(9)
    print(l1)
    l1.insert(2,20)
    print(l1)
    print(l1[0])
    return 
def dic():
    d={1:"one",2:"two",3:"three"}
    print(d.items())
    print(d.values())
    print(d.keys())
    print(d[2])
    return
while(True):
 print("  menu ")
 print("-------------")
 print("1:set")
 print("2:listt")
 print("3:dict")
 print("4:tuple")
 print("5:exit")
 option=int(input("ente your option no: "))
 if option==1:
     se()
 elif option==2:
     li()
 elif option==3:
     dic()
 elif option==4:
     tup()
 else:
     print('invalid opti')
     break