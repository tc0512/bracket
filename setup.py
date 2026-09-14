# setup.py
from pathlib import Path
from setuptools import setup, find_packages

# 读取 README
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setup(
    name="bracket-lang",
    version="0.4.0",
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
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
