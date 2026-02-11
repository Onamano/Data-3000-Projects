#employee.py

class Employee:
    def __init__(self, emp_id, name, hours_worked, hourly_rate,
                 deduction_province, deduction_federal, education_allowance):
        self.emp_id = emp_id
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.deduction_province = deduction_province
        self.deduction_federal = deduction_federal
        self.education_allowance = education_allowance

    def calc_hourly_salary(self):
        gross = self.hours_worked * self.hourly_rate
        deductions = self.deduction_province + self.deduction_federal
        total_salary = gross - deductions + self.education_allowance
        return total_salary
