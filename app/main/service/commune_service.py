from app.main import db

from sqlalchemy import text
from dumper import dump
from flask import jsonify


def get_all_communes_geojson():
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
                                id_com,
                                commune,
                                id_dep,
                                departemen,
                                shape_leng,
                            count(p.*) as count
                        ) t
                    ) as "properties"
                from public.ht_communes h
                left join public.people p  ON st_contains(h.geom,p.geom)
                group by h.id
            ) as f
        ) as fc

            """
    sql = text(myq)
    resultProxy = db.engine.execute(sql)
    result = resultProxy.fetchall()
    dump(result)
    print(result)
    resultProxy.close()
    return [dict(row) for row in result]