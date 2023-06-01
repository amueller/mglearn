from setuptools import setup, find_packages

setup(
    name="mglearn",
    version="0.2.0",
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'scikit-learn', 'pandas',
                      'pillow', 'cycler', 'imageio', 'joblib'],
    include_package_data=True,

    author="Andreas Mueller",
    author_email="t3kcit@gmail.com",
    description=("Helper functions for the book "
                 "Introduction to machine learning with Python"),
    long_description=("Helper functions for the book "
                      "`Introduction to machine learning with Python`"),
    long_description_content_type="text/markdown",
    license="BSD",
    keywords="machine learning ml sklearn scikit learn",
    url="https://github.com/amueller/introduction_to_ml_with_python",
)
