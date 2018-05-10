from setuptools import setup


setup(
    name='nagiosapi',
    packages=['nagiosapi'],
    include_package_data=True,
    install_requires=[
        'flask'
    ],
    test_suite="tests",
)
