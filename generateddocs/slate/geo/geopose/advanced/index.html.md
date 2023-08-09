---
title: GeoPose Advanced (Schema)

toc_footers:
  - Version 0.1
  - <a href='#'>GeoPose Advanced</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: GeoPose Advanced (Schema)
---


# GeoPose Advanced `ogc.geo.geopose.advanced`

Advanced GeoPose allowing flexible outer frame specification, quaternion orientation, and valid time.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong>valid</strong>
</aside>


# JSON Schema

```yaml--schema
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
$id: https://schemas.opengis.net/geopose/1.0/schemata/GeoPose.Advanced.Schema.json

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/advanced/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/advanced/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/advanced/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/advanced/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "quaternion": {
      "@id": "geopose:quaternion",
      "@context": {
        "x": "geopose:x",
        "y": "geopose:y",
        "z": "geopose:z",
        "w": "geopose:w"
      }
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
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/advanced/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/advanced/context.jsonld</a>

# References

* [OGC GeoPose 1.0 Data Exchange Draft Standard](https://docs.ogc.org/dis/21-056r10/21-056r10.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path: `registereditems/geo/geopose/advanced`

