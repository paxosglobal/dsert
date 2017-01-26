from setuptools import (
    setup,
    find_packages
)
from datetime import datetime

version = "0.1.0+{}".format(datetime.now().strftime("%Y%m%d.%H%M%S"))

setup(
    name='dsert',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    url='https://github.com/paxos-bankchain/dsert',
    license='',
    author='paxosdev',
    author_email='',
    description='',
)
