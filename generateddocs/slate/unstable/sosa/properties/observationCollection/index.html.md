---
title: SOSA ObservationCollection (Schema)

language_tabs:
  - json: JSON
  - ttl: RDF/Turtle

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

```ttl
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
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  observes: http://www.w3.org/ns/sosa/observes
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  hasInput: http://www.w3.org/ns/ssn/hasInput
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  implements: http://www.w3.org/ns/ssn/implements
  hosts: http://www.w3.org/ns/sosa/hosts
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasSample: http://www.w3.org/ns/sosa/hasSample
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  detects: http://www.w3.org/ns/ssn/detects
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  forProperty: http://www.w3.org/ns/ssn/forProperty
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  Observation: http://www.w3.org/ns/sosa/Observation
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  Sample: http://www.w3.org/ns/sosa/Sample
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy

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
    "isPropertyOf": "ssn:isPropertyOf",
    "hasDeployment": "ssn:hasDeployment",
    "isResultOf": "sosa:isResultOf",
    "madeSampling": "sosa:madeSampling",
    "implementedBy": "ssn:implementedBy",
    "observes": "sosa:observes",
    "hasSubSystem": "ssn:hasSubSystem",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "madeBySampler": "sosa:madeBySampler",
    "hasInput": "ssn:hasInput",
    "isActedOnBy": "sosa:isActedOnBy",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasProperty": "ssn:hasProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "isObservedBy": "sosa:isObservedBy",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "implements": "ssn:implements",
    "hosts": "sosa:hosts",
    "madeByActuator": "sosa:madeByActuator",
    "hasSample": "sosa:hasSample",
    "deployedSystem": "ssn:deployedSystem",
    "detects": "ssn:detects",
    "inDeployment": "ssn:inDeployment",
    "madeActuation": "sosa:madeActuation",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "actsOnProperty": "sosa:actsOnProperty",
    "hasOutput": "ssn:hasOutput",
    "madeObservation": "sosa:madeObservation",
    "forProperty": "ssn:forProperty",
    "isSampleOf": "sosa:isSampleOf",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "Observation": "sosa:Observation",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "Sample": "sosa:Sample",
    "hasResult": "sosa:hasResult",
    "isProxyFor": "ssn:isProxyFor",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "inCondition": "ssn-system:inCondition",
    "isHostedBy": "sosa:isHostedBy"
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

