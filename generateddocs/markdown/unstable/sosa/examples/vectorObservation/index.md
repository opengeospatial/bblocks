
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
    "resultTime": "http://www.w3.org/ns/sosa/resultTime",
    "phenomenonTime": "http://www.w3.org/ns/sosa/phenomenonTime",
    "hasFeatureOfInterest": {
      "@id": "http://www.w3.org/ns/sosa/hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": "http://www.w3.org/ns/sosa/observedProperty",
    "usedProcedure": {
      "@id": "http://www.w3.org/ns/sosa/usedProcedure",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "http://www.w3.org/ns/sosa/madeBySensor",
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
    "hasSimpleResult": "http://www.w3.org/ns/sosa/hasSimpleResult",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "isHostedBy": "sosa:isHostedBy",
    "inDeployment": "ssn:inDeployment",
    "hasInput": "ssn:hasInput",
    "implementedBy": "ssn:implementedBy",
    "hosts": "sosa:hosts",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "features": "sosa:hasMember",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "detects": "ssn:detects",
    "madeByActuator": "sosa:madeByActuator",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "Sample": "sosa:Sample",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "Observation": "sosa:Observation",
    "implements": "ssn:implements",
    "madeActuation": "sosa:madeActuation",
    "hasOutput": "ssn:hasOutput",
    "actsOnProperty": "sosa:actsOnProperty",
    "isObservedBy": "sosa:isObservedBy",
    "isSampleOf": "sosa:isSampleOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasMember": "sosa:hasMember",
    "isActedOnBy": "sosa:isActedOnBy",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "forProperty": "ssn:forProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "observes": "sosa:observes",
    "isProxyFor": "ssn:isProxyFor",
    "hasDeployment": "ssn:hasDeployment",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasSample": "sosa:hasSample",
    "inCondition": "ssn-system:inCondition",
    "isResultOf": "sosa:isResultOf",
    "madeSampling": "sosa:madeSampling",
    "madeBySampler": "sosa:madeBySampler",
    "hasSubSystem": "ssn:hasSubSystem",
    "deployedSystem": "ssn:deployedSystem",
    "madeObservation": "sosa:madeObservation",
    "hasProperty": "ssn:hasProperty",
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "position": "http://example.com/geopose/position",
    "angles": "http://example.com/geopose/angles",
    "yaw": "http://example.com/geopose/yaw",
    "pitch": "http://example.com/geopose/pitch",
    "roll": "http://example.com/geopose/roll",
    "lat": "http://example.com/geopose/lat",
    "lon": "http://example.com/geopose/lon",
    "h": "http://example.com/geopose/h",
    "longitude": "geo:long",
    "latitude": "geo:lat",
    "height": "geopose:height",
    "rotations": "geopose:rotations"
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

