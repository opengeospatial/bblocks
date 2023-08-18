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

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;data=description%3A+%27Advanced%3A+Advanced+GeoPose+allowing+flexible+outer+frame+specification%2C%0A++quaternion+orientation%2C+and+valid+time.%27%0Adefinitions%3A%0A++FrameSpecification%3A%0A++++type%3A+object%0A++++properties%3A%0A++++++authority%3A%0A++++++++type%3A+string%0A++++++id%3A%0A++++++++type%3A+string%0A++++++parameters%3A%0A++++++++type%3A+string%0A++++required%3A%0A++++-+authority%0A++++-+id%0A++++-+parameters%0A++Quaternion%3A%0A++++type%3A+object%0A++++properties%3A%0A++++++x%3A%0A++++++++type%3A+number%0A++++++++x-jsonld-id%3A+http%3A%2F%2Fexample.com%2Fgeopose%2Fx%0A++++++y%3A%0A++++++++type%3A+number%0A++++++++x-jsonld-id%3A+http%3A%2F%2Fexample.com%2Fgeopose%2Fy%0A++++++z%3A%0A++++++++type%3A+number%0A++++++++x-jsonld-id%3A+http%3A%2F%2Fexample.com%2Fgeopose%2Fz%0A++++++w%3A%0A++++++++type%3A+number%0A++++++++x-jsonld-id%3A+http%3A%2F%2Fexample.com%2Fgeopose%2Fw%0A++++required%3A%0A++++-+x%0A++++-+y%0A++++-+z%0A++++-+w%0Atype%3A+object%0Aproperties%3A%0A++frameSpecification%3A%0A++++%24ref%3A+%27%23%2Fdefinitions%2FFrameSpecification%27%0A++quaternion%3A%0A++++%24ref%3A+%27%23%2Fdefinitions%2FQuaternion%27%0A++++x-jsonld-id%3A+http%3A%2F%2Fexample.com%2Fgeopose%2Fquaternion%0A++validTime%3A%0A++++type%3A+integer%0Arequired%3A%0A-+frameSpecification%0A-+quaternion%0Ax-jsonld-extra-terms%3A%0A++position%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fexample.com%2Fgeopose%2Fposition%0A++++x-jsonld-context%3A%0A++++++lat%3A+http%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23lat%0A++++++lon%3A+http%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23long%0A++++++h%3A+http%3A%2F%2Fexample.com%2Fgeopose%2Fh%0Ax-jsonld-prefixes%3A%0A++geopose%3A+http%3A%2F%2Fexample.com%2Fgeopose%2F%0A++geo%3A+http%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23%0A%24id%3A+https%3A%2F%2Fschemas.opengis.net%2Fgeopose%2F1.0%2Fschemata%2FGeoPose.Advanced.Schema.json%0A">View on YAML Viewer</a>

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

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%7B%0A++++%22quaternion%22%3A+%7B%0A++++++%22%40id%22%3A+%22geopose%3Aquaternion%22%2C%0A++++++%22%40context%22%3A+%7B%0A++++++++%22x%22%3A+%22geopose%3Ax%22%2C%0A++++++++%22y%22%3A+%22geopose%3Ay%22%2C%0A++++++++%22z%22%3A+%22geopose%3Az%22%2C%0A++++++++%22w%22%3A+%22geopose%3Aw%22%0A++++++%7D%0A++++%7D%2C%0A++++%22position%22%3A+%7B%0A++++++%22%40id%22%3A+%22geopose%3Aposition%22%2C%0A++++++%22%40context%22%3A+%7B%0A++++++++%22lat%22%3A+%22geo%3Alat%22%2C%0A++++++++%22lon%22%3A+%22geo%3Along%22%2C%0A++++++++%22h%22%3A+%22geopose%3Ah%22%0A++++++%7D%0A++++%7D%2C%0A++++%22geopose%22%3A+%22http%3A%2F%2Fexample.com%2Fgeopose%2F%22%2C%0A++++%22geo%22%3A+%22http%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23%22%2C%0A++++%22%40version%22%3A+1.1%0A++%7D%0A%7D">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/advanced/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/advanced/context.jsonld</a>

# References

* [OGC GeoPose 1.0 Data Exchange Draft Standard](https://docs.ogc.org/dis/21-056r10/21-056r10.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path:
<code><a href="https://github.com/opengeospatial/bblocks/blob/HEAD/registereditems/geo/geopose/advanced" target="_blank">registereditems/geo/geopose/advanced</a></code>

