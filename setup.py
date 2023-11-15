import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sqlalchemywrapper',
    version='0.1.3',
    author='Alex Q',
    author_email='alex.quan0807@gmail.com',
    description='Personal Wrapper for SQL Alchemy operations',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['sqlalchemywrapper'],
    install_requires=[
        "sqlalchemy",
        "mysqlclient"
    ],
)