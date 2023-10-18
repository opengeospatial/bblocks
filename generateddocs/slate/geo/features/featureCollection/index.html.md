---
title: Feature Collection (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>Feature Collection</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Feature Collection (Schema)
---


# Feature Collection `ogc.geo.features.featureCollection`

A collection of features.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/stable" target="_blank" data-rainbow-uri>Stable</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/geo/features/featureCollection/" target="_blank">valid</a></strong>
</aside>

# Examples

## Example

Minimal example of this schema.

NB. uses a local @context in the data example where application specialisations would apply such mappings.



```json
{
  "@context": {
    "my": "http://my.org/featureTypes/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "name": "skos:prefLabel"
  },
  "id": "MyFeatureCollection",
  "name": "MyFeatureCollection",
  "type": "FeatureCollection",
  "features": [
    {
      "id": "f1",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          174.7501603083,
          -36.9307359096
        ]
      },
      "properties": {
        "comment": "An attribute value"
      }
    }
  ]
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/features/featureCollection/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Ffeatures%2FfeatureCollection%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "@context": [
    "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/context.jsonld",
    {
      "my": "http://my.org/featureTypes/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "name": "skos:prefLabel"
    }
  ],
  "id": "MyFeatureCollection",
  "name": "MyFeatureCollection",
  "type": "FeatureCollection",
  "features": [
    {
      "id": "f1",
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          174.7501603083,
          -36.9307359096
        ]
      },
      "properties": {
        "comment": "An attribute value"
      }
    }
  ]
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/features/featureCollection/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Ffeatures%2FfeatureCollection%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://www.example.com/features/MyFeatureCollection> a geojson:FeatureCollection ;
    skos:prefLabel "MyFeatureCollection" ;
    geojson:features <http://www.example.com/features/f1> .

<http://www.example.com/features/f1> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.747502e+02 -3.693074e+01 ) ] .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/features/featureCollection/example_1_1.ttl">Open in new window</a>
</blockquote>



# JSON Schema

```yaml--schema
allOf:
- $ref: https://geojson.org/schema/FeatureCollection.json
- type: object
  properties:
    links:
      type: array
      items:
        $ref: ../../../ogc-utils/json-link/schema.yaml
      x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
    timeStamp:
      type: string
      format: date-time
    numberMatched:
      type: integer
      minimum: 0
    numberReturned:
      type: integer
      minimum: 0
    features:
      type: array
      items:
        $ref: ../feature/schema.yaml
x-jsonld-extra-terms:
  properties: '@nest'
x-jsonld-prefixes:
  rdfs: http://www.w3.org/2000/01/rdf-schema#

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Ffeatures%2FfeatureCollection%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "properties": "@nest",
    "links": {
      "@context": {
        "href": "oa:hasTarget",
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
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "type": "@type",
    "id": "@id",
    "geometry": {
      "@context": {
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        }
      },
      "@id": "geojson:geometry"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "features": {
      "@container": "@set",
      "@id": "geojson:features"
    },
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "geojson": "https://purl.org/geojson/vocab#",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Ffeatures%2FfeatureCollection%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/context.jsonld</a>

# References

* [OGC API - Features, Part 1, 7.14.2: Feature Collection Response](https://docs.ogc.org/is/17-069r3/17-069r3.html#_response_5)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path:
<code><a href="https://github.com/opengeospatial/bblocks/blob/HEAD/registereditems/geo/features/featureCollection" target="_blank">registereditems/geo/features/featureCollection</a></code>

