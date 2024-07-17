import unittest
from student import Student

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


if __name__== '__main__':
    unittest.main()