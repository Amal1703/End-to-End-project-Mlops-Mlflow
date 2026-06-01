import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-End-project-Mlops-Mlflow" # nom de votre repo GitHub
AUTHOR_USER_NAME = "Amal Kammoun"
SRC_REPO = "mlProject" # variable qui stocke le nom de votre package tel qu'il apparaîtra sur PyPI et comment les utilisateurs l'installeront
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
    project_urls={  # project_urls : Les liens supplémentaires sur votre page PyPI 
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues", # Signaler des bugs
    },
    package_dir={"": "src"},  # code source est dans le dossier src
    packages=setuptools.find_packages(where="src") # recherche automatiquement les packages Python sous src
)

# la page PyPI de votre package End-to-End-project-Mlops-Mlflow (SRC_REPO)
# La page PyPI est la page web publique que tout le monde voit quand ils cherchent ou consultent votre package sur pypi.org
# PyPI :	Page d'un package Python avec description, installation, code
