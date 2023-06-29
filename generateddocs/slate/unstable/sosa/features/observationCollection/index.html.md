---
title: SOSA ObservationCollection Feature (Schema)

language_tabs:
  - json: JSON
  - turtle: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>SOSA ObservationCollection Feature</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: SOSA ObservationCollection Feature (Schema)
---


# SOSA ObservationCollection Feature `ogc.unstable.sosa.features.observationCollection`

This building blocks defines an ObservationCollection Feature according to the SOSA/SSN v1.1 specification.

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

<aside class="warning">
Validation for this building block has <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/unstable/sosa/features/observationCollection/" target="_blank">failed</a></strong>
</aside>

# Examples

## Example of SOSA ObservationCollection

```json
{ 
  "@id": "c1",
  "type": "Feature",
  "featureType": "sosa:ObservationCollection",
  "properties": {
    "hasMember": [
      "_:a1"
    ],
    "observedProperty": "_:p1",
    "resultTime": "2022-05-01T22:33:44Z"
  },
}
```

```json
{ 
  "@id": "c1",
  "type": "Feature",
  "featureType": "sosa:ObservationCollection",
  "properties": {
    "observedProperty": "http://dbpedia.org/ontology/population",
    "resultTime": "1999",
    "features": [
      { 
        "@id": "pop1999",
        "comment": "Example of an inline membership - would entail hasMember relations",
        "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Spanish%20Fork",
        "hasSimpleResult": 15555.0
      },
       { 
        "@id": "pop1999",
        "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
        "hasSimpleResult": 3275.0
      }
    ]
  },
}
```

```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix eg: <http://example.org/my-feature/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

eg:c1 a sosa:ObservationCollection ;
  sosa:hasMember eg:pop1999, eg:pop2000 ;
  sosa:observedProperty <http://dbpedia.org/ontology/population> ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
.

eg:pop1999 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 3275.0 ;
  sosa:resultTime "1999-01-01"^^xsd:date
.

 eg:pop2000 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 4372.0 ;
  sosa:resultTime "2000"^^xsd:gYear
.

<http://dbpedia.org/ontology/population> a skos:Concept;
  skos:prefLabel "Population";
.
```


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: SOSA Observation Feature
allOf:
- $ref: ../../../../geo/json-fg/featureCollection/schema.yaml
- type: object
  properties:
    properties:
      $ref: ../../properties/observationCollection/schema.yaml
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn: http://www.w3.org/ns/ssn/
  ssn-system: http://www.w3.org/ns/ssn/systems/
x-jsonld-extra-terms:
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  implements: http://www.w3.org/ns/ssn/implements
  observes: http://www.w3.org/ns/sosa/observes
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  hasInput: http://www.w3.org/ns/ssn/hasInput
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  Sample: http://www.w3.org/ns/sosa/Sample
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
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
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  resultTime: http://www.w3.org/ns/sosa/resultTime
  hosts: http://www.w3.org/ns/sosa/hosts
  hasMember: http://www.w3.org/ns/sosa/hasMember
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

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observationCollection/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observationCollection/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observationCollection/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observationCollection/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "http://www.w3.org/ns/ssn/systems/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
    "links": "rdfs:seeAlso",
    "features": "geojson:features",
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
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observationCollection/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observationCollection/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/features/observationCollection`

