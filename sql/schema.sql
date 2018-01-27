CREATE TABLE blocks(
	identity INTEGER NOT NULL PRIMARY KEY,
	timestamps INTEGER NOT NULL,
	proof INTEGER NOT NULL,
	previous_block_hash VARCHAR(256) NOT NULL
);

CREATE TABLE transactions(
	id INTEGER NOT NULL PRIMARY KEY,
	blockid INTEGER NOT NULL,
	sender VARCHAR(64) NOT NULL,
	receiver VARCHAR(64) NOT NULL,
	value REAL NOT NULL
);

