create_commands = [
    '''
        CREATE TABLE IF NOT EXISTS Client(
            Id INTEGER NOT NULL UNIQUE,
            LastName VARCHAR(60) NOT NULL,
            FirstName VARCHAR(60) NOT NULL,
            PersonUrl VARCHAR(60) NOT NULL,
            Age INTEGER NOT NULL,
            Sex INTEGER NOT NULL,
            City VARCHAR(60) NOT NULL,
            Relation INTEGER NOT NULL,
            PhotosUrl TEXT NOT NULL
        );
    ''',
    '''
        CREATE TABLE IF NOT EXISTS Person(
            Id INTEGER NOT NULL UNIQUE,
            LastName VARCHAR(60) NOT NULL,
            FirstName VARCHAR(60) NOT NULL,
            PersonUrl VARCHAR(60) NOT NULL,
            Age INTEGER NOT NULL,
            Sex INTEGER NOT NULL,
            City VARCHAR(60) NOT NULL,
            Relation INTEGER NOT NULL,
            PhotosUrl TEXT NOT NULL
        );
    ''',
    '''
        CREATE TABLE IF NOT EXISTS UsersConnect(
            ClientId INTEGER REFERENCES Client(Id) NOT NULL,
            PersonId INTEGER REFERENCES Person(Id) NOT NULL
        );
    '''
]
