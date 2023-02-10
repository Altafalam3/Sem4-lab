class employee:
    def __init__(self,fname,lname,age,basic):
        self.first_name=fname
        self.last_name=lname
        self.age=age
        self.basic_salary=basic
        self.email=fname+"."+lname+"@gmail.com"

    def show(self):
        print(f"Name : {self.first_name} {self.last_name}")
        print(f"Age : {self.age} \nSalary : {self.basic_salary}")
        print(f"Email : {self.email}")


class developer(employee):
    def __init__(self,fname,lname,age,basic,lang):
        super().__init__(fname,lname,age,basic)
        self.language=lang

    def show(self):
        super().show()
        print(f"Language : {self.language}")


class manager(employee):
    def __init__(self,fname,lname,age,basic,subordinates):
        super().__init__(fname,lname,age,basic)
        self.subordinates=subordinates

    def show(self):
        super().show()
        print(f"Subordinates : {self.subordinates}")

    def addEmployee(self,newEmp):
        self.subordinates.append(newEmp)


em1 = manager("Altaf","Alam",20,90000000000000000000,["Anmol","Mitesh","Chetan"])

em1.show()

em1.addEmployee("Alok")
print("\n\nAfter update of employee")
em1.show()






