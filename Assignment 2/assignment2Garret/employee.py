#employee.py
 #defining the employee class and attibutes of an employee object
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

    #method that calculates the total salary of the employees
    def calc_hourly_salary(self):
        #calculates gross pay
        gross = self.hours_worked * self.hourly_rate

        #sum provincial and federal deductions
        deductions = self.deduction_province + self.deduction_federal

        #subtract deductions from gorss pay and adds education allowance
        total_salary = gross - deductions + self.education_allowance
        return total_salary
