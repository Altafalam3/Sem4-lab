from abc import ABC,abstractmethod

class hello(ABC):
    @abstractmethod
    def calculate(self):
        pass

    @abstractmethod
    def update(self):
        pass

class customer(hello):
    def __init__(self,balance,acc):
        self.balance=balance
        self.acc=acc
        
    def calculate(self):
        interest=0
        if(self.acc=="saving"):
            interest=self.balance*0.04
        if(self.acc=="current"):
            interest=self.balance*0.06
        #print('interest ',interest)
        return interest

    def update(self):
        if(self.balance>100000):
            self.balance = self.balance + self.balance*0.05
        print('updated salary if 1lakh+  else same',self.balance)
    
class employee(hello):
    def __init__(self,classno,experience):
        self.classno=classno
        self.experience=experience

    def calculate(self):
        if(self.classno==1):
            self.salary=30000
            self.da=1.21 * self.salary
            self.hra=0.3*self.salary
            self.grossSalary=self.salary+self.da+self.hra
            
        if(self.classno==2):
            self.salary=20000
            self.da=1.15 * self.salary
            self.hra=0.3*self.salary
            self.grossSalary=self.salary+self.da+self.hra

        #print(f'gross salary for {self.classno} is {self.grossSalary}')
        return self.grossSalary

    def update(self):
        if(self.experience>15):
            self.grossSalary = self.grossSalary + self.grossSalary*0.2
        print('updated salary if 15+ years experience else same',self.grossSalary)

        
c1 = customer(200000,'saving')
print('Cust Calculating interest' , c1.calculate())
c1.update()


e1= employee(1,16)
print('Emp Calculating gross salary' , e1.calculate())
e1.update()

