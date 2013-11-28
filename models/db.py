# -*- coding: utf-8 -*-
db = DAL('postgres://web2py:web2py@localhost:5432/testw2p', lazy_tables=False,)

db.define_table('geostuff',
    Field('name', 'string'),
    Field('geometry', 'geometry()'),
)


n_rows = db(db.geostuff).count()
if not n_rows:
    db.geostuff.insert(name="My first geo point (London!)", geometry="POINT(-0.091109 51.512622)")
    db.geostuff.insert(name="My first linestring", geometry="LINESTRING (8.791595 45.660281, 11.343062 44.494932, 10.394590 43.722998)")
