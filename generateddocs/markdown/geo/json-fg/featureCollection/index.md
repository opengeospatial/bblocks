
# JSON-FG Feature Collection (Schema)

`ogc.geo.json-fg.featureCollection` *v0.1*

A collection of OGC Features and Geometries JSON (JSON-FG) Features, extending GeoJSON to support a limited set of additional capabilities that are out-of-scope for GeoJSON, but that are important for a variety of use cases involving feature data.

[*Status*](http://www.opengis.net/def/status): Stable

## Description

OGC Features and Geometries JSON (JSON-FG) extends GeoJSON to support a limited set of additional capabilities that are
out-of-scope for GeoJSON, but that are essential or important for a variety of use cases involving feature data.
A **feature collection** contains a set of features from a dataset.

Information that can be represented as GeoJSON is encoded as GeoJSON. Additional information is mainly encoded in
additional top-level members of GeoJSON objects. The members use keys that do not conflict with GeoJSON including the
obsolete version that pre-dates the IETF standard. GeoJSON clients will be able to parse and understand all aspects that
are specified by GeoJSON, JSON-FG clients will also parse and understand the additional capabilities.

This Standard specifies the following minimal extensions to the GeoJSON Standard:

* The ability to use Coordinate Reference Systems (CRSs) other than WGS 84;
* The ability to use non-Euclidean metrics, in particular ellipsoidal metrics;
* Support for solids and prisms as geometry types;
* The ability to encode temporal characteristics of a feature; and
* The ability to declare the type and the schema of a feature.

Information that can be represented as GeoJSON is encoded as GeoJSON. Additional information is mainly encoded in
additional members of the GeoJSON objects. The additional members use keys that do not conflict with GeoJSON. This is so
existing and future GeoJSON clients will continue to parse and understand GeoJSON content. JSON-FG enabled clients will
also be able to parse and understand the additional members.

JSON Schema is used to formally specify the JSON-FG syntax.
## Schema

```yaml
$schema: https://json-schema.org/draft/2019-09/schema
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
    x-jsonld-id: '@type'
  featureType:
    $ref: https://beta.schemas.opengis.net/json-fg/featuretype.json
  geometryDimension:
    type: integer
    minimum: 0
    maximum: 3
  coordRefSys:
    $ref: https://beta.schemas.opengis.net/json-fg/coordrefsys.json
  links:
    type: array
    items:
      allOf:
      - $ref: https://beta.schemas.opengis.net/json-fg/link.json
      - $ref: ../../../ogc-utils/json-link/schema.yaml
    x-jsonld-id: rdfs:seeAlso
  features:
    type: array
    items:
      $ref: ../feature/schema.yaml
    x-jsonld-container: '@set'
    x-jsonld-id: https://purl.org/geojson/vocab#features
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "type": "@type",
    "links": {
      "@id": "rdfs:seeAlso",
      "@context": {
        "href": "oa:hasTarget",
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      }
    },
    "features": {
      "@container": "@set",
      "@id": "geojson:features",
      "@context": {
        "id": "@id",
        "links": {
          "@id": "rdfs:seeAlso",
          "@context": {
            "href": "oa:hasTarget",
            "rel": {
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id",
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              }
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent"
          }
        },
        "geometry": "geojson:geometry",
        "properties": "@nest",
        "bbox": {
          "@container": "@list",
          "@id": "geojson:bbox"
        },
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        },
        "features": {
          "@container": "@set",
          "@id": "geojson:features"
        }
      }
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
    "bbox": {
      "x-jsonld-container": "@list",
      "x-jsonld-id": "https://purl.org/geojson/vocab#bbox"
    },
    "coordinates": {
      "x-jsonld-container": "@list",
      "x-jsonld-id": "https://purl.org/geojson/vocab#coordinates"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/context.jsonld)

## Sources

* [OGC Testbed-17: OGC Features and Geometries JSON Engineering Report](http://docs.ogc.org/per/21-017r1.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/geo/json-fg/featureCollection`

