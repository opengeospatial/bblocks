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

Building Blocks for implementing the core classes of the []Observations and Measurements model]

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
  x-jsonld-extra-terms: {}
- $schema: https://json-schema.org/draft/2020-12/schema
  description: Example SOSA Vector Observation
  allOf:
  - $ref: features/observation/schema.yaml
  - type: object
    properties:
      properties:
        $ref: examples/vectorObservation/schema.yaml
  x-jsonld-extra-terms: {}
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
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hosts: http://www.w3.org/ns/sosa/hosts
    hasResult: http://www.w3.org/ns/sosa/hasResult
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    Sample: http://www.w3.org/ns/sosa/Sample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    observes: http://www.w3.org/ns/sosa/observes
    hasSample: http://www.w3.org/ns/sosa/hasSample
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasMember: http://www.w3.org/ns/sosa/hasMember
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    Observation: http://www.w3.org/ns/sosa/Observation
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    detects: http://www.w3.org/ns/ssn/detects
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    implements: http://www.w3.org/ns/ssn/implements
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
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hosts: http://www.w3.org/ns/sosa/hosts
    hasResult: http://www.w3.org/ns/sosa/hasResult
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    Sample: http://www.w3.org/ns/sosa/Sample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    observes: http://www.w3.org/ns/sosa/observes
    hasSample: http://www.w3.org/ns/sosa/hasSample
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasMember: http://www.w3.org/ns/sosa/hasMember
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    Observation: http://www.w3.org/ns/sosa/Observation
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    detects: http://www.w3.org/ns/ssn/detects
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    implements: http://www.w3.org/ns/ssn/implements
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
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hosts: http://www.w3.org/ns/sosa/hosts
    hasResult: http://www.w3.org/ns/sosa/hasResult
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    Sample: http://www.w3.org/ns/sosa/Sample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    observes: http://www.w3.org/ns/sosa/observes
    hasSample: http://www.w3.org/ns/sosa/hasSample
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasMember: http://www.w3.org/ns/sosa/hasMember
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    Observation: http://www.w3.org/ns/sosa/Observation
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    detects: http://www.w3.org/ns/ssn/detects
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    implements: http://www.w3.org/ns/ssn/implements
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
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hosts: http://www.w3.org/ns/sosa/hosts
    hasResult: http://www.w3.org/ns/sosa/hasResult
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    forProperty: http://www.w3.org/ns/ssn/forProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    Sample: http://www.w3.org/ns/sosa/Sample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    observes: http://www.w3.org/ns/sosa/observes
    hasSample: http://www.w3.org/ns/sosa/hasSample
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasInput: http://www.w3.org/ns/ssn/hasInput
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    Observation: http://www.w3.org/ns/sosa/Observation
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    detects: http://www.w3.org/ns/ssn/detects
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    implements: http://www.w3.org/ns/ssn/implements

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
    "isObservedBy": "sosa:isObservedBy",
    "hosts": "sosa:hosts",
    "deployedSystem": "ssn:deployedSystem",
    "isSampleOf": "sosa:isSampleOf",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "implementedBy": "ssn:implementedBy",
    "forProperty": "ssn:forProperty",
    "isResultOf": "sosa:isResultOf",
    "madeSampling": "sosa:madeSampling",
    "hasDeployment": "ssn:hasDeployment",
    "Sample": "sosa:Sample",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "observes": "sosa:observes",
    "hasSample": "sosa:hasSample",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasProperty": "ssn:hasProperty",
    "isPropertyOf": "ssn:isPropertyOf",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasInput": "ssn:hasInput",
    "hasMember": "http://www.w3.org/ns/sosa/hasMember",
    "actsOnProperty": "sosa:actsOnProperty",
    "hasSubSystem": "ssn:hasSubSystem",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "inCondition": "ssn-system:inCondition",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasOutput": "ssn:hasOutput",
    "madeObservation": "sosa:madeObservation",
    "Observation": "sosa:Observation",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "madeByActuator": "sosa:madeByActuator",
    "isHostedBy": "sosa:isHostedBy",
    "madeBySampler": "sosa:madeBySampler",
    "isProxyFor": "ssn:isProxyFor",
    "madeActuation": "sosa:madeActuation",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "detects": "ssn:detects",
    "inDeployment": "ssn:inDeployment",
    "implements": "ssn:implements",
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
    "longitude": "geo:long",
    "height": "geopose:height",
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
    "Polygon": "geojson:Polygon",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "Point": "geojson:Point",
    "FeatureCollection": "geojson:FeatureCollection",
    "MultiPolygon": "geojson:MultiPolygon",
    "features": "geojson:features",
    "GeometryCollection": "geojson:GeometryCollection",
    "MultiPoint": "geojson:MultiPoint",
    "Feature": "geojson:Feature",
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

