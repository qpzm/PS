import unittest
import run_length

class MyTest(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(run_length.encode('HHHeellloWooorrrrlld!!'), 'H3e2l3o1W1o3r4l2d1!2')

    def test_decode(self):
        self.assertEqual('HHHeellloWooorrrrlld!!', run_length.decode('H3e2l3o1W1o3r4l2d1!2'))


if __name__ == '__main__':
    unittest.main()
