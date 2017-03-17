from setuptools import setup, find_packages

setup(
    name="mglearn",
    version="0.1.5",
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'scikit-learn', 'pandas',
                      'pillow', 'cycler'],
    include_package_data=True,

    author="Andreas Mueller",
    author_email="t3kcit@gmail.com",
    description=("Helper functions for the book "
                 "'Introduction to machine learning with Python'"),
    license="BSD",
    keywords="machine learning ml sklearn scikit learn",
    url="https://github.com/amueller/introduction_to_ml_with_python",
)
