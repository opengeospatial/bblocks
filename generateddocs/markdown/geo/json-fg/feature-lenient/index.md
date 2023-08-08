
# JSON-FG Feature - Lenient (Schema)

`ogc.geo.json-fg.feature-lenient` *v0.1*

A OGC Features and Geometries JSON (JSON-FG) Feature that does not require the "time" and "place" properties.

[*Status*](http://www.opengis.net/def/status): Stable

## Description

OGC Features and Geometries JSON (JSON-FG) extends GeoJSON to support a limited set of additional capabilities that are
out-of-scope for GeoJSON, but that are essential or important for a variety of use cases involving feature data.

This Building Block extends the standard JSON-FG one by removing the requirement to provide values for the 
"time" and "place" properties.

## Schema

```yaml
allOf:
- $ref: ../../features/feature/schema.yaml
- type: object
  required:
  - type
  - geometry
  - properties
  properties:
    type:
      type: string
      enum:
      - Feature
      x-jsonld-id: '@type'
    id:
      oneOf:
      - type: number
      - type: string
      x-jsonld-id: '@id'
    featureType:
      $ref: https://beta.schemas.opengis.net/json-fg/featuretype.json
    links:
      type: array
      items:
        $ref: https://beta.schemas.opengis.net/json-fg/link.json
    time:
      $ref: https://beta.schemas.opengis.net/json-fg/time.json
    coordRefSys:
      $ref: https://beta.schemas.opengis.net/json-fg/coordrefsys.json
    place:
      $ref: https://beta.schemas.opengis.net/json-fg/place.json
    geometry:
      $ref: https://beta.schemas.opengis.net/json-fg/geometry.json
      x-jsonld-id: https://purl.org/geojson/vocab#geometry
    properties:
      oneOf:
      - type: 'null'
      - type: object
      x-jsonld-id: https://purl.org/geojson/vocab#properties
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  GeometryCollection: https://purl.org/geojson/vocab#GeometryCollection
  LineString: https://purl.org/geojson/vocab#LineString
  MultiLineString: https://purl.org/geojson/vocab#MultiLineString
  MultiPoint: https://purl.org/geojson/vocab#MultiPoint
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
  Point: https://purl.org/geojson/vocab#Point
  Polygon: https://purl.org/geojson/vocab#Polygon
  bbox:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#bbox
  coordinates:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#coordinates
  features:
    x-jsonld-container: '@set'
    x-jsonld-id: https://purl.org/geojson/vocab#features
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature-lenient/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature-lenient/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "type": "@type",
    "id": "@id",
    "properties": "geojson:properties",
    "geometry": {
      "@id": "geojson:geometry",
      "@context": {}
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "features": {
      "@container": "@set",
      "@id": "geojson:features"
    },
    "links": {
      "@id": "rdfs:seeAlso",
      "@context": {
        "href": "@id",
        "title": "rdfs:label"
      }
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature-lenient/context.jsonld)

## Sources

* [OGC Testbed-17: OGC Features and Geometries JSON Engineering Report](http://docs.ogc.org/per/21-017r1.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/geo/json-fg/feature-lenient`

