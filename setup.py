from setuptools import setup, find_packages

setup(
    name="spring-mass-simulator",
    version="0.1.0",
    description="Interactive spring–mass–damper simulator with engineering dashboard",
    author="Mehrdad",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "scipy"
    ],
    python_requires=">=3.8",
)
