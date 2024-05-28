
# JSON-FG time member (Schema)

`ogc.geo.json-fg.time` *v0.2.2*

None

[*Status*](http://www.opengis.net/def/status): Stable

## Examples

### Sample date (May 13th, 2024)
#### json
```json
{ 
  "date": "2024-05-13"
}

```

#### jsonld
```jsonld
{
  "date": "2024-05-13",
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/context.jsonld"
}
```

#### ttl
```ttl
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] time:hasTime "2024-05-13"^^xsd:date .


```


### Sample timestamp (May 13th, 2024, at 19:15:16 UTC)
#### json
```json
{ 
  "timestamp": "2024-05-13T19:15:16Z"
}

```

#### jsonld
```jsonld
{
  "timestamp": "2024-05-13T19:15:16Z",
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/context.jsonld"
}
```

#### ttl
```ttl
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] time:hasTime "2024-05-13T19:15:16+00:00"^^xsd:dateTime .


```


### Sample timestamp with milliseconds
#### json
```json
{ 
  "timestamp": "2024-05-13T19:15:16.987Z"
}

```

#### jsonld
```jsonld
{
  "timestamp": "2024-05-13T19:15:16.987Z",
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/context.jsonld"
}
```

#### ttl
```ttl
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] time:hasTime "2024-05-13T19:15:16.987000+00:00"^^xsd:dateTime .


```


### Interval between two dates
#### json
```json
{ 
  "interval": [
    "2024-05-13", 
    "2024-05-16"
  ]
}

```

#### jsonld
```jsonld
{
  "interval": [
    "2024-05-13",
    "2024-05-16"
  ],
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/context.jsonld"
}
```

#### ttl
```ttl
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#> .

[] time:hasTime ( "2024-05-13" "2024-05-16" ) .


```


### Open-ended interval (no end timestamp)
#### json
```json
{ 
  "interval": [
    "2024-05-13T19:15:16Z",
    ".."
  ]
}

```

#### jsonld
```jsonld
{
  "interval": [
    "2024-05-13T19:15:16Z",
    ".."
  ],
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/context.jsonld"
}
```

#### ttl
```ttl
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#> .

[] time:hasTime ( "2024-05-13T19:15:16Z" ".." ) .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://beta.schemas.opengis.net/json-fg/time.json
title: the time member
description: This JSON Schema is part of JSON-FG version 0.2.2
oneOf:
- type: 'null'
- type: object
  properties:
    date:
      $ref: '#/$defs/date'
      x-jsonld-id: http://www.w3.org/2006/time#hasTime
      x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
    timestamp:
      $ref: '#/$defs/timestamp'
      x-jsonld-id: http://www.w3.org/2006/time#hasTime
      x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
    interval:
      $ref: '#/$defs/interval'
      x-jsonld-id: http://www.w3.org/2006/time#hasTime
      x-jsonld-container: '@list'
$defs:
  date:
    type: string
    pattern: ^\d{4}-\d{2}-\d{2}$
  timestamp:
    type: string
    pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$
  interval:
    type: array
    minItems: 2
    maxItems: 2
    items:
      oneOf:
      - $ref: '#/$defs/date'
      - $ref: '#/$defs/timestamp'
      - type: string
        enum:
        - ..
x-jsonld-prefixes:
  time: http://www.w3.org/2006/time#
  xsd: http://www.w3.org/2001/XMLSchema#

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "date": {
      "@id": "time:hasTime",
      "@type": "http://www.w3.org/2001/XMLSchema#date"
    },
    "timestamp": {
      "@id": "time:hasTime",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "interval": {
      "@id": "time:hasTime",
      "@container": "@list"
    },
    "time": "http://www.w3.org/2006/time#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/context.jsonld)

## Sources

* [OGC Testbed-17: OGC Features and Geometries JSON Engineering Report](http://docs.ogc.org/per/21-017r1.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/geo/json-fg/time`

