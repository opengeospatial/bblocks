---
title: SOSA Observation Feature (Schema)

language_tabs:
  - json: JSON
  - turtle: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>SOSA Observation Feature</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: SOSA Observation Feature (Schema)
---


# SOSA Observation Feature `ogc.unstable.sosa.features.observation`

This building blocks defines a GeoJSON feature containing a SOSA Observation

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/invalid" target="_blank" data-rainbow-uri>Invalid</a>
</p>

<aside class="warning">
Validation for this building block has <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/unstable/sosa/features/observation/" target="_blank">failed</a></strong>
</aside>

# Examples

## Example of SOSA observation

```json
{
  "@id": "pop1999",
  "type": "Feature",
  "featureType": "sosa:Observation",
  "geometry": null,
  "properties": {
    "observedProperty": "https://dbpedia.org/ontology/population",
    "resultTime": "1999",
    "@id": "pop1999",
    "comment": "Example of an inline membership - would entail hasMember relations",
    "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Spanish%20Fork",
    "hasSimpleResult": 15555.0
  }
}
```

```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
_:a1 a geojson:Feature;
  geojson:properties [
    sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
    sosa:hasSimpleResult 33 ;
    sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime
  ]
.
```


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: SOSA Observation Feature
type: object
allOf:
- $ref: ../../../../geo/json-fg/feature/schema.yaml
- type: object
  properties:
    properties:
      $ref: ../../properties/observation/schema.yaml
x-jsonld-extra-terms:
  Observation: http://www.w3.org/ns/sosa/Observation
  Sample: http://www.w3.org/ns/sosa/Sample
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  observes:
    x-jsonld-id: http://www.w3.org/ns/sosa/observes
    x-jsonld-type: '@id'
  isObservedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isObservedBy
    x-jsonld-type: '@id'
  madeObservation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
    x-jsonld-type: '@id'
  madeBySensor:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
    x-jsonld-type: '@id'
  actsOnProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/actsOnProperty
    x-jsonld-type: '@id'
  isActedOnBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isActedOnBy
    x-jsonld-type: '@id'
  madeActuation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeActuation
    x-jsonld-type: '@id'
  madeByActuator:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeByActuator
    x-jsonld-type: '@id'
  hasSample:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasSample
    x-jsonld-type: '@id'
  isSampleOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isSampleOf
    x-jsonld-type: '@id'
  madeSampling:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeSampling
    x-jsonld-type: '@id'
  madeBySampler:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySampler
    x-jsonld-type: '@id'
  hasFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    x-jsonld-type: '@id'
  isFeatureOfInterestOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    x-jsonld-type: '@id'
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  resultTime: http://www.w3.org/ns/sosa/resultTime
  usedProcedure:
    x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
    x-jsonld-type: '@id'
  hosts:
    x-jsonld-id: http://www.w3.org/ns/sosa/hosts
    x-jsonld-type: '@id'
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  detects: http://www.w3.org/ns/ssn/detects
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  forProperty: http://www.w3.org/ns/ssn/forProperty
  implements: http://www.w3.org/ns/ssn/implements
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  hasInput: http://www.w3.org/ns/ssn/hasInput
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  hasMember: http://www.w3.org/ns/sosa/hasMember
  features: http://www.w3.org/ns/sosa/hasMember
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn: http://www.w3.org/ns/ssn/
  ssn-system: http://www.w3.org/ns/ssn/systems/

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.json</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/features/observation`

