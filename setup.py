from setuptools import setup, find_packages

setup(
    name="geotools",
    version="1.0.0",
    description="Geotools - this is a set of scripts for solving three educational tasks.",
    author="---",
    author_email="---",
    packages=find_packages(),
    install_requires=["geopandas", "shapely"],
    entry_points={
        "console_scripts": ["geom_cut=geotools.geom_cut:main"],
    },
    extras_require={"dev": ["pytest"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
