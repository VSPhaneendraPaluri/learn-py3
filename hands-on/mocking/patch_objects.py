from unittest import main, TestCase
from unittest.mock import patch

from class_under_test import PatchClass

class TestPatchObjects(TestCase):

    def setUp(self):
        self.obj = PatchClass()

    def test_patch_object_class_attribute_1(self, spec=True):
        with patch.object(self.obj, 'attribute_1') as acm:
            self.obj.m_4()
            self.assertEqual(10, self.obj.get_attribute_1())

    def test_patch_private_objects_attribute_2(self, spec=True):
        with patch.object(self.obj, '_PatchClass__attribute_2') as acm:
            with patch.object(self.obj, '_PatchClass__get_attribute_2') as fn_cm:
                self.obj.m_4()
                self.assertEqual(20, self.obj.get_attribute_2())
                fn_cm.return_value = 100
                self.assertEqual(fn_cm.return_value, self.obj._PatchClass__get_attribute_2())


if __name__ == "__main__":
    main()
