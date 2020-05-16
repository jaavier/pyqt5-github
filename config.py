import sqlite3

# CONSTANTS

DB_FILENAME = "config.db"

# INITIALIZING SQLite3

commiter = sqlite3.connect(DB_FILENAME)
client = commiter.cursor()

# CREATING CRUD

def create(configuration):

    repository = configuration["repository"]
    branch = configuration["branch"]
    authors = configuration["authors"]
    delay = configuration["delay"]

    if not read():

        try:

            client.execute("INSERT INTO configuration (repository, branch, authors, delay) VALUES ('{}', '{}', '{}', {})".format(repository, branch, authors, delay))
            commiter.commit()
            return True

        except Exception as error:

            print("Error creating configuration:", error)
            return False

    else:

        print("You need to UPDATE")
        return False

def update(configuration):

    repository = configuration["repository"]
    branch = configuration["branch"]
    authors = configuration["authors"]
    delay = configuration["delay"]

    try:

        client.execute("UPDATE configuration SET repository = {}, branch = {}, authors = {}, delay = {}".format(repository, branch, authors, delay))
        commiter.commit()
        return True

    except Exception as error:

        print("Error updating configuration:", error)
        return False

def read():

    query = client.execute("SELECT * FROM configuration").fetchone()
    return query


configuration = {
    "repository": "ursula",
    "branch": "feat/bridge-penta-octa-put-credentials",
    "authors": "jaavier",
    "delay": 60
}

_create = create(configuration)
_read = read()
print('Created?', _create)
print('Read?', _read)
commiter.close()