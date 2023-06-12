
# Sensor, Observation, Sample, and Actuator (SOSA) (Api)

`ogc.unstable.sosa` *v1.0*

The SOSA (Sensor, Observation, Sample, and Actuator) ontology  is a realisation of the Observations, Measurements and Sampling (OMS) Conceptual model

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Description

Building Blocks for implementing the core classes of the []Observations and Measurements model]

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
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasResult: http://www.w3.org/ns/sosa/hasResult
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    implements: http://www.w3.org/ns/ssn/implements
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    observes: http://www.w3.org/ns/sosa/observes
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasMember: http://www.w3.org/ns/sosa/hasMember
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    detects: http://www.w3.org/ns/ssn/detects
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hosts: http://www.w3.org/ns/sosa/hosts
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
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
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasResult: http://www.w3.org/ns/sosa/hasResult
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    implements: http://www.w3.org/ns/ssn/implements
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    observes: http://www.w3.org/ns/sosa/observes
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasMember: http://www.w3.org/ns/sosa/hasMember
    usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
    detects: http://www.w3.org/ns/ssn/detects
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    resultTime: http://www.w3.org/ns/sosa/resultTime
    hosts: http://www.w3.org/ns/sosa/hosts
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    observedProperty: http://www.w3.org/ns/sosa/observedProperty
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
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
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasResult: http://www.w3.org/ns/sosa/hasResult
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    implements: http://www.w3.org/ns/ssn/implements
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    observes: http://www.w3.org/ns/sosa/observes
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    hasMember: http://www.w3.org/ns/sosa/hasMember
    detects: http://www.w3.org/ns/ssn/detects
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hosts: http://www.w3.org/ns/sosa/hosts
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
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
    hasOutput: http://www.w3.org/ns/ssn/hasOutput
    qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
    isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
    hasSample: http://www.w3.org/ns/sosa/hasSample
    hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
    hasResult: http://www.w3.org/ns/sosa/hasResult
    hasInput: http://www.w3.org/ns/ssn/hasInput
    hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
    implements: http://www.w3.org/ns/ssn/implements
    isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
    hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
    madeObservation: http://www.w3.org/ns/sosa/madeObservation
    isResultOf: http://www.w3.org/ns/sosa/isResultOf
    forProperty: http://www.w3.org/ns/ssn/forProperty
    hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
    observes: http://www.w3.org/ns/sosa/observes
    isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
    detects: http://www.w3.org/ns/ssn/detects
    inDeployment: http://www.w3.org/ns/ssn/inDeployment
    madeSampling: http://www.w3.org/ns/sosa/madeSampling
    madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
    inCondition: http://www.w3.org/ns/ssn/systems/inCondition
    hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
    hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
    actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
    Observation: http://www.w3.org/ns/sosa/Observation
    deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
    wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
    isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    hosts: http://www.w3.org/ns/sosa/hosts
    isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
    implementedBy: http://www.w3.org/ns/ssn/implementedBy
    hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
    madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
    madeActuation: http://www.w3.org/ns/sosa/madeActuation
    isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
    isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
    hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
    Sample: http://www.w3.org/ns/sosa/Sample
    hasProperty: http://www.w3.org/ns/ssn/hasProperty
    deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
    hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem

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
    "hasOutput": "ssn:hasOutput",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "isProxyFor": "ssn:isProxyFor",
    "hasSample": "sosa:hasSample",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasInput": "ssn:hasInput",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "implements": "ssn:implements",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "madeObservation": "sosa:madeObservation",
    "isResultOf": "sosa:isResultOf",
    "forProperty": "ssn:forProperty",
    "hasDeployment": "ssn:hasDeployment",
    "observes": "sosa:observes",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasMember": "http://www.w3.org/ns/sosa/hasMember",
    "detects": "ssn:detects",
    "inDeployment": "ssn:inDeployment",
    "madeSampling": "sosa:madeSampling",
    "madeBySampler": "sosa:madeBySampler",
    "inCondition": "ssn-system:inCondition",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "actsOnProperty": "sosa:actsOnProperty",
    "Observation": "sosa:Observation",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hosts": "sosa:hosts",
    "isHostedBy": "sosa:isHostedBy",
    "implementedBy": "ssn:implementedBy",
    "madeByActuator": "sosa:madeByActuator",
    "madeActuation": "sosa:madeActuation",
    "isSampleOf": "sosa:isSampleOf",
    "isObservedBy": "sosa:isObservedBy",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "Sample": "sosa:Sample",
    "hasProperty": "ssn:hasProperty",
    "deployedSystem": "ssn:deployedSystem",
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
    "latitude": "geo:lat",
    "rotations": "geopose:rotations",
    "height": "geopose:height",
    "longitude": "geo:long",
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
    "Feature": "geojson:Feature",
    "MultiPoint": "geojson:MultiPoint",
    "GeometryCollection": "geojson:GeometryCollection",
    "MultiPolygon": "geojson:MultiPolygon",
    "features": "geojson:features",
    "FeatureCollection": "geojson:FeatureCollection",
    "Polygon": "geojson:Polygon",
    "Point": "geojson:Point",
    "MultiLineString": "geojson:MultiLineString",
    "LineString": "geojson:LineString",
    "links": "rdfs:seeAlso"
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

