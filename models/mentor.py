class Person:
    def __init__(self, name):
        self.name = name

    def profile(self):
        return f"Person: {self.name}"


class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

    def employee_details(self):
        return f"Employee ID: {self.employee_id}"


class Mentor:
    def __init__(self, specialization):
        self.specialization = specialization

    def mentor_details(self):
        return f"Specialization: {self.specialization}"


class TESRECOMentor(Person, Employee, Mentor):
    def __init__(self, name, employee_id, specialization):
        Person.__init__(self, name)
        Employee.__init__(self, employee_id)
        Mentor.__init__(self, specialization)

    @classmethod
    def display_mro(cls):
        return [klass.__name__ for klass in cls.mro()]

    def summary(self):
        return f"{self.name} ({self.employee_id}) - {self.specialization}"


if __name__ == "__main__":
    mentor = TESRECOMentor("Dr. Kavya", "EMP001", "AI/ML")
    print(mentor.summary())
    print(TESRECOMentor.display_mro())
