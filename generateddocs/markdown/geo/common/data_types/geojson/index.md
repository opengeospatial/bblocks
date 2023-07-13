
# GeoJSON (Schema)

`ogc.geo.common.data_types.geojson` *v1.0*

A GeoJSON object

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

## Description

A feature is an abstraction of real world phenomena [ISO 19101-1:2014].

The GeoJSON representation is the currently recommended representation that all APIs should support, where GeoJSON can
be used for the data.

Each GeoJSON feature includes the following JSON members:

* `type`: fixed value "Feature".
* `geometry`: the primary geometry of the feature describing its location as a GeoJSON geometry object. `null`, if the
  feature has no spatial geometry.
* `properties`: an object with a member for each feature property.
## Schema

```yaml
$schema: http://json-schema.org/draft-07/schema#
$id: https://geojson.org/schema/Feature.json
title: GeoJSON Feature
type: object
required:
- type
- properties
- geometry
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
  properties:
    oneOf:
    - type: 'null'
    - type: object
    x-jsonld-id: https://purl.org/geojson/vocab#properties
  geometry:
    oneOf:
    - type: 'null'
    - title: GeoJSON Point
      type: object
      required:
      - type
      - coordinates
      properties:
        type:
          type: string
          enum:
          - Point
          x-jsonld-id: '@type'
        coordinates:
          type: array
          minItems: 2
          items:
            type: number
        bbox:
          type: array
          minItems: 4
          items:
            type: number
    - title: GeoJSON LineString
      type: object
      required:
      - type
      - coordinates
      properties:
        type:
          type: string
          enum:
          - LineString
          x-jsonld-id: '@type'
        coordinates:
          type: array
          minItems: 2
          items:
            type: array
            minItems: 2
            items:
              type: number
        bbox:
          type: array
          minItems: 4
          items:
            type: number
    - title: GeoJSON Polygon
      type: object
      required:
      - type
      - coordinates
      properties:
        type:
          type: string
          enum:
          - Polygon
          x-jsonld-id: '@type'
        coordinates:
          type: array
          items:
            type: array
            minItems: 4
            items:
              type: array
              minItems: 2
              items:
                type: number
        bbox:
          type: array
          minItems: 4
          items:
            type: number
    - title: GeoJSON MultiPoint
      type: object
      required:
      - type
      - coordinates
      properties:
        type:
          type: string
          enum:
          - MultiPoint
          x-jsonld-id: '@type'
        coordinates:
          type: array
          items:
            type: array
            minItems: 2
            items:
              type: number
        bbox:
          type: array
          minItems: 4
          items:
            type: number
    - title: GeoJSON MultiLineString
      type: object
      required:
      - type
      - coordinates
      properties:
        type:
          type: string
          enum:
          - MultiLineString
          x-jsonld-id: '@type'
        coordinates:
          type: array
          items:
            type: array
            minItems: 2
            items:
              type: array
              minItems: 2
              items:
                type: number
        bbox:
          type: array
          minItems: 4
          items:
            type: number
    - title: GeoJSON MultiPolygon
      type: object
      required:
      - type
      - coordinates
      properties:
        type:
          type: string
          enum:
          - MultiPolygon
          x-jsonld-id: '@type'
        coordinates:
          type: array
          items:
            type: array
            items:
              type: array
              minItems: 4
              items:
                type: array
                minItems: 2
                items:
                  type: number
        bbox:
          type: array
          minItems: 4
          items:
            type: number
    - title: GeoJSON GeometryCollection
      type: object
      required:
      - type
      - geometries
      properties:
        type:
          type: string
          enum:
          - GeometryCollection
          x-jsonld-id: '@type'
        geometries:
          type: array
          items:
            oneOf:
            - title: GeoJSON Point
              type: object
              required:
              - type
              - coordinates
              properties:
                type:
                  type: string
                  enum:
                  - Point
                  x-jsonld-id: '@type'
                coordinates:
                  type: array
                  minItems: 2
                  items:
                    type: number
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
            - title: GeoJSON LineString
              type: object
              required:
              - type
              - coordinates
              properties:
                type:
                  type: string
                  enum:
                  - LineString
                  x-jsonld-id: '@type'
                coordinates:
                  type: array
                  minItems: 2
                  items:
                    type: array
                    minItems: 2
                    items:
                      type: number
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
            - title: GeoJSON Polygon
              type: object
              required:
              - type
              - coordinates
              properties:
                type:
                  type: string
                  enum:
                  - Polygon
                  x-jsonld-id: '@type'
                coordinates:
                  type: array
                  items:
                    type: array
                    minItems: 4
                    items:
                      type: array
                      minItems: 2
                      items:
                        type: number
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
            - title: GeoJSON MultiPoint
              type: object
              required:
              - type
              - coordinates
              properties:
                type:
                  type: string
                  enum:
                  - MultiPoint
                  x-jsonld-id: '@type'
                coordinates:
                  type: array
                  items:
                    type: array
                    minItems: 2
                    items:
                      type: number
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
            - title: GeoJSON MultiLineString
              type: object
              required:
              - type
              - coordinates
              properties:
                type:
                  type: string
                  enum:
                  - MultiLineString
                  x-jsonld-id: '@type'
                coordinates:
                  type: array
                  items:
                    type: array
                    minItems: 2
                    items:
                      type: array
                      minItems: 2
                      items:
                        type: number
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
            - title: GeoJSON MultiPolygon
              type: object
              required:
              - type
              - coordinates
              properties:
                type:
                  type: string
                  enum:
                  - MultiPolygon
                  x-jsonld-id: '@type'
                coordinates:
                  type: array
                  items:
                    type: array
                    items:
                      type: array
                      minItems: 4
                      items:
                        type: array
                        minItems: 2
                        items:
                          type: number
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
        bbox:
          type: array
          minItems: 4
          items:
            type: number
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  bbox:
    type: array
    minItems: 4
    items:
      type: number
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

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "type": "@type",
    "id": "@id",
    "properties": "geojson:properties",
    "geometry": {
      "@id": "https://purl.org/geojson/vocab#geometry",
      "@context": {}
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
      "@container": "@list",
      "@id": "https://purl.org/geojson/vocab#bbox"
    },
    "coordinates": {
      "@container": "@list",
      "@id": "https://purl.org/geojson/vocab#coordinates"
    },
    "features": {
      "@container": "@set",
      "@id": "https://purl.org/geojson/vocab#features"
    }
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/context.jsonld)

## Sources

* [IETF RFC 7946 - The GeoJSON Format](https://datatracker.ietf.org/doc/html/rfc7946)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/geo/common/data_types/geojson`

