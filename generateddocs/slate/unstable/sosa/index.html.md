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
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    hasInput: http://www.w3.org/ns/ssn/hasInput
    features: http://www.w3.org/ns/sosa/hasMember
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    detects: http://www.w3.org/ns/ssn/detects
    Observation: http://www.w3.org/ns/sosa/Observation
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    implements: http://www.w3.org/ns/ssn/implements
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    Sample: http://www.w3.org/ns/sosa/Sample
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasMember: http://www.w3.org/ns/sosa/hasMember
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    observes: http://www.w3.org/ns/sosa/observes
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hosts: http://www.w3.org/ns/sosa/hosts
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
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
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    hasInput: http://www.w3.org/ns/ssn/hasInput
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    detects: http://www.w3.org/ns/ssn/detects
    Observation: http://www.w3.org/ns/sosa/Observation
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    implements: http://www.w3.org/ns/ssn/implements
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    Sample: http://www.w3.org/ns/sosa/Sample
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasMember: http://www.w3.org/ns/sosa/hasMember
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    observes: http://www.w3.org/ns/sosa/observes
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hosts: http://www.w3.org/ns/sosa/hosts
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
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
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasInput: http://www.w3.org/ns/ssn/hasInput
    features: http://www.w3.org/ns/sosa/hasMember
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    detects: http://www.w3.org/ns/ssn/detects
    Observation: http://www.w3.org/ns/sosa/Observation
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    implements: http://www.w3.org/ns/ssn/implements
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    Sample: http://www.w3.org/ns/sosa/Sample
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    observes: http://www.w3.org/ns/sosa/observes
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hosts: http://www.w3.org/ns/sosa/hosts
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
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
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasInput: http://www.w3.org/ns/ssn/hasInput
    features: http://www.w3.org/ns/sosa/hasMember
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    detects: http://www.w3.org/ns/ssn/detects
    Observation: http://www.w3.org/ns/sosa/Observation
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    implements: http://www.w3.org/ns/ssn/implements
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    Sample: http://www.w3.org/ns/sosa/Sample
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    observes: http://www.w3.org/ns/sosa/observes
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hosts: http://www.w3.org/ns/sosa/hosts
    hasResult: http://www.w3.org/ns/sosa/hasResult
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy

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

