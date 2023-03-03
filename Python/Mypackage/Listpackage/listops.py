def compare(l1,l2):
    n=len(l1)
    for i in range(n):
        if(l1[i]>l2[i]):
            return False
    return True
    
def merge(l1,l2):
    l1 = l1 +l2
    print(l1)
