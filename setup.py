import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alphavantage-wrapper",
    version="0.0.4",
    author="Paulo Alexandre Regis",
    author_email="regisin@gmail.com",
    description="A simple wrapper for the Alpha Vantage API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/regisin/alphavantage_wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)