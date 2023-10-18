import os
import sys

from test_template.math_functions import basic_functions

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import test_template  # noqa # pylint: disable=unused-import, wrong-import-position
from test_template.email_functions.email import \
    EmailUsers  # noqa # pylint: disable=unused-import, wrong-import-position
from test_template.math_functions import \
    basic_functions  # noqa # pylint: disable=unused-import, wrong-import-position
