"""
Create a student class (name the file StudentClass.py). The class 
should have 4 attributes. StudentID, Name, DOB and classification 
(F,S,Jr,Sr). 
• Create a method that will calculate the student’s current age 
• Create a method that will determine when the student can 
register – 
• Seniors – 4/1 thru 4/3
• Juniors – 4/4 thru 4/6
• Sophomores – 4/7 thru 4/9
• Freshmen – 4/10 thru 4/12
• Create a method to return the age and another method to return 
the registration dates
"""


from datetime import date, datetime


class Student:
    def __init__(self, stuID, fullName, Birthday, year):
        self.__StudentID = int(stuID)
        self.__Name = fullName
        self.__DateOfBirth = date(Birthday)
        self.__classifcation = year

    def determine_age(self):
        current_day = date.today()
        self.__age = self.__DateOfBirth - current_day
        return self.__age

    # def determine_registration(self):
