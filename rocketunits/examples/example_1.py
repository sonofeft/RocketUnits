"""
This example demonstrates a call to rocketunits.convert_value
"""
from rocketunits.rocket_units import convert_value

def disp( val, inp_units, out_units ):
    # use convert_value to convert inp_units to out_units
    ans = convert_value(val, inp_units, out_units)
    
    print( f'{val} {inp_units} = {ans} {out_units}' )

# convert_value gives the following output

disp( 180, 'deg', 'rad' )      # ==> 180 deg = 3.1415926535820002 rad

disp( 100, 'rpm', 'deg/s' )    # ==> 100 rpm = 600.0 deg/s

disp( 1, 'lbm/in**3', 'g/ml' ) # ==> 1 lbm/in**3 = 27.6799047102 g/ml
