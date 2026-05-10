"""
Setup script for CTypes Mini Project

Installation:
    pip install -e .
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ctypes-mini-project",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A complete ctypes project with pytest framework and test cases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shekharsuman12121-sudo/pythonproject",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Software",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest-cov>=3.0.0",
            "pytest-html>=3.0.0",
            "pytest-xdist>=2.5.0",
        ],
    },
)
