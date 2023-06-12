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
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasMember: http://www.w3.org/ns/sosa/hasMember
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    resultTime: http://www.w3.org/ns/sosa/resultTime
    Observation: http://www.w3.org/ns/sosa/Observation
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSample: http://www.w3.org/ns/sosa/hasSample
    detects: http://www.w3.org/ns/ssn/detects
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasInput: http://www.w3.org/ns/ssn/hasInput
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    observes: http://www.w3.org/ns/sosa/observes
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    implements: http://www.w3.org/ns/ssn/implements
    Sample: http://www.w3.org/ns/sosa/Sample
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasResult: http://www.w3.org/ns/sosa/hasResult
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hosts: http://www.w3.org/ns/sosa/hosts
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
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
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasMember: http://www.w3.org/ns/sosa/hasMember
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    resultTime: http://www.w3.org/ns/sosa/resultTime
    Observation: http://www.w3.org/ns/sosa/Observation
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSample: http://www.w3.org/ns/sosa/hasSample
    detects: http://www.w3.org/ns/ssn/detects
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasInput: http://www.w3.org/ns/ssn/hasInput
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    observes: http://www.w3.org/ns/sosa/observes
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    implements: http://www.w3.org/ns/ssn/implements
    Sample: http://www.w3.org/ns/sosa/Sample
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasResult: http://www.w3.org/ns/sosa/hasResult
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hosts: http://www.w3.org/ns/sosa/hosts
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
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
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasMember: http://www.w3.org/ns/sosa/hasMember
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    Observation: http://www.w3.org/ns/sosa/Observation
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSample: http://www.w3.org/ns/sosa/hasSample
    detects: http://www.w3.org/ns/ssn/detects
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasInput: http://www.w3.org/ns/ssn/hasInput
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    observes: http://www.w3.org/ns/sosa/observes
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    implements: http://www.w3.org/ns/ssn/implements
    Sample: http://www.w3.org/ns/sosa/Sample
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasResult: http://www.w3.org/ns/sosa/hasResult
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hosts: http://www.w3.org/ns/sosa/hosts
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
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
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    Observation: http://www.w3.org/ns/sosa/Observation
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasSample: http://www.w3.org/ns/sosa/hasSample
    detects: http://www.w3.org/ns/ssn/detects
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    hasInput: http://www.w3.org/ns/ssn/hasInput
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    observes: http://www.w3.org/ns/sosa/observes
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    implements: http://www.w3.org/ns/ssn/implements
    Sample: http://www.w3.org/ns/sosa/Sample
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    hasResult: http://www.w3.org/ns/sosa/hasResult
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    hosts: http://www.w3.org/ns/sosa/hosts
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem

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
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasMember": "http://www.w3.org/ns/sosa/hasMember",
    "hasProperty": "ssn:hasProperty",
    "isObservedBy": "sosa:isObservedBy",
    "Observation": "sosa:Observation",
    "isSampleOf": "sosa:isSampleOf",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isPropertyOf": "ssn:isPropertyOf",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "forProperty": "ssn:forProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasSample": "sosa:hasSample",
    "detects": "ssn:detects",
    "inDeployment": "ssn:inDeployment",
    "madeByActuator": "sosa:madeByActuator",
    "hasOutput": "ssn:hasOutput",
    "isActedOnBy": "sosa:isActedOnBy",
    "actsOnProperty": "sosa:actsOnProperty",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasInput": "ssn:hasInput",
    "deployedSystem": "ssn:deployedSystem",
    "observes": "sosa:observes",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "implements": "ssn:implements",
    "Sample": "sosa:Sample",
    "hasDeployment": "ssn:hasDeployment",
    "madeSampling": "sosa:madeSampling",
    "madeObservation": "sosa:madeObservation",
    "inCondition": "ssn-system:inCondition",
    "implementedBy": "ssn:implementedBy",
    "madeBySampler": "sosa:madeBySampler",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "madeActuation": "sosa:madeActuation",
    "isResultOf": "sosa:isResultOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "isProxyFor": "ssn:isProxyFor",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "hosts": "sosa:hosts",
    "isHostedBy": "sosa:isHostedBy",
    "hasSubSystem": "ssn:hasSubSystem",
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
    "longitude": "geo:long",
    "height": "geopose:height",
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
    "Point": "geojson:Point",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "Feature": "geojson:Feature",
    "Polygon": "geojson:Polygon",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPolygon": "geojson:MultiPolygon",
    "MultiPoint": "geojson:MultiPoint",
    "features": "geojson:features",
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

