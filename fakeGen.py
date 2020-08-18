
def ip():
    from random import randint
    ip=""
    for i in range(4):
        num=random.randint(0, 255)
        if(i!=3):
            ip+=str(num)+"."
        else:
            ip+=str(num)
    return ip
