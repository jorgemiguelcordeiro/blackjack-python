# automatically looks for folders containing __init__.py files in order to not list every single folder manually.

from setuptools import setup, find_packages

setup(
    name="blackjack", #if we upload this to PyPI (the Python App Store), this is what people would type to install it (pip install blackjack).
    version="0.1.0", #first functional draft
    packages=find_packages(),
    description="OOP Blackjack game",
    author="Jorge Cordeiro",
    entry_points={
        'console_scripts': [ # make a command executable in the terminal
            'play-blackjack=blackjack.game:main', #play-blackjack in any terminal window
        ],
    },
)