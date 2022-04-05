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

here = os.path.abspath( os.path.dirname(__file__) ) # Needed for py.test
up_one = os.path.split( here )[0]
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

    def test_many_si_conversions_from_pint(self):
        """
        comparison to pint: https://pint.readthedocs.io/en/stable/index.html
        check ratio of conversion done with pint to rocketunits conversion.
        Considered passing if accurate to 5 decimal places.
        """
        #  Acceleration  Using SI ref of 1.0 m/s**2 == m/s**2
        self.assertAlmostEqual(1.0, 0.101972 / convert_value(inp_val=1.0, inp_units="m/s**2", out_units="gee"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="m/s**2", out_units="m/s**2"), places=5)
        self.assertAlmostEqual(1.0, 2.23694 / convert_value(inp_val=1.0, inp_units="m/s**2", out_units="mile/hr/s"), places=5)
        self.assertAlmostEqual(1.0, 3.28084 / convert_value(inp_val=1.0, inp_units="m/s**2", out_units="ft/s**2"), places=5)
        self.assertAlmostEqual(1.0, 100 / convert_value(inp_val=1.0, inp_units="m/s**2", out_units="cm/s**2"), places=5)
        #  AngVelocity  Using SI ref of 1.0 deg/s == deg/s
        self.assertAlmostEqual(1.0, 0.0174533 / convert_value(inp_val=1.0, inp_units="deg/s", out_units="rad/s"), places=5)
        self.assertAlmostEqual(1.0, 0.166667 / convert_value(inp_val=1.0, inp_units="deg/s", out_units="rpm"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="deg/s", out_units="deg/s"), places=5)
        self.assertAlmostEqual(1.0, 1.0472 / convert_value(inp_val=1.0, inp_units="deg/s", out_units="rad/min"), places=5)
        self.assertAlmostEqual(1.0, 60 / convert_value(inp_val=1.0, inp_units="deg/s", out_units="deg/min"), places=5)
        #  Angle  Using SI ref of 1.0 deg == deg
        self.assertAlmostEqual(1.0, 0.00277778 / convert_value(inp_val=1.0, inp_units="deg", out_units="circle"), places=5)
        self.assertAlmostEqual(1.0, 0.00277778 / convert_value(inp_val=1.0, inp_units="deg", out_units="revolution"), places=5)
        self.assertAlmostEqual(1.0, 0.0174533 / convert_value(inp_val=1.0, inp_units="deg", out_units="rad"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="deg", out_units="deg"), places=5)
        self.assertAlmostEqual(1.0, 1.11111 / convert_value(inp_val=1.0, inp_units="deg", out_units="grad"), places=5)
        self.assertAlmostEqual(1.0, 60 / convert_value(inp_val=1.0, inp_units="deg", out_units="arcmin"), places=5)
        self.assertAlmostEqual(1.0, 3600 / convert_value(inp_val=1.0, inp_units="deg", out_units="arcsec"), places=5)
        #  Area  Using SI ref of 1.0 m**2 == m**2
        self.assertAlmostEqual(1.0, 3.86102e-07 / convert_value(inp_val=1.0, inp_units="m**2", out_units="mile**2"), places=5)
        self.assertAlmostEqual(1.0, 0.000247104 / convert_value(inp_val=1.0, inp_units="m**2", out_units="acre"), places=4)
        self.assertAlmostEqual(1.0, 1.0 / convert_value(inp_val=1.0, inp_units="m**2", out_units="m**2"), places=5)
        self.assertAlmostEqual(1.0, 10.7639 / convert_value(inp_val=1.0, inp_units="m**2", out_units="ft**2"), places=5)
        self.assertAlmostEqual(1.0, 1550 / convert_value(inp_val=1.0, inp_units="m**2", out_units="in**2"), places=5)
        self.assertAlmostEqual(1.0, 1550 / convert_value(inp_val=1.0, inp_units="m**2", out_units="inch**2"), places=5)
        self.assertAlmostEqual(1.0, 10000 / convert_value(inp_val=1.0, inp_units="m**2", out_units="cm**2"), places=5)

        #  CoeffThermExp(CTE)  Using SI ref of 1.0 1/degC == 1/degC
        self.assertAlmostEqual(1.0, 1.0 / convert_value(inp_val=1.0, inp_units="1/degC", out_units="1/degC"), places=5)
        self.assertAlmostEqual(1.0, 1.0 / convert_value(inp_val=1.0, inp_units="1/degC", out_units="1/degK"), places=5)
        self.assertAlmostEqual(1.0, (1.0/1.8) / convert_value(inp_val=1.0, inp_units="1/degC", out_units="1/degF"), places=5)
        self.assertAlmostEqual(1.0, (1.0/1.8) / convert_value(inp_val=1.0, inp_units="1/degC", out_units="1/degR"), places=5)

        #  DeltaT  Using SI ref of 1.0 delK == delK
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="delK", out_units="delC"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="delK", out_units="delK"), places=5)
        self.assertAlmostEqual(1.0, 1.8 / convert_value(inp_val=1.0, inp_units="delK", out_units="delF"), places=5)
        self.assertAlmostEqual(1.0, 1.8 / convert_value(inp_val=1.0, inp_units="delK", out_units="delR"), places=5)
        #  Density  Using SI ref of 1.0 kg/m**3 == kg/m**3
        self.assertAlmostEqual(1.0, 3.61273e-05 / convert_value(inp_val=1.0, inp_units="kg/m**3", out_units="lbm/in**3"), places=5)
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="kg/m**3", out_units="g/ml"), places=5)
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="kg/m**3", out_units="g/cm**3"), places=5)
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="kg/m**3", out_units="SG"), places=5)
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="kg/m**3", out_units="specific_gravity"), places=5)
        self.assertAlmostEqual(1.0, 0.00194032 / convert_value(inp_val=1.0, inp_units="kg/m**3", out_units="slug/ft**3"), places=5)
        self.assertAlmostEqual(1.0, 0.0083454 / convert_value(inp_val=1.0, inp_units="kg/m**3", out_units="lbm/galUS"), places=5)
        self.assertAlmostEqual(1.0, 0.062428 / convert_value(inp_val=1.0, inp_units="kg/m**3", out_units="lbm/ft**3"), places=5)
        self.assertAlmostEqual(1.0, 0.133526 / convert_value(inp_val=1.0, inp_units="kg/m**3", out_units="ounce/galUS"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="kg/m**3", out_units="kg/m**3"), places=5)
        #  ElementDensity  Using SI ref of 1.0 elem/cm**2 == elem/cm**2
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="elem/cm**2", out_units="elem/cm**2"), places=5)
        self.assertAlmostEqual(1.0, 6.4516 / convert_value(inp_val=1.0, inp_units="elem/cm**2", out_units="elem/in**2"), places=5)
        #  Energy  Using SI ref of 1.0 J == J
        self.assertAlmostEqual(1.0, 2.77778e-07 / convert_value(inp_val=1.0, inp_units="J", out_units="kW*hr"), places=5)
        self.assertAlmostEqual(1.0, 0.000239006 / convert_value(inp_val=1.0, inp_units="J", out_units="kcal"), places=5)
        self.assertAlmostEqual(1.0, 0.000277778 / convert_value(inp_val=1.0, inp_units="J", out_units="W*hr"), places=5)
        self.assertAlmostEqual(1.0, 0.000947817 / convert_value(inp_val=1.0, inp_units="J", out_units="BTU"), places=5)
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="J", out_units="kJ"), places=5)
        self.assertAlmostEqual(1.0, 0.239006 / convert_value(inp_val=1.0, inp_units="J", out_units="cal"), places=5)
        self.assertAlmostEqual(1.0, 0.737562 / convert_value(inp_val=1.0, inp_units="J", out_units="ft*lbf"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="J", out_units="J"), places=5)
        self.assertAlmostEqual(1.0, 1e+07 / convert_value(inp_val=1.0, inp_units="J", out_units="erg"), places=5)
        #  EnergySpec  Using SI ref of 1.0 J/kg == J/kg
        self.assertAlmostEqual(1.0, 2.39006e-07 / convert_value(inp_val=1.0, inp_units="J/kg", out_units="kcal/g"), places=5)
        self.assertAlmostEqual(1.0, 2.77778e-07 / convert_value(inp_val=1.0, inp_units="J/kg", out_units="kW*hr/kg"), places=5)
        self.assertAlmostEqual(1.0, 0.000239006 / convert_value(inp_val=1.0, inp_units="J/kg", out_units="cal/g"), places=5)
        self.assertAlmostEqual(1.0, 0.000239006 / convert_value(inp_val=1.0, inp_units="J/kg", out_units="kcal/kg"), places=5)
        self.assertAlmostEqual(1.0, 0.000429923 / convert_value(inp_val=1.0, inp_units="J/kg", out_units="BTU/lbm"), places=5)
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="J/kg", out_units="J/g"), places=5)
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="J/kg", out_units="kJ/kg"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="J/kg", out_units="J/kg"), places=5)
        #  Force  Using SI ref of 1.0 N == N
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="N", out_units="kN"), places=5)
        self.assertAlmostEqual(1.0, 0.224809 / convert_value(inp_val=1.0, inp_units="N", out_units="lbf"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="N", out_units="N"), places=5)
        self.assertAlmostEqual(1.0, 100000 / convert_value(inp_val=1.0, inp_units="N", out_units="dyn"), places=5)
        #  Frequency  Using SI ref of 1.0 Hz == Hz
        self.assertAlmostEqual(1.0, 1e-09 / convert_value(inp_val=1.0, inp_units="Hz", out_units="GHz"), places=5)
        self.assertAlmostEqual(1.0, 1e-06 / convert_value(inp_val=1.0, inp_units="Hz", out_units="MHz"), places=5)
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="Hz", out_units="kHz"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="Hz", out_units="Hz"), places=5)
        #  HeatCapacity  Using SI ref of 1.0 J/kg/K == J/kg/K
        self.assertAlmostEqual(1.0, 2.39006e-07 / convert_value(inp_val=1.0, inp_units="J/kg/K", out_units="kcal/g/C"), places=5)
        self.assertAlmostEqual(1.0, 0.000238846 / convert_value(inp_val=1.0, inp_units="J/kg/K", out_units="BTU/lbm/F"), places=5)
        self.assertAlmostEqual(1.0, 0.000239006 / convert_value(inp_val=1.0, inp_units="J/kg/K", out_units="cal/g/C"), places=5)
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="J/kg/K", out_units="kJ/kg/K"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="J/kg/K", out_units="J/kg/K"), places=5)
        #  HxCoeff  Using SI ref of 1.0 cal/cm**2/s/C == cal/cm**2/s/K
        self.assertAlmostEqual(1.0, 0.0142138 / convert_value(inp_val=1.0, inp_units="cal/cm**2/s/C", out_units="BTU/inch**2/s/F"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="cal/cm**2/s/C", out_units="cal/cm**2/s/C"), places=5)
        self.assertAlmostEqual(1.0, 7368.45 / convert_value(inp_val=1.0, inp_units="cal/cm**2/s/C", out_units="BTU/ft**2/hr/F"), places=5)
        self.assertAlmostEqual(1.0, 36000 / convert_value(inp_val=1.0, inp_units="cal/cm**2/s/C", out_units="kcal/m**2/hr/C"), places=5)
        self.assertAlmostEqual(1.0, 41840 / convert_value(inp_val=1.0, inp_units="cal/cm**2/s/C", out_units="W/m**2/C"), places=5)
        #  Isp  Using SI ref of 1.0 m/sec == m/sec
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="m/sec", out_units="km/sec"), places=5)
        self.assertAlmostEqual(1.0, 0.101972 / convert_value(inp_val=1.0, inp_units="m/sec", out_units="lbf-sec/lbm"), places=5)
        self.assertAlmostEqual(1.0, 0.101972 / convert_value(inp_val=1.0, inp_units="m/sec", out_units="sec"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="m/sec", out_units="m/sec"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="m/sec", out_units="N-sec/kg"), places=5)
        #  Length  Using SI ref of 1.0 m == m
        self.assertAlmostEqual(1.0, 1.057e-16 / convert_value(inp_val=1.0, inp_units="m", out_units="light_year"), places=5)
        self.assertAlmostEqual(1.0, 6.68459e-12 / convert_value(inp_val=1.0, inp_units="m", out_units="astronomical_unit"), places=5)
        self.assertAlmostEqual(1.0, 0.000539957 / convert_value(inp_val=1.0, inp_units="m", out_units="nautical_mile"), places=5)
        self.assertAlmostEqual(1.0, 0.000621371 / convert_value(inp_val=1.0, inp_units="m", out_units="mile"), places=5)
        self.assertAlmostEqual(1.0, 0.000621371 / convert_value(inp_val=1.0, inp_units="m", out_units="statute_mile"), places=5)
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="m", out_units="km"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="m", out_units="m"), places=5)
        self.assertAlmostEqual(1.0, 1.09361 / convert_value(inp_val=1.0, inp_units="m", out_units="yd"), places=5)
        self.assertAlmostEqual(1.0, 3.28084 / convert_value(inp_val=1.0, inp_units="m", out_units="ft"), places=5)
        self.assertAlmostEqual(1.0, 39.3701 / convert_value(inp_val=1.0, inp_units="m", out_units="inch"), places=5)
        self.assertAlmostEqual(1.0, 100 / convert_value(inp_val=1.0, inp_units="m", out_units="cm"), places=5)
        self.assertAlmostEqual(1.0, 1000 / convert_value(inp_val=1.0, inp_units="m", out_units="mm"), places=5)
        self.assertAlmostEqual(1.0, 39370.1 / convert_value(inp_val=1.0, inp_units="m", out_units="mil"), places=5)
        self.assertAlmostEqual(1.0, 1e+06 / convert_value(inp_val=1.0, inp_units="m", out_units="micron"), places=5)
        self.assertAlmostEqual(1.0, 1e+10 / convert_value(inp_val=1.0, inp_units="m", out_units="angstrom"), places=5)
        #  Mass  Using SI ref of 1.0 kg == kg
        self.assertAlmostEqual(1.0, 0.000984207 / convert_value(inp_val=1.0, inp_units="kg", out_units="long_ton"), places=5)
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="kg", out_units="metric_ton"), places=5)
        self.assertAlmostEqual(1.0, 0.00110231 / convert_value(inp_val=1.0, inp_units="kg", out_units="short_ton"), places=5)
        self.assertAlmostEqual(1.0, 0.0685218 / convert_value(inp_val=1.0, inp_units="kg", out_units="slug"), places=5)
        self.assertAlmostEqual(1.0, 0.264661 / convert_value(inp_val=1.0, inp_units="kg", out_units="gal_H2O"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="kg", out_units="kg"), places=5)
        self.assertAlmostEqual(1.0, 2.20462 / convert_value(inp_val=1.0, inp_units="kg", out_units="lbm"), places=5)
        self.assertAlmostEqual(1.0, 1000 / convert_value(inp_val=1.0, inp_units="kg", out_units="g"), places=5)
        #  MassFlow  Using SI ref of 1.0 kg/s == kg/s
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="kg/s", out_units="kg/s"), places=5)
        self.assertAlmostEqual(1.0, 2.20462 / convert_value(inp_val=1.0, inp_units="kg/s", out_units="lbm/s"), places=5)
        self.assertAlmostEqual(1.0, 60 / convert_value(inp_val=1.0, inp_units="kg/s", out_units="kg/min"), places=5)
        self.assertAlmostEqual(1.0, 132.277 / convert_value(inp_val=1.0, inp_units="kg/s", out_units="lbm/min"), places=5)
        self.assertAlmostEqual(1.0, 1000 / convert_value(inp_val=1.0, inp_units="kg/s", out_units="g/s"), places=5)
        self.assertAlmostEqual(1.0, 3600 / convert_value(inp_val=1.0, inp_units="kg/s", out_units="kg/hr"), places=5)
        self.assertAlmostEqual(1.0, 7936.64 / convert_value(inp_val=1.0, inp_units="kg/s", out_units="lbm/hr"), places=5)
        self.assertAlmostEqual(1.0, 60000 / convert_value(inp_val=1.0, inp_units="kg/s", out_units="g/min"), places=5)
        self.assertAlmostEqual(1.0, 3.6e+06 / convert_value(inp_val=1.0, inp_units="kg/s", out_units="g/hr"), places=5)
        #  MolecularWt  Using SI ref of 1.0 g/gmole == g/gmole
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="g/gmole", out_units="g/gmole"), places=5)
        self.assertAlmostEqual(1.0, 0.999999 / convert_value(inp_val=1.0, inp_units="g/gmole", out_units="lbm/lbmole"), places=5)
        #  Power  Using SI ref of 1.0 cal/s == cal/s
        self.assertAlmostEqual(1.0, 4.184e-06 / convert_value(inp_val=1.0, inp_units="cal/s", out_units="MW"), places=5)
        self.assertAlmostEqual(1.0, 0.00396567 / convert_value(inp_val=1.0, inp_units="cal/s", out_units="BTU/s"), places=5)
        self.assertAlmostEqual(1.0, 0.004184 / convert_value(inp_val=1.0, inp_units="cal/s", out_units="kW"), places=5)
        self.assertAlmostEqual(1.0, 0.00561084 / convert_value(inp_val=1.0, inp_units="cal/s", out_units="hp"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="cal/s", out_units="cal/s"), places=5)
        self.assertAlmostEqual(1.0, 3.08596 / convert_value(inp_val=1.0, inp_units="cal/s", out_units="ft*lbf/s"), places=5)
        self.assertAlmostEqual(1.0, 4.184 / convert_value(inp_val=1.0, inp_units="cal/s", out_units="W"), places=5)
        self.assertAlmostEqual(1.0, 14.2764 / convert_value(inp_val=1.0, inp_units="cal/s", out_units="BTU/hr"), places=5)
        #  Pressure  Using SI ref of 1.0 Pa == Pa
        self.assertAlmostEqual(1.0, 1e-06 / convert_value(inp_val=1.0, inp_units="Pa", out_units="MPa"), places=5)
        self.assertAlmostEqual(1.0, 9.86923e-06 / convert_value(inp_val=1.0, inp_units="Pa", out_units="atm"), places=5)
        self.assertAlmostEqual(1.0, 1e-05 / convert_value(inp_val=1.0, inp_units="Pa", out_units="bar"), places=5)
        self.assertAlmostEqual(1.0, 0.0001 / convert_value(inp_val=1.0, inp_units="Pa", out_units="N/cm**2"), places=5)
        self.assertAlmostEqual(1.0, 0.000145038 / convert_value(inp_val=1.0, inp_units="Pa", out_units="lbf/inch**2"), places=5)
        self.assertAlmostEqual(1.0, 0.000145038 / convert_value(inp_val=1.0, inp_units="Pa", out_units="psia"), places=5)
        self.assertAlmostEqual(1.0, 0.000145038 / convert_value(inp_val=1.0, inp_units="Pa", out_units="psid"), places=5)
        self.assertAlmostEqual(1.0, 0.0002953 / convert_value(inp_val=1.0, inp_units="Pa", out_units="inHg"), places=5)
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="Pa", out_units="kPa"), places=5)
        self.assertAlmostEqual(1.0, 0.00750062 / convert_value(inp_val=1.0, inp_units="Pa", out_units="mmHg"), places=5)
        self.assertAlmostEqual(1.0, 0.00750062 / convert_value(inp_val=1.0, inp_units="Pa", out_units="torr"), places=5)
        self.assertAlmostEqual(1.0, 0.0208854 / convert_value(inp_val=1.0, inp_units="Pa", out_units="lbf/ft**2"), places=5)
        self.assertAlmostEqual(1.0, 0.0208854 / convert_value(inp_val=1.0, inp_units="Pa", out_units="psf"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="Pa", out_units="N/m**2"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="Pa", out_units="Pa"), places=5)
        #  SurfaceTension  Using SI ref of 1.0 N/m == N/m
        self.assertAlmostEqual(1.0, 0.00571015 / convert_value(inp_val=1.0, inp_units="N/m", out_units="lbf/in"), places=5)
        self.assertAlmostEqual(1.0, 0.0685218 / convert_value(inp_val=1.0, inp_units="N/m", out_units="lbf/ft"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="N/m", out_units="N/m"), places=5)
        self.assertAlmostEqual(1.0, 1000 / convert_value(inp_val=1.0, inp_units="N/m", out_units="mN/m"), places=5)
        self.assertAlmostEqual(1.0, 1000 / convert_value(inp_val=1.0, inp_units="N/m", out_units="dyne/cm"), places=5)
        #  Tank_PV/W  Using SI ref of 1.0 bar-liter/kg == bar*liter/kg
        self.assertAlmostEqual(1.0, 0.1 / convert_value(inp_val=1.0, inp_units="bar-liter/kg", out_units="MPa-liter/kg"), places=5)
        self.assertAlmostEqual(1.0, 0.232328 / convert_value(inp_val=1.0, inp_units="bar-liter/kg", out_units="psia-ft**3/lbm"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="bar-liter/kg", out_units="bar-liter/kg"), places=5)
        self.assertAlmostEqual(1.0, 401.463 / convert_value(inp_val=1.0, inp_units="bar-liter/kg", out_units="psia-in**3/lbm"), places=5)
        #  Temperature  Using SI ref of 1.0 degK == degK
        self.assertAlmostEqual(1.0, -272.15 / convert_value(inp_val=1.0, inp_units="degK", out_units="degC"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="degK", out_units="degK"), places=5)
        self.assertAlmostEqual(1.0, -457.87 / convert_value(inp_val=1.0, inp_units="degK", out_units="degF"), places=5)
        self.assertAlmostEqual(1.0, 1.8 / convert_value(inp_val=1.0, inp_units="degK", out_units="degR"), places=5)
        #  ThermalCond  Using SI ref of 1.0 W/m/K == W/m/K
        self.assertAlmostEqual(1.0, 1.33748e-05 / convert_value(inp_val=1.0, inp_units="W/m/K", out_units="BTU/s/inch/F"), places=5)
        self.assertAlmostEqual(1.0, 0.000160497 / convert_value(inp_val=1.0, inp_units="W/m/K", out_units="BTU/s/ft/F"), places=5)
        self.assertAlmostEqual(1.0, 0.00239006 / convert_value(inp_val=1.0, inp_units="W/m/K", out_units="cal/s/cm/C"), places=5)
        self.assertAlmostEqual(1.0, 0.01 / convert_value(inp_val=1.0, inp_units="W/m/K", out_units="W/cm/C"), places=5)
        self.assertAlmostEqual(1.0, 0.239006 / convert_value(inp_val=1.0, inp_units="W/m/K", out_units="cal/s/m/C"), places=5)
        self.assertAlmostEqual(1.0, 0.577789 / convert_value(inp_val=1.0, inp_units="W/m/K", out_units="BTU/hr/ft/F"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="W/m/K", out_units="W/m/K"), places=5)
        #  Time  Using SI ref of 1.0 s == s
        self.assertAlmostEqual(1.0, 3.16881e-08 / convert_value(inp_val=1.0, inp_units="s", out_units="year"), places=4)
        self.assertAlmostEqual(1.0, 1.15741e-05 / convert_value(inp_val=1.0, inp_units="s", out_units="day"), places=5)
        self.assertAlmostEqual(1.0, 0.000277778 / convert_value(inp_val=1.0, inp_units="s", out_units="hr"), places=5)
        self.assertAlmostEqual(1.0, 0.0166667 / convert_value(inp_val=1.0, inp_units="s", out_units="min"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="s", out_units="s"), places=5)
        self.assertAlmostEqual(1.0, 1000 / convert_value(inp_val=1.0, inp_units="s", out_units="millisec"), places=5)
        self.assertAlmostEqual(1.0, 1000 / convert_value(inp_val=1.0, inp_units="s", out_units="ms"), places=5)
        self.assertAlmostEqual(1.0, 1e+06 / convert_value(inp_val=1.0, inp_units="s", out_units="microsec"), places=5)
        self.assertAlmostEqual(1.0, 1e+09 / convert_value(inp_val=1.0, inp_units="s", out_units="nanosec"), places=5)
        #  Velocity  Using SI ref of 1.0 m/s == m/s
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="m/s", out_units="m/s"), places=5)
        self.assertAlmostEqual(1.0, 2.23694 / convert_value(inp_val=1.0, inp_units="m/s", out_units="mile/hr"), places=5)
        self.assertAlmostEqual(1.0, 3.28084 / convert_value(inp_val=1.0, inp_units="m/s", out_units="ft/s"), places=5)
        self.assertAlmostEqual(1.0, 3.6 / convert_value(inp_val=1.0, inp_units="m/s", out_units="km/hr"), places=5)
        self.assertAlmostEqual(1.0, 39.3701 / convert_value(inp_val=1.0, inp_units="m/s", out_units="inch/s"), places=5)
        self.assertAlmostEqual(1.0, 100 / convert_value(inp_val=1.0, inp_units="m/s", out_units="cm/s"), places=5)
        #  Viscosity_Dynamic  Using SI ref of 1.0 kg/s/m == kg/s/m
        self.assertAlmostEqual(1.0, 0.01 / convert_value(inp_val=1.0, inp_units="kg/s/m", out_units="kg/s/cm"), places=5)
        self.assertAlmostEqual(1.0, 0.0559974 / convert_value(inp_val=1.0, inp_units="kg/s/m", out_units="lbm/s/inch"), places=5)
        self.assertAlmostEqual(1.0, 0.671969 / convert_value(inp_val=1.0, inp_units="kg/s/m", out_units="lbm/s/ft"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="kg/s/m", out_units="kg/s/m"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="kg/s/m", out_units="Pa*s"), places=5)
        self.assertAlmostEqual(1.0, 10 / convert_value(inp_val=1.0, inp_units="kg/s/m", out_units="poise"), places=5)
        self.assertAlmostEqual(1.0, 36 / convert_value(inp_val=1.0, inp_units="kg/s/m", out_units="kg/hr/cm"), places=5)
        self.assertAlmostEqual(1.0, 201.591 / convert_value(inp_val=1.0, inp_units="kg/s/m", out_units="lbm/hr/inch"), places=5)
        self.assertAlmostEqual(1.0, 1000 / convert_value(inp_val=1.0, inp_units="kg/s/m", out_units="cp"), places=5)
        self.assertAlmostEqual(1.0, 1000 / convert_value(inp_val=1.0, inp_units="kg/s/m", out_units="cpoise"), places=5)
        self.assertAlmostEqual(1.0, 2419.09 / convert_value(inp_val=1.0, inp_units="kg/s/m", out_units="lbm/hr/ft"), places=5)
        self.assertAlmostEqual(1.0, 3600 / convert_value(inp_val=1.0, inp_units="kg/s/m", out_units="kg/hr/m"), places=5)
        #  Viscosity_Kinematic  Using SI ref of 1.0 m**2/s == m**2/s
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="m**2/s", out_units="m**2/s"), places=5)
        self.assertAlmostEqual(1.0, 10.7639 / convert_value(inp_val=1.0, inp_units="m**2/s", out_units="ft**2/s"), places=5)
        self.assertAlmostEqual(1.0, 10000 / convert_value(inp_val=1.0, inp_units="m**2/s", out_units="stokes"), places=5)
        self.assertAlmostEqual(1.0, 38750.1 / convert_value(inp_val=1.0, inp_units="m**2/s", out_units="ft**2/hr"), places=5)
        self.assertAlmostEqual(1.0, 1e+06 / convert_value(inp_val=1.0, inp_units="m**2/s", out_units="centistokes"), places=5)
        #  Volume  Using SI ref of 1.0 m**3 == m**3
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="m**3", out_units="m**3"), places=5)
        self.assertAlmostEqual(1.0, 1.30795 / convert_value(inp_val=1.0, inp_units="m**3", out_units="yd**3"), places=5)
        self.assertAlmostEqual(1.0, 6.28981 / convert_value(inp_val=1.0, inp_units="m**3", out_units="barOil"), places=5)
        self.assertAlmostEqual(1.0, 35.3147 / convert_value(inp_val=1.0, inp_units="m**3", out_units="ft**3"), places=5)
        self.assertAlmostEqual(1.0, 219.969 / convert_value(inp_val=1.0, inp_units="m**3", out_units="galUK"), places=5)
        self.assertAlmostEqual(1.0, 264.172 / convert_value(inp_val=1.0, inp_units="m**3", out_units="galUS"), places=5)
        self.assertAlmostEqual(1.0, 1000 / convert_value(inp_val=1.0, inp_units="m**3", out_units="liter"), places=5)
        self.assertAlmostEqual(1.0, 1056.69 / convert_value(inp_val=1.0, inp_units="m**3", out_units="quart"), places=5)
        self.assertAlmostEqual(1.0, 2113.38 / convert_value(inp_val=1.0, inp_units="m**3", out_units="pint"), places=5)
        self.assertAlmostEqual(1.0, 4226.75 / convert_value(inp_val=1.0, inp_units="m**3", out_units="cup"), places=5)
        self.assertAlmostEqual(1.0, 61023.7 / convert_value(inp_val=1.0, inp_units="m**3", out_units="in**3"), places=5)
        self.assertAlmostEqual(1.0, 61023.7 / convert_value(inp_val=1.0, inp_units="m**3", out_units="inch**3"), places=5)
        self.assertAlmostEqual(1.0, 1e+06 / convert_value(inp_val=1.0, inp_units="m**3", out_units="cm**3"), places=5)
        #  VolumeFlow  Using SI ref of 1.0 m**3/s == m**3/s
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="m**3/s"), places=5)
        self.assertAlmostEqual(1.0, 35.3147 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="ft**3/s"), places=5)
        self.assertAlmostEqual(1.0, 264.172 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="galUS/s"), places=5)
        self.assertAlmostEqual(1.0, 1000 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="l/s"), places=5)
        self.assertAlmostEqual(1.0, 2118.88 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="ft**3/min"), places=5)
        self.assertAlmostEqual(1.0, 3600 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="m**3/hr"), places=5)
        self.assertAlmostEqual(1.0, 15850.3 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="galUS/min"), places=5)
        self.assertAlmostEqual(1.0, 15850.3 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="gpm"), places=5)
        self.assertAlmostEqual(1.0, 61023.7 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="inch**3/s"), places=5)
        self.assertAlmostEqual(1.0, 127133 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="ft**3/hr"), places=5)
        self.assertAlmostEqual(1.0, 951019 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="galUS/hr"), places=5)
        self.assertAlmostEqual(1.0, 1e+06 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="ml/s"), places=5)
        self.assertAlmostEqual(1.0, 3.66142e+06 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="inch**3/min"), places=5)
        self.assertAlmostEqual(1.0, 2.28245e+07 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="galUS/day"), places=5)
        self.assertAlmostEqual(1.0, 6e+07 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="ml/min"), places=5)
        self.assertAlmostEqual(1.0, 2.19685e+08 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="inch**3/hr"), places=5)
        self.assertAlmostEqual(1.0, 3.6e+09 / convert_value(inp_val=1.0, inp_units="m**3/s", out_units="ml/hr"), places=5)


    def test_many_english_conversions_from_pint(self):
        """
        comparison to pint: https://pint.readthedocs.io/en/stable/index.html
        check ratio of conversion done with pint to rocketunits conversion.
        Considered passing if accurate to 5 decimal places.
        """
        #  Acceleration  Using English ref of 1.0 ft/s**2 == ft/s**2
        self.assertAlmostEqual(1.0, 0.031081 / convert_value(inp_val=1.0, inp_units="ft/s**2", out_units="gee"), places=5)
        self.assertAlmostEqual(1.0, 0.3048 / convert_value(inp_val=1.0, inp_units="ft/s**2", out_units="m/s**2"), places=5)
        self.assertAlmostEqual(1.0, 0.681818 / convert_value(inp_val=1.0, inp_units="ft/s**2", out_units="mile/hr/s"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="ft/s**2", out_units="ft/s**2"), places=5)
        self.assertAlmostEqual(1.0, 30.48 / convert_value(inp_val=1.0, inp_units="ft/s**2", out_units="cm/s**2"), places=5)
        #  AngVelocity  Using English ref of 1.0 rpm == rpm
        self.assertAlmostEqual(1.0, 0.10472 / convert_value(inp_val=1.0, inp_units="rpm", out_units="rad/s"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="rpm", out_units="rpm"), places=5)
        self.assertAlmostEqual(1.0, 6 / convert_value(inp_val=1.0, inp_units="rpm", out_units="deg/s"), places=5)
        self.assertAlmostEqual(1.0, 6.28319 / convert_value(inp_val=1.0, inp_units="rpm", out_units="rad/min"), places=5)
        self.assertAlmostEqual(1.0, 360 / convert_value(inp_val=1.0, inp_units="rpm", out_units="deg/min"), places=5)
        #  Angle  Using English ref of 1.0 deg == deg
        self.assertAlmostEqual(1.0, 0.00277778 / convert_value(inp_val=1.0, inp_units="deg", out_units="circle"), places=5)
        self.assertAlmostEqual(1.0, 0.00277778 / convert_value(inp_val=1.0, inp_units="deg", out_units="revolution"), places=5)
        self.assertAlmostEqual(1.0, 0.0174533 / convert_value(inp_val=1.0, inp_units="deg", out_units="rad"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="deg", out_units="deg"), places=5)
        self.assertAlmostEqual(1.0, 1.11111 / convert_value(inp_val=1.0, inp_units="deg", out_units="grad"), places=5)
        self.assertAlmostEqual(1.0, 60 / convert_value(inp_val=1.0, inp_units="deg", out_units="arcmin"), places=5)
        self.assertAlmostEqual(1.0, 3600 / convert_value(inp_val=1.0, inp_units="deg", out_units="arcsec"), places=5)
        #  Area  Using English ref of 1.0 inch**2 == inch**2
        self.assertAlmostEqual(1.0, 2.49098e-10 / convert_value(inp_val=1.0, inp_units="inch**2", out_units="mile**2"), places=5)
        self.assertAlmostEqual(1.0, 1.59422e-07 / convert_value(inp_val=1.0, inp_units="inch**2", out_units="acre"), places=5)
        self.assertAlmostEqual(1.0, 0.00064516 / convert_value(inp_val=1.0, inp_units="inch**2", out_units="m**2"), places=5)
        self.assertAlmostEqual(1.0, 0.00694444 / convert_value(inp_val=1.0, inp_units="inch**2", out_units="ft**2"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="inch**2", out_units="in**2"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="inch**2", out_units="inch**2"), places=5)
        self.assertAlmostEqual(1.0, 6.4516 / convert_value(inp_val=1.0, inp_units="inch**2", out_units="cm**2"), places=5)

        #  CoeffThermExp(CTE)  Using English ref of 1.0 1/degF == 1/degF
        self.assertAlmostEqual(1.0, 1.8 / convert_value(inp_val=1.0, inp_units="1/degF", out_units="1/degC"), places=5)
        self.assertAlmostEqual(1.0, 1.8 / convert_value(inp_val=1.0, inp_units="1/degF", out_units="1/degK"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="1/degF", out_units="1/degF"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="1/degF", out_units="1/degR"), places=5)

        #  DeltaT  Using English ref of 1.0 delF == delF
        self.assertAlmostEqual(1.0, 0.555556 / convert_value(inp_val=1.0, inp_units="delF", out_units="delC"), places=5)
        self.assertAlmostEqual(1.0, 0.555556 / convert_value(inp_val=1.0, inp_units="delF", out_units="delK"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="delF", out_units="delF"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="delF", out_units="delR"), places=5)
        #  Density  Using English ref of 1.0 lbm/in**3 == lbm/in**3
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="lbm/in**3", out_units="lbm/in**3"), places=5)
        self.assertAlmostEqual(1.0, 27.6799 / convert_value(inp_val=1.0, inp_units="lbm/in**3", out_units="g/ml"), places=5)
        self.assertAlmostEqual(1.0, 27.6799 / convert_value(inp_val=1.0, inp_units="lbm/in**3", out_units="g/cm**3"), places=5)
        self.assertAlmostEqual(1.0, 27.6799 / convert_value(inp_val=1.0, inp_units="lbm/in**3", out_units="SG"), places=5)
        self.assertAlmostEqual(1.0, 27.6799 / convert_value(inp_val=1.0, inp_units="lbm/in**3", out_units="specific_gravity"), places=5)
        self.assertAlmostEqual(1.0, 53.7079 / convert_value(inp_val=1.0, inp_units="lbm/in**3", out_units="slug/ft**3"), places=5)
        self.assertAlmostEqual(1.0, 231 / convert_value(inp_val=1.0, inp_units="lbm/in**3", out_units="lbm/galUS"), places=5)
        self.assertAlmostEqual(1.0, 1728 / convert_value(inp_val=1.0, inp_units="lbm/in**3", out_units="lbm/ft**3"), places=5)
        self.assertAlmostEqual(1.0, 3696 / convert_value(inp_val=1.0, inp_units="lbm/in**3", out_units="ounce/galUS"), places=5)
        self.assertAlmostEqual(1.0, 27679.9 / convert_value(inp_val=1.0, inp_units="lbm/in**3", out_units="kg/m**3"), places=5)
        #  ElementDensity  Using English ref of 1.0 elem/cm**2 == elem/cm**2
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="elem/cm**2", out_units="elem/cm**2"), places=5)
        self.assertAlmostEqual(1.0, 6.4516 / convert_value(inp_val=1.0, inp_units="elem/cm**2", out_units="elem/in**2"), places=5)
        #  Energy  Using English ref of 1.0 BTU == BTU
        self.assertAlmostEqual(1.0, 0.000293071 / convert_value(inp_val=1.0, inp_units="BTU", out_units="kW*hr"), places=5)
        self.assertAlmostEqual(1.0, 0.252164 / convert_value(inp_val=1.0, inp_units="BTU", out_units="kcal"), places=5)
        self.assertAlmostEqual(1.0, 0.293071 / convert_value(inp_val=1.0, inp_units="BTU", out_units="W*hr"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="BTU", out_units="BTU"), places=5)
        self.assertAlmostEqual(1.0, 1.05506 / convert_value(inp_val=1.0, inp_units="BTU", out_units="kJ"), places=5)
        self.assertAlmostEqual(1.0, 252.164 / convert_value(inp_val=1.0, inp_units="BTU", out_units="cal"), places=5)
        self.assertAlmostEqual(1.0, 778.169 / convert_value(inp_val=1.0, inp_units="BTU", out_units="ft*lbf"), places=5)
        self.assertAlmostEqual(1.0, 1055.06 / convert_value(inp_val=1.0, inp_units="BTU", out_units="J"), places=5)
        self.assertAlmostEqual(1.0, 1.05506e+10 / convert_value(inp_val=1.0, inp_units="BTU", out_units="erg"), places=5)
        #  EnergySpec  Using English ref of 1.0 BTU/lbm == BTU/lbm
        self.assertAlmostEqual(1.0, 0.000555927 / convert_value(inp_val=1.0, inp_units="BTU/lbm", out_units="kcal/g"), places=5)
        self.assertAlmostEqual(1.0, 0.000646111 / convert_value(inp_val=1.0, inp_units="BTU/lbm", out_units="kW*hr/kg"), places=5)
        self.assertAlmostEqual(1.0, 0.555927 / convert_value(inp_val=1.0, inp_units="BTU/lbm", out_units="cal/g"), places=5)
        self.assertAlmostEqual(1.0, 0.555927 / convert_value(inp_val=1.0, inp_units="BTU/lbm", out_units="kcal/kg"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="BTU/lbm", out_units="BTU/lbm"), places=5)
        self.assertAlmostEqual(1.0, 2.326 / convert_value(inp_val=1.0, inp_units="BTU/lbm", out_units="J/g"), places=5)
        self.assertAlmostEqual(1.0, 2.326 / convert_value(inp_val=1.0, inp_units="BTU/lbm", out_units="kJ/kg"), places=5)
        self.assertAlmostEqual(1.0, 2326 / convert_value(inp_val=1.0, inp_units="BTU/lbm", out_units="J/kg"), places=5)
        #  Force  Using English ref of 1.0 lbf == lbf
        self.assertAlmostEqual(1.0, 0.00444822 / convert_value(inp_val=1.0, inp_units="lbf", out_units="kN"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="lbf", out_units="lbf"), places=5)
        self.assertAlmostEqual(1.0, 4.44822 / convert_value(inp_val=1.0, inp_units="lbf", out_units="N"), places=5)
        self.assertAlmostEqual(1.0, 444822 / convert_value(inp_val=1.0, inp_units="lbf", out_units="dyn"), places=5)
        #  Frequency  Using English ref of 1.0 Hz == Hz
        self.assertAlmostEqual(1.0, 1e-09 / convert_value(inp_val=1.0, inp_units="Hz", out_units="GHz"), places=5)
        self.assertAlmostEqual(1.0, 1e-06 / convert_value(inp_val=1.0, inp_units="Hz", out_units="MHz"), places=5)
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="Hz", out_units="kHz"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="Hz", out_units="Hz"), places=5)
        #  HeatCapacity  Using English ref of 1.0 BTU/lbm/F == BTU/lbm/degR
        self.assertAlmostEqual(1.0, 0.00100067 / convert_value(inp_val=1.0, inp_units="BTU/lbm/F", out_units="kcal/g/C"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="BTU/lbm/F", out_units="BTU/lbm/F"), places=5)
        self.assertAlmostEqual(1.0, 1.00067 / convert_value(inp_val=1.0, inp_units="BTU/lbm/F", out_units="cal/g/C"), places=5)
        self.assertAlmostEqual(1.0, 4.1868 / convert_value(inp_val=1.0, inp_units="BTU/lbm/F", out_units="kJ/kg/K"), places=5)
        self.assertAlmostEqual(1.0, 4186.8 / convert_value(inp_val=1.0, inp_units="BTU/lbm/F", out_units="J/kg/K"), places=5)
        #  HxCoeff  Using English ref of 1.0 BTU/inch**2/s/F == BTU/inch**2/s/degR
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="BTU/inch**2/s/F", out_units="BTU/inch**2/s/F"), places=5)
        self.assertAlmostEqual(1.0, 70.354 / convert_value(inp_val=1.0, inp_units="BTU/inch**2/s/F", out_units="cal/cm**2/s/C"), places=5)
        self.assertAlmostEqual(1.0, 518400 / convert_value(inp_val=1.0, inp_units="BTU/inch**2/s/F", out_units="BTU/ft**2/hr/F"), places=5)
        self.assertAlmostEqual(1.0, 2.53274e+06 / convert_value(inp_val=1.0, inp_units="BTU/inch**2/s/F", out_units="kcal/m**2/hr/C"), places=5)
        self.assertAlmostEqual(1.0, 2.94361e+06 / convert_value(inp_val=1.0, inp_units="BTU/inch**2/s/F", out_units="W/m**2/C"), places=5)
        #  Isp  Using English ref of 1.0 sec == sec
        self.assertAlmostEqual(1.0, 0.00980665 / convert_value(inp_val=1.0, inp_units="sec", out_units="km/sec"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="sec", out_units="lbf-sec/lbm"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="sec", out_units="sec"), places=5)
        self.assertAlmostEqual(1.0, 9.80665 / convert_value(inp_val=1.0, inp_units="sec", out_units="m/sec"), places=5)
        self.assertAlmostEqual(1.0, 9.80665 / convert_value(inp_val=1.0, inp_units="sec", out_units="N-sec/kg"), places=5)
        #  Length  Using English ref of 1.0 inch == inch
        self.assertAlmostEqual(1.0, 2.68478e-18 / convert_value(inp_val=1.0, inp_units="inch", out_units="light_year"), places=5)
        self.assertAlmostEqual(1.0, 1.69789e-13 / convert_value(inp_val=1.0, inp_units="inch", out_units="astronomical_unit"), places=5)
        self.assertAlmostEqual(1.0, 1.37149e-05 / convert_value(inp_val=1.0, inp_units="inch", out_units="nautical_mile"), places=5)
        self.assertAlmostEqual(1.0, 1.57828e-05 / convert_value(inp_val=1.0, inp_units="inch", out_units="mile"), places=5)
        self.assertAlmostEqual(1.0, 2.54e-05 / convert_value(inp_val=1.0, inp_units="inch", out_units="km"), places=5)
        self.assertAlmostEqual(1.0, 0.0254 / convert_value(inp_val=1.0, inp_units="inch", out_units="m"), places=5)
        self.assertAlmostEqual(1.0, 0.0277778 / convert_value(inp_val=1.0, inp_units="inch", out_units="yd"), places=5)
        self.assertAlmostEqual(1.0, 0.0833333 / convert_value(inp_val=1.0, inp_units="inch", out_units="ft"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="inch", out_units="inch"), places=5)
        self.assertAlmostEqual(1.0, 2.54 / convert_value(inp_val=1.0, inp_units="inch", out_units="cm"), places=5)
        self.assertAlmostEqual(1.0, 25.4 / convert_value(inp_val=1.0, inp_units="inch", out_units="mm"), places=5)
        self.assertAlmostEqual(1.0, 1000 / convert_value(inp_val=1.0, inp_units="inch", out_units="mil"), places=5)
        self.assertAlmostEqual(1.0, 25400 / convert_value(inp_val=1.0, inp_units="inch", out_units="micron"), places=5)
        self.assertAlmostEqual(1.0, 2.54e+08 / convert_value(inp_val=1.0, inp_units="inch", out_units="angstrom"), places=5)
        #  Mass  Using English ref of 1.0 lbm == lbm
        self.assertAlmostEqual(1.0, 0.000446429 / convert_value(inp_val=1.0, inp_units="lbm", out_units="long_ton"), places=5)
        self.assertAlmostEqual(1.0, 0.000453592 / convert_value(inp_val=1.0, inp_units="lbm", out_units="metric_ton"), places=5)
        self.assertAlmostEqual(1.0, 0.0005 / convert_value(inp_val=1.0, inp_units="lbm", out_units="short_ton"), places=5)
        self.assertAlmostEqual(1.0, 0.031081 / convert_value(inp_val=1.0, inp_units="lbm", out_units="slug"), places=5)
        self.assertAlmostEqual(1.0, 0.120048 / convert_value(inp_val=1.0, inp_units="lbm", out_units="gal_H2O"), places=5)
        self.assertAlmostEqual(1.0, 0.453592 / convert_value(inp_val=1.0, inp_units="lbm", out_units="kg"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="lbm", out_units="lbm"), places=5)
        self.assertAlmostEqual(1.0, 453.592 / convert_value(inp_val=1.0, inp_units="lbm", out_units="g"), places=5)
        #  MassFlow  Using English ref of 1.0 lbm/s == lbm/s
        self.assertAlmostEqual(1.0, 0.453592 / convert_value(inp_val=1.0, inp_units="lbm/s", out_units="kg/s"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="lbm/s", out_units="lbm/s"), places=5)
        self.assertAlmostEqual(1.0, 27.2155 / convert_value(inp_val=1.0, inp_units="lbm/s", out_units="kg/min"), places=5)
        self.assertAlmostEqual(1.0, 60 / convert_value(inp_val=1.0, inp_units="lbm/s", out_units="lbm/min"), places=5)
        self.assertAlmostEqual(1.0, 453.592 / convert_value(inp_val=1.0, inp_units="lbm/s", out_units="g/s"), places=5)
        self.assertAlmostEqual(1.0, 1632.93 / convert_value(inp_val=1.0, inp_units="lbm/s", out_units="kg/hr"), places=5)
        self.assertAlmostEqual(1.0, 3600 / convert_value(inp_val=1.0, inp_units="lbm/s", out_units="lbm/hr"), places=5)
        self.assertAlmostEqual(1.0, 27215.5 / convert_value(inp_val=1.0, inp_units="lbm/s", out_units="g/min"), places=5)
        self.assertAlmostEqual(1.0, 1.63293e+06 / convert_value(inp_val=1.0, inp_units="lbm/s", out_units="g/hr"), places=5)
        #  MolecularWt  Using English ref of 1.0 g/gmole == g/gmole
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="g/gmole", out_units="g/gmole"), places=5)
        self.assertAlmostEqual(1.0, 0.999999 / convert_value(inp_val=1.0, inp_units="g/gmole", out_units="lbm/lbmole"), places=5)
        #  Power  Using English ref of 1.0 hp == hp
        self.assertAlmostEqual(1.0, 0.0007457 / convert_value(inp_val=1.0, inp_units="hp", out_units="MW"), places=5)
        self.assertAlmostEqual(1.0, 0.706787 / convert_value(inp_val=1.0, inp_units="hp", out_units="BTU/s"), places=5)
        self.assertAlmostEqual(1.0, 0.7457 / convert_value(inp_val=1.0, inp_units="hp", out_units="kW"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="hp", out_units="hp"), places=5)
        self.assertAlmostEqual(1.0, 178.227 / convert_value(inp_val=1.0, inp_units="hp", out_units="cal/s"), places=5)
        self.assertAlmostEqual(1.0, 550 / convert_value(inp_val=1.0, inp_units="hp", out_units="ft*lbf/s"), places=5)
        self.assertAlmostEqual(1.0, 745.7 / convert_value(inp_val=1.0, inp_units="hp", out_units="W"), places=5)
        self.assertAlmostEqual(1.0, 2544.43 / convert_value(inp_val=1.0, inp_units="hp", out_units="BTU/hr"), places=5)
        #  Pressure  Using English ref of 1.0 psia == psia
        self.assertAlmostEqual(1.0, 0.00689476 / convert_value(inp_val=1.0, inp_units="psia", out_units="MPa"), places=5)
        self.assertAlmostEqual(1.0, 0.068046 / convert_value(inp_val=1.0, inp_units="psia", out_units="atm"), places=5)
        self.assertAlmostEqual(1.0, 0.0689476 / convert_value(inp_val=1.0, inp_units="psia", out_units="bar"), places=5)
        self.assertAlmostEqual(1.0, 0.689476 / convert_value(inp_val=1.0, inp_units="psia", out_units="N/cm**2"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="psia", out_units="lbf/inch**2"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="psia", out_units="psia"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="psia", out_units="psid"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=0.0, inp_units="psig", out_units="atm"), places=5)
        self.assertAlmostEqual(1.0, 2.03602 / convert_value(inp_val=1.0, inp_units="psia", out_units="inHg"), places=5)
        self.assertAlmostEqual(1.0, 6.89476 / convert_value(inp_val=1.0, inp_units="psia", out_units="kPa"), places=5)
        self.assertAlmostEqual(1.0, 51.7149 / convert_value(inp_val=1.0, inp_units="psia", out_units="mmHg"), places=5)
        self.assertAlmostEqual(1.0, 51.7149 / convert_value(inp_val=1.0, inp_units="psia", out_units="torr"), places=5)
        self.assertAlmostEqual(1.0, 144 / convert_value(inp_val=1.0, inp_units="psia", out_units="lbf/ft**2"), places=5)
        self.assertAlmostEqual(1.0, 144 / convert_value(inp_val=1.0, inp_units="psia", out_units="psf"), places=5)
        self.assertAlmostEqual(1.0, 6894.76 / convert_value(inp_val=1.0, inp_units="psia", out_units="N/m**2"), places=5)
        self.assertAlmostEqual(1.0, 6894.76 / convert_value(inp_val=1.0, inp_units="psia", out_units="Pa"), places=5)
        #  SurfaceTension  Using English ref of 1.0 lbf/in == lbf/in
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="lbf/in", out_units="lbf/in"), places=5)
        self.assertAlmostEqual(1.0, 12 / convert_value(inp_val=1.0, inp_units="lbf/in", out_units="lbf/ft"), places=5)
        self.assertAlmostEqual(1.0, 175.127 / convert_value(inp_val=1.0, inp_units="lbf/in", out_units="N/m"), places=5)
        self.assertAlmostEqual(1.0, 175127 / convert_value(inp_val=1.0, inp_units="lbf/in", out_units="mN/m"), places=5)
        self.assertAlmostEqual(1.0, 175127 / convert_value(inp_val=1.0, inp_units="lbf/in", out_units="dyne/cm"), places=5)
        #  Tank_PV/W  Using English ref of 1.0 psia-in**3/lbm == psia*in**3/lbm
        self.assertAlmostEqual(1.0, 0.000249089 / convert_value(inp_val=1.0, inp_units="psia-in**3/lbm", out_units="MPa-liter/kg"), places=5)
        self.assertAlmostEqual(1.0, 0.000578704 / convert_value(inp_val=1.0, inp_units="psia-in**3/lbm", out_units="psia-ft**3/lbm"), places=5)
        self.assertAlmostEqual(1.0, 0.00249089 / convert_value(inp_val=1.0, inp_units="psia-in**3/lbm", out_units="bar-liter/kg"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="psia-in**3/lbm", out_units="psia-in**3/lbm"), places=5)
        #  Temperature  Using English ref of 1.0 degR == degR
        self.assertAlmostEqual(1.0, -272.594 / convert_value(inp_val=1.0, inp_units="degR", out_units="degC"), places=5)
        self.assertAlmostEqual(1.0, 0.555556 / convert_value(inp_val=1.0, inp_units="degR", out_units="degK"), places=5)
        self.assertAlmostEqual(1.0, -458.67 / convert_value(inp_val=1.0, inp_units="degR", out_units="degF"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="degR", out_units="degR"), places=5)
        #  ThermalCond  Using English ref of 1.0 BTU/hr/ft/F == BTU/hr/ft/degR
        self.assertAlmostEqual(1.0, 2.31481e-05 / convert_value(inp_val=1.0, inp_units="BTU/hr/ft/F", out_units="BTU/s/inch/F"), places=5)
        self.assertAlmostEqual(1.0, 0.000277778 / convert_value(inp_val=1.0, inp_units="BTU/hr/ft/F", out_units="BTU/s/ft/F"), places=5)
        self.assertAlmostEqual(1.0, 0.00413656 / convert_value(inp_val=1.0, inp_units="BTU/hr/ft/F", out_units="cal/s/cm/C"), places=5)
        self.assertAlmostEqual(1.0, 0.0173073 / convert_value(inp_val=1.0, inp_units="BTU/hr/ft/F", out_units="W/cm/C"), places=5)
        self.assertAlmostEqual(1.0, 0.413656 / convert_value(inp_val=1.0, inp_units="BTU/hr/ft/F", out_units="cal/s/m/C"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="BTU/hr/ft/F", out_units="BTU/hr/ft/F"), places=5)
        self.assertAlmostEqual(1.0, 1.73073 / convert_value(inp_val=1.0, inp_units="BTU/hr/ft/F", out_units="W/m/K"), places=5)
        #  Time  Using English ref of 1.0 s == s
        self.assertAlmostEqual(1.0, 3.16881e-08 / convert_value(inp_val=1.0, inp_units="s", out_units="year"), places=4)
        self.assertAlmostEqual(1.0, 1.15741e-05 / convert_value(inp_val=1.0, inp_units="s", out_units="day"), places=5)
        self.assertAlmostEqual(1.0, 0.000277778 / convert_value(inp_val=1.0, inp_units="s", out_units="hr"), places=5)
        self.assertAlmostEqual(1.0, 0.0166667 / convert_value(inp_val=1.0, inp_units="s", out_units="min"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="s", out_units="s"), places=5)
        self.assertAlmostEqual(1.0, 1000 / convert_value(inp_val=1.0, inp_units="s", out_units="millisec"), places=5)
        self.assertAlmostEqual(1.0, 1000 / convert_value(inp_val=1.0, inp_units="s", out_units="ms"), places=5)
        self.assertAlmostEqual(1.0, 1e+06 / convert_value(inp_val=1.0, inp_units="s", out_units="microsec"), places=5)
        self.assertAlmostEqual(1.0, 1e+09 / convert_value(inp_val=1.0, inp_units="s", out_units="nanosec"), places=5)
        #  Velocity  Using English ref of 1.0 ft/s == ft/s
        self.assertAlmostEqual(1.0, 0.3048 / convert_value(inp_val=1.0, inp_units="ft/s", out_units="m/s"), places=5)
        self.assertAlmostEqual(1.0, 0.681818 / convert_value(inp_val=1.0, inp_units="ft/s", out_units="mile/hr"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="ft/s", out_units="ft/s"), places=5)
        self.assertAlmostEqual(1.0, 1.09728 / convert_value(inp_val=1.0, inp_units="ft/s", out_units="km/hr"), places=5)
        self.assertAlmostEqual(1.0, 12 / convert_value(inp_val=1.0, inp_units="ft/s", out_units="inch/s"), places=5)
        self.assertAlmostEqual(1.0, 30.48 / convert_value(inp_val=1.0, inp_units="ft/s", out_units="cm/s"), places=5)
        #  Viscosity_Dynamic  Using English ref of 1.0 poise == poise
        self.assertAlmostEqual(1.0, 0.001 / convert_value(inp_val=1.0, inp_units="poise", out_units="kg/s/cm"), places=5)
        self.assertAlmostEqual(1.0, 0.00559974 / convert_value(inp_val=1.0, inp_units="poise", out_units="lbm/s/inch"), places=5)
        self.assertAlmostEqual(1.0, 0.0671969 / convert_value(inp_val=1.0, inp_units="poise", out_units="lbm/s/ft"), places=5)
        self.assertAlmostEqual(1.0, 0.1 / convert_value(inp_val=1.0, inp_units="poise", out_units="kg/s/m"), places=5)
        self.assertAlmostEqual(1.0, 0.1 / convert_value(inp_val=1.0, inp_units="poise", out_units="Pa*s"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="poise", out_units="poise"), places=5)
        self.assertAlmostEqual(1.0, 3.6 / convert_value(inp_val=1.0, inp_units="poise", out_units="kg/hr/cm"), places=5)
        self.assertAlmostEqual(1.0, 20.1591 / convert_value(inp_val=1.0, inp_units="poise", out_units="lbm/hr/inch"), places=5)
        self.assertAlmostEqual(1.0, 100 / convert_value(inp_val=1.0, inp_units="poise", out_units="cp"), places=5)
        self.assertAlmostEqual(1.0, 100 / convert_value(inp_val=1.0, inp_units="poise", out_units="cpoise"), places=5)
        self.assertAlmostEqual(1.0, 241.909 / convert_value(inp_val=1.0, inp_units="poise", out_units="lbm/hr/ft"), places=5)
        self.assertAlmostEqual(1.0, 360 / convert_value(inp_val=1.0, inp_units="poise", out_units="kg/hr/m"), places=5)
        #  Viscosity_Kinematic  Using English ref of 1.0 ft**2/s == ft**2/s
        self.assertAlmostEqual(1.0, 0.092903 / convert_value(inp_val=1.0, inp_units="ft**2/s", out_units="m**2/s"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="ft**2/s", out_units="ft**2/s"), places=5)
        self.assertAlmostEqual(1.0, 929.03 / convert_value(inp_val=1.0, inp_units="ft**2/s", out_units="stokes"), places=5)
        self.assertAlmostEqual(1.0, 3600 / convert_value(inp_val=1.0, inp_units="ft**2/s", out_units="ft**2/hr"), places=5)
        self.assertAlmostEqual(1.0, 92903 / convert_value(inp_val=1.0, inp_units="ft**2/s", out_units="centistokes"), places=5)
        #  Volume  Using English ref of 1.0 inch**3 == inch**3
        self.assertAlmostEqual(1.0, 1.63871e-05 / convert_value(inp_val=1.0, inp_units="inch**3", out_units="m**3"), places=5)
        self.assertAlmostEqual(1.0, 2.14335e-05 / convert_value(inp_val=1.0, inp_units="inch**3", out_units="yd**3"), places=5)
        self.assertAlmostEqual(1.0, 0.000103072 / convert_value(inp_val=1.0, inp_units="inch**3", out_units="barOil"), places=5)
        self.assertAlmostEqual(1.0, 0.000578704 / convert_value(inp_val=1.0, inp_units="inch**3", out_units="ft**3"), places=5)
        self.assertAlmostEqual(1.0, 0.00360464 / convert_value(inp_val=1.0, inp_units="inch**3", out_units="galUK"), places=5)
        self.assertAlmostEqual(1.0, 0.004329 / convert_value(inp_val=1.0, inp_units="inch**3", out_units="galUS"), places=5)
        self.assertAlmostEqual(1.0, 0.0163871 / convert_value(inp_val=1.0, inp_units="inch**3", out_units="liter"), places=5)
        self.assertAlmostEqual(1.0, 0.017316 / convert_value(inp_val=1.0, inp_units="inch**3", out_units="quart"), places=5)
        self.assertAlmostEqual(1.0, 0.034632 / convert_value(inp_val=1.0, inp_units="inch**3", out_units="pint"), places=5)
        self.assertAlmostEqual(1.0, 0.0692641 / convert_value(inp_val=1.0, inp_units="inch**3", out_units="cup"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="inch**3", out_units="in**3"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="inch**3", out_units="inch**3"), places=5)
        self.assertAlmostEqual(1.0, 16.3871 / convert_value(inp_val=1.0, inp_units="inch**3", out_units="cm**3"), places=5)
        self.assertAlmostEqual(1.0, 16.3871 / convert_value(inp_val=1.0, inp_units="inch**3", out_units="ml"), places=5)
        #  VolumeFlow  Using English ref of 1.0 inch**3/s == inch**3/s
        self.assertAlmostEqual(1.0, 1.63871e-05 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="m**3/s"), places=5)
        self.assertAlmostEqual(1.0, 0.000578704 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="ft**3/s"), places=5)
        self.assertAlmostEqual(1.0, 0.004329 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="galUS/s"), places=5)
        self.assertAlmostEqual(1.0, 0.0163871 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="l/s"), places=5)
        self.assertAlmostEqual(1.0, 0.0347222 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="ft**3/min"), places=5)
        self.assertAlmostEqual(1.0, 0.0589934 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="m**3/hr"), places=5)
        self.assertAlmostEqual(1.0, 0.25974 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="galUS/min"), places=5)
        self.assertAlmostEqual(1.0, 0.25974 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="gpm"), places=5)
        self.assertAlmostEqual(1.0, 1 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="inch**3/s"), places=5)
        self.assertAlmostEqual(1.0, 2.08333 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="ft**3/hr"), places=5)
        self.assertAlmostEqual(1.0, 15.5844 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="galUS/hr"), places=5)
        self.assertAlmostEqual(1.0, 16.3871 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="ml/s"), places=5)
        self.assertAlmostEqual(1.0, 60 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="inch**3/min"), places=5)
        self.assertAlmostEqual(1.0, 374.026 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="galUS/day"), places=5)
        self.assertAlmostEqual(1.0, 983.224 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="ml/min"), places=5)
        self.assertAlmostEqual(1.0, 3600 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="inch**3/hr"), places=5)
        self.assertAlmostEqual(1.0, 58993.4 / convert_value(inp_val=1.0, inp_units="inch**3/s", out_units="ml/hr"), places=5)


# if __name__ == '__main__':
#     # Can test just this file from command prompt
#     #  or it can be part of test discovery from nose, unittest, pytest, etc.
#     unittest.main()

