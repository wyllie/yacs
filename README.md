# Yacs
Yet Another Cow Say

## WHY?
The main goal of this is to demonstrate  some of the features of Python OO
in hopefully a fun way.

This porgram could easily be written as a standalone script.  The idea here
though is to build something that can be used from a number of different
applications.  A simple command line interface is provided here, but the Yacs
object sould also be intergrated into a larger application like a website
via flask or eve provided as a serivce using AWS Lambda/ApiGateway.

## Install

As this is really just a demo, the best way to use it is to just grab the sources
from github:
```
$ mkdir Yacs
$ git clone git@github.com:wyllie/yacs.git
``` 

Alternatively, you can install it via pip
```
$ pip install git+ssh://git@github.com/wyllie/yacs.git -t /some/directory
```

--OR, even better--

```
$ pip install git+ssh://git@github.com/wyllie/yacs.git -t /some/directory
```
which will install it the directory of your choosing (`/some/directory`)

## Usage

The CLI interface is in the bin directory.  Simple usage looks like this:
```
$ bin/yacsay hello world
```

A few options exist:
* `bin/yacsay -h` will list all of the options
* `bin/yacsay -e eye_type` to change the eyes
* `bin/yacsay -w #chars` to change the length of the thought bubble (default is 30)

## Testing

Tetsing is slim right now, but `pytest` or `pytest -v` can be used to run all of 
the tests (where 'all' means one)
