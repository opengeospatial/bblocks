
# Feature Collection (Schema)

`ogc.geo.features.featureCollection` *v1.0*

A collection of features.

[*Status*](http://www.opengis.net/def/status): Stable

## Examples

### Example
Minimal example of this schema.

NB. uses a local @context in the data example where application specialisations would apply such mappings.
#### json
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

#### jsonld
```jsonld
{
  "@context": [
    "http://blocks.ogc.org/annotated-schemas/geo/features/featureCollection/context.jsonld",
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

#### ttl
```ttl
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

## Schema

```yaml
allOf:
- $ref: https://geojson.org/schema/FeatureCollection.json
- type: object
  properties:
    links:
      type: array
      items:
        $ref: http://blocks.ogc.org/annotated-schemas/ogc-utils/json-link/schema.yaml
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
        $ref: http://blocks.ogc.org/annotated-schemas/geo/features/feature/schema.yaml
x-jsonld-extra-terms:
  properties: '@nest'
x-jsonld-prefixes:
  rdfs: http://www.w3.org/2000/01/rdf-schema#

```

Links to the schema:

* YAML version: [schema.yaml](http://blocks.ogc.org/annotated-schemas/geo/features/featureCollection/schema.json)
* JSON version: [schema.json](http://blocks.ogc.org/annotated-schemas/geo/features/featureCollection/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
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
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "geojson": "https://purl.org/geojson/vocab#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](http://blocks.ogc.org/annotated-schemas/geo/features/featureCollection/context.jsonld)

## Sources

* [OGC API - Features, Part 1, 7.14.2: Feature Collection Response](https://docs.ogc.org/is/17-069r3/17-069r3.html#_response_5)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/geo/features/featureCollection`

