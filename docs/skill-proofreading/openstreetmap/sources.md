# OpenStreetMap sources

All retrieved on 2026-10-28 JST. Primary files remain private in the production workspace; no external model or generation API used.

- about: https://www.openstreetmap.org/about — retrieved 17660 bytes
- copyright: https://www.openstreetmap.org/copyright — retrieved 21314 bytes
- elements: https://wiki.openstreetmap.org/wiki/Elements — retrieved 64715 bytes
- xml: https://wiki.openstreetmap.org/wiki/OSM_XML — retrieved 78420 bytes
- pbf: https://wiki.openstreetmap.org/wiki/PBF_Format — retrieved 109989 bytes
- api: https://wiki.openstreetmap.org/wiki/API_v0.6 — retrieved 303514 bytes
- download: https://planet.openstreetmap.org/ — retrieved 6840 bytes
- features: https://wiki.openstreetmap.org/wiki/Map_features — retrieved 1471210 bytes
- multipolygon: https://wiki.openstreetmap.org/wiki/Relation:multipolygon — retrieved 175944 bytes
- odbl: https://opendatacommons.org/licenses/odbl/1-0/ — retrieved 51543 bytes
- data: https://api.openstreetmap.org/api/0.6/map?bbox=135.755,35.000,135.765,35.010 — retrieved 8075418 bytes

- History of OpenStreetMap: https://wiki.openstreetmap.org/wiki/History_of_OpenStreetMap — project began in 2004; downloaded official wiki HTML.
- Attribution Guidelines: https://osmfoundation.org/wiki/Licence/Attribution_Guidelines — static images and database distinction; downloaded official OSMF HTML.

## Data and rendering

The official map API returned complete way nodes plus directly related relations for the requested bbox. Node extent exceeds that bbox; relation members are not all included. Four illustrations are clipped to 135.755–135.765 E,35.002–35.006 N, projected into EPSG:3857. Roads are highway-tagged ways; building polygons are closed building-tagged ways; POIs are amenity/shop nodes. This is a selected thematic view, not all OSM geometry. SVG is generated from actual node references and captured by Chromium via set_content. The 200m bar is corrected by cos(latitude) for local ground distance.

PBF structure is described from its primary specification only, not an acquired PBF. GeoJSON is a derived representation, not the native OSM model. Shape counts are the full acquired XML response, not clipped geographic feature counts.
