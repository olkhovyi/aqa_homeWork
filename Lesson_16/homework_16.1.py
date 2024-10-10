class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


    def display_info(self):
        return (f"Name: {self.name}, Salary: {self.salary}, "
                f"Department: {self.department}, Programming language: {self.programming_language}, "
                f"Team size: {self.team_size}")


team_lead = TeamLead("Alex", 4000, "NASA", "Python", 3)
print(team_lead.display_info())