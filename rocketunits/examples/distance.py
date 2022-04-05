
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
    GETVAL = my_units.get_input_value # a convenience method
    
    # let Units convert inputs into internal units
    vinit = GETVAL("vinit")
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

