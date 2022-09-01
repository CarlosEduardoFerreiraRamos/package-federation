from asyncio import subprocess
from distutils.core import setup
import os
import sys

install_requires = [
        'app_one',
        'app_two',
        'app_three'
    ]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", f"../{package}"])

for r in install_requires:
    install(r)

setup(
    name="app_config",
    packages=["app_config"],
    install_requires=install_requires
)