import pytest


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f' Name: {self.name}, Salary: {self.salary}'


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

    def __str__(self):
        return f' Name: {self.name}, Salary: {self.salary}, department: {self.department}'


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

    def __str__(self):
        return f' Name: {self.name}, Salary: {self.salary}, Programming language: {self.programming_language}'


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

    def __str__(self):
        return f' Name: {self.name}, Salary: {self.salary}, department: {self.department}, ' \
               f'Programming language: {self.programming_language}, team size: {self.team_size}'


@pytest.mark.parametrize(
    "name, salary, department, programming_language, team_size",
    [
        ("Viktor", 3000, "RDT", "Python", 10),
        ("Peter", 5000, "Challengers", "C++", 8),
        ("Olga", 2500, "Retro", None, 7),
        ("Denis", 4000, None, "Java", None),
     ],
    )
def test_check_teamlead_parameters(name, salary, department, programming_language, team_size):
    teamlead = TeamLead(name, salary, department, programming_language, team_size)
    teamlead.__str__()
    print(teamlead.programming_language)
    if not teamlead.department:
        raise AttributeError(f' Parameter department is missing for {teamlead.name}')
    elif not teamlead.programming_language:
        raise AttributeError(f'Parameter programming_language is missing for {teamlead.name}')



