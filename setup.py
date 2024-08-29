from setuptools import setup, find_packages

setup(
    name="python-sdk",
    version="0.1.0",
    description="A Python SDK for interacting with LiteAPI's hotel and booking services.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/python-sdk",  # Replace with your GitHub repo URL
    packages=find_packages(exclude=["tests", "venv"]),
    install_requires=[
        "requests>=2.25.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
