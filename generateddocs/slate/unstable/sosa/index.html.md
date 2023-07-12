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
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    forProperty: http://www.w3.org/ns/ssn/forProperty
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasInput: http://www.w3.org/ns/ssn/hasInput
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    observes: http://www.w3.org/ns/sosa/observes
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hosts: http://www.w3.org/ns/sosa/hosts
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasResult: http://www.w3.org/ns/sosa/hasResult
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    Observation: http://www.w3.org/ns/sosa/Observation
    hasMember: http://www.w3.org/ns/sosa/hasMember
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    detects: http://www.w3.org/ns/ssn/detects
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    implements: http://www.w3.org/ns/ssn/implements
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    features: http://www.w3.org/ns/sosa/hasMember
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    Sample: http://www.w3.org/ns/sosa/Sample
- $schema: https://json-schema.org/draft/2020-12/schema
  description: SOSA Observation Feature
  allOf:
  - $ref: ../../geo/json-fg/featureCollection/schema.yaml
  - type: object
    properties:
      properties:
        $ref: properties/observationCollection/schema.yaml
      features:
        type: array
        items:
          oneOf:
          - $ref: features/observation/schema.yaml
          - type: string
        x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
  x-jsonld-prefixes:
    sosa: http://www.w3.org/ns/sosa/
    ssn: http://www.w3.org/ns/ssn/
    ssn-system: http://www.w3.org/ns/ssn/systems/
  x-jsonld-extra-terms:
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    forProperty: http://www.w3.org/ns/ssn/forProperty
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasInput: http://www.w3.org/ns/ssn/hasInput
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    observes: http://www.w3.org/ns/sosa/observes
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hosts: http://www.w3.org/ns/sosa/hosts
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasResult: http://www.w3.org/ns/sosa/hasResult
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    Observation: http://www.w3.org/ns/sosa/Observation
    hasMember: http://www.w3.org/ns/sosa/hasMember
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    detects: http://www.w3.org/ns/ssn/detects
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    implements: http://www.w3.org/ns/ssn/implements
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    Sample: http://www.w3.org/ns/sosa/Sample
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
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    forProperty: http://www.w3.org/ns/ssn/forProperty
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    observes: http://www.w3.org/ns/sosa/observes
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hosts: http://www.w3.org/ns/sosa/hosts
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasResult: http://www.w3.org/ns/sosa/hasResult
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    Observation: http://www.w3.org/ns/sosa/Observation
    hasMember: http://www.w3.org/ns/sosa/hasMember
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    detects: http://www.w3.org/ns/ssn/detects
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    implements: http://www.w3.org/ns/ssn/implements
    features: http://www.w3.org/ns/sosa/hasMember
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    Sample: http://www.w3.org/ns/sosa/Sample
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
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    forProperty: http://www.w3.org/ns/ssn/forProperty
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    observes: http://www.w3.org/ns/sosa/observes
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hosts: http://www.w3.org/ns/sosa/hosts
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasResult: http://www.w3.org/ns/sosa/hasResult
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    Observation: http://www.w3.org/ns/sosa/Observation
    hasMember: http://www.w3.org/ns/sosa/hasMember
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    detects: http://www.w3.org/ns/ssn/detects
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    implements: http://www.w3.org/ns/ssn/implements
    features: http://www.w3.org/ns/sosa/hasMember
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    Sample: http://www.w3.org/ns/sosa/Sample

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/schema.json</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources`

