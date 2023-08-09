
# IRI or CURIE (Datatype)

`ogc.ogc-utils.iri-or-curie` *v1.0*

This Building Block defines a data type for a full IRI/URI or a CURIE (with or without a prefix)

[*Status*](http://www.opengis.net/def/status): Stable

## Description

A Uniform Resource Identifier (URI) is defined in [RFC3986](https://www.ietf.org/rfc/rfc3986.txt) as a
sequence of characters chosen from a limited subset of the repertoire
of US-ASCII ASCII characters.

A CURIE ("Compact URI") is a data type whose purpose is specifically to allow for the definition
of scoped names that map to URIs.

The "IRI-or-CURIE" building block defines a data type representing either an IRI or a CURIE (with or without a prefix).
## Examples

### Example HTTP URI
#### plaintext
```plaintext
http://www.example.org/roles/myRoles?param=value#fragment
```

#### json
```json
"http://www.example.org/roles/myRoles?param=value#fragment"
```

#### jsonld
```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/context.jsonld",
  "@graph": "http://www.example.org/roles/myRoles?param=value#fragment"
}
```

#### ttl
```ttl


```


### Example ISBN URN
#### plaintext
```plaintext
urn:isbn:9780387359731
```

#### json
```json
"urn:isbn:9780387359731"
```

#### jsonld
```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/context.jsonld",
  "@graph": "urn:isbn:9780387359731"
}
```

#### ttl
```ttl


```


### Example Dublin Core CURIE
#### plaintext
```plaintext
dc:creator
```

#### json
```json
"dc:creator"
```

#### jsonld
```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/context.jsonld",
  "@graph": "dc:creator"
}
```

#### ttl
```ttl


```


### Example local part
#### plaintext
```plaintext
relative-ref
```

#### json
```json
"relative-ref"
```

#### jsonld
```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/context.jsonld",
  "@graph": "relative-ref"
}
```

#### ttl
```ttl


```


### Example local part (fragment only)
#### plaintext
```plaintext
#same-document-ref
```

#### json
```json
"#same-document-ref"
```

#### jsonld
```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/context.jsonld",
  "@graph": "#same-document-ref"
}
```

#### ttl
```ttl


```


### Multiple IRIs or CURIEs
#### plaintext
```plaintext
urn:isbn:9780387359731
http://www.example.org/roles/myRoles?param=value#fragment
#same-document-ref
another-document#ref

```

#### json
```json
[
  "urn:isbn:9780387359731",
  "http://www.example.org/roles/myRoles?param=value#fragment",
  "#same-document-ref",
  "another-document#ref"
]

```

#### jsonld
```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/context.jsonld",
  "@graph": [
    "urn:isbn:9780387359731",
    "http://www.example.org/roles/myRoles?param=value#fragment",
    "#same-document-ref",
    "another-document#ref"
  ]
}
```

#### ttl
```ttl


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: IRI or CURIE
$defs:
  IRI:
    type: string
    pattern: ^\w+:(\/?\/?)[^\s]+$
  CURIE:
    type: string
    pattern: ^[A-Za-z_][^\s:]*:.*$
  LocalPart:
    type: string
    pattern: ^[^:]*(\?.*)?(#.*)?$
  Single:
    anyOf:
    - $ref: '#/$defs/IRI'
    - $ref: '#/$defs/CURIE'
    - $ref: '#/$defs/LocalPart'
  Multiple:
    oneOf:
    - $ref: '#/$defs/Single'
    - type: array
      items:
        $ref: '#/$defs/Single'
  MultipleOrObject:
    oneOf:
    - $ref: '#/$defs/Multiple'
    - type: object
  MultipleOrObjectOrNull:
    oneOf:
    - $ref: '#/$defs/MultipleOrObject'
    - type: 'null'
$ref: '#/$defs/Single'

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/context.jsonld)

## Sources

* [IETF RFC 3986 - Uniform Resource Identifiers (URI): Generic Syntax](https://www.ietf.org/rfc/rfc3986.txt)
* [IETF RFC 3987 - Internationalized Resource Identifiers (IRIs)](https://www.ietf.org/rfc/rfc3987.txt)
* [CURIE Syntax 1.0](https://www.w3.org/TR/curie/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/ogc-utils/iri-or-curie`

