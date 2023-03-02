def compare(l1,l2):
    small=0
    status=True
    for i in l2:
        if(small>i):
            small=i

    for j in l1:
        if(j>small):
            status= False
            break

    print(status)

    
def merge(l1,l2):
    l1 = l1 +l2
    print(l1)
