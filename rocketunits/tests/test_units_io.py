import unittest
# import unittest2 as unittest # for versions of python < 2.7

"""
        Method                            Checks that
self.assertEqual(a, b)                      a == b   
self.assertNotEqual(a, b)                   a != b   
self.assertTrue(x)                          bool(x) is True  
self.assertFalse(x)                         bool(x) is False     
self.assertIs(a, b)                         a is b
self.assertIsNot(a, b)                      a is not b
self.assertIsNone(x)                        x is None 
self.assertIsNotNone(x)                     x is not None 
self.assertIn(a, b)                         a in b
self.assertNotIn(a, b)                      a not in b
self.assertIsInstance(a, b)                 isinstance(a, b)  
self.assertNotIsInstance(a, b)              not isinstance(a, b)  
self.assertAlmostEqual(a, b, places=5)      a within 5 decimal places of b
self.assertNotAlmostEqual(a, b, delta=0.1)  a is not within 0.1 of b
self.assertGreater(a, b)                    a is > b
self.assertGreaterEqual(a, b)               a is >= b
self.assertLess(a, b)                       a is < b
self.assertLessEqual(a, b)                  a is <= b

for expected exceptions, use:

with self.assertRaises(Exception):
    blah...blah...blah

with self.assertRaises(KeyError):
    blah...blah...blah

Test if __name__ == "__main__":
    def test__main__(self):
        # assume bottom section: if __name__ == "__main__"
        # simply calls a function named main() inside 
        main()


See:
      https://docs.python.org/2/library/unittest.html
         or
      https://docs.python.org/dev/library/unittest.html
for more assert options
"""

import sys, os

here = os.path.abspath(os.path.dirname(__file__)) # Needed for py.test
up_one = os.path.split( here )[0]
if here not in sys.path[:2]:
    sys.path.insert(0, here)
if up_one not in sys.path[:2]:
    sys.path.insert(0, up_one)

from rocketunits.units_io import Units, main

class Bar:
    def __init__(self, xxx, x="4 ft**2", y="5 s", z="6 ft/s**2", j=66, k=99,
                 output_units="Both", my_flag=True):
        self.my_io = Units( self.__class__, locals() )

        self.x = self.my_io.get_input_value("x")
        self.y = self.my_io.get_input_value("y")
        self.z = self.my_io.get_input_value("z")
        self.j = j

        self.xxx = self.my_io.get_input_value("xxx", def_units="deg")

        self.my_io.set_vars_dict( vars(self) )

        self.my_io.set_print_template( template="%s = %s %s")

class SomeInches:
    def __init__(self, d1="1 in", d2="2 inch", a1="1 in**2", a2="2 in**2",
                 v1="1 in**3", v2="2 inch**3", output_units="English"):
        self.my_io = Units( self.__class__, locals() )

        self.d1 = self.my_io.get_input_value("d1")
        self.d2 = self.my_io.get_input_value("d2")

        self.a1 = self.my_io.get_input_value("a1")
        self.a2 = self.my_io.get_input_value("a2")

        self.v1 = self.my_io.get_input_value("v1")
        self.v2 = self.my_io.get_input_value("v2")

        self.my_io.set_vars_dict( vars(self) )
        self.my_io.set_print_template( template="%s = %s %s")

class BarNone:
    def __init__(self, x="4 ft**2", y="None psia", pdiff="10 psid"):
        self.my_io = Units( self.__class__, locals() )

        self.x = self.my_io.get_input_value("x")
        self.y = self.my_io.get_input_value("y")

        self.pdiff = self.my_io.get_input_value("pdiff")
        self.my_io.set_vars_dict( vars(self) )
        self.my_io.set_print_template( template="%s = %s %s")



class MyTest(unittest.TestCase):

    def test_should_always_pass_cleanly(self):
        """Should always pass cleanly."""
        pass

    def test_inch_u_string_values(self):
        """test u_string values"""

        b = SomeInches()
        def get_s(name):
            s = b.my_io.u_string( name, "" )
            return s.strip()

        self.assertEqual(get_s('d1'), 'd1 = 1 inch')
        self.assertEqual(get_s('d2'), 'd2 = 2 inch')

        self.assertEqual(get_s('a1'), 'a1 = 1 in**2')
        self.assertEqual(get_s('a2'), 'a2 = 2 in**2')

        self.assertEqual(get_s('v1'), 'v1 = 1 in**3')
        self.assertEqual(get_s('v2'), 'v2 = 2 in**3')

    def test_none_input_var(self):
        """test none_input_var"""
        b = BarNone( x="5 in**2" )
        self.assertEqual(None, b.y)

    def test_none_default_w_input_var(self):
        """test none_input_var"""
        b = BarNone( x="5 in**2", y="1 atm" )
        self.assertAlmostEqual(14.6959488, b.y, places=5)

        s = b.my_io.u_string( 'pdiff', "" )
        self.assertEqual(s.strip(), 'pdiff = 10 psid (68947.6 Pa)')


    def test_set_unitless_self_var(self):
        """test set_unitless_self_var"""
        b = Bar( 32.2, z="1 gee", y="3 hr", x=6 )
        b.my_io.set_units('j', '')
        
    def test_set_user_units(self):
        """test set_user_units"""
        b = Bar( 32.2, z="1 gee", y="3 hr", x=6 )
        b.my_io.set_user_units( name='y', user_units='min')
        
        with self.assertRaises(Exception):
            b.my_io.set_user_units( name='y', user_units='non-units')

        with self.assertRaises(Exception):
            b.my_io.set_user_units( name='', user_units='min')
        

    def test_bad_assign_units_in_u_string(self):
        """test bad assign units in u_string"""
        b = Bar( 32.2, z="1 gee", y="3 hr", x=6 )
        with self.assertRaises(Exception):
            s = b.my_io.u_string( 'j', desc="", primary_units="goobers", added_units="", fmt="%g")

    def test_bad_added_units_in_assign_unit(self):
        """test bad added units in assign units"""
        b = Bar( 32.2, z="1 gee", y="3 hr", x=6 )
        with self.assertRaises(Exception):
            s = b.my_io.u_string( 'j', desc="", primary_units="ft", added_units="goobers", fmt="%g")

    def test_bad_added_units_in_assign_unit_v2(self):
        """test bad added units in assign units v2"""
        b = Bar( 32.2, z="1 gee", y="3 hr", x=6 )
        with self.assertRaises(Exception):
            s = b.my_io.u_string( 'j', desc="", primary_units="ft", added_units="lbm", fmt="%g")
        
        

    def test_bad_set_units(self):
        """test bad set units"""        
        b = Bar( 32.2, z="1 gee", y="3 hr", x=6 )

        with self.assertRaises(Exception):
            b.my_io.set_units(name='', units='')

        with self.assertRaises(Exception):
            b.my_io.set_units(name='what', units='goobers')

        b.my_io.set_units(name='what', units='ft')

    def test_bad_set_units_same_as(self):
        """test bad set units same as"""
        b = Bar( 32.2, z="1 gee", y="3 hr", x=6 )
        with self.assertRaises(Exception):
            b.my_io.set_units_same_as('z', 'y')
        
        with self.assertRaises(Exception):
            b.my_io.set_units_same_as('j', 'k')

    def test_get_unitless_value_string(self):
        """test get unitless value string"""
        b = Bar( 32.2, z="1 gee", y="3 hr", x=6 )
        s = b.my_io.u_string( 'j', desc="", primary_units="", added_units="", fmt="%g")
        self.assertEqual(s, 'j = 66 ')

    def test_user_defining_default_values(self):
        """test user defining default values"""
        b = Bar( 32.2, z="1 gee", y="3 hr", x=6 )

        j = b.my_io.get_input_value( 'j', def_units="mile/hr")
        
        self.assertEqual(j, 66)

    def test_get_input_for_bad_name(self):
        """test bad name in get_input_value"""
        b = Bar( 32.2, z="1 gee", y="3 hr", x=6 )

        with self.assertRaises(Exception):
            t = b.my_io.get_input_value( 'time')

    def test_bad_user_defining_default_values(self):
        """test bad user defining default values"""
        b = Bar( 32.2, z="1 gee", y="3 hr", x=6 )

        with self.assertRaises(Exception):
            y = b.my_io.get_input_value( 'y', def_units="s")
        
        y = b.my_io.get_input_value( 'y', def_units="")
        self.assertAlmostEqual(y, 10800, places=5)

    def test_my_io_existence(self):
        """Check that my_io exists"""
        
        b = Bar( 32.2, z="1 gee", y="3 hr", x=6 )

        # See if the self.my_io object exists
        self.assertTrue(b.my_io)

    def test_bad_units_input(self):
        """Check bad units for z in call."""
        
        with self.assertRaises(Exception):
            b = Bar( 32.2, z="1 gxxx", y="3 hr", x=6 )

    def test_bad_output_units(self):
        """Check bad output units"""
        
        #with self.assertRaises(Exception):
        b = Bar( 32.2)
        with self.assertRaises(Exception):
            b.my_io.set_output_units( output_units="None")

    def test_u_string_values(self):
        """test u_string values"""

        b = Bar( 32.2, z="1 gee", y="3 hr", x=6 )
        s = b.my_io.u_string( "z", "acceleration" )
        
        self.assertEqual(s, 'z = 1 gee (32.1741 ft/s**2, 9.80665 m/s**2) acceleration')

    def test_unitsio__main__(self):
        """test the __main__ section of units_io"""
        if sys.version_info[0] == 3 and sys.version_info[1] >= 5:
            import importlib.util
            file_path = os.path.join( up_one, 'units_io.py' )
            spec = importlib.util.spec_from_file_location( '__main__', file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        # else:
        #     main()


# if __name__ == '__main__':
#     # Can test just this file from command prompt
#     #  or it can be part of test discovery from nose, unittest, pytest, etc.
#     unittest.main()

