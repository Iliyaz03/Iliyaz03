def a():
    return ("привет")
print(a())

def a(b,c,d):
    for e in b,c,d:
        print(e)
a("привет","мир","как дела")

def aa(*bb):
    for cc in bb:
        print(cc)
aa(1,2,3)

def aaa(*bbb):
    for ccc in bbb:
        print(ccc,len(ccc))
aaa("Илияз","Ислам","Бека","Сыймык")

def aaa(**bbb):
    for ccc,ddd in bbb.items():
        print(ccc,ddd)
aaa(name="Илияз",film="Поймай меня если сможешь")

def aaa(bbb,ccc):
    for ddd in range(ccc):
        bbb=bbb*1.1
        print(bbb)
aaa(3000,5)






