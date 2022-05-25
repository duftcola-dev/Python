from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name="scripts",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click"],
    entry_points={
        "console_scripts":[
            "config=scripts.config:config",
            "load=scripts.config:load_config",
            "reset=scripts.config:reset_config",
            "execute=scripts.execute:execute"
        ]
    }

)