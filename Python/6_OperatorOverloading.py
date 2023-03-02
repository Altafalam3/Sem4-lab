class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show(self):
        print((self.x,self.y))

    def calAmp(self):
        amp = ((self.x)**2 + (self.y)**2)**0.5
        return amp

    def __lt__(self,v2):
        return (self.calAmp() < v2.calAmp())
    
    def __gt__(self,v2):
        return (self.calAmp() > v2.calAmp())

    def __le__(self,v2):
        return (self.calAmp() <= v2.calAmp())
    
    def __ge__(self,v2):
        return (self.calAmp() >= v2.calAmp())
        
    
v1 = vector(9,4)
v1.show()
v2 = vector(5,6)

status = v1<v2
print(status)

print(v1>v2)

print(v1<=v2)

print(v1>=v2)

