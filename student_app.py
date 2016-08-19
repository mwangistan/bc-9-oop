import student
from student import Student

#create atleast 10 students
s1 = Student('Kevin', 'Chiteri')
s2 = Student('Allan', 'Mwangi', 'UG')
s3 = Student('Mike', 'Njoro')
s4 = Student('Liz', 'Omondi', 'NG')
s5 = Student('Kim', 'Kioko')
s6 = Student('Baraza', 'Priza', 'TZ')
s7 = Student('Paul', 'Akoth')
s8 = Student('Omondi', 'Mwendwa')
s9 = Student('Angie', 'Waweru')
s10 = Student('Beth', 'Quasi')

#Make atleast 5 students attend class
s1.attend_class(date='2016, 8, 18', id= s1.id, first_name=s1.fname, last_name=s1.lname, country=s1.country)
s2.attend_class(date = '2016, 8, 13', teacher='Mwaleh', id= s2.id, first_name=s2.fname, last_name=s2.lname, country=s2.country)
s3.attend_class(date='2016, 8, 15', id= s1.id, first_name=s3.fname, last_name=s3.lname, country=s3.country)
s4.attend_class(date='2016, 8, 18', teacher='Nandaa', id= s4.id, first_name=s4.fname, last_name=s4.lname, country=s4.country)
s5.attend_class(date='2016, 8, 18', id= s5.id, first_name=s5.fname, last_name=s5.lname, country=s5.country)

'''You should be able to print the list of
 students who attend class on a particular 
 day'''

print(student.student_attendance(date = '2016, 8, 18'))




