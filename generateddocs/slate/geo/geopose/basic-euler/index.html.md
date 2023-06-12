---
title: GeoPose Basic-Euler (Schema)

toc_footers:
  - Version 0.1
  - <a href='#'>GeoPose Basic-Euler</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: GeoPose Basic-Euler (Schema)
---


# GeoPose Basic-Euler `ogc.geo.geopose.basic-euler`

Basic GeoPose using Euler angle rotations to specify orientation

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Proposal

<aside class="success">
This building block is <strong>valid</strong>
</aside>


# JSON Schema

```yaml--schema
description: 'Basic-Euler: Basic GeoPose using Euler angle rotations to specify orientation'
type: object
properties:
  longitude:
    type: number
    minimum: -180.0
    maximum: 180.0
    x-jsonld-id: http://www.w3.org/2003/01/geo/wgs84_pos#long
  latitude:
    type: number
    minimum: -90.0
    maximum: 90.0
    x-jsonld-id: http://www.w3.org/2003/01/geo/wgs84_pos#lat
  height:
    type: number
    x-jsonld-id: http://example.com/geopose/height
  rotations:
    type: array
    items:
      type: number
    minItems: 3
    maxItems: 3
    x-jsonld-id: http://example.com/geopose/rotations
required:
- longitude
- latitude
- height
- rotations
x-jsonld-prefixes:
  geopose: http://example.com/geopose/
  geo: http://www.w3.org/2003/01/geo/wgs84_pos#
x-jsonld-extra-terms:
  lon: http://example.com/geopose/lon
  lat: http://example.com/geopose/lat
  position: http://example.com/geopose/position
  yaw: http://example.com/geopose/yaw
  angles: http://example.com/geopose/angles
  pitch: http://example.com/geopose/pitch
  roll: http://example.com/geopose/roll
  h: http://example.com/geopose/h
$id: https://schemas.opengis.net/geopose/1.0/schemata/GeoPose.Basic.Euler.Schema.json

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic-euler/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic-euler/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic-euler/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic-euler/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "longitude": "geo:long",
    "latitude": "geo:lat",
    "height": "geopose:height",
    "rotations": "geopose:rotations",
    "lon": "geopose:lon",
    "lat": "geopose:lat",
    "position": "geopose:position",
    "yaw": "geopose:yaw",
    "angles": "geopose:angles",
    "pitch": "geopose:pitch",
    "roll": "geopose:roll",
    "h": "geopose:h"
  }
}
```

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic-euler/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic-euler/context.jsonld</a>

# References

* [OGC GeoPose 1.0 Data Exchange Draft Standard](https://docs.ogc.org/dis/21-056r10/21-056r10.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path: `registereditems/geo/geopose/basic-euler`

