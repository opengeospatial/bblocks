---
title: SOSA ObservationCollection (Schema)

language_tabs:
  - json: JSON
  - turtle: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>SOSA ObservationCollection</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: SOSA ObservationCollection (Schema)
---


# SOSA ObservationCollection `ogc.unstable.sosa.properties.observationCollection`

This building blocks defines an ObservationCollection according to the SOSA/SSN v1.1 specification.

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/unstable/sosa/properties/observationCollection/" target="_blank">valid</a></strong>
</aside>

# Description

## SOSA ObservationCollection

Collection of one or more observations, whose members share a common value for one or more properties.
# Examples

## Example of SOSA ObservationCollection

```json
{ 
  "hasMember": [
    "_:a1"
  ],
  "observedProperty": "_:p1",
  "resultTime": "2022-05-01T22:33:44Z"
}
```

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


# JSON Schema

```yaml--schema
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
  hasMember:
    type: array
    items:
      oneOf:
      - $ref: ../observation/schema.yaml
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
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  implements: http://www.w3.org/ns/ssn/implements
  observes: http://www.w3.org/ns/sosa/observes
  hasInput: http://www.w3.org/ns/ssn/hasInput
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  Sample: http://www.w3.org/ns/sosa/Sample
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  detects: http://www.w3.org/ns/ssn/detects
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  hasSample: http://www.w3.org/ns/sosa/hasSample
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hosts: http://www.w3.org/ns/sosa/hosts
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  Observation: http://www.w3.org/ns/sosa/Observation
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  forProperty: http://www.w3.org/ns/ssn/forProperty
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.json</a>


# JSON-LD Context

```json--ldContext
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
    "hasMember": "sosa:hasMember",
    "madeObservation": "sosa:madeObservation",
    "hasResult": "sosa:hasResult",
    "isHostedBy": "sosa:isHostedBy",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "implements": "ssn:implements",
    "observes": "sosa:observes",
    "hasInput": "ssn:hasInput",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "isProxyFor": "ssn:isProxyFor",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "Sample": "sosa:Sample",
    "madeActuation": "sosa:madeActuation",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "isActedOnBy": "sosa:isActedOnBy",
    "madeSampling": "sosa:madeSampling",
    "hasDeployment": "ssn:hasDeployment",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "detects": "ssn:detects",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "inCondition": "ssn-system:inCondition",
    "deployedSystem": "ssn:deployedSystem",
    "hasSample": "sosa:hasSample",
    "madeByActuator": "sosa:madeByActuator",
    "hosts": "sosa:hosts",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasProperty": "ssn:hasProperty",
    "inDeployment": "ssn:inDeployment",
    "isResultOf": "sosa:isResultOf",
    "Observation": "sosa:Observation",
    "isObservedBy": "sosa:isObservedBy",
    "implementedBy": "ssn:implementedBy",
    "madeBySampler": "sosa:madeBySampler",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "forProperty": "ssn:forProperty",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasSubSystem": "ssn:hasSubSystem",
    "isSampleOf": "sosa:isSampleOf",
    "hasOutput": "ssn:hasOutput",
    "actsOnProperty": "sosa:actsOnProperty"
  }
}
```

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/properties/observationCollection`

