# Greenspace


## About

Basically an excuse to experiment with cool stuff. A playable game might eventually emerge from this.

Right now the game is turn based, meaning base production(1) and fleet movement happens at predetermined intervals. A player can issue orders during these intervals.

*(1) not actually happening*

## Architecture

### Backend

* MongoDB
* Python 2.7
    * MongoEngine ODM

MongoDB keeps the game state. A python script generates a playing area consisting of several stars randomly placed across a grid. A python service handles turns.

### Frontend

* server
    * MongoDB
    * NodeJS
        * Mongoose
        * Express
* client
    * Underscore.js

A nodejs app reads game state from the database and conveys it to the player on request. The nodejs app also writes to the database when the player issues orders, though this is undesireable and should be delegated to the backend.


## Installation

Copy the files somewhere in your server. Then:

1. `python backend/genesis.py` Generate the playing area
2. `python backend/ticker.py` Get the game running
3. `node frontend/app.js` Start the front-end
4. Point your browser to < server ip >:80 and enjoy 
