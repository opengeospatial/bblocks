
# GeoPose Advanced (Schema)

`ogc.geo.geopose.advanced` *v0.1*

Advanced GeoPose allowing flexible outer frame specification, quaternion orientation, and valid time.

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
description: 'Advanced: Advanced GeoPose allowing flexible outer frame specification,
  quaternion orientation, and valid time.'
definitions:
  FrameSpecification:
    type: object
    properties:
      authority:
        type: string
      id:
        type: string
      parameters:
        type: string
    required:
    - authority
    - id
    - parameters
  Quaternion:
    type: object
    properties:
      x:
        type: number
        x-jsonld-id: http://example.com/geopose/x
      y:
        type: number
        x-jsonld-id: http://example.com/geopose/y
      z:
        type: number
        x-jsonld-id: http://example.com/geopose/z
      w:
        type: number
        x-jsonld-id: http://example.com/geopose/w
    required:
    - x
    - y
    - z
    - w
type: object
properties:
  frameSpecification:
    $ref: '#/definitions/FrameSpecification'
  quaternion:
    $ref: '#/definitions/Quaternion'
    x-jsonld-id: http://example.com/geopose/quaternion
  validTime:
    type: integer
required:
- frameSpecification
- quaternion
x-jsonld-extra-terms:
  position:
    x-jsonld-id: http://example.com/geopose/position
    x-jsonld-context:
      lat: http://www.w3.org/2003/01/geo/wgs84_pos#lat
      lon: http://www.w3.org/2003/01/geo/wgs84_pos#long
      h: http://example.com/geopose/h
x-jsonld-prefixes:
  geopose: http://example.com/geopose/
  geo: http://www.w3.org/2003/01/geo/wgs84_pos#

```

Links to the schema:

* YAML version: [schema.yaml](http://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/advanced/schema.json)
* JSON version: [schema.json](http://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/advanced/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "quaternion": {
      "@context": {
        "x": "geopose:x",
        "y": "geopose:y",
        "z": "geopose:z",
        "w": "geopose:w"
      },
      "@id": "geopose:quaternion"
    },
    "position": {
      "@id": "geopose:position",
      "@context": {
        "lat": "geo:lat",
        "lon": "geo:long",
        "h": "geopose:h"
      }
    },
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](http://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/advanced/context.jsonld)

## Sources

* [OGC GeoPose 1.0 Data Exchange Draft Standard](https://docs.ogc.org/dis/21-056r10/21-056r10.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/geo/geopose/advanced`

