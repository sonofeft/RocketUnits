rem python setup.py sdist bdist_wheel

rem only upload source to PyPI
twine upload --repository testpypi --skip-existing dist/*.gz

rem use:  twine check dist/*  OR twine check dist/*24.tar.gz (where: 24 is current version)

rem C:\Users\Charlie\AppData\Roaming\Python\Scripts\twine.exe upload --repository testpypi --skip-existing dist/*.gz
rem C:\Users\Charlie\AppData\Roaming\Python\Scripts\twine.exe upload --repository testpypi  dist/*
