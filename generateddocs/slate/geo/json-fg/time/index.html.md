---
title: JSON-FG time member (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 0.2.2
  - <a href='#'>JSON-FG time member</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: JSON-FG time member (Schema)
---


# JSON-FG time member `ogc.geo.json-fg.time`

None

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/stable" target="_blank" data-rainbow-uri>Stable</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/geo/json-fg/time/" target="_blank">valid</a></strong>
</aside>

# Examples

## Sample date (May 13th, 2024)



```json
{ 
  "date": "2024-05-13"
}

```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Fjson-fg%2Ftime%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "date": "2024-05-13",
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Fjson-fg%2Ftime%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] time:hasTime "2024-05-13"^^xsd:date .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_1_1.ttl">Open in new window</a>
</blockquote>



## Sample timestamp (May 13th, 2024, at 19:15:16 UTC)



```json
{ 
  "timestamp": "2024-05-13T19:15:16Z"
}

```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_2_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Fjson-fg%2Ftime%2Fexample_2_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "timestamp": "2024-05-13T19:15:16Z",
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_2_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Fjson-fg%2Ftime%2Fexample_2_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] time:hasTime "2024-05-13T19:15:16+00:00"^^xsd:dateTime .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_2_1.ttl">Open in new window</a>
</blockquote>



## Sample timestamp with milliseconds



```json
{ 
  "timestamp": "2024-05-13T19:15:16.987Z"
}

```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_3_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Fjson-fg%2Ftime%2Fexample_3_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "timestamp": "2024-05-13T19:15:16.987Z",
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_3_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Fjson-fg%2Ftime%2Fexample_3_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] time:hasTime "2024-05-13T19:15:16.987000+00:00"^^xsd:dateTime .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_3_1.ttl">Open in new window</a>
</blockquote>



## Interval between two dates



```json
{ 
  "interval": [
    "2024-05-13", 
    "2024-05-16"
  ]
}

```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_4_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Fjson-fg%2Ftime%2Fexample_4_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "interval": [
    "2024-05-13",
    "2024-05-16"
  ],
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_4_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Fjson-fg%2Ftime%2Fexample_4_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#> .

[] time:hasTime ( "2024-05-13" "2024-05-16" ) .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_4_1.ttl">Open in new window</a>
</blockquote>



## Open-ended interval (no end timestamp)



```json
{ 
  "interval": [
    "2024-05-13T19:15:16Z",
    ".."
  ]
}

```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_5_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Fjson-fg%2Ftime%2Fexample_5_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "interval": [
    "2024-05-13T19:15:16Z",
    ".."
  ],
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_5_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Fjson-fg%2Ftime%2Fexample_5_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#> .

[] time:hasTime ( "2024-05-13T19:15:16Z" ".." ) .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/time/example_5_1.ttl">Open in new window</a>
</blockquote>



# JSON Schema

```yaml--schema
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

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Fjson-fg%2Ftime%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/schema.json</a>


# JSON-LD Context

```json--ldContext
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

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Fjson-fg%2Ftime%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/time/context.jsonld</a>

# References

* [OGC Testbed-17: OGC Features and Geometries JSON Engineering Report](http://docs.ogc.org/per/21-017r1.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path:
<code><a href="https://github.com/opengeospatial/bblocks/blob/HEAD/registereditems/geo/json-fg/time" target="_blank">registereditems/geo/json-fg/time</a></code>

