### WorldPop Collector
[![Build Status](https://travis-ci.org/luiscape/hdxscraper-worldpop.svg)](https://travis-ci.org/luiscape/hdxscraper-worldpop)

Collector for data publicly available from the [WorldPop](http://www.worldpop.org.uk/) project. This collector fetches data from WorldPop's webiste and register equivalents in the [Humanitarian Data Exchange](http://data.hdx.rwlabs.org).

### Usage
Use the `Makefile` instructions to run this collector successfully:

```shell
$ make setup && make test
$ make collect && make register
```

or

```shell
$ make setup && make test
$ make run
```

The environment variable `WP_KEY` must be defined before running the program. It will fail to collect data otherwise.
