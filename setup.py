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
    name = "redisstats",
    version= "1.00",
    description= "Show the statistics about redis server",
    long_description = long_description,
    author = "Filippo Ferrazini",
    author_email = "filippo.ferrazini@gmail.com",
    url = "https://github.com/Filippo125/redisstats",
    license = "MIT",
    packages = [
        "redisstat",
        ],
    install_requires=["redis"],
    scripts = [ "main.py" ],
    cmdclass = {
        "install_scripts" : strip_py_ext
    }
)
