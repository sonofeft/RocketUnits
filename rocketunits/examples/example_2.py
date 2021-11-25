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

    def summ_print(self):

        # give Units object the current locals()/vars()
        self.my_io.set_vars_dict( vars(self) )
        self.my_io.set_print_template( template="%12s = %-45s | %s")

        print()
        u_print = self.my_io.u_print
        u_print("x", "area of interest")
        u_print("x")
        u_print("x", "area of interest", "inch**2", added_units="cm**2")

        print()
        u_print("xxx",  desc="Angle of interest")
        u_print("xxx", primary_units="rad", desc="Angle of interest")
        u_print("xxx", "Angle of interest", "rad", "circle")

        print()
        u_print("y", desc="Time of flight", added_units="hr")
        u_print("j", desc="Just a Number")



b = Bar( 32.2, z="1 gee", y="3 hr", x=6 )
b.summ_print()
