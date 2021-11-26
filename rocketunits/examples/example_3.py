"""
This example demonstrates the typical use units_io
"""

from rocketunits.units_io import Units

class Bar:
    def __init__(self, xxx, x="4 ft**2", y="5 s", z="6 ft/s**2", j=66,
                 output_units="Both"):
        self.my_io = Units( self.__class__, locals() )

        self.x = self.my_io.get_input_value("x")
        self.y = self.my_io.get_input_value("y")
        self.z = self.my_io.get_input_value("z")
        self.j = j

        self.xxx = self.my_io.get_input_value("xxx", def_units="deg")

        self.xxx_x3 = 3.0 * self.xxx
        self.my_io.set_units_same_as("xxx_x3", "xxx")

    def summ_print(self):

        # give Units object the current locals()/vars()
        self.my_io.set_vars_dict( vars(self) )
        self.my_io.set_print_template( template="%12s = %-45s %s")

        u_print = self.my_io.u_print
        for name in self.my_io.default_unitsD.keys():
            u_print(name)

        print()

b = Bar( 32.2, z="9.80665 m/s**2", y="3 hr", x=6 )
b.summ_print()
