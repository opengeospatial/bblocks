
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
x-jsonld-extra-terms: {}

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservation/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservation/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "http://www.w3.org/ns/ssn/systems/",
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
      "@context": {
        "distance": {
          "@id": "http://example.com/properties/distance",
          "@type": "http://www.w3.org/2001/XMLSchema#float"
        }
      }
    },
    "hasSimpleResult": "sosa:hasSimpleResult",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasDeployment": "ssn:hasDeployment",
    "isResultOf": "sosa:isResultOf",
    "madeSampling": "sosa:madeSampling",
    "implementedBy": "ssn:implementedBy",
    "observes": "sosa:observes",
    "hasSubSystem": "ssn:hasSubSystem",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "madeBySampler": "sosa:madeBySampler",
    "hasInput": "ssn:hasInput",
    "isActedOnBy": "sosa:isActedOnBy",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasProperty": "ssn:hasProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "isObservedBy": "sosa:isObservedBy",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "implements": "ssn:implements",
    "hosts": "sosa:hosts",
    "madeByActuator": "sosa:madeByActuator",
    "hasSample": "sosa:hasSample",
    "deployedSystem": "ssn:deployedSystem",
    "detects": "ssn:detects",
    "inDeployment": "ssn:inDeployment",
    "madeActuation": "sosa:madeActuation",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "actsOnProperty": "sosa:actsOnProperty",
    "hasOutput": "ssn:hasOutput",
    "madeObservation": "sosa:madeObservation",
    "forProperty": "ssn:forProperty",
    "isSampleOf": "sosa:isSampleOf",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasMember": "sosa:hasMember",
    "Observation": "sosa:Observation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "Sample": "sosa:Sample",
    "isProxyFor": "ssn:isProxyFor",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "inCondition": "ssn-system:inCondition",
    "isHostedBy": "sosa:isHostedBy",
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
    "latitude": "geo:lat",
    "height": "geopose:height",
    "longitude": "geo:long"
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

