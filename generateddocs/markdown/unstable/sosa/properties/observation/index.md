
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
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "isHostedBy": "sosa:isHostedBy",
    "inDeployment": "ssn:inDeployment",
    "hasInput": "ssn:hasInput",
    "implementedBy": "ssn:implementedBy",
    "hosts": "sosa:hosts",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "features": "sosa:hasMember",
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
    "hasProperty": "ssn:hasProperty"
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

