---
title: Example SOSA Vector Observation (Schema)


toc_footers:
  - Version 1.0
  - <a href='#'>Example SOSA Vector Observation</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Example SOSA Vector Observation (Schema)
---


# Example SOSA Vector Observation `ogc.unstable.sosa.examples.vectorObservation`

This building block defines an example SOSA Vector Observation

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/unstable/sosa/examples/vectorObservation/" target="_blank">valid</a></strong>
</aside>

# Examples

## Example 1

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


# JSON Schema

```yaml--schema
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

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservation/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservation/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservation/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservation/schema.json</a>


# JSON-LD Context

```json--ldContext
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
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasProperty": "ssn:hasProperty",
    "forProperty": "ssn:forProperty",
    "madeBySampler": "sosa:madeBySampler",
    "hasDeployment": "ssn:hasDeployment",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasSample": "sosa:hasSample",
    "hasInput": "ssn:hasInput",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "madeObservation": "sosa:madeObservation",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "observes": "sosa:observes",
    "inCondition": "ssn-system:inCondition",
    "isProxyFor": "ssn:isProxyFor",
    "isHostedBy": "sosa:isHostedBy",
    "isResultOf": "sosa:isResultOf",
    "madeSampling": "sosa:madeSampling",
    "deployedSystem": "ssn:deployedSystem",
    "hosts": "sosa:hosts",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "isActedOnBy": "sosa:isActedOnBy",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasOutput": "ssn:hasOutput",
    "isObservedBy": "sosa:isObservedBy",
    "isSampleOf": "sosa:isSampleOf",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "madeActuation": "sosa:madeActuation",
    "Observation": "sosa:Observation",
    "hasMember": "sosa:hasMember",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "madeByActuator": "sosa:madeByActuator",
    "inDeployment": "ssn:inDeployment",
    "detects": "ssn:detects",
    "actsOnProperty": "sosa:actsOnProperty",
    "implements": "ssn:implements",
    "features": "sosa:hasMember",
    "implementedBy": "ssn:implementedBy",
    "hasSubSystem": "ssn:hasSubSystem",
    "Sample": "sosa:Sample",
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
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservation/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservation/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/examples/vectorObservation`

