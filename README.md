## Tournament Based on Swiss System - part of [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

A Python project using PostgreSQL database to manage tournament players and rounds.

The game tournament uses the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

# How to run the code

* Install [Vagrant](http://vagrantup.com) and [VirtualBox](https://www.virtualbox.org)
* Clone this repository
* Launch the Vagrant VM 
* login to the linux box and cd to the tournament folder
```sh
$ vagrant up
$ vagrant ssh
$ cd path/to/project/folder
```

* Create the database
```sh
$ psql
=> \i tournament.sql
=> \q
```

* Run the test script
```sh
$ python tournament_test.py
