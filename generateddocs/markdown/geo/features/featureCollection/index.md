
# Feature Collection (Schema)

`ogc.geo.features.featureCollection` *v1.0*

A collection of features.

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

## Schema

```yaml
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
      x-jsonld-id: https://purl.org/geojson/vocab#features
x-jsonld-prefixes:
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  geojson: https://purl.org/geojson/vocab#

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
    "links": "http://www.w3.org/2000/01/rdf-schema#seeAlso",
    "features": "https://purl.org/geojson/vocab#features"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/context.jsonld)

## Sources

* [OGC API - Features, Part 1, 7.14.2: Feature Collection Response](https://docs.ogc.org/is/17-069r3/17-069r3.html#_response_5)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/geo/features/featureCollection`

