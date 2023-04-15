from setuptools import setup, find_packages

setup(
    name="llm-prompt-cache",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'psutil'
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A caching library for language model prompts and responses using Jaccard similarity",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/llm-prompt-cache",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
