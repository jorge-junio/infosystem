from setuptools import setup, find_packages
from infosystem._version import version

REQUIRED_PACKAGES = [
    'apscheduler',
    'flask==1.1.2',
    'werkzeug==1.0.1',
    'itsdangerous==1.1.0',
    'Jinja2==2.11.3',
    'MarkupSafe==1.1.1',
    'attrs==20.3.0',
    'flask-rbac',
    'flask-sqlalchemy',
    'flask-migrate',
    'gabbi',
    'pika',
    'sparkpost',
    'celery',
    'pillow'
]

setup(
    name='infosystem',
    version=version,
    summary='Infosystem Framework',
    url='https://github.com/objetorelacional/infosystem',
    author='Samuel de Medeiros Queiroz, Francois Oliveira',
    author_email='samueldmq@gmail.com, oliveira.francois@gmail.com',
    license='Apache-2',
    packages=find_packages(exclude=["tests"]),
    install_requires=REQUIRED_PACKAGES
)
