from unittest import main, TestCase
from unittest.mock import patch
import builtins

import os

class TestBuiltIns(TestCase):

    @patch('os.listdir')
    def test_patch_os_listdir(self, os_listdir_mock):
        expected_list = ['dir_a', 'dir_b', 'file_a.xml']
        os_listdir_mock.return_value = ['dir_a', 'dir_b', 'file_a.xml']
        self.assertCountEqual(expected_list, os_listdir_mock.return_value)

    @patch('os.walk')
    def test_patch_os_walk(self, os_walk_mock):
        #
        #  dir_parent
        #  |     L_____ file_1.bit
        #  |
        #  L____ dir_child
        #         L____ file_2.bit
        #
        test_directory_contents = {
            ('\dir_parent', '\dir_child', '\\file_1.bit'),
            ('\dir_parent\dir_child', '', '\\file_2.bit')
        }
        expected_root_list = ['\dir_parent', '\dir_parent\dir_child']
        expected_dir_list = ['\dir_child', '']
        expected_file_list = ['\\file_1.bit', '\\file_2.bit']

        os_walk_mock.return_value = test_directory_contents

        root_list = []
        dir_list = []
        file_list = []
        for r, d, f in os.walk(test_directory_contents):
            root_list.append(r)
            dir_list.append(d)
            file_list.append(f)
        
        self.assertCountEqual(expected_root_list, root_list)
        self.assertCountEqual(expected_dir_list, dir_list)
        self.assertCountEqual(expected_file_list, file_list)


if __name__ == "__main__":
    main()
