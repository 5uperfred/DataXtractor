from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="DataXtractor",
    version="1.0.7",
    description="DataXtractor is a versatile Python library designed to simplify the extraction of valuable data from a variety of sources, including images and PDF documents. Whether you need to extract text, tables, or structured content, DataXtractor provides powerful and intuitive tools to streamline the process.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rahul Katoch",
    author_email="rahulkatoch99@gmail.com",
    url="https://github.com/Rahulkatoch99/DataXtractor",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "opencv-python",
        "pytesseract",
        "pdf2image",
        "pdftotext",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="data extraction pdf image",
    python_requires=">=3.6",
    license="MIT",
)
