
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
    "inCondition": "ssn-system:inCondition",
    "hasProperty": "ssn:hasProperty",
    "madeObservation": "sosa:madeObservation",
    "isSampleOf": "sosa:isSampleOf",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasInput": "ssn:hasInput",
    "features": "sosa:hasMember",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "hasSample": "sosa:hasSample",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "isProxyFor": "ssn:isProxyFor",
    "forProperty": "ssn:forProperty",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "inDeployment": "ssn:inDeployment",
    "madeByActuator": "sosa:madeByActuator",
    "isHostedBy": "sosa:isHostedBy",
    "isObservedBy": "sosa:isObservedBy",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "madeSampling": "sosa:madeSampling",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "actsOnProperty": "sosa:actsOnProperty",
    "detects": "ssn:detects",
    "Observation": "sosa:Observation",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "implements": "ssn:implements",
    "hasOutput": "ssn:hasOutput",
    "deployedSystem": "ssn:deployedSystem",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "Sample": "sosa:Sample",
    "hasDeployment": "ssn:hasDeployment",
    "hasMember": "sosa:hasMember",
    "isResultOf": "sosa:isResultOf",
    "madeActuation": "sosa:madeActuation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "madeBySampler": "sosa:madeBySampler",
    "hasSubSystem": "ssn:hasSubSystem",
    "observes": "sosa:observes",
    "implementedBy": "ssn:implementedBy",
    "hosts": "sosa:hosts",
    "hasResult": "sosa:hasResult",
    "isActedOnBy": "sosa:isActedOnBy"
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

