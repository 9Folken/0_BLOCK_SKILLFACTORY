import unittest
from unittest.mock import patch

class BasicTest(unittest.TestCase):
    # Тест для значений 'John' и 'Friday'
    # Результат должен быть 'Hello, John! Today is Friday. Have a nice day!'
    @patch('builtins.print')
    def test_print_with_default_params(self, print_):
        import for_testing 
        print_.assert_called_once_with('Hello, John! Today is Friday. Have a nice day!')


if __name__ == '__main__':
    unittest.main()