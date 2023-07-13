
# JSON Link (Schema)

`ogc.ogc-utils.json-link` *v0.1*

Web linking is used to express relationships between resources. The JSON object representation of links described here is used consistently in OGC API’s.

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

## Schema

```yaml
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

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "href": "@id",
    "title": "rdfs:label",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/context.jsonld)

## Sources

* [IETF RFC 8288 - Web Linking](https://www.rfc-editor.org/rfc/rfc8288.txt)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/ogc-utils/json-link`

