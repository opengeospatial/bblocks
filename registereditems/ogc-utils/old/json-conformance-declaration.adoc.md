Version: 1.0.1

# Description

An OGC Conformance Declaration is a JSON object that lists the
conformance classes from standards or community specifications,
identified by a URI, that the API conforms to.

Clients may but are not required to use this information. This resource
is intended to support "generic" clients that want to access multiple
implementations of OGC API standards - and not "just" a specific API /
server. For this purpose, the server can declare the conformance classes
it implements and conforms to.

[**Maturity**](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity):
Mature

# Pre-defined properties

| Property   | Type      | Description                                                                                                                                                                          |
| ---------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| conformsTo | \[ URI \] | **REQUIRED**. The list of URIs of all OGC API conformance classes that the API conforms to. Servers MAY add also URIs of conformance classes that have not been standardized by OGC. |

Properties

# Link relation types

This resource has no requirements or recommendations for outgoing links.

The following link relation types are commonly used in links to an OGC
Conformance Declaration:

<table>
<caption>Incoming link relation types</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Link relation type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>conformance</code></p></td>
<td><p>From any resource that provides information about the API, e.g. a <a href="landing-page.adoc">landing page</a>.</p>
<p>This link relation type will not be registered with IANA. It will in the future be superseded by the <code>http://www.opengis.net/def/rel/ogc/1.0/conformance</code> link relation type.</p></td>
</tr>
<tr class="even">
<td><p><code>http://www.opengis.net/def/rel/ogc/1.0/conformance</code></p></td>
<td><p>From any resource that provides information about the API, e.g. a <a href="landing-page.adoc">landing page</a>.</p>
<p>This link relation type will in the future supersede the <code>conformance</code> link relation type.</p></td>
</tr>
</tbody>
</table>

## Example

This example is for an API implementing OGC API - Features - Part 1:
Core and that supports OpenAPI 3.0 for the API definition and HTML and
GeoJSON as encodings for features.

``` JSON
{
  "conformsTo": [
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/core",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/oas30",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/html",
    "http://www.opengis.net/spec/ogcapi-features-1/1.0/conf/geojson"
  ]
}
```

## Media type

`application/json`

## Schema

``` YAML
type: object
required:
  - conformsTo
properties:
  conformsTo:
    type: array
    items:
      type: string
      format: uri
```

# Alternate Representation: HTML

An HTML representation should include all information that is part of
the JSON representation.

## Media type

`text/html`
