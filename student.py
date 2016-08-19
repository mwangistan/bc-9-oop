from datetime import datetime

map_ ={
	'KE': 'Kenya',
	'NG': 'Nigeria',
	'UG': 'Uganda',
	'TZ': 'Tanzania'
}

class Student(object):

	attended = []
	unique_id = 0
	def __init__(self, fname, lname, cc='KE'):
		Student.unique_id += 1
		self.id = Student.unique_id
		self.fname = fname
		self.lname = lname
		self.country = map_[cc]

	#Add students who attended to a list

	def attend_class(self, **kwargs):
		
		self.loc = kwargs.setdefault('loc', 'Hogwarts')
		self.date = kwargs.setdefault('date', datetime.today().date())
		self.teacher = kwargs.setdefault('teacher', 'Alex')

		Student.attended.append(kwargs)

	#Print students who attended on a specific date

def student_attendance(date=datetime.today().date()):
	for item in Student.attended:
		if item['date'] == date:
			print item

		


