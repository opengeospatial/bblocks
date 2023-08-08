---
title: IRI or CURIE (Datatype)

language_tabs:
  - plaintext: Plain text
  - json: JSON

toc_footers:
  - Version 1.0
  - <a href='#'>IRI or CURIE</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: IRI or CURIE (Datatype)
---


# IRI or CURIE `ogc.ogc-utils.iri-or-curie`

This Building Block defines a data type for a full IRI/URI or a CURIE (with or without a prefix)

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/stable" target="_blank" data-rainbow-uri>Stable</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/ogc-utils/iri-or-curie/" target="_blank">valid</a></strong>
</aside>

# Description

A Uniform Resource Identifier (URI) is defined in [RFC3986](https://www.ietf.org/rfc/rfc3986.txt) as a
sequence of characters chosen from a limited subset of the repertoire
of US-ASCII ASCII characters.

A CURIE ("Compact URI") is a data type whose purpose is specifically to allow for the definition
of scoped names that map to URIs.

The "IRI-or-CURIE" building block defines a data type representing either an IRI or a CURIE (with or without a prefix).
# Examples

## Example HTTP URI

```plaintext
http://www.example.org/roles/myRoles?param=value#fragment
```

```json
"http://www.example.org/roles/myRoles?param=value#fragment"
```


## Example ISBN URN

```plaintext
urn:isbn:9780387359731
```

```json
"urn:isbn:9780387359731"
```


## Example Dublin Core CURIE

```plaintext
dc:creator
```

```json
"dc:creator"
```


## Example local part

```plaintext
relative-ref
```

```json
"relative-ref"
```


## Example local part (fragment only)

```plaintext
#same-document-ref
```

```json
"#same-document-ref"
```


## Multiple IRIs or CURIEs

```plaintext
urn:isbn:9780387359731
http://www.example.org/roles/myRoles?param=value#fragment
#same-document-ref
another-document#ref

```

```json
[
  "urn:isbn:9780387359731",
  "http://www.example.org/roles/myRoles?param=value#fragment",
  "#same-document-ref",
  "another-document#ref"
]

```


# JSON Schema

```yaml--schema
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

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.json</a>

# References

* [W3C RFC 3986 - Uniform Resource Identifiers (URI): Generic Syntax](https://www.ietf.org/rfc/rfc3986.txt)
* [W3C RFC 3987 - Internationalized Resource Identifiers (IRIs)](https://www.ietf.org/rfc/rfc3987.txt)
* [CURIE Syntax 1.0](https://www.w3.org/TR/curie/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path: `registereditems/ogc-utils/iri-or-curie`

