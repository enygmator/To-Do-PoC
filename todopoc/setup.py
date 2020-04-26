import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='todopoc',
    version='1.2',
    author='Tarun & Moyank & Vaibhav',
    author_email='tarun.aditya.bc@gmail.com',
    description='A To-Do app for Proof of various Concepts',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/enygmator/To-Do-PoC",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Development Status :: 7 - Inactive",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: JavaScript",
        "Programming Language :: Unix Shell",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license='Apache license 2.0',
    include_package_data=True,
    zip_safe=False)