import sqlite3

conn = sqlite3.connect("coachdata.sqlite")

cursor = conn.cursor()

cursor.execute("""create table runner(id integer primary key autoincrement unique not null, 
        name text not null, 
        dob date not null
        )""")

cursor.execute("""create table times(runner_id integer not null,
        value text not null,
        foreign key(runner_id) references runners
        )""")

conn.commit()

conn.close()

