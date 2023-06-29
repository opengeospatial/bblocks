---
title: Sensor, Observation, Sample, and Actuator (SOSA) (Api)

toc_footers:
  - Version 1.0
  - <a href='#'>Sensor, Observation, Sample, and Actuator (SOSA)</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Sensor, Observation, Sample, and Actuator (SOSA) (Api)
---


# Sensor, Observation, Sample, and Actuator (SOSA) `ogc.unstable.sosa`

The SOSA (Sensor, Observation, Sample, and Actuator) ontology  is a realisation of the Observations, Measurements and Sampling (OMS) Conceptual model

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

<aside class="success">
This building block is <strong>valid</strong>
</aside>

# Description

Building Blocks for implementing the core classes of the [Observations and Measurements model]

Each class is implemented using a schema is tied to the equivalent semantic description using the SOSA (Sensor, Observation, Sample, and Actuator) ontology.

An [aggregate schema](schema.yaml) is provided allowing any of these elements to be combined in a single payload, or each class may be used independently using the relevant schema.

TBD: Convenience API paths may be defined to support traversal of relationships - such as inverse relationships `hasResult`/`isResultOf` , `hasSample`/`isSampleOf` etc. where only one property is present in the data and the inverse is not otherwise accessible.


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: Sensor, Observation, Sample, and Actuator (SOSA)
anyOf:
- $schema: https://json-schema.org/draft/2020-12/schema
  description: Example SOSA Vector Observation
  allOf:
  - $ref: properties/observation/schema.yaml
  - type: object
    properties:
      hasResult:
        properties:
          pose:
            $ref: ../../geo/geopose/basic-ypr/schema.yaml
          distance:
            type: number
            x-jsonld-id: http://example.com/properties/distance
            x-jsonld-type: http://www.w3.org/2001/XMLSchema#float
    required:
    - hasResult
    not:
      required:
      - hasSimpleResult
- $schema: https://json-schema.org/draft/2020-12/schema
  description: Example SOSA Vector Observation
  allOf:
  - $ref: features/observation/schema.yaml
  - type: object
    properties:
      properties:
        $ref: examples/vectorObservation/schema.yaml
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA Observation Feature
  type: object
  allOf:
  - $ref: ../../geo/json-fg/feature/schema.yaml
  - type: object
    properties:
      properties:
        $ref: properties/observation/schema.yaml
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
  x-jsonld-extra-terms:
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    implements: http://www.w3.org/ns/ssn/implements
    observes: http://www.w3.org/ns/sosa/observes
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    detects: http://www.w3.org/ns/ssn/detects
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasSample: http://www.w3.org/ns/sosa/hasSample
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hosts: http://www.w3.org/ns/sosa/hosts
    hasMember: http://www.w3.org/ns/sosa/hasMember
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    Observation: http://www.w3.org/ns/sosa/Observation
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA Observation Feature
  allOf:
  - $ref: ../../geo/json-fg/featureCollection/schema.yaml
  - type: object
    properties:
      properties:
        $ref: properties/observationCollection/schema.yaml
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
  x-jsonld-extra-terms:
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    implements: http://www.w3.org/ns/ssn/implements
    observes: http://www.w3.org/ns/sosa/observes
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    detects: http://www.w3.org/ns/ssn/detects
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasSample: http://www.w3.org/ns/sosa/hasSample
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hosts: http://www.w3.org/ns/sosa/hosts
    hasMember: http://www.w3.org/ns/sosa/hasMember
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    Observation: http://www.w3.org/ns/sosa/Observation
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA Observation
  type: object
  properties:
    resultTime:
      type: string
      format: date-time
      x-jsonld-id: http://www.w3.org/ns/sosa/resultTime
    phenomenonTime:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/phenomenonTime
    hasFeatureOfInterest:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
      x-jsonld-type: '@id'
    observedProperty:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
    usedProcedure:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
      x-jsonld-type: '@id'
    madeBySensor:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
      x-jsonld-type: '@id'
    hasResult:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasResult
    hasSimpleResult:
      x-jsonld-id: http://www.w3.org/ns/sosa/hasSimpleResult
  oneOf:
  - required:
    - hasResult
  - required:
    - hasSimpleResult
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
  x-jsonld-extra-terms:
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    implements: http://www.w3.org/ns/ssn/implements
    observes: http://www.w3.org/ns/sosa/observes
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    detects: http://www.w3.org/ns/ssn/detects
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasSample: http://www.w3.org/ns/sosa/hasSample
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hosts: http://www.w3.org/ns/sosa/hosts
    hasMember: http://www.w3.org/ns/sosa/hasMember
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    Observation: http://www.w3.org/ns/sosa/Observation
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA ObservationCollection
  type: object
  properties:
    resultTime:
      type: string
      format: date-time
      x-jsonld-id: http://www.w3.org/ns/sosa/resultTime
    phenomenonTime:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/phenomenonTime
    hasFeatureOfInterest:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
      x-jsonld-type: '@id'
    observedProperty:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
    usedProcedure:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
      x-jsonld-type: '@id'
    madeBySensor:
      type:
      - object
      - string
      x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
      x-jsonld-type: '@id'
    hasMember:
      type: array
      items:
        oneOf:
        - $ref: properties/observation/schema.yaml
        - type: string
      minItems: 1
      x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
  required:
  - hasMember
  not:
    anyOf:
    - required:
      - hasResult
    - required:
      - hasSimpleResult
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
  x-jsonld-extra-terms:
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    implements: http://www.w3.org/ns/ssn/implements
    observes: http://www.w3.org/ns/sosa/observes
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    detects: http://www.w3.org/ns/ssn/detects
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasSample: http://www.w3.org/ns/sosa/hasSample
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hosts: http://www.w3.org/ns/sosa/hosts
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    Observation: http://www.w3.org/ns/sosa/Observation
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/schema.json</a>


# JSON-LD Context

```json--ldContext
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
    "hasResult": "http://www.w3.org/ns/sosa/hasResult",
    "hasSimpleResult": "http://www.w3.org/ns/sosa/hasSimpleResult",
    "madeObservation": "sosa:madeObservation",
    "isHostedBy": "sosa:isHostedBy",
    "implements": "ssn:implements",
    "observes": "sosa:observes",
    "hasInput": "ssn:hasInput",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "isProxyFor": "ssn:isProxyFor",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "Sample": "sosa:Sample",
    "madeActuation": "sosa:madeActuation",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "isActedOnBy": "sosa:isActedOnBy",
    "madeSampling": "sosa:madeSampling",
    "hasDeployment": "ssn:hasDeployment",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "detects": "ssn:detects",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "inCondition": "ssn-system:inCondition",
    "deployedSystem": "ssn:deployedSystem",
    "hasSample": "sosa:hasSample",
    "madeByActuator": "sosa:madeByActuator",
    "hosts": "sosa:hosts",
    "hasMember": "http://www.w3.org/ns/sosa/hasMember",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasProperty": "ssn:hasProperty",
    "inDeployment": "ssn:inDeployment",
    "isResultOf": "sosa:isResultOf",
    "Observation": "sosa:Observation",
    "isObservedBy": "sosa:isObservedBy",
    "implementedBy": "ssn:implementedBy",
    "madeBySampler": "sosa:madeBySampler",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "forProperty": "ssn:forProperty",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasSubSystem": "ssn:hasSubSystem",
    "isSampleOf": "sosa:isSampleOf",
    "hasOutput": "ssn:hasOutput",
    "actsOnProperty": "sosa:actsOnProperty",
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
    "latitude": "geo:lat",
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
    "GeometryCollection": "geojson:GeometryCollection",
    "features": "geojson:features",
    "FeatureCollection": "geojson:FeatureCollection",
    "MultiLineString": "geojson:MultiLineString",
    "Polygon": "geojson:Polygon",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Feature": "geojson:Feature",
    "MultiPoint": "geojson:MultiPoint",
    "LineString": "geojson:LineString",
    "links": "rdfs:seeAlso"
  }
}
```

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources`

