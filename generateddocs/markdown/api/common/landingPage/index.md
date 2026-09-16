
# Landing Page schema (Schema)

`ogc.api.common.landingPage` *v0.1*

Alias of the OGC API - Common Landing Page schema, published in the OGC API Common building blocks register.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

This block is an alias of the [Landing Page schema](bblocks://ogc.api.common.part1.schemas.landingPage)
defined in the OGC API - Common building blocks register. It exists so that other blocks in this
register can depend on it directly, without importing the OGC API - Common register themselves.

## Examples

### Example landing page
#### json
```json
{
  "title": "Example API Landing Page",
  "description": "This is an example of an API landing page in JSON format",
  "attribution": "<a href='www.ign.es' rel=' '>IGN</a> <a href='www.govdata.de/dl-de/by-2-0'>(c)</a>",
  "links": [
    {
      "rel": "service-desc",
      "type": "application/json",
      "title": "API definition for this endpoint as JSON",
      "href": "http://www.example.com/oapi-c/api?f=application/json"
    },
    {
      "rel": "service-desc",
      "type": "text/html",
      "title": "API definition for this endpoint as HTML",
      "href": "http://www.example.com/oapi-c/api?f=text/html"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/data-meta",
      "type": "application/xml",
      "title": "ISO 19115 Metadata as XML",
      "href": "http://www.example.com/oapi-c/data-meta?f=application/xml"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/conformance",
      "type": "application/json",
      "title": "Conformance Declaration as JSON",
      "href": "http://www.example.com/oapi-c/conformance?f=application/json"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/conformance",
      "type": "application/xml",
      "title": "Conformance Declaration as XML",
      "href": "http://www.example.com/oapi-c/conformance?f=application/xml"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/conformance",
      "type": "text/html",
      "title": "Conformance Declaration as HTML",
      "href": "http://www.example.com/oapi-c/conformance?f=text/html"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/data",
      "type": "application/json",
      "title": "Collections Metadata as JSON",
      "href": "http://www.example.com/oapi-c/collections?f=application/json"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/data",
      "type": "application/xml",
      "title": "Collections Metadata as XML",
      "href": "http://www.example.com/oapi-c/collections?f=application/xml"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/data",
      "type": "text/html",
      "title": "Collections Metadata as HTML",
      "href": "http://www.example.com/oapi-c/collections?f=text/html"
    },
    {
      "rel": "self",
      "type": "application/json",
      "title": "This Document",
      "href": "http://www.example.com/oapi-c?f=application/json"
    },
    {
      "rel": "alternate",
      "type": "application/xml",
      "title": "This Document as XML",
      "href": "http://www.example.com/oapi-c?f=application/xml"
    },
    {
      "rel": "alternate",
      "type": "text/html",
      "title": "This Document as HTML",
      "href": "http://www.example.com/oapi-c?f=text/html"
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/api/common/landingPage/context.jsonld",
  "title": "Example API Landing Page",
  "description": "This is an example of an API landing page in JSON format",
  "attribution": "<a href='www.ign.es' rel=' '>IGN</a> <a href='www.govdata.de/dl-de/by-2-0'>(c)</a>",
  "links": [
    {
      "rel": "service-desc",
      "type": "application/json",
      "title": "API definition for this endpoint as JSON",
      "href": "http://www.example.com/oapi-c/api?f=application/json"
    },
    {
      "rel": "service-desc",
      "type": "text/html",
      "title": "API definition for this endpoint as HTML",
      "href": "http://www.example.com/oapi-c/api?f=text/html"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/data-meta",
      "type": "application/xml",
      "title": "ISO 19115 Metadata as XML",
      "href": "http://www.example.com/oapi-c/data-meta?f=application/xml"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/conformance",
      "type": "application/json",
      "title": "Conformance Declaration as JSON",
      "href": "http://www.example.com/oapi-c/conformance?f=application/json"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/conformance",
      "type": "application/xml",
      "title": "Conformance Declaration as XML",
      "href": "http://www.example.com/oapi-c/conformance?f=application/xml"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/conformance",
      "type": "text/html",
      "title": "Conformance Declaration as HTML",
      "href": "http://www.example.com/oapi-c/conformance?f=text/html"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/data",
      "type": "application/json",
      "title": "Collections Metadata as JSON",
      "href": "http://www.example.com/oapi-c/collections?f=application/json"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/data",
      "type": "application/xml",
      "title": "Collections Metadata as XML",
      "href": "http://www.example.com/oapi-c/collections?f=application/xml"
    },
    {
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/data",
      "type": "text/html",
      "title": "Collections Metadata as HTML",
      "href": "http://www.example.com/oapi-c/collections?f=text/html"
    },
    {
      "rel": "self",
      "type": "application/json",
      "title": "This Document",
      "href": "http://www.example.com/oapi-c?f=application/json"
    },
    {
      "rel": "alternate",
      "type": "application/xml",
      "title": "This Document as XML",
      "href": "http://www.example.com/oapi-c?f=application/xml"
    },
    {
      "rel": "alternate",
      "type": "text/html",
      "title": "This Document as HTML",
      "href": "http://www.example.com/oapi-c?f=text/html"
    }
  ]
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .

[] dct:description "This is an example of an API landing page in JSON format" ;
    dct:title "Example API Landing Page" .


```

## Schema

```yaml
$ref: https://ogcincubator.github.io/bblocks-ogcapi-common/build/annotated/api/common/part1/schemas/landingPage/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/api/common/landingPage/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/api/common/landingPage/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "title": "dct:title",
    "description": "dct:description",
    "dct": "http://purl.org/dc/terms/",
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/api/common/landingPage/context.jsonld)

## Sources

* [OGC API - Common - Part 1: Core](https://docs.ogc.org/is/19-072/19-072.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/api/common/landingPage`

