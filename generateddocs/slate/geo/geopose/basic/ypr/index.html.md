---
title: GeoPose Basic-YPR (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 0.1
  - <a href='#'>GeoPose Basic-YPR</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: GeoPose Basic-YPR (Schema)
---


# GeoPose Basic-YPR `ogc.geo.geopose.basic.ypr`

Basic GeoPose using yaw, pitch, and roll to specify orientation

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/geo/geopose/basic/ypr/" target="_blank">valid</a></strong>
</aside>

# Description

GeoPose 1.0 is an OGC Implementation Standard for exchanging the location and orientation of real or virtual geometric
objects (“Poses”) within reference frames anchored to the earth’s surface (“Geo”) or within other astronomical
coordinate systems.

The Basic-YPR Target has a simple structure with no options. Position is specified as a point in an LTP-ENU frame and
rotation is specified by yaw, pitch, and roll angles specified in decimal degrees.

The Basic_YPR.position attribute shall represent the outer frame, specified by an implicit WGS-84 CRS and an implicit
EPSG 4461-CS (LTP-ENU) coordinate system and explicit parameters to define the tangent point.

The Basic_YPR.angles attribute shall represent the inner frame, which is a rotation-only transformation with Yaw, Pitch,
and Roll (YPR) angles, which expressed as three consecutive rotations of a reference frame oriented East-North-Up (ENU)
coordinate system (where the coordinate axes East, North, and Up correspond to the axes X, Y, Z) about the local (
rotated) axes z, y, and x, applied in that order, corresponding to the conventional Yaw, Pitch, and Roll angles. The
unit of measure SHALL be the degree and the angles represented as signed real number values.
# Examples

## Example 1


```json
{
  "position": {
    "lat": 47.7,
    "lon": -122.3,
    "h": 11.5
  },
  "angles": {
    "yaw": 5.514456741060452,
    "pitch": -0.43610515937237904,
    "roll": 0.0
  }
}

```

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;data=%7B%0A++%22position%22%3A+%7B%0A++++%22lat%22%3A+47.7%2C%0A++++%22lon%22%3A+-122.3%2C%0A++++%22h%22%3A+11.5%0A++%7D%2C%0A++%22angles%22%3A+%7B%0A++++%22yaw%22%3A+5.514456741060452%2C%0A++++%22pitch%22%3A+-0.43610515937237904%2C%0A++++%22roll%22%3A+0.0%0A++%7D%0A%7D%0A">View on JSON Viewer</a></p>
</blockquote>



```jsonld
{
  "position": {
    "lat": 47.7,
    "lon": -122.3,
    "h": 11.5
  },
  "angles": {
    "yaw": 5.514456741060452,
    "pitch": -0.43610515937237904,
    "roll": 0.0
  },
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic/ypr/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22position%22%3A+%7B%0A++++%22lat%22%3A+47.7%2C%0A++++%22lon%22%3A+-122.3%2C%0A++++%22h%22%3A+11.5%0A++%7D%2C%0A++%22angles%22%3A+%7B%0A++++%22yaw%22%3A+5.514456741060452%2C%0A++++%22pitch%22%3A+-0.43610515937237904%2C%0A++++%22roll%22%3A+0.0%0A++%7D%2C%0A++%22%40context%22%3A+%22https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Fgeopose%2Fbasic%2Fypr%2Fcontext.jsonld%22%0A%7D">View on JSON-LD Playground</a></p>
</blockquote>



```turtle
@prefix geo1: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix geopose: <http://example.com/geopose/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] geopose:angles [ geopose:pitch -4.361052e-01 ;
            geopose:roll 0e+00 ;
            geopose:yaw 5.514457e+00 ] ;
    geopose:position [ geopose:h 1.15e+01 ;
            geo1:lat 4.77e+01 ;
            geo1:long -1.223e+02 ] .


```


## Example 2


```json
{
  "position": {
    "lat": 47.7,
    "lon": -122.3,
    "h": 11.5
  },
  "angles": {
    "yaw": 5.518671098486835,
    "pitch": -0.4381464123477409,
    "roll": 0.0
  }
}

```

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;data=%7B%0A++%22position%22%3A+%7B%0A++++%22lat%22%3A+47.7%2C%0A++++%22lon%22%3A+-122.3%2C%0A++++%22h%22%3A+11.5%0A++%7D%2C%0A++%22angles%22%3A+%7B%0A++++%22yaw%22%3A+5.518671098486835%2C%0A++++%22pitch%22%3A+-0.4381464123477409%2C%0A++++%22roll%22%3A+0.0%0A++%7D%0A%7D%0A">View on JSON Viewer</a></p>
</blockquote>



```jsonld
{
  "position": {
    "lat": 47.7,
    "lon": -122.3,
    "h": 11.5
  },
  "angles": {
    "yaw": 5.518671098486835,
    "pitch": -0.4381464123477409,
    "roll": 0.0
  },
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic/ypr/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22position%22%3A+%7B%0A++++%22lat%22%3A+47.7%2C%0A++++%22lon%22%3A+-122.3%2C%0A++++%22h%22%3A+11.5%0A++%7D%2C%0A++%22angles%22%3A+%7B%0A++++%22yaw%22%3A+5.518671098486835%2C%0A++++%22pitch%22%3A+-0.4381464123477409%2C%0A++++%22roll%22%3A+0.0%0A++%7D%2C%0A++%22%40context%22%3A+%22https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Fgeopose%2Fbasic%2Fypr%2Fcontext.jsonld%22%0A%7D">View on JSON-LD Playground</a></p>
</blockquote>



```turtle
@prefix geo1: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix geopose: <http://example.com/geopose/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] geopose:angles [ geopose:pitch -4.381464e-01 ;
            geopose:roll 0e+00 ;
            geopose:yaw 5.518671e+00 ] ;
    geopose:position [ geopose:h 1.15e+01 ;
            geo1:lat 4.77e+01 ;
            geo1:long -1.223e+02 ] .


```


## Example 3


```json
{
  "position": {
    "lat": 47.7,
    "lon": -122.3,
    "h": 11.5
  },
  "angles": {
    "yaw": 5.522894747595089,
    "pitch": -0.4401787262476278,
    "roll": 0.0
  }
}

```

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;data=%7B%0A++%22position%22%3A+%7B%0A++++%22lat%22%3A+47.7%2C%0A++++%22lon%22%3A+-122.3%2C%0A++++%22h%22%3A+11.5%0A++%7D%2C%0A++%22angles%22%3A+%7B%0A++++%22yaw%22%3A+5.522894747595089%2C%0A++++%22pitch%22%3A+-0.4401787262476278%2C%0A++++%22roll%22%3A+0.0%0A++%7D%0A%7D%0A">View on JSON Viewer</a></p>
</blockquote>



```jsonld
{
  "position": {
    "lat": 47.7,
    "lon": -122.3,
    "h": 11.5
  },
  "angles": {
    "yaw": 5.522894747595089,
    "pitch": -0.4401787262476278,
    "roll": 0.0
  },
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic/ypr/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22position%22%3A+%7B%0A++++%22lat%22%3A+47.7%2C%0A++++%22lon%22%3A+-122.3%2C%0A++++%22h%22%3A+11.5%0A++%7D%2C%0A++%22angles%22%3A+%7B%0A++++%22yaw%22%3A+5.522894747595089%2C%0A++++%22pitch%22%3A+-0.4401787262476278%2C%0A++++%22roll%22%3A+0.0%0A++%7D%2C%0A++%22%40context%22%3A+%22https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Fgeopose%2Fbasic%2Fypr%2Fcontext.jsonld%22%0A%7D">View on JSON-LD Playground</a></p>
</blockquote>



```turtle
@prefix geo1: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix geopose: <http://example.com/geopose/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] geopose:angles [ geopose:pitch -4.401787e-01 ;
            geopose:roll 0e+00 ;
            geopose:yaw 5.522895e+00 ] ;
    geopose:position [ geopose:h 1.15e+01 ;
            geo1:lat 4.77e+01 ;
            geo1:long -1.223e+02 ] .


```


## Example 4


```json
{
  "position": {
    "lat": 47.7,
    "lon": -122.3,
    "h": 11.5
  },
  "angles": {
    "yaw": 5.527127708845192,
    "pitch": -0.44220204512692407,
    "roll": 0.0
  }
}

```

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;data=%7B%0A++%22position%22%3A+%7B%0A++++%22lat%22%3A+47.7%2C%0A++++%22lon%22%3A+-122.3%2C%0A++++%22h%22%3A+11.5%0A++%7D%2C%0A++%22angles%22%3A+%7B%0A++++%22yaw%22%3A+5.527127708845192%2C%0A++++%22pitch%22%3A+-0.44220204512692407%2C%0A++++%22roll%22%3A+0.0%0A++%7D%0A%7D%0A">View on JSON Viewer</a></p>
</blockquote>



```jsonld
{
  "position": {
    "lat": 47.7,
    "lon": -122.3,
    "h": 11.5
  },
  "angles": {
    "yaw": 5.527127708845192,
    "pitch": -0.44220204512692407,
    "roll": 0.0
  },
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic/ypr/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22position%22%3A+%7B%0A++++%22lat%22%3A+47.7%2C%0A++++%22lon%22%3A+-122.3%2C%0A++++%22h%22%3A+11.5%0A++%7D%2C%0A++%22angles%22%3A+%7B%0A++++%22yaw%22%3A+5.527127708845192%2C%0A++++%22pitch%22%3A+-0.44220204512692407%2C%0A++++%22roll%22%3A+0.0%0A++%7D%2C%0A++%22%40context%22%3A+%22https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Fgeopose%2Fbasic%2Fypr%2Fcontext.jsonld%22%0A%7D">View on JSON-LD Playground</a></p>
</blockquote>



```turtle
@prefix geo1: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix geopose: <http://example.com/geopose/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] geopose:angles [ geopose:pitch -4.42202e-01 ;
            geopose:roll 0e+00 ;
            geopose:yaw 5.527128e+00 ] ;
    geopose:position [ geopose:h 1.15e+01 ;
            geo1:lat 4.77e+01 ;
            geo1:long -1.223e+02 ] .


```


# JSON Schema

```yaml--schema
description: 'Basic-YPR: Basic GeoPose using yaw, pitch, and roll to specify orientation'
definitions:
  angles:
    type: object
    properties:
      yaw:
        type: number
        x-jsonld-id: http://example.com/geopose/yaw
      pitch:
        type: number
        x-jsonld-id: http://example.com/geopose/pitch
      roll:
        type: number
        x-jsonld-id: http://example.com/geopose/roll
    required:
    - yaw
    - pitch
    - roll
  Position:
    type: object
    properties:
      lat:
        type: number
        x-jsonld-id: http://www.w3.org/2003/01/geo/wgs84_pos#lat
      lon:
        type: number
        x-jsonld-id: http://www.w3.org/2003/01/geo/wgs84_pos#long
      h:
        type: number
        x-jsonld-id: http://example.com/geopose/h
    required:
    - lat
    - lon
    - h
type: object
properties:
  position:
    $ref: '#/definitions/Position'
    x-jsonld-id: http://example.com/geopose/position
  angles:
    $ref: '#/definitions/angles'
    x-jsonld-id: http://example.com/geopose/angles
required:
- position
- angles
x-jsonld-prefixes:
  geopose: http://example.com/geopose/
  geo: http://www.w3.org/2003/01/geo/wgs84_pos#
$id: https://schemas.opengis.net/geopose/1.0/schemata/GeoPose.Basic.YPR.Schema.json

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;data=description%3A+%27Basic-YPR%3A+Basic+GeoPose+using+yaw%2C+pitch%2C+and+roll+to+specify+orientation%27%0Adefinitions%3A%0A++angles%3A%0A++++type%3A+object%0A++++properties%3A%0A++++++yaw%3A%0A++++++++type%3A+number%0A++++++++x-jsonld-id%3A+http%3A%2F%2Fexample.com%2Fgeopose%2Fyaw%0A++++++pitch%3A%0A++++++++type%3A+number%0A++++++++x-jsonld-id%3A+http%3A%2F%2Fexample.com%2Fgeopose%2Fpitch%0A++++++roll%3A%0A++++++++type%3A+number%0A++++++++x-jsonld-id%3A+http%3A%2F%2Fexample.com%2Fgeopose%2Froll%0A++++required%3A%0A++++-+yaw%0A++++-+pitch%0A++++-+roll%0A++Position%3A%0A++++type%3A+object%0A++++properties%3A%0A++++++lat%3A%0A++++++++type%3A+number%0A++++++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23lat%0A++++++lon%3A%0A++++++++type%3A+number%0A++++++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23long%0A++++++h%3A%0A++++++++type%3A+number%0A++++++++x-jsonld-id%3A+http%3A%2F%2Fexample.com%2Fgeopose%2Fh%0A++++required%3A%0A++++-+lat%0A++++-+lon%0A++++-+h%0Atype%3A+object%0Aproperties%3A%0A++position%3A%0A++++%24ref%3A+%27%23%2Fdefinitions%2FPosition%27%0A++++x-jsonld-id%3A+http%3A%2F%2Fexample.com%2Fgeopose%2Fposition%0A++angles%3A%0A++++%24ref%3A+%27%23%2Fdefinitions%2Fangles%27%0A++++x-jsonld-id%3A+http%3A%2F%2Fexample.com%2Fgeopose%2Fangles%0Arequired%3A%0A-+position%0A-+angles%0Ax-jsonld-prefixes%3A%0A++geopose%3A+http%3A%2F%2Fexample.com%2Fgeopose%2F%0A++geo%3A+http%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23%0A%24id%3A+https%3A%2F%2Fschemas.opengis.net%2Fgeopose%2F1.0%2Fschemata%2FGeoPose.Basic.YPR.Schema.json%0A">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic/ypr/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic/ypr/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic/ypr/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic/ypr/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "position": {
      "@id": "geopose:position",
      "@context": {
        "lat": "geo:lat",
        "lon": "geo:long",
        "h": "geopose:h"
      }
    },
    "angles": {
      "@id": "geopose:angles",
      "@context": {
        "yaw": "geopose:yaw",
        "pitch": "geopose:pitch",
        "roll": "geopose:roll"
      }
    },
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%7B%0A++++%22position%22%3A+%7B%0A++++++%22%40id%22%3A+%22geopose%3Aposition%22%2C%0A++++++%22%40context%22%3A+%7B%0A++++++++%22lat%22%3A+%22geo%3Alat%22%2C%0A++++++++%22lon%22%3A+%22geo%3Along%22%2C%0A++++++++%22h%22%3A+%22geopose%3Ah%22%0A++++++%7D%0A++++%7D%2C%0A++++%22angles%22%3A+%7B%0A++++++%22%40id%22%3A+%22geopose%3Aangles%22%2C%0A++++++%22%40context%22%3A+%7B%0A++++++++%22yaw%22%3A+%22geopose%3Ayaw%22%2C%0A++++++++%22pitch%22%3A+%22geopose%3Apitch%22%2C%0A++++++++%22roll%22%3A+%22geopose%3Aroll%22%0A++++++%7D%0A++++%7D%2C%0A++++%22geopose%22%3A+%22http%3A%2F%2Fexample.com%2Fgeopose%2F%22%2C%0A++++%22geo%22%3A+%22http%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23%22%2C%0A++++%22%40version%22%3A+1.1%0A++%7D%0A%7D">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic/ypr/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/geopose/basic/ypr/context.jsonld</a>

# References

* [OGC GeoPose 1.0 Data Exchange Draft Standard](https://docs.ogc.org/dis/21-056r10/21-056r10.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path:
<code><a href="https://github.com/opengeospatial/bblocks/blob/HEAD/registereditems/geo/geopose/basic/ypr" target="_blank">registereditems/geo/geopose/basic/ypr</a></code>

