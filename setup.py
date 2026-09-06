# setup.py
from setuptools import setup, find_packages

setup(
    name="bracket-lang",
    version="0.3.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "bracket = bracket.cli:main",
        ],
    },
    python_requires=">=3.8",
    install_requires=[
        "rich>=13.0.0",
        "pyinstaller>=6.0.0"
    ]
)
