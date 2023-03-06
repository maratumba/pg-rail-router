# Open Rail Routing Using pgRoute

## Importing osm data

Convert data if necessary with osmosis:

```
osmosis --read-pbf planet-rail-210315.osm.pbf --write-xml planet-rail.osm
```

import data into db

```
osm2pgrouting --dbname pgr_routing --file planet-rail.osm --username pgr_routing --tags --attributes --clean -p 5436
```
