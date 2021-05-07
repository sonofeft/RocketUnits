.. usage


Using RocketUnits GUI
=====================

The motivation behind **RocketUnits** is to allow for the quick copy and paste
of conversions for physical unit values in the desired number format.

Because the values are listed in ascending order, **RocketUnits** also gives
at-a-glance intuition as to the relative size of different units.

Category
--------

To use **RocketUnits**, select a units Category,
for example *Length* as shown below.

The full complement of physical unit categories includes;
Acceleration, Angle, AngVelocity, 
Area, DeltaT, Density, ElementDensity, Energy, Specific Energy, Force, Frequency, 
Heat Capacity, Heat Transfer Coefficient, Isp, Length, Mass, MassFlow, 
Molecular Weight, Power, 
Pressure, Surface Tension, Temperature, Thermal Conductivity, Time, Velocity, 
Viscosity_Dynamic, Viscosity_Kinematic, Volume, and VolumeFlow.

Note that new categories and units can be added by editing the 
file **rocket_units.py**.

.. image:: ./_static/categories.jpg
    :alt: Categories Selection
    

Units 
-----

Then select the desired reference *Units* as shown below.

.. image:: ./_static/pick_units.jpg
    :alt: Units Selection

Value 
-----

Enter the *Value* of the reference *Units* and see all the resulting
values of other units in the *Category*.

.. image:: ./_static/enter_value.jpg
    :alt: Value Entry

Number Format
-------------

Select the desired number format from the drop-down selector shown below.

.. image:: ./_static/number_format_options.jpg
    :alt: Number Format Selection

Examples from the Length *Cagegory* are shown below.

.. image:: ./_static/number_format_comparison.jpg
    :alt: Number Format Comparison


.. _import-rocketunits:

Importing RocketUnits
---------------------


Unit conversion can be performed either with the GUI, or directly
from python by importing **RocketUnits**.

The following code demonstrates how to call **rocket_units.convert_value** 
from a python file.

.. code-block:: python

    from rocketunits.rocket_units import convert_value

    def disp( val, inp_units, out_units ):
        # use convert_value to convert inp_units to out_units
        ans = convert_value(val, inp_units, out_units)
        
        print( f'{val} {inp_units} = {ans} {out_units}' )

    # convert_value gives the following output
    
    disp( 180, 'deg', 'rad' )      # ==> 180 deg = 3.1415926535820002 rad

    disp( 100, 'rpm', 'deg/s' )    # ==> 100 rpm = 600.0 deg/s

    disp( 1, 'lbm/in**3', 'g/ml' ) # ==> 1 lbm/in**3 = 27.6799047102 g/ml




