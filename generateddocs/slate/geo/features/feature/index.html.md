---
title: Feature (Schema)

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
This building block is <strong>valid</strong>
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
x-jsonld-prefixes:
  rdfs: http://www.w3.org/2000/01/rdf-schema#

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;data=allOf%3A%0A-+%24ref%3A+..%2F..%2Fcommon%2Fdata_types%2Fgeojson%2Fschema.yaml%0A-+type%3A+object%0A++properties%3A%0A++++links%3A%0A++++++type%3A+array%0A++++++items%3A%0A++++++++%24ref%3A+..%2F..%2F..%2Fogc-utils%2Fjson-link%2Fschema.yaml%0A++++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23seeAlso%0A++++type%3A%0A++++++const%3A+Feature%0A++required%3A%0A++-+type%0A++-+geometry%0A++-+properties%0Ax-jsonld-prefixes%3A%0A++rdfs%3A+http%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%0A">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "type": "@type",
    "id": "@id",
    "properties": "geojson:properties",
    "geometry": {
      "@id": "geojson:geometry",
      "@context": {
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        }
      }
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
      "@id": "rdfs:seeAlso",
      "@context": {
        "href": "@id",
        "title": "rdfs:label"
      }
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%7B%0A++++%22type%22%3A+%22%40type%22%2C%0A++++%22id%22%3A+%22%40id%22%2C%0A++++%22properties%22%3A+%22geojson%3Aproperties%22%2C%0A++++%22geometry%22%3A+%7B%0A++++++%22%40id%22%3A+%22geojson%3Ageometry%22%2C%0A++++++%22%40context%22%3A+%7B%0A++++++++%22coordinates%22%3A+%7B%0A++++++++++%22%40container%22%3A+%22%40list%22%2C%0A++++++++++%22%40id%22%3A+%22geojson%3Acoordinates%22%0A++++++++%7D%0A++++++%7D%0A++++%7D%2C%0A++++%22bbox%22%3A+%7B%0A++++++%22%40container%22%3A+%22%40list%22%2C%0A++++++%22%40id%22%3A+%22geojson%3Abbox%22%0A++++%7D%2C%0A++++%22Feature%22%3A+%22geojson%3AFeature%22%2C%0A++++%22FeatureCollection%22%3A+%22geojson%3AFeatureCollection%22%2C%0A++++%22GeometryCollection%22%3A+%22geojson%3AGeometryCollection%22%2C%0A++++%22LineString%22%3A+%22geojson%3ALineString%22%2C%0A++++%22MultiLineString%22%3A+%22geojson%3AMultiLineString%22%2C%0A++++%22MultiPoint%22%3A+%22geojson%3AMultiPoint%22%2C%0A++++%22MultiPolygon%22%3A+%22geojson%3AMultiPolygon%22%2C%0A++++%22Point%22%3A+%22geojson%3APoint%22%2C%0A++++%22Polygon%22%3A+%22geojson%3APolygon%22%2C%0A++++%22features%22%3A+%7B%0A++++++%22%40container%22%3A+%22%40set%22%2C%0A++++++%22%40id%22%3A+%22geojson%3Afeatures%22%0A++++%7D%2C%0A++++%22links%22%3A+%7B%0A++++++%22%40id%22%3A+%22rdfs%3AseeAlso%22%2C%0A++++++%22%40context%22%3A+%7B%0A++++++++%22href%22%3A+%22%40id%22%2C%0A++++++++%22title%22%3A+%22rdfs%3Alabel%22%0A++++++%7D%0A++++%7D%2C%0A++++%22geojson%22%3A+%22https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23%22%2C%0A++++%22rdfs%22%3A+%22http%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%22%2C%0A++++%22%40version%22%3A+1.1%0A++%7D%0A%7D">View on JSON-LD Playground</a>

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

