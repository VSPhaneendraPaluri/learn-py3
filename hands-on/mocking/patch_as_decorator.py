from unittest import main, TestCase
from unittest.mock import patch

from class_under_test import PatchClass

class TestPatchClass(TestCase):

    def setUp(self):
        self.obj = PatchClass()

    @patch('class_under_test.PatchClass.m_2')
    def test_patch_as_decorator(self, m_2_mock):
            self.obj.m_1()
            m_2_mock.assert_called()


if __name__ == "__main__":
    main()

## Run it on the command line using 'python patch_as_cm.py' (since unittest.main() is called within the test)
## Otherwise run, >$ python -m unittest <test_class_file.py>
