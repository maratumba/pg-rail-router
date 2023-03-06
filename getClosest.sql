-- SELECT 
--     gid, ST_AsText(ST_ClosestPoint(ST_MakePoint(x1,y1), ST_GeomFromText('POINT(-71.0931906 42.3873776)')))
-- FROM ways LIMIT 10;

-- Plug the geometry into a nearest-neighbor query
-- SELECT streets.gid, streets.name,
--   ways.the_geom,
--   ways.the_geom <-> 'POINT(-71.0931906 42.3873776)'::geometry AS dist
-- FROM
--   ways
-- ORDER BY
--   dist
-- LIMIT 3;

SELECT ST_Distance(ways.the_geom, 'SRID=4326;POINT(-71.0931906 42.3873776)'::geometry) as d, gid
FROM ways
ORDER BY d limit 1;