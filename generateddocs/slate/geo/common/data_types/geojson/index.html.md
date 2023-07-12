---
title: GeoJSON (Schema)

toc_footers:
  - Version 1.0
  - <a href='#'>GeoJSON</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: GeoJSON (Schema)
---


# GeoJSON `ogc.geo.common.data_types.geojson`

A GeoJSON object

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

<aside class="success">
This building block is <strong>valid</strong>
</aside>

# Description

A feature is an abstraction of real world phenomena [ISO 19101-1:2014].

The GeoJSON representation is the currently recommended representation that all APIs should support, where GeoJSON can
be used for the data.

Each GeoJSON feature includes the following JSON members:

* `type`: fixed value "Feature".
* `geometry`: the primary geometry of the feature describing its location as a GeoJSON geometry object. `null`, if the
  feature has no spatial geometry.
* `properties`: an object with a member for each feature property.

# JSON Schema

```yaml--schema
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
          x-jsonld-container: '@list'
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
          x-jsonld-container: '@list'
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
          x-jsonld-container: '@list'
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
          x-jsonld-container: '@list'
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
          x-jsonld-container: '@list'
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
          x-jsonld-container: '@list'
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
          x-jsonld-container: '@list'
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
          x-jsonld-container: '@list'
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
          x-jsonld-container: '@list'
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
          x-jsonld-container: '@list'
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
          x-jsonld-container: '@list'
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
          x-jsonld-container: '@list'
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
                  x-jsonld-container: '@list'
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-id: https://purl.org/geojson/vocab#bbox
                  x-jsonld-container: '@list'
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
                  x-jsonld-container: '@list'
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-id: https://purl.org/geojson/vocab#bbox
                  x-jsonld-container: '@list'
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
                  x-jsonld-container: '@list'
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-id: https://purl.org/geojson/vocab#bbox
                  x-jsonld-container: '@list'
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
                  x-jsonld-container: '@list'
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-id: https://purl.org/geojson/vocab#bbox
                  x-jsonld-container: '@list'
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
                  x-jsonld-container: '@list'
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-id: https://purl.org/geojson/vocab#bbox
                  x-jsonld-container: '@list'
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
                  x-jsonld-container: '@list'
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-id: https://purl.org/geojson/vocab#bbox
                  x-jsonld-container: '@list'
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
          x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  bbox:
    type: array
    minItems: 4
    items:
      type: number
    x-jsonld-id: https://purl.org/geojson/vocab#bbox
    x-jsonld-container: '@list'
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  GeometryCollection: https://purl.org/geojson/vocab#GeometryCollection
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  MultiPoint: https://purl.org/geojson/vocab#MultiPoint
  features: https://purl.org/geojson/vocab#features
  Polygon: https://purl.org/geojson/vocab#Polygon
  LineString: https://purl.org/geojson/vocab#LineString
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
  Point: https://purl.org/geojson/vocab#Point
  MultiLineString: https://purl.org/geojson/vocab#MultiLineString

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "type": "@type",
    "id": "@id",
    "properties": "geojson:properties",
    "geometry": {
      "@id": "https://purl.org/geojson/vocab#geometry",
      "@context": {
        "type": "@type",
        "coordinates": {
          "@id": "https://purl.org/geojson/vocab#coordinates",
          "@container": "@list"
        }
      }
    },
    "bbox": {
      "@id": "https://purl.org/geojson/vocab#bbox",
      "@container": "@list"
    },
    "Feature": "geojson:Feature",
    "GeometryCollection": "geojson:GeometryCollection",
    "FeatureCollection": "geojson:FeatureCollection",
    "MultiPoint": "geojson:MultiPoint",
    "features": "geojson:features",
    "Polygon": "geojson:Polygon",
    "LineString": "geojson:LineString",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "MultiLineString": "geojson:MultiLineString"
  }
}
```

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/context.jsonld</a>

# References

* [IETF RFC 7946 - The GeoJSON Format](https://datatracker.ietf.org/doc/html/rfc7946)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path: `registereditems/geo/common/data_types/geojson`

