from setuptools import setup, find_packages
from infosystem._version import version


REQUIRED_PACKAGES = [
    'alembic==1.6.2',
    'amqp==5.0.6',
    'APScheduler==3.7.0',
    'attrs==21.2.0',
    'billiard==3.6.4.0',
    'celery==5.0.5',
    'certifi==2020.12.5',
    'chardet==4.0.0',
    'click==7.1.2',
    'click-didyoumean==0.0.3',
    'click-plugins==1.1.1',
    'click-repl==0.1.6',
    'colorama==0.4.4',
    'decorator==5.0.8',
    'Flask==2.0.0',
    'Flask-Migrate==2.7.0',
    'Flask-RBAC==0.5.0',
    'Flask-SQLAlchemy==2.5.1',
    'gabbi==2.2.0',
    'greenlet==1.1.0',
    'idna==2.10',
    'iniconfig==1.1.1',
    'itsdangerous==2.0.0',
    'Jinja2==3.0.0',
    'jsonpath-rw==1.4.0',
    'jsonpath-rw-ext==1.2.2',
    'kombu==5.0.2',
    'Mako==1.1.4',
    'MarkupSafe==2.0.0',
    'packaging==20.9',
    'pbr==5.6.0',
    'pika==1.2.0',
    'Pillow==8.2.0',
    'pluggy==0.13.1',
    'ply==3.11',
    'prompt-toolkit==3.0.18',
    'py==1.10.0',
    'pyparsing==2.4.7',
    'pytest==6.2.4',
    'python-dateutil==2.8.1',
    'python-editor==1.0.4',
    'pytz==2021.1',
    'PyYAML==5.4.1',
    'requests==2.25.1',
    'six==1.16.0',
    'sparkpost==1.3.9',
    'SQLAlchemy==1.4.15',
    'toml==0.10.2',
    'tzlocal==2.1',
    'urllib3==1.26.5',
    'vine==5.0.0',
    'wcwidth==0.2.5',
    'Werkzeug==2.0.0',
    'wsgi-intercept==1.9.2',
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
