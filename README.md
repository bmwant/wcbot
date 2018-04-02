## wcbot
World Cup 2018 Win Outright Comparison.

### Features
* Easily configurable via YAML files
* Nice UI via web application
* Very extensible: add any fetcher/browser driver/parser, customize
parser engines, choose cache backend for any taste
* Convenient process of adding new resource

### Prerequisites
Make sure you have next items installed:
* pipenv
* Chrome + [chromedriver](https://chromedriver.storage.googleapis.com/index.html)

### Installation
```
$ git clone https://github.com/bmwant/wcbot.git
$ pipenv install
$ npm install
$ pipenv shell
$ python runserver.py
```
or using CLI scripts
```
$ python cli.py monitor
```
You may need to 
```
$ export PYTHONPATH=`pwd`
```
in case you encounter some import errors.

### Test
```
$ pytest -sv tests
```

### Extend
To add new resource follow these steps:

