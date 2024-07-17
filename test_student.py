import unittest
from student import Student

class TestStudent(unittest.TestCase):
    
    def test_full_name(self):
        student = Student('Joe', 'Bloggs')

        self.assertEqual(student.full_name, 'Joe Bloggs')

    def test_alert_santa(self):
        student = Student('Joe', 'Bloggs')
        student.alert_santa()

        self.assertTrue(student.naughty_list)
    
    def test_email(self):
        student = Student('Joe', 'Bloggs')

        self.assertEqual(student.email, 'joe.bloggs@email.com')


if __name__== '__main__':
    unittest.main()