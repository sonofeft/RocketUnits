
.. units_io

Units for IO
============

In science and engineering programming, it is most common for programs to use 
a fixed set of internal units. Users with different units
from the internal units simply accept the responsibility of converting their
inputs into the software's required units.

The **Units** class in *rocketunits.units_io* addresses that issue by 
allowing users to input their natural units into software regardless of 
that softwares internal units.

For python functions or classes using fixed internal physical units, 
the **Units** class can allow those functions and classes to accept 
any units a user desires.

By changing the input parameters from float to strings of the form 
"<value> <units>", **Units** can accept and convert input values automatically.

For example:

.. code-block:: python3

    def my_func(P="14.7 psia", T="98.6 degF"):
        """
        P = Pressure with default units of psia (lbf/in**2)
        T = Temperature with default units of degF (Fahrenheit)
        """

**Units** assumes that the parameter default strings hold the internal 
units of the parameters.

When calling the function or class, either a new string with units 
specified or a simple numeric input can be used.

For example:

.. code-block:: python3

    # call my_func with pressure    = 10 atmospheres 
    #                   temperature = 72.0 degrees F
    my_func( P="10 atm", T=72.0 )


Any units of the same type (e.g. Pressure or Temperature ) can be input
as a "<value> <units>" string and **Units** will convert them to the 
internal units of "psia" and "degF".


.. _input-only-class:

Input-Only Class
----------------

The most common use case will probably be to allow any units to be input
into a function or class, but the function or class will still return 
values from its internal units.

The interface will accept the user's input units, but translate them into
the required internal units.

The following example demonstrates how to use **Units** to enable
a class to accept any units that RocketUnits recognizes. 
Note that the output units are not affected.

.. code-block:: python3

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

        def delta_v(self, pcent_burned=100.0):
            """
            Assuming a given percentage of the propellant is burned, 
            calculate the ideal change in velocity, ft/sec

            Args:
                pcent_burned (float): percent of propellant burned
            Returns:
                delta_v (float): ideal rocket velocity, ft/s
            """
            if pcent_burned < 0.0 or pcent_burned > 100.0:
                raise Exception("pcent_burned must be >=0 and <=100")
            prop_mass = (pcent_burned/100.0) * self.prop_mass_frac * self.mass
            delta_v = self.gc * self.Isp * log( self.mass / (self.mass-prop_mass) )
            return delta_v # ft/s

    R = RocketDeltaV(Isp="330.0 sec", mass="10000.0 lbm", prop_mass_frac=0.8)
    print(  "%g ft/s"%R.delta_v( 100.0 ) )

    R = RocketDeltaV(Isp="3236.2 m/sec", mass="10000.0 lbm", prop_mass_frac=0.8)
    print(  "%g ft/s"%R.delta_v( 100.0 ) )

The output from the above code gives the same answer for equivalent inputs 
with different units.

.. code-block:: python3

    17088.1 ft/s
    17088.1 ft/s



Input/Output Class
------------------

If using **Units** to create output, the parameter "output_units" 
can be included in the parameter list
so that **Units** will be sure to include units of type "SI", "English" or "Both".
(see the "summarize_delta_v" function below.)

The inclusion of "output_units" will also affect the number of units 
printed for input as well as output variables as shown in the example below.

The code below adds output functionality to the above example for 
:ref:`Input-Only Class<input-only-class>`.

.. code-block:: python3


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

            # add some units to "delta_v" output
            u_print("delta_v", primary_units="km/hr", added_units="mile/hr")
            print()

    R = RocketDeltaV(Isp="330.0 sec", mass="10000.0 lbm", prop_mass_frac=0.8)

    R.summarize_delta_v( pcent_burned=100.0, output_units="English" )
    R.summarize_delta_v( pcent_burned=100.0, output_units="Both" )

Notice in the output below how changing the value of "output_units" affects
the units displayed in the output.


.. code-block:: python3

    ..              Isp = 330 sec
    ..             mass = 10000 lbm
    ..   prop_mass_frac = 0.8
    ..        prop_mass = 8000 lbm
    ..     pcent_burned = 100
    ..       final_mass = 2000 lbm
    ..          delta_v = 17088.1 ft/s
    ..          delta_v = 18750.4 km/hr (11651 mile/hr, 17088.1 ft/s)

    ..              Isp = 330 sec (3236.19 m/sec)
    ..             mass = 10000 lbm (4535.92 kg)
    ..   prop_mass_frac = 0.8
    ..        prop_mass = 8000 lbm (3628.74 kg)
    ..     pcent_burned = 100
    ..       final_mass = 2000 lbm (907.185 kg)
    ..          delta_v = 17088.1 ft/s (5208.45 m/s)
    ..          delta_v = 18750.4 km/hr (11651 mile/hr, 17088.1 ft/s, 5208.45 m/s)

.. _input-only-function:

Input-Only Function
-------------------

As above for classes,
the most common use case for functions will probably be to allow any units to be input
into the function, but the function will still return 
values from its internal units.

The interface will accept the user's input units, but translate them into
the required internal units.

The following example demonstrates how to use **Units** to enable
a function to accept any units that RocketUnits recognizes. 
Note that the output units are not affected.

.. code-block:: python3

    from rocketunits.units_io import Units

    def distance( vinit="10.0 m/s", acc="9.80665 m/s**2", time="30 s"):
        """
        Calculate the distance traveled by an object with some initial velocity,
        and a constant acceleration over a given time.

        Note that any units available in RocketUnits may be used
        as inputs for vinit, acc and time.

        Args:
            vinit (float): Initial velocity, m/s
            acc (float): Acceleration(standard gravity=9.80665), m/s**2
            time (float): Time, s
        
        Returns:
            float: Distance traveled, m
        """
        # let Units inspect the distance interface and get locals() values
        my_units = Units( distance, vars() )
        
        # let Units convert inputs into internal units
        vinit = my_units.get_input_value("vinit")
        acc = my_units.get_input_value("acc")
        time = my_units.get_input_value("time")

        # with internal units, do the calculation
        d = vinit*time + acc * time**2 / 2.0
        return d # d will always be in units of meters, m

    # call the function with different units and compare results
    d = distance(vinit="1.0 m/s", acc="0.980665 m/s**2", time="60 s")
    print( "Returned Value for Distance = %g m"%d )

    d = distance( vinit="3.28084 ft/s", acc="0.1 gee", time="1 min" )
    print( "Returned Value for Distance = %g m"%d )

Using different units for equivalent inputs, gives identical results.

.. code-block:: python3

    Returned Value for Distance = 1825.2 m
    Returned Value for Distance = 1825.2 m

Input/Output Function
---------------------

If using **Units** to create output, the parameter "output_units" 
can be included in the parameter list
so that **Units** will be sure to include units of type "SI", "English" or "Both".

The inclusion of "output_units" will also affect the number of units 
printed for input as well as output variables (see the example below).

The code below adds output functionality to the above example for 
:ref:`Input-Only Function<input-only-function>` .

.. code-block:: python3

    from rocketunits.units_io import Units

    def distance( vinit="10.0 m/s", acc="9.80665 m/s**2", time="30 s", 
                output_units="SI" ):
        """
        Calculate the distance traveled by an object with some initial velocity,
        and a constant acceleration over a given time.

        Note that any units available in RocketUnits may be used
        as inputs for vinit, acc and time.

        Args:
            vinit (float): Initial velocity, m/s
            acc (float): Acceleration(standard gravity=9.80665), m/s**2
            time (float): Time, s
        
        Returns:
            float: Distance traveled, m
        """
        # let Units inspect the distance interface and get locals() values
        my_units = Units( distance, vars() )
        
        # let Units convert inputs into internal units
        vinit = my_units.get_input_value("vinit")
        acc = my_units.get_input_value("acc")
        time = my_units.get_input_value("time")

        # If using Units for output, tell Units the internal units for "d"
        my_units.set_units( "d", "m" )
        d = vinit*time + acc * time**2 / 2.0 # do the calculation with internal units

        # give local variable values to Units
        my_units.set_vars_dict( vars() )
        # set a desired output template
        my_units.set_print_template( template="%8s = %-40s %s")
        # make a convenience copy of my_units.u_print
        u_print = my_units.u_print

        u_print("vinit", "Initial velocity") # optional , fmt="%g"
        u_print("acc", "Acceleration")
        u_print("time", "Time")
        u_print("d", primary_units="km", added_units="yd")


        return d

    d = distance()
    print( "Returned Value for Distance = %g m"%d )
    print("===================================================")
    d = distance(output_units="English")
    print( "Returned Value for Distance = %g m"%d )
    print("===================================================")
    d = distance( vinit="32 ft/s", acc="1 gee", time="0.5 min",output_units="SI" )
    print( "Returned Value for Distance = %g m"%d )

The output of the above code is:

.. code-block:: python3
    
        vinit = 10 m/s                                 Initial velocity
        acc = 9.80665 m/s**2                           Acceleration
        time = 30 s                                    Time
        d = 4.71299 km (5154.19 yd, 4712.99 m)
    Returned Value for Distance = 4712.99 m
    ===================================================
        vinit = 10 m/s (32.8084 ft/s)                  Initial velocity
        acc = 9.80665 m/s**2 (32.174 ft/s**2)          Acceleration
        time = 30 s                                    Time
        d = 4.71299 km (5154.19 yd, 4712.99 m, 185551 inch)
    Returned Value for Distance = 4712.99 m
    ===================================================
        vinit = 32 ft/s (9.7536 m/s)                   Initial velocity
        acc = 1 gee (9.80665 m/s**2)                   Acceleration
        time = 0.5 min (30 s)                          Time
        d = 4.7056 km (5146.11 yd, 4705.6 m)
    Returned Value for Distance = 4705.6 m

