from setuptools import setup, find_packages

setup(
    name = 'potasio',
    version = '0.1',
    description = '',
    author = 'Alfredo Deza',
    author_email = 'contact[at]deza.pe',
    install_requires = [
        "Mako==0.7.3",
        "MarkupSafe==0.15",
        "WebHelpers==1.3",
        "WebOb==1.2.3",
        "WebTest==1.4.3",
        "pecan==0.3.0",
        "simplegeneric==0.8.1",
        "wsgiref==0.1.2",
        "beaker",
    ],
    zip_safe = False,
    include_package_data = True,
    packages = find_packages(exclude=['ez_setup']),
)
