"""
Test suite for continuous integration build verification
"""
import unittest
from service import app_running


class TestService(unittest.TestCase):
    """Basic unit tests to ensure application test harness functions"""

    def test_service_running(self):
        """Test service is operational"""
        self.assertTrue(app_running())


if __name__ == '__main__':
    unittest.main()
