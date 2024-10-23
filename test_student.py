# setUp and tearDown defined using camel case

import unittest
from student import Student # from student.py, import Student class
from datetime import timedelta
from unittest.mock import patch # used for mocking (in this case, making a request to the fictional API service)

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')


    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


    def setUp(self): # used to create temp files and folders or set up db connection during tests
        print('setUp')
        self.student = Student('John', 'Doe')


    def tearDown(self): # used to remove temp files or folders or close db connection
        print('tearDown')


    def test_full_name(self): # test 1
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')
    

    def test_start_date(self):  # test 2
        print(self.student._start_date)


    def test_email(self): # test 3
        print('test_email')
        self.student = Student('John', 'Doe')
        self.assertEqual(self.student.email, 'john.doe@email.com')


    def test_alert_santa(self): # test 4
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list) # checks if the value is True
    

    def test_apply_extension(self):  # test 5
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))


    def test_course_schedule_success(self): # test 6
        with patch("student.requests.get") as mocked_get: #creates an object called 'mocked_get' which we can use to test the get request functionality.
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")


    def test_course_schedule_fail(self): # test 7
        with patch("student.requests.get") as mocked_get: #creates an object called 'mocked_get' which we can use to test the get request functionality.
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")

if __name__ == '__main__':
    unittest.main()