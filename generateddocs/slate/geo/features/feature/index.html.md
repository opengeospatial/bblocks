---
title: Feature (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>Feature</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Feature (Schema)
---


# Feature `ogc.geo.features.feature`

A feature. Every feature is a sub-resource of an OGC Collection.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/stable" target="_blank" data-rainbow-uri>Stable</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/geo/features/feature/" target="_blank">valid</a></strong>
</aside>

# Description

A feature is an abstraction of real world phenomena [ISO 19101-1:2014].

The GeoJSON representation is the currently recommended representation that all APIs should support, where GeoJSON can
be used for the data.

Each GeoJSON feature includes the following JSON members:

* `type`: fixed value "Feature".
* `geometry`: the primary geometry of the feature describing its location as a GeoJSON geometry object. `null`, if the
  feature has no spatial geometry.
* `properties`: an object with a member for each feature property.
# Examples

## Example



```json
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
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/features/feature/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Ffeatures%2Ffeature%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
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
  },
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/features/feature/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Ffeatures%2Ffeature%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://www.example.com/features/f1> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.747502e+02 -3.693074e+01 ) ] .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/features/feature/example_1_1.ttl">Open in new window</a>
</blockquote>


Minimal example of this schema.

NB. uses a local @context in the data example where application specialisations would apply such mappings.


# JSON Schema

```yaml--schema
allOf:
- $ref: ../../common/data_types/geojson/schema.yaml
- type: object
  properties:
    links:
      type: array
      items:
        $ref: ../../../ogc-utils/json-link/schema.yaml
      x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
    type:
      const: Feature
  required:
  - type
  - geometry
  - properties
x-jsonld-extra-terms:
  properties: '@nest'
x-jsonld-prefixes:
  rdfs: http://www.w3.org/2000/01/rdf-schema#

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Ffeatures%2Ffeature%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "type": "@type",
    "id": "@id",
    "properties": "@nest",
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
    "links": {
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
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Ffeatures%2Ffeature%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/context.jsonld</a>

# References

* [OGC API - Features, Part 1, 7.16.2: Feature Response](https://docs.ogc.org/is/17-069r3/17-069r3.html#_response_7)
* [ISO 19101-1:2014 - Geographic information - Reference model - Part 1: Fundamentals](https://www.iso.org/standard/59164.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path:
<code><a href="https://github.com/opengeospatial/bblocks/blob/HEAD/registereditems/geo/features/feature" target="_blank">registereditems/geo/features/feature</a></code>

