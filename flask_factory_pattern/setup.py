
# THE goal of this file is to make this flask application and installable package 
# that can be moved around
# spifify the main deppendencies this project requries in instakll requires 
# other files like templates and static can be spefifyed in MANIFEST.in

# install the project with pip install -e .

# Nothing changes from how you’ve been running your project so far. 
# FLASK_APP is still set to flaskr and flask run still runs the 
# application, but you can call it from anywhere, not just the 
# flask-tutorial directory.

from setuptools import find_packages, setup
setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)