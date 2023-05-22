# GeoPose Basic-Euler (Schema)

*Version 0.1*

Basic GeoPose using Euler angle rotations to specify orientation

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Proposal

## Schema

[schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic-euler/schema.yaml)

```yaml
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
$id: https://schemas.opengis.net/geopose/1.0/schemata/GeoPose.Basic.Euler.Schema.json

```
## Sources

* [OGC GeoPose 1.0 Data Exchange Draft Standard](https://docs.ogc.org/dis/21-056r10/21-056r10.html)
