import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sammy-sjsu-dev2",
    version="0.0.2",
    author="SJSU-Dev2 Organization",
    description="A tool for managing SJSU-Dev2 firmware projects and to install external packages such as platforms and libraries.",long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SJSU-Dev2/sammy/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)