---
title: IRI or CURIE (Datatype)

language_tabs:
  - plaintext: Plain text
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

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

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;data=%22http%3A%2F%2Fwww.example.org%2Froles%2FmyRoles%3Fparam%3Dvalue%23fragment%22">View on JSON Viewer</a></p>
</blockquote>



```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/context.jsonld",
  "@graph": "http://www.example.org/roles/myRoles?param=value#fragment"
}
```

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%22https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fogc-utils%2Firi-or-curie%2Fcontext.jsonld%22%2C%0A++%22%40graph%22%3A+%22http%3A%2F%2Fwww.example.org%2Froles%2FmyRoles%3Fparam%3Dvalue%23fragment%22%0A%7D">View on JSON-LD Playground</a></p>
</blockquote>



```turtle


```


## Example ISBN URN


```plaintext
urn:isbn:9780387359731
```


```json
"urn:isbn:9780387359731"
```

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;data=%22urn%3Aisbn%3A9780387359731%22">View on JSON Viewer</a></p>
</blockquote>



```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/context.jsonld",
  "@graph": "urn:isbn:9780387359731"
}
```

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%22https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fogc-utils%2Firi-or-curie%2Fcontext.jsonld%22%2C%0A++%22%40graph%22%3A+%22urn%3Aisbn%3A9780387359731%22%0A%7D">View on JSON-LD Playground</a></p>
</blockquote>



```turtle


```


## Example Dublin Core CURIE


```plaintext
dc:creator
```


```json
"dc:creator"
```

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;data=%22dc%3Acreator%22">View on JSON Viewer</a></p>
</blockquote>



```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/context.jsonld",
  "@graph": "dc:creator"
}
```

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%22https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fogc-utils%2Firi-or-curie%2Fcontext.jsonld%22%2C%0A++%22%40graph%22%3A+%22dc%3Acreator%22%0A%7D">View on JSON-LD Playground</a></p>
</blockquote>



```turtle


```


## Example local part


```plaintext
relative-ref
```


```json
"relative-ref"
```

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;data=%22relative-ref%22">View on JSON Viewer</a></p>
</blockquote>



```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/context.jsonld",
  "@graph": "relative-ref"
}
```

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%22https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fogc-utils%2Firi-or-curie%2Fcontext.jsonld%22%2C%0A++%22%40graph%22%3A+%22relative-ref%22%0A%7D">View on JSON-LD Playground</a></p>
</blockquote>



```turtle


```


## Example local part (fragment only)


```plaintext
#same-document-ref
```


```json
"#same-document-ref"
```

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;data=%22%23same-document-ref%22">View on JSON Viewer</a></p>
</blockquote>



```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/context.jsonld",
  "@graph": "#same-document-ref"
}
```

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%22https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fogc-utils%2Firi-or-curie%2Fcontext.jsonld%22%2C%0A++%22%40graph%22%3A+%22%23same-document-ref%22%0A%7D">View on JSON-LD Playground</a></p>
</blockquote>



```turtle


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

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;data=%5B%0A++%22urn%3Aisbn%3A9780387359731%22%2C%0A++%22http%3A%2F%2Fwww.example.org%2Froles%2FmyRoles%3Fparam%3Dvalue%23fragment%22%2C%0A++%22%23same-document-ref%22%2C%0A++%22another-document%23ref%22%0A%5D%0A">View on JSON Viewer</a></p>
</blockquote>



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

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%22https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fogc-utils%2Firi-or-curie%2Fcontext.jsonld%22%2C%0A++%22%40graph%22%3A+%5B%0A++++%22urn%3Aisbn%3A9780387359731%22%2C%0A++++%22http%3A%2F%2Fwww.example.org%2Froles%2FmyRoles%3Fparam%3Dvalue%23fragment%22%2C%0A++++%22%23same-document-ref%22%2C%0A++++%22another-document%23ref%22%0A++%5D%0A%7D">View on JSON-LD Playground</a></p>
</blockquote>



```turtle


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

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;data=%24schema%3A+https%3A%2F%2Fjson-schema.org%2Fdraft%2F2020-12%2Fschema%0Adescription%3A+IRI+or+CURIE%0A%24defs%3A%0A++IRI%3A%0A++++type%3A+string%0A++++pattern%3A+%5E%5Cw%2B%3A%28%5C%2F%3F%5C%2F%3F%29%5B%5E%5Cs%5D%2B%24%0A++CURIE%3A%0A++++type%3A+string%0A++++pattern%3A+%5E%5BA-Za-z_%5D%5B%5E%5Cs%3A%5D%2A%3A.%2A%24%0A++LocalPart%3A%0A++++type%3A+string%0A++++pattern%3A+%5E%5B%5E%3A%5D%2A%28%5C%3F.%2A%29%3F%28%23.%2A%29%3F%24%0A++Single%3A%0A++++anyOf%3A%0A++++-+%24ref%3A+%27%23%2F%24defs%2FIRI%27%0A++++-+%24ref%3A+%27%23%2F%24defs%2FCURIE%27%0A++++-+%24ref%3A+%27%23%2F%24defs%2FLocalPart%27%0A++Multiple%3A%0A++++oneOf%3A%0A++++-+%24ref%3A+%27%23%2F%24defs%2FSingle%27%0A++++-+type%3A+array%0A++++++items%3A%0A++++++++%24ref%3A+%27%23%2F%24defs%2FSingle%27%0A++MultipleOrObject%3A%0A++++oneOf%3A%0A++++-+%24ref%3A+%27%23%2F%24defs%2FMultiple%27%0A++++-+type%3A+object%0A++MultipleOrObjectOrNull%3A%0A++++oneOf%3A%0A++++-+%24ref%3A+%27%23%2F%24defs%2FMultipleOrObject%27%0A++++-+type%3A+%27null%27%0A%24ref%3A+%27%23%2F%24defs%2FSingle%27%0A">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%7B%0A++++%22%40version%22%3A+1.1%0A++%7D%0A%7D">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/context.jsonld</a>

# References

* [IETF RFC 3986 - Uniform Resource Identifiers (URI): Generic Syntax](https://www.ietf.org/rfc/rfc3986.txt)
* [IETF RFC 3987 - Internationalized Resource Identifiers (IRIs)](https://www.ietf.org/rfc/rfc3987.txt)
* [CURIE Syntax 1.0](https://www.w3.org/TR/curie/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path:
<code><a href="https://github.com/opengeospatial/bblocks/blob/HEAD/registereditems/ogc-utils/iri-or-curie" target="_blank">registereditems/ogc-utils/iri-or-curie</a></code>

