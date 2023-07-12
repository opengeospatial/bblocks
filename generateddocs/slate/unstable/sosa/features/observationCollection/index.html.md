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
  "type": "FeatureCollection",
  "featureType": "sosa:ObservationCollection",
  "properties": {
    "observedProperty": "https://dbpedia.org/ontology/population",
    "resultTime": "1999"
  },
  "features": [
    {
      "@id": "pop1999",
      "type": "Feature",
      "geometry": null,
      "properties": null,
      "comment": "Example of an inline membership - would entail hasMember relations",
      "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Spanish%20Fork",
      "hasSimpleResult": 15555.0
    },
    {
      "@id": "pop1999",
      "type": "Feature",
      "geometry": null,
      "properties": null,
      "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
      "hasSimpleResult": 3275.0
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
    features:
      type: array
      items:
        oneOf:
        - $ref: ../observation/schema.yaml
        - type: string
      x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn: http://www.w3.org/ns/ssn/
  ssn-system: http://www.w3.org/ns/ssn/systems/
x-jsonld-extra-terms:
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  detects: http://www.w3.org/ns/ssn/detects
  resultTime: http://www.w3.org/ns/sosa/resultTime
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
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
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
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
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  implements: http://www.w3.org/ns/ssn/implements
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  forProperty: http://www.w3.org/ns/ssn/forProperty
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  hasInput: http://www.w3.org/ns/ssn/hasInput

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observationCollection/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observationCollection/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observationCollection/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observationCollection/schema.json</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/features/observationCollection`

