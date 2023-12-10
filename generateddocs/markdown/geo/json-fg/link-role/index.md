
# Link with role and target conformance (Schema)

`ogc.geo.json-fg.link-role` *v0.1*

A JSON-FG compliant web link with mandatory annotation of link role and optional conformance information to describe target resource. Compliant with profile resource descriptor model.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Example Topology object
See panel to right - note that a more user friendly "collapsable" version is in development. 
#### json
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

#### jsonld
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

#### ttl
```ttl
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prof: <http://www.w3.org/ns/dx/prof/> .

[] ns1:relation <http://www.iana.org/assignments/relation/related> ;
    prof:hasRole <http://example.org/animals> ;
    oa:hasTarget <http://example.org/http/example.org/frog> .


```

## Schema

```yaml
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

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/link-role/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/link-role/schema.yaml)


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

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/link-role/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/geo/json-fg/link-role`

