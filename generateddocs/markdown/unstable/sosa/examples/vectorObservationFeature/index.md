
# Example SOSA Vector Observation Feature (Schema)

`ogc.unstable.sosa.examples.vectorObservationFeature` *v1.0*

This building block defines an example SOSA Observation Feature for a Vector Observation

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Examples

### Example 1
#### json
```json
{
  "type": "Feature",
   "geometry": {
    "type": "LineString",
    "coordinates": [
      [
      -111.67183507997295,
      40.056709946862874
      ],
      [ 
      -111.67183507997295,
      40.056709946862874
      ]
    ]
  },
  "time": null,
  "place": null,
  "properties": {
    "hasFeatureOfInterest": "eg:Traverse-P1-P2",
    "resultTime": "2023-05-22T16:41:00+2",
    "hasResult": {
      "pose": {
        "position": {
          "lat": -111.67183507997295,
          "lon": 40.056709946862874,
          "h": 0.5
        },
        "angles": {
          "yaw": 15.35,
          "pitch": -0.01,
          "roll": 0
        }
      },
      "distance": 6889234.2
    }
  }
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Example SOSA Vector Observation
allOf:
- $ref: ../../features/observation/schema.yaml
- type: object
  properties:
    properties:
      $ref: ../vectorObservation/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "http://www.w3.org/ns/ssn/systems/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
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
    "features": "geojson:features",
    "links": "rdfs:seeAlso",
    "resultTime": "sosa:resultTime",
    "phenomenonTime": "sosa:phenomenonTime",
    "hasFeatureOfInterest": {
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": "sosa:observedProperty",
    "usedProcedure": {
      "@id": "sosa:usedProcedure",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "sosa:madeBySensor",
      "@type": "@id"
    },
    "hasResult": {
      "@id": "sosa:hasResult",
      "@context": {
        "distance": {
          "@id": "http://example.com/properties/distance",
          "@type": "http://www.w3.org/2001/XMLSchema#float"
        }
      }
    },
    "hasSimpleResult": "sosa:hasSimpleResult",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "madeSampling": "sosa:madeSampling",
    "isResultOf": "sosa:isResultOf",
    "implementedBy": "ssn:implementedBy",
    "inDeployment": "ssn:inDeployment",
    "madeBySampler": "sosa:madeBySampler",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "detects": "ssn:detects",
    "hasInput": "ssn:hasInput",
    "forProperty": "ssn:forProperty",
    "madeObservation": "sosa:madeObservation",
    "implements": "ssn:implements",
    "hasDeployment": "ssn:hasDeployment",
    "observes": "sosa:observes",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "isSampleOf": "sosa:isSampleOf",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSubSystem": "ssn:hasSubSystem",
    "isObservedBy": "sosa:isObservedBy",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "isProxyFor": "ssn:isProxyFor",
    "isPropertyOf": "ssn:isPropertyOf",
    "madeActuation": "sosa:madeActuation",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasSample": "sosa:hasSample",
    "hasMember": "sosa:hasMember",
    "Observation": "sosa:Observation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "Sample": "sosa:Sample",
    "inCondition": "ssn-system:inCondition",
    "hasProperty": "ssn:hasProperty",
    "madeByActuator": "sosa:madeByActuator",
    "hasOutput": "ssn:hasOutput",
    "isHostedBy": "sosa:isHostedBy",
    "hosts": "sosa:hosts",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "actsOnProperty": "sosa:actsOnProperty",
    "deployedSystem": "ssn:deployedSystem",
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "position": "geopose:position",
    "angles": "geopose:angles",
    "yaw": "geopose:yaw",
    "pitch": "geopose:pitch",
    "roll": "geopose:roll",
    "lat": "geopose:lat",
    "lon": "geopose:lon",
    "h": "geopose:h",
    "rotations": "geopose:rotations",
    "height": "geopose:height",
    "latitude": "geo:lat",
    "longitude": "geo:long"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/examples/vectorObservationFeature`

