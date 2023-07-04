
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
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    resultTime: http://www.w3.org/ns/sosa/resultTime
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasInput: http://www.w3.org/ns/ssn/hasInput
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hosts: http://www.w3.org/ns/sosa/hosts
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    features: http://www.w3.org/ns/sosa/hasMember
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    detects: http://www.w3.org/ns/ssn/detects
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    Sample: http://www.w3.org/ns/sosa/Sample
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    Observation: http://www.w3.org/ns/sosa/Observation
    implements: http://www.w3.org/ns/ssn/implements
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    observes: http://www.w3.org/ns/sosa/observes
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasResult: http://www.w3.org/ns/sosa/hasResult
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
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
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    resultTime: http://www.w3.org/ns/sosa/resultTime
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasInput: http://www.w3.org/ns/ssn/hasInput
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hosts: http://www.w3.org/ns/sosa/hosts
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    detects: http://www.w3.org/ns/ssn/detects
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    Sample: http://www.w3.org/ns/sosa/Sample
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    Observation: http://www.w3.org/ns/sosa/Observation
    implements: http://www.w3.org/ns/ssn/implements
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    observes: http://www.w3.org/ns/sosa/observes
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasResult: http://www.w3.org/ns/sosa/hasResult
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
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
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasInput: http://www.w3.org/ns/ssn/hasInput
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hosts: http://www.w3.org/ns/sosa/hosts
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    features: http://www.w3.org/ns/sosa/hasMember
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    detects: http://www.w3.org/ns/ssn/detects
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    Sample: http://www.w3.org/ns/sosa/Sample
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    Observation: http://www.w3.org/ns/sosa/Observation
    implements: http://www.w3.org/ns/ssn/implements
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    observes: http://www.w3.org/ns/sosa/observes
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasResult: http://www.w3.org/ns/sosa/hasResult
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
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
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    hasInput: http://www.w3.org/ns/ssn/hasInput
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hosts: http://www.w3.org/ns/sosa/hosts
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    features: http://www.w3.org/ns/sosa/hasMember
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    detects: http://www.w3.org/ns/ssn/detects
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    Sample: http://www.w3.org/ns/sosa/Sample
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    Observation: http://www.w3.org/ns/sosa/Observation
    implements: http://www.w3.org/ns/ssn/implements
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    hasMember: http://www.w3.org/ns/sosa/hasMember
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    observes: http://www.w3.org/ns/sosa/observes
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasResult: http://www.w3.org/ns/sosa/hasResult
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    hasProperty: http://www.w3.org/ns/ssn/hasProperty

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/schema.yaml)


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
    "hasResult": "http://www.w3.org/ns/sosa/hasResult",
    "hasSimpleResult": "http://www.w3.org/ns/sosa/hasSimpleResult",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "isHostedBy": "sosa:isHostedBy",
    "inDeployment": "ssn:inDeployment",
    "hasInput": "ssn:hasInput",
    "implementedBy": "ssn:implementedBy",
    "hosts": "sosa:hosts",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "features": "http://www.w3.org/ns/sosa/hasMember",
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
    "rotations": "geopose:rotations",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
    "type": "@type",
    "id": "@id",
    "properties": "https://purl.org/geojson/vocab#properties",
    "geometry": {
      "@context": {
        "type": "@type",
        "coordinates": {
          "@id": "https://purl.org/geojson/vocab#coordinates",
          "@container": "@list"
        }
      },
      "@id": "https://purl.org/geojson/vocab#geometry"
    },
    "bbox": {
      "@id": "https://purl.org/geojson/vocab#bbox",
      "@container": "@list"
    },
    "MultiLineString": "geojson:MultiLineString",
    "FeatureCollection": "geojson:FeatureCollection",
    "LineString": "geojson:LineString",
    "MultiPolygon": "geojson:MultiPolygon",
    "Feature": "geojson:Feature",
    "GeometryCollection": "geojson:GeometryCollection",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "MultiPoint": "geojson:MultiPoint",
    "links": "http://www.w3.org/2000/01/rdf-schema#seeAlso"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources`

