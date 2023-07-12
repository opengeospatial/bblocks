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

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

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
  features: http://www.w3.org/ns/sosa/hasMember
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

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.json</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/features/observation`

