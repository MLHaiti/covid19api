from app.main import db

from sqlalchemy import text
from flask import jsonify


def get_all_departements_geojson():
    myq = """

        select row_to_json(fc) as geojson
        from (
            select
                'FeatureCollection' as "type",
                array_to_json(array_agg(f)) as "features"
            from (
                select
                    'Feature' as "type",
                    ST_AsGeoJSON(ST_Transform(h.geom, 4326), 6) :: json as "geometry",
                    (
                        select json_strip_nulls(row_to_json(t))
                        from (
                            select
                                id_dep,
                                departemen,
                                shape_leng,
                            count(p.*) as count
                        ) t
                    ) as "properties"
                from public.ht_departements h
                left join public.people p  ON st_contains(h.geom,p.geom)
                group by h.id
            ) as f
        ) as fc

            """
    sql = text(myq)
    resultProxy = db.engine.execute(sql)
    result = resultProxy.fetchall()
    resultProxy.close()
    return [dict(row) for row in result][0]["geojson"]


def get_all_departements_geojson_point():
    myq = """

        select row_to_json(fc) as geojson
        from (
            select
                'FeatureCollection' as "type",
                array_to_json(array_agg(f)) as "features"
            from (
                select
                    'Feature' as "type",
                    ST_AsGeoJSON(ST_Transform(ST_centroid(h.geom), 4326), 6) :: json as "geometry",
                    (
                        select json_strip_nulls(row_to_json(t))
                        from (
                            select
                                id_dep,
                                departemen,
                                shape_leng,
                            count(p.*) as count
                        ) t
                    ) as "properties"
                from public.ht_departements h
                left join public.people p  ON st_contains(h.geom,p.geom)
                group by h.id
            ) as f
        ) as fc

            """
    sql = text(myq)
    resultProxy = db.engine.execute(sql)
    result = resultProxy.fetchall()
    resultProxy.close()
    return [dict(row) for row in result][0]["geojson"]