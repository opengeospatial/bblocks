
# Feature (Schema)

`ogc.geo.features.feature` *v1.0*

A feature. Every feature is a sub-resource of an OGC Collection.

[*Status*](http://www.opengis.net/def/status): Stable

## Description

A feature is an abstraction of real world phenomena [ISO 19101-1:2014].

The GeoJSON representation is the currently recommended representation that all APIs should support, where GeoJSON can
be used for the data.

Each GeoJSON feature includes the following JSON members:

* `type`: fixed value "Feature".
* `geometry`: the primary geometry of the feature describing its location as a GeoJSON geometry object. `null`, if the
  feature has no spatial geometry.
* `properties`: an object with a member for each feature property.
## Examples

### Example
Minimal example of this schema.

NB. uses a local @context in the data example where application specialisations would apply such mappings.
#### json
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

#### jsonld
```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/context.jsonld",
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

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://www.example.com/features/f1> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.747502e+02 -3.693074e+01 ) ] .


```

## Schema

```yaml
allOf:
- $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/geojson/schema.yaml
- type: object
  properties:
    bbox:
      $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/data_types/bounding_box/schema.yaml
    links:
      type: array
      items:
        $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml
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

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
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
    "type": "@type",
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        },
        "geometries": {}
      },
      "@id": "geojson:geometry"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
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
        "anchor": {},
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

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/context.jsonld)

## Sources

* [OGC API - Features, Part 1, 7.16.2: Feature Response](https://docs.ogc.org/is/17-069r3/17-069r3.html#_response_7)
* [ISO 19101-1:2014 - Geographic information - Reference model - Part 1: Fundamentals](https://www.iso.org/standard/59164.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/geo/features/feature`

