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

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.json</a>


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
    "hasSimpleResult": "sosa:hasSimpleResult",
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
    "hasResult": "sosa:hasResult",
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
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/properties/observationCollection`

