"""
Test Vocabulary creation in iRODS.
"""

import unittest
import subprocess
import shutil
import os

from tests import VocabConfig


class TestCreateVocabularyRule(unittest.TestCase, VocabConfig):
    def setUp(self):
        # subprocess.call(['su', '-', VOCAB_AUTHOR])
        subprocess.call(['irm', self.VOCAB_NAME])

        if os.path.exists(self.VOCAB_DIR):
            shutil.rmtree(self.VOCAB_DIR)

        VocabConfig.copy_vocab_rules_file_to_etc_irods()

    def test_create_valid_vocab_rule(self):
        """
        mlxCreateVocabulary rule should be executed successfully in iRODS when adding a vocabulary to
        a collection that does not have one.
        """

        self.assertTrue(VocabConfig.call_create_vocab_rule() == 0)

    def tearDown(self):
        VocabConfig.rm_rf_vocab_file()


class TestCreateVocabularyInFileSystem(unittest.TestCase, VocabConfig):
    def setUp(self):
        # subprocess.call(['su', '-', VOCAB_AUTHOR])
        subprocess.call(['irm', self.VOCAB_NAME])

        if os.path.exists(self.VOCAB_DIR):
            shutil.rmtree(self.VOCAB_DIR)

        VocabConfig.copy_vocab_rules_file_to_etc_irods()

        VocabConfig.call_create_vocab_rule()

    def test_create_valid_vocab_dir_tree(self):
        """
        mlxCreateVocabulary rule should create a vocabulary tree under the vocabularies directory
        in the local file system
        """
        self.assertTrue(os.path.exists(self.VOCAB_DIR))

    def test_create_valid_vocab_db_file(self):
        """
        mlxCreateVocabulary rule should create a *.vocab file in the file system
        """

        self.assertTrue(os.path.join(self.VOCAB_DIR, self.IRODS_TEST_COLL_PATH, self.VOCAB_NAME))

    def tearDown(self):
        VocabConfig.rm_rf_vocab_file()


class TestCreateVocabularyInIRODS(unittest.TestCase, VocabConfig):
    def setUp(self):
        # subprocess.call(['su', '-', VOCAB_AUTHOR])
        subprocess.call(['irm', self.VOCAB_NAME])

        if os.path.exists(self.VOCAB_DIR):
            shutil.rmtree(self.VOCAB_DIR)

        VocabConfig.copy_vocab_rules_file_to_etc_irods()

        VocabConfig.call_create_vocab_rule()

    def test_create_valid_vocab_is_linked(self):
        """
        mlxCreateVocabulary rule should link the vocabulary database file to iRODS
        """

        self.assertIn(self.VOCAB_NAME, subprocess.check_output(['ils']))

    def tearDown(self):
        VocabConfig.rm_rf_vocab_file()


if __name__ == '__main__':
    unittest.main()