# Redis Monitor 
[![Build Status](https://travis-ci.org/Filippo125/redis_monitor.svg?branch=devel)](https://travis-ci.org/Filippo125/redis_monitor)

This project is a simple utility to monitoring a redis server

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

Installing the tool can be done in two ways, by running the main script directly or through seuptools.

#### Using main script
```
1. cd to the utility directory
2. run the script: python3 redis_monitor.py <options>
```
#### Using python-setuptools
This will install a hook for redis_monitor in /usr/bin so running the script doesn't
need the .py extension.
```
1. cd to the utility directory
2. run the setup.py: python setup.py install
3. use redis_monitor <options>
```


## Running the tests
To do test use tox, coverage and pytest.<br>

### Test
Run tox, it build a python3.7 virtual environment,install dependencies and execute pytest 
### Coverage
Coming soon....

### And coding style tests

All source code try to handle PEP8 with little change:<br>
1. the max line length is increase up to 160 characters
2. ignore E221 (multiple spaces before operator)<br>

To verify compliance with specifications use pycodestyle package.
The pycodestyle configuration is:
```
[pycodestyle]
count = False
ignore = E221
max-line-length = 160
statistics = True
```
Install pycodestyle
```
pip install pycodestyle
```
The output is something like:
```
$ pycodestyle
.\redis_monitor.py:9:1: E302 expected 2 blank lines, found 1
.\redis_monitor.py:9:18: E231 missing whitespace after ','
.\redis_monitor.py:26:42: W291 trailing whitespace
.\redis_monitor.py:28:30: E231 missing whitespace after ','
```
or if there aren't any issue:
```
$ pycodestyle

```




## Built With
* [redis](https://pypi.org/project/redis/) - The Python interface to the Redis key-value store

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
