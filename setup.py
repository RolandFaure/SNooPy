from setuptools import setup

setup(
    name='snoopy',
    version='0.4.3',
    python_requires='>=3.8',
    py_modules=['snoopy'],
    entry_points={
        'console_scripts': [
            'snoopy = snoopy:main'
        ]
    },
)
