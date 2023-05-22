# GeoJSON (Schema)

*Version 1.0*

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

[schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/schema.yaml)

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
          x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
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
          x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
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
          x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
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
          x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
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
          x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
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
          x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
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
                  x-jsonld-id: https://purl.org/geojson/vocab#coordinates
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-id: https://purl.org/geojson/vocab#bbox
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
                  x-jsonld-id: https://purl.org/geojson/vocab#coordinates
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-id: https://purl.org/geojson/vocab#bbox
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
                  x-jsonld-id: https://purl.org/geojson/vocab#coordinates
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-id: https://purl.org/geojson/vocab#bbox
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
                  x-jsonld-id: https://purl.org/geojson/vocab#coordinates
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-id: https://purl.org/geojson/vocab#bbox
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
                  x-jsonld-id: https://purl.org/geojson/vocab#coordinates
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-id: https://purl.org/geojson/vocab#bbox
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
                  x-jsonld-id: https://purl.org/geojson/vocab#coordinates
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-id: https://purl.org/geojson/vocab#bbox
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  bbox:
    type: array
    minItems: 4
    items:
      type: number
    x-jsonld-id: https://purl.org/geojson/vocab#bbox
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#

```
## Sources

* [IETF RFC 7946 - The GeoJSON Format](https://datatracker.ietf.org/doc/html/rfc7946)
