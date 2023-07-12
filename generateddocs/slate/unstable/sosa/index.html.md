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
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    detects: http://www.w3.org/ns/ssn/detects
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    features: http://www.w3.org/ns/sosa/hasMember
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    hasResult: http://www.w3.org/ns/sosa/hasResult
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    observes: http://www.w3.org/ns/sosa/observes
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasMember: http://www.w3.org/ns/sosa/hasMember
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hosts: http://www.w3.org/ns/sosa/hosts
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    hasSample: http://www.w3.org/ns/sosa/hasSample
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    Sample: http://www.w3.org/ns/sosa/Sample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    implements: http://www.w3.org/ns/ssn/implements
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    forProperty: http://www.w3.org/ns/ssn/forProperty
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasInput: http://www.w3.org/ns/ssn/hasInput
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
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    detects: http://www.w3.org/ns/ssn/detects
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    hasResult: http://www.w3.org/ns/sosa/hasResult
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    observes: http://www.w3.org/ns/sosa/observes
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasMember: http://www.w3.org/ns/sosa/hasMember
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hosts: http://www.w3.org/ns/sosa/hosts
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    hasSample: http://www.w3.org/ns/sosa/hasSample
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    Sample: http://www.w3.org/ns/sosa/Sample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    implements: http://www.w3.org/ns/ssn/implements
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    forProperty: http://www.w3.org/ns/ssn/forProperty
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasInput: http://www.w3.org/ns/ssn/hasInput
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
    detects: http://www.w3.org/ns/ssn/detects
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    features: http://www.w3.org/ns/sosa/hasMember
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasResult: http://www.w3.org/ns/sosa/hasResult
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    observes: http://www.w3.org/ns/sosa/observes
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasMember: http://www.w3.org/ns/sosa/hasMember
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hosts: http://www.w3.org/ns/sosa/hosts
    hasSample: http://www.w3.org/ns/sosa/hasSample
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    Sample: http://www.w3.org/ns/sosa/Sample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    implements: http://www.w3.org/ns/ssn/implements
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasInput: http://www.w3.org/ns/ssn/hasInput
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
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    detects: http://www.w3.org/ns/ssn/detects
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    features: http://www.w3.org/ns/sosa/hasMember
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasResult: http://www.w3.org/ns/sosa/hasResult
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    observes: http://www.w3.org/ns/sosa/observes
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasMember: http://www.w3.org/ns/sosa/hasMember
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hosts: http://www.w3.org/ns/sosa/hosts
    hasSample: http://www.w3.org/ns/sosa/hasSample
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    Sample: http://www.w3.org/ns/sosa/Sample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    implements: http://www.w3.org/ns/ssn/implements
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasInput: http://www.w3.org/ns/ssn/hasInput

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

