#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.
    Returns a database connection and the cursor.
    """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("connection to the tournament database has failed")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    cursor.execute("TRUNCATE match CASCADE;")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    cursor.execute("TRUNCATE player CASCADE;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    query = 'SELECT count(*) FROM player;'
    cursor.execute(query)
    result = cursor.fetchone()
    db.close()
    return result[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.

    Args:
      name: the player's full name.
    """
    db, cursor = connect()
    query = 'INSERT INTO player (full_name) VALUES (%s);'
    param = (name,)
    cursor.execute(query, param)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    query = """SELECT id, full_name as name, wins, games_played as matches
               FROM player ORDER BY wins DESC, matches DESC;
            """
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()

    """create game record"""
    query = 'INSERT INTO match VALUES (%s, %s);'
    params = (winner, loser,)
    cursor.execute(query, params)

    """update winner game record"""
    query = """UPDATE player SET games_played = games_played + 1,
               wins = wins + 1 WHERE id = %s;
            """
    param = (winner,)
    cursor.execute(query, param)

    """update loser game count"""
    query = 'UPDATE player SET games_played = games_played + 1 WHERE id = %s;'
    param = (loser,)
    cursor.execute(query, param)

    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()

    """retain the id and name for each player"""
    standings_summary = [(x[0], x[1]) for x in standings]

    """create two player lists"""
    player_lst_1 = standings_summary[0::2]
    player_lst_2 = standings_summary[1::2]

    """combine and format the player lists"""
    pairinglst = zip(player_lst_1, player_lst_2)
    pairinglst = [x[0] + x[1] for x in pairinglst]

    return pairinglst
