
from math import log
from rocketunits.units_io import Units

class RocketDeltaV:

    gc = 32.174 # gravitational converstion factor lbm-ft/lbf-sec**2

    def __init__(self, Isp="330.0 sec", mass="10000.0 lbm", prop_mass_frac=0.8):

        """
        Calculate the ideal rocket velocity based on the percent of propellant burned.
        (see: https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation)
        (or: https://www.translatorscafe.com/unit-converter/en-US/calculator/rocket-equation/)

        Args:
            Isp (float): specific impulse, sec (https://en.wikipedia.org/wiki/Specific_impulse)
            mass (float): total rocket mass, lbm
            prop_mass_frac (float): mass fraction of rocket that is propellant
        """
        # let Units inspect the class interface and get locals() values
        self.my_io = Units( self.__class__, locals() )

        # let Units convert inputs into internal units (sec and lbm)
        self.Isp            = self.my_io.get_input_value("Isp")
        self.mass           = self.my_io.get_input_value("mass")
        self.prop_mass_frac = prop_mass_frac # note: mass fraction is unitless

    def summarize_delta_v(self, pcent_burned=100.0, output_units="Both"):
        """
        Assuming a given percentage of the propellant is burned, 
        calculate the ideal change in velocity, ft/sec
        Print a summary of the calculation.

        Args:
            pcent_burned (float): percent of propellant burned
        Returns:
            delta_v (float): ideal rocket velocity, ft/s
        """
        if pcent_burned < 0.0 or pcent_burned > 100.0:
            raise Exception("pcent_burned must be >=0 and <=100")
        
        self.pcent_burned = pcent_burned
        self.prop_mass = (pcent_burned/100.0) * self.prop_mass_frac * self.mass
        self.final_mass = self.mass-self.prop_mass
        self.delta_v = self.gc * self.Isp * log( self.mass / self.final_mass )


        # give Units object the current locals()/vars()
        self.my_io.set_output_units(output_units=output_units)
        self.my_io.set_vars_dict( vars(self) )
        self.my_io.set_print_template( template="%16s = %-45s %s")
        self.my_io.set_units('prop_mass', 'lbm')
        self.my_io.set_units('pcent_burned', '')
        self.my_io.set_units('final_mass', 'lbm')
        self.my_io.set_units('delta_v', 'ft/s')

        # make a convenience copy of my_units.u_print
        u_print = self.my_io.u_print

        # lazy way to iterate over object parameters known to Units.
        for name in self.my_io.default_unitsD.keys():
            u_print(name)

        u_print("delta_v", primary_units="km/hr", added_units="mile/hr")
        print()

R = RocketDeltaV(Isp="330.0 sec", mass="10000.0 lbm", prop_mass_frac=0.8)

R.summarize_delta_v( pcent_burned=100.0, output_units="English" )
R.summarize_delta_v( pcent_burned=100.0, output_units="Both" )

