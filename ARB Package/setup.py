from setuptools import setup
from distutils.core import setup

setup(
    name="ARB-Recommender",
    version="0.0.1",
    description="ARB-Recommender : A Movie Recommendation toolkit",
    author="Alla Durga Umesh Chandra",
    author_email="umeshalla3@gmail.com",
    py_modules=["ARB-Recommender"],
    package_dir={"":"SRC"},
    include_package_data=True,
    )
