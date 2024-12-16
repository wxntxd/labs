from codecs import replace_errors
class Employee:
    def __init__(self,name, e_id):
        self.name = name
        self.e_id = e_id
    def get_info(self):
        return f"Employee's name is {self.name}, and id: {self.e_id}"
class Manager(Employee):
    def __init__(self,name,e_id,department):
        super().__init__(name, e_id)
        self.department = department
    def manage_project (self,manage_project):
        return  f"  Manager department is {self.department} and his project is {self.manage_project}"
class Technician(Employee):
    def __init__(self, name, e_id, specialization):
        super().__init__(name, e_id)
        self.specialization = specialization
    def perform_maintenance(self):
        return f"Technician is {self.name} and perform mainteance is {self.specialization}. His id is {self.e_id}"
class TechManager(Manager, Technician):
    def __init__(self, name, e_id,specialization, department ):
        self.manager = Employee(name,e_id)
        self.department = department
        self.specialization =specialization
        workers = []
    def add_employee(self, employeers):
        self.workers.append(employeers)
    def get_team_info(self):
        info = [workers.get_info() for  workers in  self.workers]
        return info

    def __str__(self):
        return f"{self.manager.name},her id : {self.manager.e_id} specialization: {self.specialization} department: {self.department}"
emp1 = Employee("Alex" , 77)
tech = Technician ("John" , 444, "programmer")
tech_manager = TechManager("Alice" , 123, "programmer" , "Backend")
print(emp1.get_info())
print(tech.get_info())
print(tech_manager)