from setuptools import setup, find_packages

setup(
    name='Library App',
    version='1.0',
    author='Liubomyr Vykhvatniuk',
    author_email='lubomirvihvatniuk@gmail.com',
    description='Web application to manage books, authors, orders and users using '
                'web service',
    url='https://github.com/lubart2517/Epam_project',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==2.0.0',
        'Flask-Migrate==3.0.0',
        'Flask-RESTful==0.3.8',
        'Flask-SQLAlchemy==2.5.1',
        'marshmallow-sqlalchemy==0.25.0',
    ]
)