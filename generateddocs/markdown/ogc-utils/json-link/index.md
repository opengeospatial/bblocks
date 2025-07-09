
# JSON Link (Schema)

`ogc.ogc-utils.json-link` *v0.1*

Web linking is used to express relationships between resources. The JSON object representation of links described here is used consistently in OGC API’s.

[*Status*](http://www.opengis.net/def/status): Stable

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
    x-jsonld-type: '@id'
    x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
  rel:
    type: string
    x-jsonld-id: http://www.iana.org/assignments/relation
    x-jsonld-type: '@id'
    x-jsonld-base: http://www.iana.org/assignments/relation/
  anchor:
    type: string
  type:
    type: string
    x-jsonld-id: http://purl.org/dc/terms/type
  hreflang:
    type: string
    x-jsonld-id: http://purl.org/dc/terms/language
  title:
    type: string
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#label
  length:
    type: integer
    x-jsonld-id: http://purl.org/dc/terms/extent
x-jsonld-prefixes:
  oa: http://www.w3.org/ns/oa#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](http://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.json)
* JSON version: [schema.json](http://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "rel": {
      "@context": {
        "@base": "http://www.iana.org/assignments/relation/"
      },
      "@id": "http://www.iana.org/assignments/relation",
      "@type": "@id"
    },
    "type": "dct:type",
    "hreflang": "dct:language",
    "title": "rdfs:label",
    "length": "dct:extent",
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](http://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/context.jsonld)

## Sources

* [IETF RFC 8288 - Web Linking](https://www.rfc-editor.org/rfc/rfc8288.txt)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/ogc-utils/json-link`

