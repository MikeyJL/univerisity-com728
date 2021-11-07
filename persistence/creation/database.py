import sqlite3
from init_data import data

class Database:
    def __init__(self, generate=False):
        self.db = sqlite3.connect('./database.db')
        self.cur = self.db.cursor()
        self.setup()

        if generate:
            # Countries
            sql = "INSERT INTO countries (name) VALUES (?)"
            for country in data["countries"]:
                self.cur.execute(sql, [country])

            # Locations
            sql = "INSERT INTO locations (city, country_id) VALUES (?, ?)"
            for location in data["locations"]:
                self.cur.execute(sql, location)
            self.db.commit()
            
            # organisations
            sql = "INSERT INTO organisations (name, location_id) VALUES (?, ?)"
            for organisation in data["organisations"]:
                self.cur.execute(sql, organisation)
            self.db.commit()
            
            # events
            sql = "INSERT INTO events (name, type, host_id) VALUES (?, ?, ?)"
            for event in data["events"]:
                self.cur.execute(sql, event)
            self.db.commit()
            
            # presenters
            sql = "INSERT INTO presenters (name, organisation_id) VALUES (?, ?)"
            for presenter in data["presenters"]:
                self.cur.execute(sql, presenter)
            self.db.commit()
            
            # event_presenters 
            sql = "INSERT INTO event_presenters (event_id, presenter_id) VALUES (?, ?)"
            for event_presenter in data["event_presenters"]:
                self.cur.execute(sql, event_presenter)
            self.db.commit()

    def setup(self):
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
            "event_id" INTEGER NOT NULL,
            "presenter_id" INTEGER NOT NULL,
            CONSTRAINT "event_presenter" PRIMARY KEY ("event_id", "presenter_id"),
            FOREIGN KEY ("event_id") REFERENCES "events" ("id")
            FOREIGN KEY ("presenter_id") REFERENCES "presenters" ("id")
        );
        COMMIT;
        """

        self.cur.executescript(sql)
        self.db.commit()

    def get_all_presenters_and_org(self):
        sql = "SELECT presenters.name, organisations.name FROM presenters " \
              "LEFT OUTER JOIN organisations " \
              "ON presenters.organisation_id = organisations.id;"
        records = self.cur.execute(sql).fetchall()
        print("\nList of all the presenters and the organisation(s) they belong to:")
        for record in records:
            print(f"\n{record[0]}")
            print(f"{record[1]}")

    def get_all_events_and_location(self):
        sql = "SELECT events.name, locations.city, countries.name  FROM events " \
              "LEFT OUTER JOIN organisations " \
              "ON events.host_id = organisations.id " \
              "LEFT OUTER JOIN locations " \
              "ON organisations.location_id = locations.id " \
              "LEFT OUTER JOIN countries " \
              "ON locations.country_id = countries.id;"
        records = self.cur.execute(sql).fetchall()
        print("\nList of all the events and its location:")
        for record in records:
            print(f"\n{record[0]}")
            print(f"{record[1]}")
            print(f"{record[2]}")

    def get_all_presenters_for_event(self):
        eid = input("\nEvent ID: ")
        sql = "SELECT events.name, presenters.name, organisations.name FROM event_presenters " \
              "LEFT OUTER JOIN events " \
              "ON event_presenters.event_id = events.id " \
              "LEFT OUTER JOIN presenters " \
              "ON event_presenters.presenter_id = presenters.id " \
              "LEFT OUTER JOIN organisations " \
              "ON presenters.organisation_id = organisations.id " \
              "WHERE event_id = ?;"
        records = self.cur.execute(sql, [eid]).fetchall()
        if not records:
            return print("ERROR: Event not found")
        print(f"\nName of the event: {records[0][0]}\n")
        for record in records:
            print(f"{record[1]} ({record[2]})")

    def close_db(self):
        self.db.close()