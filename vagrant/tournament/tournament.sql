-- Create database "tournament" and connect to that database before creating tables
\c vagrant
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

-- player table
CREATE TABLE player ( id SERIAL PRIMARY KEY,
					  full_name VARCHAR(40) NOT NULL,
					  games_played INTEGER DEFAULT 0,
					  wins INTEGER DEFAULT 0);

-- game table
CREATE TABLE match ( winner_id INTEGER REFERENCES player(id),
				   	 loser_id INTEGER REFERENCES player(id),
				   	 CONSTRAINT game_key PRIMARY KEY (winner_id, loser_id));
