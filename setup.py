# setup.py
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SQLGlassBoxFunction",
    version="0.1.4",
    author="Gordil",
    author_email="gordil.tech@gmail.com",
    description="A package to provide glass box functions for SQL analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gordil/SQL-glass-box-function",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)