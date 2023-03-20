Version: 1.0.1

# Description

The OGC API Landing Page provides links to important resources in the
API, as a JSON object. All other OGC API resources are sub-resources of
this resource.

The landing page will typically also include essential metadata about
the API, for example, a title and a description.

[**Maturity**](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity):
Mature

# Pre-defined properties

| Property    | Type                    | Description                                                                                                                               |
| ----------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| title       | string                  | The name of the API.                                                                                                                      |
| description | string                  | A free-text description of the API. The content may include Markdown and HTML markup.                                                     |
| links       | \[ [Link](link.adoc) \] | **REQUIRED**. Links to other resources. See [Link relation types](#link-relations) for typical link relations included in a landing page. |

Properties

# Link relation types

The following link relation types are commonly used in links from an OGC
Collection:

<table>
<caption>Outgoing link relation types</caption>
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
<td><p><code>service-desc</code></p></td>
<td><p><strong>REQUIRED</strong>. Identifies a service description for the API that is primarily intended for consumption by machines. Typically an OpenAPI definition.</p></td>
</tr>
<tr class="even">
<td><p><code>service-doc</code></p></td>
<td><p><strong>REQUIRED</strong>. Identifies a service documentation for the API that is primarily intended for human consumption. Typically HTML pages derived from an OpenAPI definition.</p></td>
</tr>
<tr class="odd">
<td><p><code>conformance</code></p></td>
<td><p><strong>REQUIRED</strong>. Refers to a <a href="conformance-declaration.adoc">conformance declaration</a> resource that identifies the specifications that the API conforms to.</p>
<p>This link relation type will not be registered with IANA. It will in the future be superseded by the <code>http://www.opengis.net/def/rel/ogc/1.0/conformance</code> link relation type.</p></td>
</tr>
<tr class="even">
<td><p><code>http://www.opengis.net/def/rel/ogc/1.0/conformance</code></p></td>
<td><p><strong>RECOMMENDED</strong>. Refers to a <a href="conformance-declaration.adoc">conformance declaration</a> resource that identifies the specifications that the API conforms to.</p>
<p>This link relation type will in the future supersede the <code>conformance</code> link relation type, so it is recommended to already include this link.</p></td>
</tr>
<tr class="odd">
<td><p><code>data</code></p></td>
<td><p><strong>CONDITIONAL</strong>. Refers to a <a href="../../../geo/common/resources/collections.adoc">OGC Collections</a> resource that represents the root resource of the distributions of a dataset.</p>
<p>This link relation type will not be registered with IANA. It will in the future be superseded by the <code>http://www.opengis.net/def/rel/ogc/1.0/data</code> link relation type.</p></td>
</tr>
<tr class="even">
<td><p><code>http://www.opengis.net/def/rel/ogc/1.0/data</code></p></td>
<td><p>Refers to a <a href="../../../geo/common/resources/collections.adoc">OGC Collections</a> resource that represents the root resource of the distributions of a dataset.</p>
<p>This link relation type will in the future supersede the <code>data</code> link relation type, so it is recommended to already include this link.</p></td>
</tr>
<tr class="odd">
<td><p><code>self</code></p></td>
<td><p><strong>STRONGLY RECOMMENDED</strong>. Link to the resource in the current representation.</p></td>
</tr>
<tr class="even">
<td><p><code>alternate</code></p></td>
<td><p><strong>STRONGLY RECOMMENDED</strong>. Link to the resource in every other media type supported by the server.</p></td>
</tr>
</tbody>
</table>

The following link relation types may be useful in links to an OGC API
Landing Page:

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
<td><p><code>home</code></p></td>
<td><p>From sub-resources or external resources.</p>
<p>The link relation type is not yet registered with IANA. It is proposed in an Internet Draft <a href="https://datatracker.ietf.org/doc/html/draft-nottingham-json-home-06">Home Documents for HTTP APIs</a>.</p></td>
</tr>
</tbody>
</table>

## Example

``` JSON
{
  "title": "Buildings in Bonn",
  "description": "Access to data about buildings in the city of Bonn via a Web API that conforms to the OGC API Features specification.",
  "links": [
    { "href": "http://data.example.org/",
      "rel": "self", "type": "application/json", "title": "this document" },
    { "href": "http://data.example.org/?f=html",
      "rel": "alternate", "type": "text/html", "title": "this document as HTML" },
    { "href": "http://data.example.org/api.json",
      "rel": "service-desc", "type": "application/vnd.oai.openapi+json;version=3.0", "title": "the API definition" },
    { "href": "http://data.example.org/api.html",
      "rel": "service-doc", "type": "text/html", "title": "the API documentation" },
    { "href": "http://data.example.org/conformance",
      "rel": "conformance", "title": "OGC API conformance classes implemented by this server" },
    { "href": "http://data.example.org/conformance",
      "rel": "http://www.opengis.nte/def/rel/ogc/1.0/conformance", "title": "OGC API conformance classes implemented by this server" },
    { "href": "http://data.example.org/collections",
      "rel": "data", "type": "application/json", "title": "Information about the collections in the dataset" },
    { "href": "http://data.example.org/collections",
      "rel": "http://www.opengis.nte/def/rel/ogc/1.0/data", "type": "application/json", "title": "Information about the collections in the dataset" }
  ]
}
```

## Media type

`application/json`

## Schema

``` YAML
Unresolved directive in json-landing-page.adoc - include::schemas/landing-page.yaml[]
```

# Alternate Representation: HTML

Providing an HTML representation is recommended so that the resource can
be displayed in a web browser and indexed by search engines.

The HTML representation should include all information that is part of
the JSON representation.

## Media type

`text/html`
