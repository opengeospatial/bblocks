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

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/stable" target="_blank" data-rainbow-uri>Stable</a>
</p>

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
          x-jsonld-container: '@list'
          x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-container: '@list'
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
          x-jsonld-container: '@list'
          x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-container: '@list'
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
          x-jsonld-container: '@list'
          x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-container: '@list'
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
          x-jsonld-container: '@list'
          x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-container: '@list'
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
          x-jsonld-container: '@list'
          x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-container: '@list'
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
          x-jsonld-container: '@list'
          x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-container: '@list'
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
                  x-jsonld-container: '@list'
                  x-jsonld-id: https://purl.org/geojson/vocab#coordinates
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-container: '@list'
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
                  x-jsonld-container: '@list'
                  x-jsonld-id: https://purl.org/geojson/vocab#coordinates
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-container: '@list'
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
                  x-jsonld-container: '@list'
                  x-jsonld-id: https://purl.org/geojson/vocab#coordinates
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-container: '@list'
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
                  x-jsonld-container: '@list'
                  x-jsonld-id: https://purl.org/geojson/vocab#coordinates
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-container: '@list'
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
                  x-jsonld-container: '@list'
                  x-jsonld-id: https://purl.org/geojson/vocab#coordinates
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-container: '@list'
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
                  x-jsonld-container: '@list'
                  x-jsonld-id: https://purl.org/geojson/vocab#coordinates
                bbox:
                  type: array
                  minItems: 4
                  items:
                    type: number
                  x-jsonld-container: '@list'
                  x-jsonld-id: https://purl.org/geojson/vocab#bbox
        bbox:
          type: array
          minItems: 4
          items:
            type: number
          x-jsonld-container: '@list'
          x-jsonld-id: https://purl.org/geojson/vocab#bbox
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  bbox:
    type: array
    minItems: 4
    items:
      type: number
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#bbox
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
  features:
    x-jsonld-container: '@set'
    x-jsonld-id: https://purl.org/geojson/vocab#features
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;data=%24schema%3A+http%3A%2F%2Fjson-schema.org%2Fdraft-07%2Fschema%23%0A%24id%3A+https%3A%2F%2Fgeojson.org%2Fschema%2FFeature.json%0Atitle%3A+GeoJSON+Feature%0Atype%3A+object%0Arequired%3A%0A-+type%0A-+properties%0A-+geometry%0Aproperties%3A%0A++type%3A%0A++++type%3A+string%0A++++enum%3A%0A++++-+Feature%0A++++x-jsonld-id%3A+%27%40type%27%0A++id%3A%0A++++oneOf%3A%0A++++-+type%3A+number%0A++++-+type%3A+string%0A++++x-jsonld-id%3A+%27%40id%27%0A++properties%3A%0A++++oneOf%3A%0A++++-+type%3A+%27null%27%0A++++-+type%3A+object%0A++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23properties%0A++geometry%3A%0A++++oneOf%3A%0A++++-+type%3A+%27null%27%0A++++-+title%3A+GeoJSON+Point%0A++++++type%3A+object%0A++++++required%3A%0A++++++-+type%0A++++++-+coordinates%0A++++++properties%3A%0A++++++++type%3A%0A++++++++++type%3A+string%0A++++++++++enum%3A%0A++++++++++-+Point%0A++++++++++x-jsonld-id%3A+%27%40type%27%0A++++++++coordinates%3A%0A++++++++++type%3A+array%0A++++++++++minItems%3A+2%0A++++++++++items%3A%0A++++++++++++type%3A+number%0A++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23coordinates%0A++++++++bbox%3A%0A++++++++++type%3A+array%0A++++++++++minItems%3A+4%0A++++++++++items%3A%0A++++++++++++type%3A+number%0A++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0A++++-+title%3A+GeoJSON+LineString%0A++++++type%3A+object%0A++++++required%3A%0A++++++-+type%0A++++++-+coordinates%0A++++++properties%3A%0A++++++++type%3A%0A++++++++++type%3A+string%0A++++++++++enum%3A%0A++++++++++-+LineString%0A++++++++++x-jsonld-id%3A+%27%40type%27%0A++++++++coordinates%3A%0A++++++++++type%3A+array%0A++++++++++minItems%3A+2%0A++++++++++items%3A%0A++++++++++++type%3A+array%0A++++++++++++minItems%3A+2%0A++++++++++++items%3A%0A++++++++++++++type%3A+number%0A++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23coordinates%0A++++++++bbox%3A%0A++++++++++type%3A+array%0A++++++++++minItems%3A+4%0A++++++++++items%3A%0A++++++++++++type%3A+number%0A++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0A++++-+title%3A+GeoJSON+Polygon%0A++++++type%3A+object%0A++++++required%3A%0A++++++-+type%0A++++++-+coordinates%0A++++++properties%3A%0A++++++++type%3A%0A++++++++++type%3A+string%0A++++++++++enum%3A%0A++++++++++-+Polygon%0A++++++++++x-jsonld-id%3A+%27%40type%27%0A++++++++coordinates%3A%0A++++++++++type%3A+array%0A++++++++++items%3A%0A++++++++++++type%3A+array%0A++++++++++++minItems%3A+4%0A++++++++++++items%3A%0A++++++++++++++type%3A+array%0A++++++++++++++minItems%3A+2%0A++++++++++++++items%3A%0A++++++++++++++++type%3A+number%0A++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23coordinates%0A++++++++bbox%3A%0A++++++++++type%3A+array%0A++++++++++minItems%3A+4%0A++++++++++items%3A%0A++++++++++++type%3A+number%0A++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0A++++-+title%3A+GeoJSON+MultiPoint%0A++++++type%3A+object%0A++++++required%3A%0A++++++-+type%0A++++++-+coordinates%0A++++++properties%3A%0A++++++++type%3A%0A++++++++++type%3A+string%0A++++++++++enum%3A%0A++++++++++-+MultiPoint%0A++++++++++x-jsonld-id%3A+%27%40type%27%0A++++++++coordinates%3A%0A++++++++++type%3A+array%0A++++++++++items%3A%0A++++++++++++type%3A+array%0A++++++++++++minItems%3A+2%0A++++++++++++items%3A%0A++++++++++++++type%3A+number%0A++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23coordinates%0A++++++++bbox%3A%0A++++++++++type%3A+array%0A++++++++++minItems%3A+4%0A++++++++++items%3A%0A++++++++++++type%3A+number%0A++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0A++++-+title%3A+GeoJSON+MultiLineString%0A++++++type%3A+object%0A++++++required%3A%0A++++++-+type%0A++++++-+coordinates%0A++++++properties%3A%0A++++++++type%3A%0A++++++++++type%3A+string%0A++++++++++enum%3A%0A++++++++++-+MultiLineString%0A++++++++++x-jsonld-id%3A+%27%40type%27%0A++++++++coordinates%3A%0A++++++++++type%3A+array%0A++++++++++items%3A%0A++++++++++++type%3A+array%0A++++++++++++minItems%3A+2%0A++++++++++++items%3A%0A++++++++++++++type%3A+array%0A++++++++++++++minItems%3A+2%0A++++++++++++++items%3A%0A++++++++++++++++type%3A+number%0A++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23coordinates%0A++++++++bbox%3A%0A++++++++++type%3A+array%0A++++++++++minItems%3A+4%0A++++++++++items%3A%0A++++++++++++type%3A+number%0A++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0A++++-+title%3A+GeoJSON+MultiPolygon%0A++++++type%3A+object%0A++++++required%3A%0A++++++-+type%0A++++++-+coordinates%0A++++++properties%3A%0A++++++++type%3A%0A++++++++++type%3A+string%0A++++++++++enum%3A%0A++++++++++-+MultiPolygon%0A++++++++++x-jsonld-id%3A+%27%40type%27%0A++++++++coordinates%3A%0A++++++++++type%3A+array%0A++++++++++items%3A%0A++++++++++++type%3A+array%0A++++++++++++items%3A%0A++++++++++++++type%3A+array%0A++++++++++++++minItems%3A+4%0A++++++++++++++items%3A%0A++++++++++++++++type%3A+array%0A++++++++++++++++minItems%3A+2%0A++++++++++++++++items%3A%0A++++++++++++++++++type%3A+number%0A++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23coordinates%0A++++++++bbox%3A%0A++++++++++type%3A+array%0A++++++++++minItems%3A+4%0A++++++++++items%3A%0A++++++++++++type%3A+number%0A++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0A++++-+title%3A+GeoJSON+GeometryCollection%0A++++++type%3A+object%0A++++++required%3A%0A++++++-+type%0A++++++-+geometries%0A++++++properties%3A%0A++++++++type%3A%0A++++++++++type%3A+string%0A++++++++++enum%3A%0A++++++++++-+GeometryCollection%0A++++++++++x-jsonld-id%3A+%27%40type%27%0A++++++++geometries%3A%0A++++++++++type%3A+array%0A++++++++++items%3A%0A++++++++++++oneOf%3A%0A++++++++++++-+title%3A+GeoJSON+Point%0A++++++++++++++type%3A+object%0A++++++++++++++required%3A%0A++++++++++++++-+type%0A++++++++++++++-+coordinates%0A++++++++++++++properties%3A%0A++++++++++++++++type%3A%0A++++++++++++++++++type%3A+string%0A++++++++++++++++++enum%3A%0A++++++++++++++++++-+Point%0A++++++++++++++++++x-jsonld-id%3A+%27%40type%27%0A++++++++++++++++coordinates%3A%0A++++++++++++++++++type%3A+array%0A++++++++++++++++++minItems%3A+2%0A++++++++++++++++++items%3A%0A++++++++++++++++++++type%3A+number%0A++++++++++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23coordinates%0A++++++++++++++++bbox%3A%0A++++++++++++++++++type%3A+array%0A++++++++++++++++++minItems%3A+4%0A++++++++++++++++++items%3A%0A++++++++++++++++++++type%3A+number%0A++++++++++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0A++++++++++++-+title%3A+GeoJSON+LineString%0A++++++++++++++type%3A+object%0A++++++++++++++required%3A%0A++++++++++++++-+type%0A++++++++++++++-+coordinates%0A++++++++++++++properties%3A%0A++++++++++++++++type%3A%0A++++++++++++++++++type%3A+string%0A++++++++++++++++++enum%3A%0A++++++++++++++++++-+LineString%0A++++++++++++++++++x-jsonld-id%3A+%27%40type%27%0A++++++++++++++++coordinates%3A%0A++++++++++++++++++type%3A+array%0A++++++++++++++++++minItems%3A+2%0A++++++++++++++++++items%3A%0A++++++++++++++++++++type%3A+array%0A++++++++++++++++++++minItems%3A+2%0A++++++++++++++++++++items%3A%0A++++++++++++++++++++++type%3A+number%0A++++++++++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23coordinates%0A++++++++++++++++bbox%3A%0A++++++++++++++++++type%3A+array%0A++++++++++++++++++minItems%3A+4%0A++++++++++++++++++items%3A%0A++++++++++++++++++++type%3A+number%0A++++++++++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0A++++++++++++-+title%3A+GeoJSON+Polygon%0A++++++++++++++type%3A+object%0A++++++++++++++required%3A%0A++++++++++++++-+type%0A++++++++++++++-+coordinates%0A++++++++++++++properties%3A%0A++++++++++++++++type%3A%0A++++++++++++++++++type%3A+string%0A++++++++++++++++++enum%3A%0A++++++++++++++++++-+Polygon%0A++++++++++++++++++x-jsonld-id%3A+%27%40type%27%0A++++++++++++++++coordinates%3A%0A++++++++++++++++++type%3A+array%0A++++++++++++++++++items%3A%0A++++++++++++++++++++type%3A+array%0A++++++++++++++++++++minItems%3A+4%0A++++++++++++++++++++items%3A%0A++++++++++++++++++++++type%3A+array%0A++++++++++++++++++++++minItems%3A+2%0A++++++++++++++++++++++items%3A%0A++++++++++++++++++++++++type%3A+number%0A++++++++++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23coordinates%0A++++++++++++++++bbox%3A%0A++++++++++++++++++type%3A+array%0A++++++++++++++++++minItems%3A+4%0A++++++++++++++++++items%3A%0A++++++++++++++++++++type%3A+number%0A++++++++++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0A++++++++++++-+title%3A+GeoJSON+MultiPoint%0A++++++++++++++type%3A+object%0A++++++++++++++required%3A%0A++++++++++++++-+type%0A++++++++++++++-+coordinates%0A++++++++++++++properties%3A%0A++++++++++++++++type%3A%0A++++++++++++++++++type%3A+string%0A++++++++++++++++++enum%3A%0A++++++++++++++++++-+MultiPoint%0A++++++++++++++++++x-jsonld-id%3A+%27%40type%27%0A++++++++++++++++coordinates%3A%0A++++++++++++++++++type%3A+array%0A++++++++++++++++++items%3A%0A++++++++++++++++++++type%3A+array%0A++++++++++++++++++++minItems%3A+2%0A++++++++++++++++++++items%3A%0A++++++++++++++++++++++type%3A+number%0A++++++++++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23coordinates%0A++++++++++++++++bbox%3A%0A++++++++++++++++++type%3A+array%0A++++++++++++++++++minItems%3A+4%0A++++++++++++++++++items%3A%0A++++++++++++++++++++type%3A+number%0A++++++++++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0A++++++++++++-+title%3A+GeoJSON+MultiLineString%0A++++++++++++++type%3A+object%0A++++++++++++++required%3A%0A++++++++++++++-+type%0A++++++++++++++-+coordinates%0A++++++++++++++properties%3A%0A++++++++++++++++type%3A%0A++++++++++++++++++type%3A+string%0A++++++++++++++++++enum%3A%0A++++++++++++++++++-+MultiLineString%0A++++++++++++++++++x-jsonld-id%3A+%27%40type%27%0A++++++++++++++++coordinates%3A%0A++++++++++++++++++type%3A+array%0A++++++++++++++++++items%3A%0A++++++++++++++++++++type%3A+array%0A++++++++++++++++++++minItems%3A+2%0A++++++++++++++++++++items%3A%0A++++++++++++++++++++++type%3A+array%0A++++++++++++++++++++++minItems%3A+2%0A++++++++++++++++++++++items%3A%0A++++++++++++++++++++++++type%3A+number%0A++++++++++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23coordinates%0A++++++++++++++++bbox%3A%0A++++++++++++++++++type%3A+array%0A++++++++++++++++++minItems%3A+4%0A++++++++++++++++++items%3A%0A++++++++++++++++++++type%3A+number%0A++++++++++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0A++++++++++++-+title%3A+GeoJSON+MultiPolygon%0A++++++++++++++type%3A+object%0A++++++++++++++required%3A%0A++++++++++++++-+type%0A++++++++++++++-+coordinates%0A++++++++++++++properties%3A%0A++++++++++++++++type%3A%0A++++++++++++++++++type%3A+string%0A++++++++++++++++++enum%3A%0A++++++++++++++++++-+MultiPolygon%0A++++++++++++++++++x-jsonld-id%3A+%27%40type%27%0A++++++++++++++++coordinates%3A%0A++++++++++++++++++type%3A+array%0A++++++++++++++++++items%3A%0A++++++++++++++++++++type%3A+array%0A++++++++++++++++++++items%3A%0A++++++++++++++++++++++type%3A+array%0A++++++++++++++++++++++minItems%3A+4%0A++++++++++++++++++++++items%3A%0A++++++++++++++++++++++++type%3A+array%0A++++++++++++++++++++++++minItems%3A+2%0A++++++++++++++++++++++++items%3A%0A++++++++++++++++++++++++++type%3A+number%0A++++++++++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23coordinates%0A++++++++++++++++bbox%3A%0A++++++++++++++++++type%3A+array%0A++++++++++++++++++minItems%3A+4%0A++++++++++++++++++items%3A%0A++++++++++++++++++++type%3A+number%0A++++++++++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0A++++++++bbox%3A%0A++++++++++type%3A+array%0A++++++++++minItems%3A+4%0A++++++++++items%3A%0A++++++++++++type%3A+number%0A++++++++++x-jsonld-container%3A+%27%40list%27%0A++++++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0A++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23geometry%0A++bbox%3A%0A++++type%3A+array%0A++++minItems%3A+4%0A++++items%3A%0A++++++type%3A+number%0A++++x-jsonld-container%3A+%27%40list%27%0A++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0Ax-jsonld-extra-terms%3A%0A++Feature%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23Feature%0A++FeatureCollection%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23FeatureCollection%0A++GeometryCollection%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23GeometryCollection%0A++LineString%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23LineString%0A++MultiLineString%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23MultiLineString%0A++MultiPoint%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23MultiPoint%0A++MultiPolygon%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23MultiPolygon%0A++Point%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23Point%0A++Polygon%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23Polygon%0A++features%3A%0A++++x-jsonld-container%3A+%27%40set%27%0A++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23features%0Ax-jsonld-prefixes%3A%0A++geojson%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23%0A">View on YAML Viewer</a>

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
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%7B%0A++++%22type%22%3A+%22%40type%22%2C%0A++++%22id%22%3A+%22%40id%22%2C%0A++++%22properties%22%3A+%22geojson%3Aproperties%22%2C%0A++++%22geometry%22%3A+%7B%0A++++++%22%40id%22%3A+%22geojson%3Ageometry%22%2C%0A++++++%22%40context%22%3A+%7B%0A++++++++%22coordinates%22%3A+%7B%0A++++++++++%22%40container%22%3A+%22%40list%22%2C%0A++++++++++%22%40id%22%3A+%22geojson%3Acoordinates%22%0A++++++++%7D%0A++++++%7D%0A++++%7D%2C%0A++++%22bbox%22%3A+%7B%0A++++++%22%40container%22%3A+%22%40list%22%2C%0A++++++%22%40id%22%3A+%22geojson%3Abbox%22%0A++++%7D%2C%0A++++%22Feature%22%3A+%22geojson%3AFeature%22%2C%0A++++%22FeatureCollection%22%3A+%22geojson%3AFeatureCollection%22%2C%0A++++%22GeometryCollection%22%3A+%22geojson%3AGeometryCollection%22%2C%0A++++%22LineString%22%3A+%22geojson%3ALineString%22%2C%0A++++%22MultiLineString%22%3A+%22geojson%3AMultiLineString%22%2C%0A++++%22MultiPoint%22%3A+%22geojson%3AMultiPoint%22%2C%0A++++%22MultiPolygon%22%3A+%22geojson%3AMultiPolygon%22%2C%0A++++%22Point%22%3A+%22geojson%3APoint%22%2C%0A++++%22Polygon%22%3A+%22geojson%3APolygon%22%2C%0A++++%22features%22%3A+%7B%0A++++++%22%40container%22%3A+%22%40set%22%2C%0A++++++%22%40id%22%3A+%22geojson%3Afeatures%22%0A++++%7D%2C%0A++++%22geojson%22%3A+%22https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23%22%2C%0A++++%22%40version%22%3A+1.1%0A++%7D%0A%7D">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/context.jsonld</a>

# References

* [IETF RFC 7946 - The GeoJSON Format](https://datatracker.ietf.org/doc/html/rfc7946)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path:
<code><a href="https://github.com/opengeospatial/bblocks/blob/HEAD/registereditems/geo/common/data_types/geojson" target="_blank">registereditems/geo/common/data_types/geojson</a></code>

