
# SOSA Observation (Schema)

`ogc.unstable.sosa.properties.observation` *v1.0*

This building block defines the set of properties for an observation according to the SOSA/SSN specification. These properties may be directly included into a root element of a JSON object or used in the properties container of a GeoJSON feature.

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Description

## SOSA Observation

An observation is "the Act of carrying out an (Observation) Procedure to estimate or calculate a value 
of a property of a FeatureOfInterest. Links to a Sensor to describe what made the Observation and how;
links to an ObservableProperty to describe what the result is an estimate of, and to a FeatureOfInterest
to detail what that property was associated with."
## Examples

### Example of SOSA observation
#### json
```json
{ 
  "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
  "hasSimpleResult": 33,
  "resultTime": "2022-05-01T22:33:44Z"
}
```

#### turtle
```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
_:a1 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 33 ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
.
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
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

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observation/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observation/schema.yaml)


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
    "madeActuation": "sosa:madeActuation",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "hasSample": "sosa:hasSample",
    "Observation": "sosa:Observation",
    "isHostedBy": "sosa:isHostedBy",
    "implementedBy": "ssn:implementedBy",
    "hasSubSystem": "ssn:hasSubSystem",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "features": "sosa:hasMember",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "madeObservation": "sosa:madeObservation",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "inDeployment": "ssn:inDeployment",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "isObservedBy": "sosa:isObservedBy",
    "isResultOf": "sosa:isResultOf",
    "detects": "ssn:detects",
    "implements": "ssn:implements",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasOutput": "ssn:hasOutput",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "Sample": "sosa:Sample",
    "actsOnProperty": "sosa:actsOnProperty",
    "hasInput": "ssn:hasInput",
    "deployedSystem": "ssn:deployedSystem",
    "madeBySampler": "sosa:madeBySampler",
    "hasProperty": "ssn:hasProperty",
    "isSampleOf": "sosa:isSampleOf",
    "madeSampling": "sosa:madeSampling",
    "isPropertyOf": "ssn:isPropertyOf",
    "forProperty": "ssn:forProperty",
    "hasDeployment": "ssn:hasDeployment",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hosts": "sosa:hosts",
    "observes": "sosa:observes",
    "hasMember": "sosa:hasMember",
    "inCondition": "ssn-system:inCondition",
    "isProxyFor": "ssn:isProxyFor",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "madeByActuator": "sosa:madeByActuator"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observation/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/properties/observation`

