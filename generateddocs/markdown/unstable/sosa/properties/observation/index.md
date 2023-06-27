
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
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  detects: http://www.w3.org/ns/ssn/detects
  hasInput: http://www.w3.org/ns/ssn/hasInput
  forProperty: http://www.w3.org/ns/ssn/forProperty
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  implements: http://www.w3.org/ns/ssn/implements
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  observes: http://www.w3.org/ns/sosa/observes
  hasResult: http://www.w3.org/ns/sosa/hasResult
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  hasSample: http://www.w3.org/ns/sosa/hasSample
  hasMember: http://www.w3.org/ns/sosa/hasMember
  Observation: http://www.w3.org/ns/sosa/Observation
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  Sample: http://www.w3.org/ns/sosa/Sample
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  hosts: http://www.w3.org/ns/sosa/hosts
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem

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
    "resultTime": "sosa:resultTime",
    "phenomenonTime": "sosa:phenomenonTime",
    "hasFeatureOfInterest": {
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": "sosa:observedProperty",
    "usedProcedure": {
      "@id": "sosa:usedProcedure",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "sosa:madeBySensor",
      "@type": "@id"
    },
    "hasResult": "sosa:hasResult",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "madeSampling": "sosa:madeSampling",
    "isResultOf": "sosa:isResultOf",
    "implementedBy": "ssn:implementedBy",
    "inDeployment": "ssn:inDeployment",
    "madeBySampler": "sosa:madeBySampler",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "detects": "ssn:detects",
    "hasInput": "ssn:hasInput",
    "forProperty": "ssn:forProperty",
    "madeObservation": "sosa:madeObservation",
    "implements": "ssn:implements",
    "hasDeployment": "ssn:hasDeployment",
    "observes": "sosa:observes",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "isSampleOf": "sosa:isSampleOf",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSubSystem": "ssn:hasSubSystem",
    "isObservedBy": "sosa:isObservedBy",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "isProxyFor": "ssn:isProxyFor",
    "isPropertyOf": "ssn:isPropertyOf",
    "madeActuation": "sosa:madeActuation",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasSample": "sosa:hasSample",
    "hasMember": "sosa:hasMember",
    "Observation": "sosa:Observation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "Sample": "sosa:Sample",
    "inCondition": "ssn-system:inCondition",
    "hasProperty": "ssn:hasProperty",
    "madeByActuator": "sosa:madeByActuator",
    "hasOutput": "ssn:hasOutput",
    "isHostedBy": "sosa:isHostedBy",
    "hosts": "sosa:hosts",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "actsOnProperty": "sosa:actsOnProperty",
    "deployedSystem": "ssn:deployedSystem"
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

