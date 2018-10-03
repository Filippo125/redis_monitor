#!/usr/bin/python
from setuptools import setup
import distutils.command.install_scripts
import shutil

import sys
if sys.version_info < (2,7):
    sys.exit('Sorry, Python < 2.7 is not supported')

# idea from http://stackoverflow.com/a/11400431/2139420
class strip_py_ext(distutils.command.install_scripts.install_scripts):
    def run(self):
        distutils.command.install_scripts.install_scripts.run(self)
        for script in self.get_outputs():
            if script.endswith(".py"):
                shutil.move(script, script[:-3])


setup(
    name="redis_monitor",
    version="1.2",
    description="Show the statistics about redis server",
    long_description="Show the statistics about redis server",
    author="Filippo Ferrazini",
    author_email="filippo.ferrazini@gmail.com",
    url="https://github.com/Filippo125/redis_monitor",
    license="MIT",
    packages=["redis_monitor"],
    install_requires=["redis"],
    scripts=["redis_monitor.py"],
    cmdclass={"install_scripts": strip_py_ext},
    keywords="monitoring redis",
)
