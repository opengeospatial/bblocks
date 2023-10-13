---
title: Link with role and target conformance (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 0.1
  - <a href='#'>Link with role and target conformance</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Link with role and target conformance (Schema)
---


# Link with role and target conformance `ogc.geo.json-fg.link-role`

A JSON-FG compliant web link with mandatory annotation of link role and optional conformance information to describe target resource. Compliant with profile resource descriptor model.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/geo/json-fg/link-role/" target="_blank">valid</a></strong>
</aside>

# Examples

## Example Topology object

See panel to right - note that a more user friendly "collapsable" version is in development. 



```json
{
  "@context": {
    "@base": "http://example.org"
  },
  "href": "http//example.org/frog",
  "rel":"related",
  "role": "animals"
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/link-role/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Fjson-fg%2Flink-role%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "@context": [
    "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/link-role/context.jsonld",
    {
      "@base": "http://example.org"
    }
  ],
  "href": "http//example.org/frog",
  "rel": "related",
  "role": "animals"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/link-role/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Fjson-fg%2Flink-role%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prof: <http://www.w3.org/ns/dx/prof/> .

[] ns1:relation <http://www.iana.org/assignments/relation/related> ;
    prof:hasRole <http://example.org/animals> ;
    oa:hasTarget "http//example.org/frog" .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/link-role/example_1_1.ttl">Open in new window</a>
</blockquote>



# JSON Schema

```yaml--schema
description: annotated link with role and conformance
$defs:
  coderef:
    $ref: ../../../ogc-utils/iri-or-curie/schema.yaml
  coderefs:
    $ref: ../../../ogc-utils/iri-or-curie/schema.yaml
allOf:
- $ref: ../../../ogc-utils/json-link/schema.yaml
- properties:
    role:
      $ref: '#/$defs/coderef'
      x-jsonld-id: http://www.w3.org/ns/dx/prof/hasRole
      x-jsonld-type: '@id'
    conformsTo:
      $ref: '#/$defs/coderefs'
      x-jsonld-id: http://purl.org/dc/terms/conformsTo
      x-jsonld-type: '@id'
  required:
  - role
x-jsonld-prefixes:
  prof: http://www.w3.org/ns/dx/prof/
  dct: http://purl.org/dc/terms/

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Fjson-fg%2Flink-role%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/link-role/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/link-role/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/link-role/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/link-role/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "href": "oa:hasTarget",
    "rel": {
      "@id": "http://www.iana.org/assignments/relation",
      "@type": "@id",
      "@context": {
        "@base": "http://www.iana.org/assignments/relation/"
      }
    },
    "type": "dct:type",
    "hreflang": "dct:language",
    "title": "rdfs:label",
    "length": "dct:extent",
    "role": {
      "@id": "prof:hasRole",
      "@type": "@id"
    },
    "conformsTo": {
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "prof": "http://www.w3.org/ns/dx/prof/",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Fjson-fg%2Flink-role%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/link-role/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/link-role/context.jsonld</a>

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path:
<code><a href="https://github.com/opengeospatial/bblocks/blob/HEAD/registereditems/geo/json-fg/link-role" target="_blank">registereditems/geo/json-fg/link-role</a></code>

