
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
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "inDeployment": "ssn:inDeployment",
    "implementedBy": "ssn:implementedBy",
    "actsOnProperty": "sosa:actsOnProperty",
    "deployedSystem": "ssn:deployedSystem",
    "Sample": "sosa:Sample",
    "madeObservation": "sosa:madeObservation",
    "isProxyFor": "ssn:isProxyFor",
    "madeByActuator": "sosa:madeByActuator",
    "forProperty": "ssn:forProperty",
    "isHostedBy": "sosa:isHostedBy",
    "hasOutput": "ssn:hasOutput",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hosts": "sosa:hosts",
    "hasSample": "sosa:hasSample",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "madeActuation": "sosa:madeActuation",
    "hasMember": "sosa:hasMember",
    "Observation": "sosa:Observation",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "observes": "sosa:observes",
    "madeSampling": "sosa:madeSampling",
    "detects": "ssn:detects",
    "hasDeployment": "ssn:hasDeployment",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "madeBySampler": "sosa:madeBySampler",
    "isObservedBy": "sosa:isObservedBy",
    "isSampleOf": "sosa:isSampleOf",
    "implements": "ssn:implements",
    "hasInput": "ssn:hasInput",
    "hasSubSystem": "ssn:hasSubSystem",
    "isResultOf": "sosa:isResultOf",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasProperty": "ssn:hasProperty",
    "inCondition": "ssn-system:inCondition",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
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
    "height": "geopose:height",
    "longitude": "geo:long",
    "rotations": "geopose:rotations",
    "latitude": "geo:lat"
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

