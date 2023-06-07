---
title: JSON Link (Schema)

toc_footers:
  - Version 0.1
  - <a href='#'>JSON Link</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: JSON Link (Schema)
---


# JSON Link `ogc.ogc-utils.json-link`

Web linking is used to express relationships between resources. The JSON object representation of links described here is used consistently in OGC API’s.

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

<aside class="success">
This building block is <strong>valid</strong>
</aside>


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: JSON Link
type: object
required:
- href
- rel
properties:
  href:
    type: string
    format: uri-reference
    x-jsonld-id: '@id'
  rel:
    type: string
  anchor:
    type: string
  type:
    type: string
  hreflang:
    type: string
  title:
    type: string
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#label
  length:
    type: integer
x-jsonld-prefixes:
  rdfs: http://www.w3.org/2000/01/rdf-schema#

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "href": "@id",
    "title": "rdfs:label"
  }
}
```

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/context.jsonld</a>

# References

* [IETF RFC 8288 - Web Linking](https://www.rfc-editor.org/rfc/rfc8288.txt)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path: `registereditems/ogc-utils/json-link`

