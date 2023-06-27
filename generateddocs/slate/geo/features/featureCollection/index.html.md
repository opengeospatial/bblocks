---
title: Feature Collection (Schema)

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

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

<aside class="success">
This building block is <strong>valid</strong>
</aside>


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
      $ref: ../feature/schema.yaml
      x-jsonld-id: https://purl.org/geojson/vocab#features
x-jsonld-prefixes:
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  geojson: https://purl.org/geojson/vocab#

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
    "links": "rdfs:seeAlso",
    "type": "@type",
    "id": "@id",
    "properties": "geojson:properties",
    "geometry": {
      "@context": {
        "type": "@type",
        "coordinates": "geojson:coordinates"
      },
      "@id": "geojson:geometry"
    },
    "bbox": "geojson:bbox",
    "MultiPoint": "geojson:MultiPoint",
    "Polygon": "geojson:Polygon",
    "GeometryCollection": "geojson:GeometryCollection",
    "Point": "geojson:Point",
    "Feature": "geojson:Feature",
    "MultiPolygon": "geojson:MultiPolygon",
    "MultiLineString": "geojson:MultiLineString",
    "LineString": "geojson:LineString",
    "FeatureCollection": "geojson:FeatureCollection",
    "features": "geojson:features"
  }
}
```

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/context.jsonld</a>

# References

* [OGC API - Features, Part 1, 7.14.2: Feature Collection Response](https://docs.ogc.org/is/17-069r3/17-069r3.html#_response_5)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path: `registereditems/geo/features/featureCollection`

