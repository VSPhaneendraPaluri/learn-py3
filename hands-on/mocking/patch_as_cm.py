from unittest import main, TestCase
from unittest.mock import patch

from class_under_test import PatchClass

class TestPatchClass(TestCase):

    def setUp(self):
        self.obj = PatchClass()

    def test_patch_as_context_manager_with_incorrect_import(self):
        with patch('PatchClass.m_2') as cm:
            self.obj.m_1()
            cm.assert_called()

    def test_patch_as_context_manager_with_correct_assert(self):
        with patch('class_under_test.PatchClass.m_2') as cm:
            self.obj.m_1()
            cm.assert_called()

    def test_patch_as_context_manager_with_incorrect_assert(self):
        with patch('class_under_test.PatchClass.m_2') as cm:
            self.obj.m_1()
            cm.assert_not_called()


if __name__ == "__main__":
    main()

## Run it on the command line using 'python patch_as_cm.py' (since unittest.main() is called within the test)
## Otherwise run, >$ python -m unittest <test_class_file.py>


