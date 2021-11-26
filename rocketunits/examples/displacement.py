


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

