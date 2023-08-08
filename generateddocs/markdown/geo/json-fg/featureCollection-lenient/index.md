
# JSON-FG Feature Collection - Lenient (Schema)

`ogc.geo.json-fg.featureCollection-lenient` *v0.1*

A collection of lenient OGC Features and Geometries JSON (JSON-FG) Features, that do not require the "time" and "place" properties

[*Status*](http://www.opengis.net/def/status): Stable

## Description

OGC Features and Geometries JSON (JSON-FG) extends GeoJSON to support a limited set of additional capabilities that are
out-of-scope for GeoJSON, but that are essential or important for a variety of use cases involving feature data.
A **lenient** feature collection contains a set of **lenient** features from a dataset (features that do not
need to provide values for their `place` or `time` properties).
## Schema

```yaml
allOf:
- $schema: https://json-schema.org/draft/2019-09/schema
  title: a JSON-FG Feature Collection
  description: This JSON Schema is part of JSON-FG version 0.1.1
  type: object
  required:
  - type
  - features
  properties:
    type:
      type: string
      enum:
      - FeatureCollection
    featureType:
      $ref: https://beta.schemas.opengis.net/json-fg/featuretype.json
    geometryDimension:
      type: integer
      minimum: 0
      maximum: 3
    coordRefSys:
      $ref: https://beta.schemas.opengis.net/json-fg/coordrefsys.json
- $ref: ../../features/featureCollection/schema.yaml
x-jsonld-extra-terms:
  features:
    x-jsonld-container: '@set'
    x-jsonld-id: https://purl.org/geojson/vocab#features
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection-lenient/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection-lenient/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "links": {
      "@id": "rdfs:seeAlso",
      "@context": {
        "href": "@id",
        "title": "rdfs:label"
      }
    },
    "features": {
      "@id": "geojson:features",
      "@context": {
        "type": "@type",
        "id": "@id",
        "properties": "geojson:properties",
        "geometry": {
          "@id": "geojson:geometry",
          "@context": {
            "coordinates": {
              "@container": "@list",
              "@id": "geojson:coordinates"
            }
          }
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
        }
      }
    },
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection-lenient/context.jsonld)

## Sources

* [OGC Testbed-17: OGC Features and Geometries JSON Engineering Report](http://docs.ogc.org/per/21-017r1.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/geo/json-fg/featureCollection-lenient`

