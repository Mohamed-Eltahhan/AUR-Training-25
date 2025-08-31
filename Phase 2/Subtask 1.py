from random import randint

class Employee:
    def __init__(self, name, family, manager = None):
        self._name = name
        self._id = randint(1000, 9999)
        self._family = family
        self._manager = manager
        self.salary = 2500

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def family(self) -> dict:
        return self._family
    
    @property
    def manager(self):
        return self._manager
    
    def apply_raise(self, managed_employee: 'Employee', raise_percent: int):
        if managed_employee.manager == self:
            managed_employee.salary = managed_employee.salary * (1 + raise_percent/100)
            print(f'New salary: {managed_employee.salary}')
        else:
            print('Error: employee not managed by user')
    


# Test Code:
if __name__ == '__main__':
    boss = Employee('Jane Redmond', {})
    name = 'John Smith'
    family = {
        'Son': {
            'Insured' : True,
            'Age': 16
        },
        'Wife': {
            'Insured': False,
            'Age': 32
        }
    }
    my_employee = Employee(name, family, boss)
    not_boss = Employee('Adam Cater', {})

    print(id(my_employee.family))
    print(id(my_employee._family))
    boss.apply_raise(my_employee, 25)
    print(not_boss.apply_raise(my_employee, 25))