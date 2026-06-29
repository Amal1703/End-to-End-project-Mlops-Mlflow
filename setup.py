import setuptools


#The setup.py file is the identity card of the project.

#It answers questions like:

#What is the name of the project?
#What is its version?
#Who is the author?
#Which Python files are part of the package?
#Which libraries need to be installed?


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-End-project-Mlops-Mlflow" # name of your GitHub repository
AUTHOR_USER_NAME = "Amal Kammoun"
SRC_REPO = "mlProject" # Variable that stores the package name as it will appear on PyPI and how users will install it
AUTHOR_EMAIL = "kamounamal34@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}", # Github url
    project_urls={  # project_urls : additional links displayed on your PyPI page
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues", # report bugs
    },
    package_dir={"": "src"},  # source code is located in the src folder
    packages=setuptools.find_packages(where="src") # automatically discovers Python packages under the src directory
)

# python setup.py install


