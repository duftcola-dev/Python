from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name="web_scraper_cli",
    version="1.0.0",
    py_modules=["./cli/scripts/web"],
    install_requires=[
        "click",
        "beautifulsoup4",
        "requests",
        "pytest"

    ],
    entry_points={
        "console_scripts":[
            "web=scripts.web:crawl",
            ],
    },
)