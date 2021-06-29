#!/usr/bin/python3
"""test module for filestorage """
import os
import unittest

import models
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class testFilestorage_instantination(unittest.TestCase):
    """unittest for instantiation of file storage class"""

    def test_Filestorge_instantination_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_Filestorage_instantination_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_Filestorage_intalization(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFilestorage_methods(unittest.TestCase):
    """unitest for the methdos of Filestorage"""

if __name__ == "__main__":
    unittest.main()
