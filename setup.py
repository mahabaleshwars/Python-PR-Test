from setuptools import setup

setup(
    name="sampleproject",
    version="0.1.0",
    install_requires=[
        "requests==2.31.0"
    ],
    extras_require={
        "test": ["pytest==7.4.0"]
    }
)
