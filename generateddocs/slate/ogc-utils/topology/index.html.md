---
title: Geometry using references (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 0.1
  - <a href='#'>Geometry using references</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Geometry using references (Schema)
---


# Geometry using references `ogc.ogc-utils.topology`

Demonstration of a schema using coordinates of points, withpout duplication

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/ogc-utils/topology/" target="_blank">valid</a></strong>
</aside>

# Description

A datatype containing ordered list of references to other features. 

Other features may be either features with topology properties or GeoJSON (or FG-JSON) point objects.

This is a generalisation of the TopoJSON concept using inline data, and not limited to linestrings.


# Examples

## Example Topology object

See panel to right - note that a more user friendly "collapsable" version is in development. 



```json
{
  "type": "LineString",
  "references": [
    "P1",
    "P2"
  ]
}
```

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fogc-utils%2Ftopology%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "type": "LineString",
  "references": [
    "P1",
    "P2"
  ],
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/topology/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fogc-utils%2Ftopology%2Fexample_1_1.jsonld">View on JSON-LD Playground</a></p>
</blockquote>




```turtle
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

[] a geojson:LineString ;
    geojson:relatedFeatures ( <http://www.example.com/features/P1> <http://www.example.com/features/P2> ) .


```


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: feature with geometry by reference
properties:
  type:
    $ref: ../iri-or-curie/schema.yaml
    x-jsonld-id: '@type'
  references:
    type: array
    items:
      $ref: ../iri-or-curie/schema.yaml
    x-jsonld-id: https://purl.org/geojson/vocab#relatedFeatures
    x-jsonld-type: '@id'
    x-jsonld-container: '@list'
required:
- references
- type
x-jsonld-extra-terms:
  csdm: https://linked.data.gov.au/def/csdm/
  dct: http://purl.org/dc/terms/
  LineString: https://purl.org/geojson/vocab#LineString
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fogc-utils%2Ftopology%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/topology/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/topology/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/topology/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/topology/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "type": "@type",
    "references": {
      "@id": "geojson:relatedFeatures",
      "@type": "@id",
      "@container": "@list"
    },
    "csdm": "https://linked.data.gov.au/def/csdm/",
    "dct": "http://purl.org/dc/terms/",
    "LineString": "geojson:LineString",
    "geojson": "https://purl.org/geojson/vocab#",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fogc-utils%2Ftopology%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/topology/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/topology/context.jsonld</a>

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path:
<code><a href="https://github.com/opengeospatial/bblocks/blob/HEAD/registereditems/ogc-utils/topology" target="_blank">registereditems/ogc-utils/topology</a></code>

