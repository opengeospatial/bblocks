
# SOSA ObservationCollection (Schema)

`ogc.unstable.sosa.properties.observationCollection` *v1.0*

This building blocks defines an ObservationCollection according to the SOSA/SSN v1.1 specification.

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Description

## SOSA ObservationCollection

Collection of one or more observations, whose members share a common value for one or more properties.
## Examples

### Example of SOSA ObservationCollection
#### json
```json
{ 
  "hasMember": [
    "_:a1"
  ],
  "observedProperty": "_:p1",
  "resultTime": "2022-05-01T22:33:44Z"
}
```

#### json
```json
{ 
  "observedProperty": "p1",
  "resultTime": "2022-05-01T22:33:44Z",
  "hasMember": [
    { 
      "@id": "a1",
      "comment": "Example of an inline membership - would entail hasMember relations",
      "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
      "hasSimpleResult": 1995.2,
    }
  ]
}
```

#### turtle
```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix eg: <http://example.org/my-feature/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

eg:c1 a sosa:ObservationCollection ;
  sosa:hasMember eg:a1 ;
  sosa:observedProperty eg:p1 ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
.

eg:a1 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 33 ;
.
eg:p1 a skos:Concept;
  skos:prefLabel "Some Observable Property";
.
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
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
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  forProperty: http://www.w3.org/ns/ssn/forProperty
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  observes: http://www.w3.org/ns/sosa/observes
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasInput: http://www.w3.org/ns/ssn/hasInput
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasResult: http://www.w3.org/ns/sosa/hasResult
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  implements: http://www.w3.org/ns/ssn/implements
  detects: http://www.w3.org/ns/ssn/detects
  hasSample: http://www.w3.org/ns/sosa/hasSample
  Observation: http://www.w3.org/ns/sosa/Observation
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  hasMember: http://www.w3.org/ns/sosa/hasMember
  Sample: http://www.w3.org/ns/sosa/Sample
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  features: http://www.w3.org/ns/sosa/hasMember
  hosts: http://www.w3.org/ns/sosa/hosts

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "resultTime": "sosa:resultTime",
    "phenomenonTime": "sosa:phenomenonTime",
    "hasFeatureOfInterest": {
      "@id": "http://www.w3.org/ns/sosa/hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": "sosa:observedProperty",
    "usedProcedure": {
      "@id": "http://www.w3.org/ns/sosa/usedProcedure",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "http://www.w3.org/ns/sosa/madeBySensor",
      "@type": "@id"
    },
    "deployedSystem": "ssn:deployedSystem",
    "forProperty": "ssn:forProperty",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "madeBySampler": "sosa:madeBySampler",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "inCondition": "ssn-system:inCondition",
    "hasProperty": "ssn:hasProperty",
    "observes": "sosa:observes",
    "madeSampling": "sosa:madeSampling",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "isObservedBy": "sosa:isObservedBy",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasOutput": "ssn:hasOutput",
    "isSampleOf": "sosa:isSampleOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "implementedBy": "ssn:implementedBy",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "isResultOf": "sosa:isResultOf",
    "madeActuation": "sosa:madeActuation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "madeByActuator": "sosa:madeByActuator",
    "hasInput": "ssn:hasInput",
    "madeObservation": "sosa:madeObservation",
    "isProxyFor": "ssn:isProxyFor",
    "hasResult": "sosa:hasResult",
    "hasSubSystem": "ssn:hasSubSystem",
    "implements": "ssn:implements",
    "detects": "ssn:detects",
    "hasSample": "sosa:hasSample",
    "Observation": "sosa:Observation",
    "isHostedBy": "sosa:isHostedBy",
    "isPropertyOf": "ssn:isPropertyOf",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "actsOnProperty": "sosa:actsOnProperty",
    "hasMember": "sosa:hasMember",
    "Sample": "sosa:Sample",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasDeployment": "ssn:hasDeployment",
    "inDeployment": "ssn:inDeployment",
    "features": "sosa:hasMember",
    "hosts": "sosa:hosts"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/properties/observationCollection`

