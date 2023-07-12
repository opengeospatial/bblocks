
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
    "isObservedBy": "sosa:isObservedBy",
    "detects": "ssn:detects",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "isResultOf": "sosa:isResultOf",
    "features": "sosa:hasMember",
    "isActedOnBy": "sosa:isActedOnBy",
    "madeSampling": "sosa:madeSampling",
    "hasProperty": "ssn:hasProperty",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "madeBySampler": "sosa:madeBySampler",
    "hasResult": "sosa:hasResult",
    "madeByActuator": "sosa:madeByActuator",
    "isSampleOf": "sosa:isSampleOf",
    "observes": "sosa:observes",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "hasMember": "sosa:hasMember",
    "inDeployment": "ssn:inDeployment",
    "isProxyFor": "ssn:isProxyFor",
    "deployedSystem": "ssn:deployedSystem",
    "isPropertyOf": "ssn:isPropertyOf",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "hosts": "sosa:hosts",
    "hasSample": "sosa:hasSample",
    "implementedBy": "ssn:implementedBy",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "inCondition": "ssn-system:inCondition",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "Sample": "sosa:Sample",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "Observation": "sosa:Observation",
    "isHostedBy": "sosa:isHostedBy",
    "actsOnProperty": "sosa:actsOnProperty",
    "hasOutput": "ssn:hasOutput",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "madeActuation": "sosa:madeActuation",
    "madeObservation": "sosa:madeObservation",
    "hasSubSystem": "ssn:hasSubSystem",
    "implements": "ssn:implements",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasDeployment": "ssn:hasDeployment",
    "forProperty": "ssn:forProperty",
    "hasInput": "ssn:hasInput"
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

