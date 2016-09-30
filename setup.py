from setuptools import setup, find_packages

setup(
    name="mglearn",
    version="0.1",
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'scikit-learn'],

    author="Andreas Mueller",
    author_email="t3kcit@gmail.com",
    description=("Helper functions for the book "
                 "'Introduction to machine learning with Python'"),
    license="BSD",
    keywords="machine learning ml sklearn scikit learn",
    url="https://github.com/amueller/introduction_to_ml_with_python",
)
