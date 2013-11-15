# -*- coding: utf-8 -*-
from gluon.serializers import loads_json

def index():
    return {}

def get_geojson():
    rows= db(db.geostuff).select(db.geostuff.name, db.geostuff.geometry.st_asgeojson())

    features= [{"type": "Feature",
                "properties": {
                    "popupContent": r[db.geostuff.name]
                },
                "geometry": loads_json(r[db.geostuff.geometry.st_asgeojson()])} for r in rows] 

    return response.json({"type": "FeatureCollection", 'features': features})
