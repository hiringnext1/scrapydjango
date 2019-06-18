# Indeed Scrapy
An Indeed scrapper that extracts all the jobs related to the field specified by the user

## Getting Started
These instructions will tell you how to download, run and use this project:

### Installing

```
https://github.com/david1707/indeed_scrapy
```

If you don't have Scrapy, create an enviroment (better pipenv than virtualenv) and install the requirements:

```
pip install -r requirements.txt
```

### Usage

Navigate to the main folder, then run it with:
```
scrapy crawl indeed
```

If you want to save the yield result, do it like this:

```
scrapy crawl indeed -o jobs.json
```

By default will search all the jobs. If you want to specify a field, pass it as a 'job' argument:

```
scrapy crawl indeed -a job='Scrapy python' -o file.json
```

You can use .json, .xml, .csv....


### MongoDB support

If you have a local MognoDB Database, it will store every result at the 'indeed' database, 'jobs' collection. For more info, check pipelines.py and settings.py, rows 67-74

## Built With

* [Python](https://www.python.org/) - Python is an interpreted high-level programming language for general-purpose programming.
* [Scrapy](https://scrapy.org/) - An open source and collaborative framework for extracting the data you need from websites.

## Author

* **David Membrives** - *Initial work* - [david1707](https://github.com/david1707)


## License

This project is licensed under the ISC License