from setuptools import setup, find_packages

setup(
    name="spring-mass-simulator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "plotly",
        "dash",
    ],
)
