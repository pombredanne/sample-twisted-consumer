from setuptools import setup

setup(
    name = 'sample-twisted-consumer',
    packages = ['sample_twisted_consumer'],
    version = '0.0.1',
    description = 'Sample library that uses twisted',
    author = 'Quinn Slack',
    author_email = 'sqs@sourcegraph.com',
    url = 'https://github.com/sourcegraph/sample-twisted-consumer',
    install_requires = ['Twisted'],
)
