.. commit signature, "date_str author_str sha_str"
   Maintain spacing of "History" and "GitHub Log" titles

History
=======


RocketUnits History
-------------------

**RocketUnits** was largely developed on the three companion projects
`RocketCEA <https://rocketcea.readthedocs.io/en/latest/>`__ ,
`RocketIsp <https://rocketisp.readthedocs.io/en/latest/>`__ and 
`RocketProps <https://rocketprops.readthedocs.io/en/latest/>`__.

`RocketCEA <https://rocketcea.readthedocs.io/en/latest/>`__
makes direct calls to the NASA FORTRAN CEA code in “rocket” mode to 
calculate Isp, Cstar, Tcham etc. and provides tools to help determine 
useful mixture ratio range, optimum MR and more.

`RocketIsp <https://rocketisp.readthedocs.io/en/latest/>`__ uses a simplified JANNAF 
approach to calculate delivered specific impulse (Isp) for liquid rocket thrust chambers.

`RocketProps <https://rocketprops.readthedocs.io/en/latest/>`__
calculates the various liquid propellant properties required to analyze 
a liquid propellant thrust chamber.


GitHub Log
----------

* Apr 11, 2022
    - (by: Charlie)
        - version 0.1.11 includes more William True suggestions
        - doc updates

* Apr 4, 2022
    - (by: Charlie)
        - Added Units from William True

* Jan 7, 2022
    - (by: Charlie)
        - added hPa to pressure

* Dec 9, 2021
    - (by: Charlie)
        - added CoeffThermExp(CTE)

* Dec 5, 2021
    - (by: Charlie)
        - when psid is default, do not output psia
        - added tests for last updates

* Dec 2, 2021
    - (by: Charlie)
        - added inch output regulation
        - added some convenience methods to set user's input units

* Nov 29, 2021
    - (by: Charlie)
        - added HeatFlux
        - updated comparison to pint results

* Nov 28, 2021
    - (by: Charlie)
        - added Tank PV/W

* Nov 27, 2021
    - (by: Charlie)
        - v 0.1.9 adds "None <units>" option
        - added __main__ test using importlib

* Nov 26, 2021
    - (by: Charlie)
        - wrote docs for units_io

* Nov 24, 2021
    - (by: Charlie)
        - included pint conversion check
        - added units_io

* Nov 21, 2021
    - (by: Charlie)
        - trying to fix ReadTheDocs problem
        - try to fix READTHEDOCS functions.html
        - added convert_string to rocket_units.py

* May 8, 2021
    - (by: sonofeft)
        - tweaked docs, added version number to title

* May 7, 2021
    - (by: sonofeft)
        - Update docs for refactored code
        - refactored the code

* May 6, 2021
    - (by: sonofeft)
        - Updated docs
        - Update example_1.py
        - remove python 2.7 future imports

* May 5, 2021
    - (by: sonofeft)
        - update tox.ini
        - sphinx files added
        - travis CI only check out python 3.7
        - add a short unit test
        - put EXE in rocketunits
        - Initial Commit
        - Initial commit
        - 
* May 04, 2021
    - (by: sonofeft)
        - First Created RocketUnits with PyHatch
