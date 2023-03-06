from fastapi import FastAPI
import sqlalchemy
from models import RouteRequest
from settings import settings

app = FastAPI()


def get_engine():
    url = sqlalchemy.engine.URL.create(
        drivername="postgresql+psycopg2",
        host=settings.pgr_db.host,
        port=settings.pgr_db.port,
        database=settings.pgr_db.db,
        username=settings.pgr_db.user,
        password=settings.pgr_db.password,
    )
    return sqlalchemy.create_engine(
        url,
        future=True,
        pool_pre_ping=True,
    )


engine = get_engine()

fix_null_lengths = """
UPDATE ways SET length_m=ST_Length(ST_Transform(ST_GeomFromEWKT('SRID=4326;'||st_astext(the_geom)),26986)) WHERE length_m IS NULL;
"""

q = """
SELECT ST_Distance(the_geom, 'SRID=4326;POINT(:lng :lat)'::geometry) as d, id
FROM ways_vertices_pgr
ORDER BY d limit 1;
"""

dq = """
SELECT a.*, b.maxspeed_forward ,ST_AsText(b.the_geom) FROM pgr_dijkstra(
    'SELECT gid as id, source, target, length_m as cost, length_m as reverse_cost FROM ways',
    :start_gid, :end_gid,
    FALSE
) AS a LEFT JOIN ways as b on (a.edge = b.gid) ORDER BY seq
"""

# Berlin gid: 229443
# Cologne gid: 929881


@app.post("/route/")
def calculate_route(route_request: RouteRequest):
    with engine.connect() as connection:
        sql_text = sqlalchemy.text(q)
        sql_text_distance = sqlalchemy.text(dq)
        start_nearest = connection.execute(
            sql_text, dict(lat=route_request.start.lat, lng=route_request.start.lng)
        ).first()
        end_nearest = connection.execute(
            sql_text, dict(lat=route_request.end.lat, lng=route_request.end.lng)
        ).first()
        start_gid = dict(start_nearest)["id"]  # 206
        end_gid = dict(end_nearest)["id"]  # 249
        route = connection.execute(
            sql_text_distance, dict(start_gid=start_gid, end_gid=end_gid)
        ).all()
        print(route)
