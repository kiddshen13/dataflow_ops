from setuptools import setup, find_packages

setup(
    name="dataflow",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # Add any package dependencies here
    install_requires=[
        # e.g., 'requests >= 2.25.1',
    ],
    # If you have scripts or executables, you can specify them here
    scripts=[
        # e.g., 'bin/script1',
    ],
    # Specify test suite (optional)
    test_suite="tests",
)
