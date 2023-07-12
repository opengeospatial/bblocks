
# Example SOSA Vector Observation (Schema)

`ogc.unstable.sosa.examples.vectorObservation` *v1.0*

This building block defines an example SOSA Vector Observation

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Examples

### Example 1
#### json
```json
{
  "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
  "resultTime": "2023-05-22T16:41:00+2",
  "hasResult": {
    "pose": {
      "position": {
        "lat": 43.46498208387333,
        "lon": -3.803638278687769,
        "h": 0.5
      },
      "angles": {
        "yaw": 5.553,
        "pitch": -0.92,
        "roll": 0.33
      }
    }
  }
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Example SOSA Vector Observation
allOf:
- $ref: ../../properties/observation/schema.yaml
- type: object
  properties:
    hasResult:
      properties:
        pose:
          $ref: ../../../../geo/geopose/basic-ypr/schema.yaml
        distance:
          type: number
          x-jsonld-id: http://example.com/properties/distance
          x-jsonld-type: http://www.w3.org/2001/XMLSchema#float
  required:
  - hasResult
  not:
    required:
    - hasSimpleResult

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservation/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservation/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "resultTime": "sosa:resultTime",
    "phenomenonTime": "sosa:phenomenonTime",
    "hasFeatureOfInterest": {
      "@id": "http://www.w3.org/ns/sosa/hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": "sosa:observedProperty",
    "usedProcedure": {
      "@id": "http://www.w3.org/ns/sosa/usedProcedure",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "http://www.w3.org/ns/sosa/madeBySensor",
      "@type": "@id"
    },
    "hasResult": "sosa:hasResult",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "inCondition": "ssn-system:inCondition",
    "hasProperty": "ssn:hasProperty",
    "madeObservation": "sosa:madeObservation",
    "isSampleOf": "sosa:isSampleOf",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasInput": "ssn:hasInput",
    "features": "sosa:hasMember",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "hasSample": "sosa:hasSample",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "isProxyFor": "ssn:isProxyFor",
    "forProperty": "ssn:forProperty",
    "inDeployment": "ssn:inDeployment",
    "madeByActuator": "sosa:madeByActuator",
    "isHostedBy": "sosa:isHostedBy",
    "isObservedBy": "sosa:isObservedBy",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "madeSampling": "sosa:madeSampling",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "actsOnProperty": "sosa:actsOnProperty",
    "detects": "ssn:detects",
    "Observation": "sosa:Observation",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "implements": "ssn:implements",
    "hasOutput": "ssn:hasOutput",
    "deployedSystem": "ssn:deployedSystem",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "Sample": "sosa:Sample",
    "hasDeployment": "ssn:hasDeployment",
    "hasMember": "sosa:hasMember",
    "isResultOf": "sosa:isResultOf",
    "madeActuation": "sosa:madeActuation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "madeBySampler": "sosa:madeBySampler",
    "hasSubSystem": "ssn:hasSubSystem",
    "observes": "sosa:observes",
    "implementedBy": "ssn:implementedBy",
    "hosts": "sosa:hosts",
    "isActedOnBy": "sosa:isActedOnBy",
    "position": {
      "@id": "http://example.com/geopose/position",
      "@context": {
        "lat": "geopose:lat",
        "lon": "geopose:lon",
        "h": "geopose:h"
      }
    },
    "angles": {
      "@id": "http://example.com/geopose/angles",
      "@context": {
        "yaw": "geopose:yaw",
        "pitch": "geopose:pitch",
        "roll": "geopose:roll"
      }
    },
    "height": "geopose:height",
    "rotations": "geopose:rotations",
    "latitude": "geo:lat",
    "longitude": "geo:long",
    "distance": {
      "@id": "http://example.com/properties/distance",
      "@type": "http://www.w3.org/2001/XMLSchema#float"
    }
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservation/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/examples/vectorObservation`

