## Tournament Based on Swiss System - part of [Full Stack Web Developer Nanodegree] 

A Python project using PostgreSQL database to manage tournament players and rounds.

The game tournament uses the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

# How to run the code

1. Install [Vagrant] and [VirtualBox]
2. Clone this repository
3. Launch the Vagrant VM 
4. login to the linux box and cd to the tournament folder
```sh
$ vagrant up
$ vagrant ssh
$ cd path/to/project/folder
```
5. Create the database
```sh
$ psql
=> \i tournament.sql
=> \q
```
6. Run the test script
```sh
$ python tournament_test.py

[Full Stack Web Developer Nanodegree]:https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004
[Vagrant]:http://vagrantup.com
[VirtualBox]:https://www.virtualbox.org