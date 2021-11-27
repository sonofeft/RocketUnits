import unittest
# import unittest2 as unittest # for versions of python < 2.7

import sys, os

here = os.path.abspath(os.path.dirname(__file__)) # Needed for py.test
up_one = os.path.split( here )[0]  # Needed to find rocketunits development version
if here not in sys.path[:2]:
    sys.path.insert(0, here)
if up_one not in sys.path[:2]:
    sys.path.insert(0, up_one)
    
from rocketunits.rocket_units import convert_value, main, convert_string, \
                                     chk_units_in_category, get_category

class MyTest(unittest.TestCase):

    # def setUp(self):
    #     unittest.TestCase.setUp(self)

    # def tearDown(self):
    #     unittest.TestCase.tearDown(self)

    def test_should_always_pass_cleanly(self):
        """Should always pass cleanly."""
        pass

    def test_get_units_category(self):
        """test get units category"""
        a = get_category("degF")
        self.assertEqual(a, "Temperature")

        a = get_category("psia")
        self.assertEqual(a, "Pressure")

        a = get_category("nuttin")
        self.assertEqual(a, "")


    def test_bad_convert_string(self):
        """test bad convert_string"""
        
        with self.assertRaises(Exception):
            result = convert_string( sinp="1 atm ft", rtn_units="psia" )

    def test_exercise_chk_units_in_category(self):
        """test exercise chk_units_in_category"""

        a = chk_units_in_category("degF", "Temperature")
        self.assertEqual(a, True)

        with self.assertRaises(Exception):
            a = chk_units_in_category("psia", "Temperature")

        with self.assertRaises(Exception):
            a = chk_units_in_category("psia", "Press")

        with self.assertRaises(Exception):
            a = chk_units_in_category("F", "Temperature")

    def test_myclass_existence(self):
        """Check that function returns result"""
        result = convert_value(1.0, 'lbm', 'g')

        # Function should return None
        self.assertAlmostEqual(result, 453.59237, places=3)  # a within 3 decimal places of b

    def test__main__(self):
        """test the __main__ section of rocket_units"""
        if sys.version_info[0] == 3 and sys.version_info[1] >= 5:
            import importlib.util
            file_path = os.path.join( up_one, 'rocket_units.py' )
            spec = importlib.util.spec_from_file_location( '__main__', file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        # else:
        #     main()

# if __name__ == '__main__':
#     # Can test just this file from command prompt
#     #  or it can be part of test discovery from nose, unittest, pytest, etc.
#     unittest.main()

