# -*- coding: utf-8 -*-
import os

from gitlint.tests.base import BaseTestCase
from gitlint.contrib import rules as contrib_rules
from gitlint.tests import contrib as contrib_tests

from gitlint.utils import ustr


class ContribRuleTests(BaseTestCase):

    def test_contrib_tests(self):
        """ Tests that every contrib rule file has an associated test file.
            While this doesn't guarantee that every contrib rule has associated tests (as we don't check the content
            of the tests file), it's a good leading indicator. """

        contrib_dir = os.path.dirname(os.path.realpath(contrib_rules.__file__))
        contrib_tests_dir = os.path.dirname(os.path.realpath(contrib_tests.__file__))
        contrib_test_files = os.listdir(contrib_tests_dir)

        # Find all python files in the contrib dir and assert there's a corresponding test file
        for filename in os.listdir(contrib_dir):
            if filename.endswith(".py") and filename not in ["__init__.py"]:
                expected_test_file = ustr(u"test_" + filename)
                error_msg = u"Every Contrib Rule must have associated tests. " + \
                            "Expected test file {0} not found.".format(os.path.join(contrib_tests_dir,
                                                                                    expected_test_file))
                self.assertIn(expected_test_file, contrib_test_files, error_msg)
