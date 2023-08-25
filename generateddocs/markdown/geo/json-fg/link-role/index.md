
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
@prefix dcterms: <http://purl.org/dc/terms/> .

<http://example.org/http/example.org/frog> dcterms:role <http://example.org/animals> .


```

## Schema

```yaml
description: annotated link with role and conformance
$defs:
  coderef:
    $ref: ../../../ogc-utils/iri-or-curie/schema.yaml
  coderefs:
    $ref: ../../../ogc-utils/iri-or-curie/schema.yaml#/$defs/MultipleOrObjectOrNull
allOf:
- $ref: ../../../ogc-utils/json-link/schema.yaml
- properties:
    role:
      $ref: '#/$defs/coderef'
      x-jsonld-id: http://purl.org/dc/terms/role
      x-jsonld-type: '@id'
    conformsTo:
      $ref: '#/$defs/coderefs'
      x-jsonld-id: http://purl.org/dc/terms/conformsTo
      x-jsonld-type: '@id'
      x-jsonld-container: '@nest'
  required:
  - role
x-jsonld-prefixes:
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/link-role/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/link-role/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "href": "@id",
    "title": "rdfs:label",
    "role": {
      "@id": "dct:role",
      "@type": "@id"
    },
    "conformsTo": {
      "@id": "dct:conformsTo",
      "@type": "@id",
      "@container": "@nest"
    },
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
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

