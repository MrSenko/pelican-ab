import os
import jinja_ab
# import pelican_ab
from unittest import TestCase


class PelicanAbTestCase(TestCase):
    def tearDown(self):
        "Clean-up the environment"
        if jinja_ab._ENV in os.environ:
            del os.environ[jinja_ab._ENV]
