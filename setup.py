#!/usr/bin/python
from setuptools import setup
import distutils.command.install_scripts
import shutil


f = open('README')
long_description = f.read().strip()
f.close()

class strip_py_ext(distutils.command.install_scripts.install_scripts):
    def run(self):
        distutils.command.install_scripts.install_scripts.run(self)
        for script in self.get_outputs():
            if script.endswith(".py"):
                shutil.move(script, script[:-3])


setup(
    name = "redis_monitor",
    version= "1.0",
    description= "Show the statistics about redis server",
    long_description = long_description,
    author = "Filippo Ferrazini",
    author_email = "filippo.ferrazini@gmail.com",
    url = "https://github.com/Filippo125/redis_monitor",
    license = "MIT",
    packages = ["rmonitor"],
    install_requires=["redis"],
    scripts = [ "redis_monitor.py" ],
    cmdclass = {
        "install_scripts" : strip_py_ext
    },
    keywords='monitoring redis',
)
