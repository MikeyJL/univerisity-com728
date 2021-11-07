import sqlite3

def setup():
    db = sqlite3.connect('./database.db')
    cur = db.cursor()

    sql = """
    BEGIN TRANSACTION;
    CREATE TABLE IF NOT EXISTS "countries" (
        "id" INTEGER NOT NULL UNIQUE,
        "name" TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    CREATE TABLE IF NOT EXISTS "locations" (
        "id" INTEGER NOT NULL UNIQUE,
        "city" TEXT NOT NULL,
        "country_id" INTEGER NOT NULL,
        PRIMARY KEY ("id" AUTOINCREMENT),
        FOREIGN KEY ("country_id") REFERENCES "countries" ("id")
    );
    CREATE TABLE IF NOT EXISTS "organisations" (
        "id" INTEGER NOT NULL UNIQUE,
        "name" TEXT NOT NULL,
        "location_id" INTEGER NOT NULL,
        PRIMARY KEY ("id" AUTOINCREMENT),
        FOREIGN KEY ("location_id") REFERENCES "location" ("id")
    );
    CREATE TABLE IF NOT EXISTS "events" (
        "id" INTEGER NOT NULL UNIQUE,
        "name" TEXT NOT NULL,
        "type" TEXT NOT NULL,
        "host_id" INTEGER NOT NULL,
        PRIMARY KEY ("id" AUTOINCREMENT),
        FOREIGN KEY ("host_id") REFERENCES "organisations" ("id")
    );
    CREATE TABLE IF NOT EXISTS "presenters" (
        "id" INTEGER NOT NULL UNIQUE,
        "name" TEXT NOT NULL,
        "organisation_id" INTEGER NOT NULL,
        PRIMARY KEY ("id" AUTOINCREMENT),
        FOREIGN KEY ("organisation_id") REFERENCES "organisations" ("id")
    );
    CREATE TABLE IF NOT EXISTS "event_presenters" (
        "event_id" INTEGER NOT NULL UNIQUE,
        "presenter_id" INTEGER NOT NULL UNIQUE,
        CONSTRAINT "event_presenter" PRIMARY KEY ("event_id", "presenter_id"),
        FOREIGN KEY ("event_id") REFERENCES "events" ("id")
        FOREIGN KEY ("presenter_id") REFERENCES "presenters" ("id")
    );
    COMMIT;
    """

    cur.executescript(sql)
    db.commit()