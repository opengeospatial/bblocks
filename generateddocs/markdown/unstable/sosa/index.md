
# Sensor, Observation, Sample, and Actuator (SOSA) (Api)

`ogc.unstable.sosa` *v1.0*

The SOSA (Sensor, Observation, Sample, and Actuator) ontology  is a realisation of the Observations, Measurements and Sampling (OMS) Conceptual model

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Description

Building Blocks for implementing the core classes of the [Observations and Measurements model]

Each class is implemented using a schema is tied to the equivalent semantic description using the SOSA (Sensor, Observation, Sample, and Actuator) ontology.

An [aggregate schema](schema.yaml) is provided allowing any of these elements to be combined in a single payload, or each class may be used independently using the relevant schema.

TBD: Convenience API paths may be defined to support traversal of relationships - such as inverse relationships `hasResult`/`isResultOf` , `hasSample`/`isSampleOf` etc. where only one property is present in the data and the inverse is not otherwise accessible.

## Schema

```yaml
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
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasSample: http://www.w3.org/ns/sosa/hasSample
    Observation: http://www.w3.org/ns/sosa/Observation
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    detects: http://www.w3.org/ns/ssn/detects
    implements: http://www.w3.org/ns/ssn/implements
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasResult: http://www.w3.org/ns/sosa/hasResult
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasInput: http://www.w3.org/ns/ssn/hasInput
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hosts: http://www.w3.org/ns/sosa/hosts
    observes: http://www.w3.org/ns/sosa/observes
    hasMember: http://www.w3.org/ns/sosa/hasMember
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    resultTime: http://www.w3.org/ns/sosa/resultTime
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
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasSample: http://www.w3.org/ns/sosa/hasSample
    Observation: http://www.w3.org/ns/sosa/Observation
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    features: http://www.w3.org/ns/sosa/hasMember
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    detects: http://www.w3.org/ns/ssn/detects
    implements: http://www.w3.org/ns/ssn/implements
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasResult: http://www.w3.org/ns/sosa/hasResult
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasInput: http://www.w3.org/ns/ssn/hasInput
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hosts: http://www.w3.org/ns/sosa/hosts
    observes: http://www.w3.org/ns/sosa/observes
    hasMember: http://www.w3.org/ns/sosa/hasMember
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
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
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasSample: http://www.w3.org/ns/sosa/hasSample
    Observation: http://www.w3.org/ns/sosa/Observation
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    features: http://www.w3.org/ns/sosa/hasMember
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    detects: http://www.w3.org/ns/ssn/detects
    implements: http://www.w3.org/ns/ssn/implements
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasResult: http://www.w3.org/ns/sosa/hasResult
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    hasInput: http://www.w3.org/ns/ssn/hasInput
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hosts: http://www.w3.org/ns/sosa/hosts
    observes: http://www.w3.org/ns/sosa/observes
    hasMember: http://www.w3.org/ns/sosa/hasMember
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/schema.yaml)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources`
