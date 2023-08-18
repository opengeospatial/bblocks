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

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/stable" target="_blank" data-rainbow-uri>Stable</a>
</p>

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

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;data=%24schema%3A+https%3A%2F%2Fjson-schema.org%2Fdraft%2F2020-12%2Fschema%0Adescription%3A+JSON+Link%0Atype%3A+object%0Arequired%3A%0A-+href%0A-+rel%0Aproperties%3A%0A++href%3A%0A++++type%3A+string%0A++++format%3A+uri-reference%0A++++x-jsonld-id%3A+%27%40id%27%0A++rel%3A%0A++++type%3A+string%0A++anchor%3A%0A++++type%3A+string%0A++type%3A%0A++++type%3A+string%0A++hreflang%3A%0A++++type%3A+string%0A++title%3A%0A++++type%3A+string%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23label%0A++length%3A%0A++++type%3A+integer%0Ax-jsonld-prefixes%3A%0A++rdfs%3A+http%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%0A">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "href": "@id",
    "title": "rdfs:label",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%7B%0A++++%22href%22%3A+%22%40id%22%2C%0A++++%22title%22%3A+%22rdfs%3Alabel%22%2C%0A++++%22rdfs%22%3A+%22http%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%22%2C%0A++++%22%40version%22%3A+1.1%0A++%7D%0A%7D">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/context.jsonld</a>

# References

* [IETF RFC 8288 - Web Linking](https://www.rfc-editor.org/rfc/rfc8288.txt)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path:
<code><a href="https://github.com/opengeospatial/bblocks/blob/HEAD/registereditems/ogc-utils/json-link" target="_blank">registereditems/ogc-utils/json-link</a></code>

