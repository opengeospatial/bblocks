
# GeoPose Basic-Euler (Schema)

`ogc.geo.geopose.basic-euler` *v0.1*

Basic GeoPose using Euler angle rotations to specify orientation

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Proposal

## Schema

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
x-jsonld-extra-terms:
  position: http://example.com/geopose/position
  angles: http://example.com/geopose/angles
  lat: http://example.com/geopose/lat
  yaw: http://example.com/geopose/yaw
  h: http://example.com/geopose/h
  pitch: http://example.com/geopose/pitch
  lon: http://example.com/geopose/lon
  roll: http://example.com/geopose/roll
$id: https://schemas.opengis.net/geopose/1.0/schemata/GeoPose.Basic.Euler.Schema.json

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic-euler/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic-euler/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "longitude": "geo:long",
    "latitude": "geo:lat",
    "height": "geopose:height",
    "rotations": "geopose:rotations",
    "position": "geopose:position",
    "angles": "geopose:angles",
    "lat": "geopose:lat",
    "yaw": "geopose:yaw",
    "h": "geopose:h",
    "pitch": "geopose:pitch",
    "lon": "geopose:lon",
    "roll": "geopose:roll"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic-euler/context.jsonld)

## Sources

* [OGC GeoPose 1.0 Data Exchange Draft Standard](https://docs.ogc.org/dis/21-056r10/21-056r10.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/geo/geopose/basic-euler`

