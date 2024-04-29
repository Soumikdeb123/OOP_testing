class Date:
    monthNames = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    @classmethod
    def getMonthName(cls, number):
        if 1 <= number <= 12:
            return cls.monthNames[number - 1]
        else:
            return "Invalid month number"
    
    @classmethod
    def getDaysInMonth(cls, month, year=1):
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                return 29
            else:
                return 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31
    
    @classmethod
    def isValidYear(cls, year):
        return isinstance(year, int)
    
    @classmethod
    def isValidMonth(cls, month):
        return isinstance(month, int) and 1 <= month <= 12
    
    @classmethod
    def isValidDay(cls, day, month, year):
        if not cls.isValidMonth(month) or not cls.isValidYear(year):
            return False
        days_in_month = cls.getDaysInMonth(month, year)
        return 1 <= day <= days_in_month
    

# Task 1,2
# Testing getMonthName method
print(Date.getMonthName(1))  
print(Date.getMonthName(6))  
print(Date.getMonthName(12))

# Testing getDaysInMonth method
print(Date.getDaysInMonth(2, 2024))  
print(Date.getDaysInMonth(2, 2023)) 
print(Date.getDaysInMonth(4))

# Testing isValidYear method
print(Date.isValidYear(2021))  
print(Date.isValidYear("2021")) 
print(Date.isValidYear(0))     

# Testing isValidMonth method
print(Date.isValidMonth(6))   
print(Date.isValidMonth(15))  
print(Date.isValidMonth("7")) 

# Testing isValidDay method
print(Date.isValidDay(31, 12, 2023))  
print(Date.isValidDay(30, 4, 2021))   
print(Date.isValidDay(29, 2, 2021))   
