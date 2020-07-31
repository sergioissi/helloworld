from setuptools import setup


with open("README.md", "r") as fp:
    long_description = fp.read()

setup(
    name='helloworld',
    version='0.0.1',

    descritption='Say hello!',
    long_description=long_description,
    long_description_content_type="text/markdown",

    py_modules=["helloworld"],
    package_dir={'': 'src'},

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: GNU General Public License v3.0",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)