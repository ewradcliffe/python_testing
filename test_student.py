import unittest
from student import Student
from datetime import timedelta

class TestStudent(unittest.TestCase):

    def setUp(self):
        print('setUP')
        self.student = Student('Joe', 'Bloggs')
        

    def tearDown(self):
        print('tearDown')
    
    def test_full_name(self):
        self.assertEqual(self.student.full_name, 'Joe Bloggs')

    def test_alert_santa(self):
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)
    
    def test_email(self):

        self.assertEqual(self.student.email, 'joe.bloggs@email.com')

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days = 5))
        



if __name__== '__main__':
    unittest.main()