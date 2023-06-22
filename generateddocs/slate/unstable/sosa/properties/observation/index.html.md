---
title: SOSA Observation (Schema)

language_tabs:
  - json: JSON
  - turtle: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>SOSA Observation</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: SOSA Observation (Schema)
---


# SOSA Observation `ogc.unstable.sosa.properties.observation`

This building block defines the set of properties for an observation according to the SOSA/SSN specification. These properties may be directly included into a root element of a JSON object or used in the properties container of a GeoJSON feature.

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/unstable/sosa/properties/observation/" target="_blank">valid</a></strong>
</aside>

# Description

## SOSA Observation

An observation is "the Act of carrying out an (Observation) Procedure to estimate or calculate a value 
of a property of a FeatureOfInterest. Links to a Sensor to describe what made the Observation and how;
links to an ObservableProperty to describe what the result is an estimate of, and to a FeatureOfInterest
to detail what that property was associated with."
# Examples

## Example of SOSA observation

```json
{ 
  "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
  "hasSimpleResult": 33,
  "resultTime": "2022-05-01T22:33:44Z"
}
```

```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
_:a1 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 33 ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
.
```


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: SOSA Observation
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
  hasResult:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasResult
  hasSimpleResult:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasSimpleResult
oneOf:
- required:
  - hasResult
- required:
  - hasSimpleResult
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn: http://www.w3.org/ns/ssn/
  ssn-system: http://www.w3.org/ns/ssn/systems/
x-jsonld-extra-terms:
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  Sample: http://www.w3.org/ns/sosa/Sample
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasResult: http://www.w3.org/ns/sosa/hasResult
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  forProperty: http://www.w3.org/ns/ssn/forProperty
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hosts: http://www.w3.org/ns/sosa/hosts
  hasSample: http://www.w3.org/ns/sosa/hasSample
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  hasMember: http://www.w3.org/ns/sosa/hasMember
  Observation: http://www.w3.org/ns/sosa/Observation
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  observes: http://www.w3.org/ns/sosa/observes
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  detects: http://www.w3.org/ns/ssn/detects
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  implements: http://www.w3.org/ns/ssn/implements
  hasInput: http://www.w3.org/ns/ssn/hasInput
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observation/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observation/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observation/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observation/schema.json</a>


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
    "hasResult": "sosa:hasResult",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "inDeployment": "ssn:inDeployment",
    "implementedBy": "ssn:implementedBy",
    "actsOnProperty": "sosa:actsOnProperty",
    "deployedSystem": "ssn:deployedSystem",
    "Sample": "sosa:Sample",
    "madeObservation": "sosa:madeObservation",
    "isProxyFor": "ssn:isProxyFor",
    "madeByActuator": "sosa:madeByActuator",
    "forProperty": "ssn:forProperty",
    "isHostedBy": "sosa:isHostedBy",
    "hasOutput": "ssn:hasOutput",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hosts": "sosa:hosts",
    "hasSample": "sosa:hasSample",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "madeActuation": "sosa:madeActuation",
    "hasMember": "sosa:hasMember",
    "Observation": "sosa:Observation",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "observes": "sosa:observes",
    "madeSampling": "sosa:madeSampling",
    "detects": "ssn:detects",
    "hasDeployment": "ssn:hasDeployment",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "madeBySampler": "sosa:madeBySampler",
    "isObservedBy": "sosa:isObservedBy",
    "isSampleOf": "sosa:isSampleOf",
    "implements": "ssn:implements",
    "hasInput": "ssn:hasInput",
    "hasSubSystem": "ssn:hasSubSystem",
    "isResultOf": "sosa:isResultOf",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasProperty": "ssn:hasProperty",
    "inCondition": "ssn-system:inCondition",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty"
  }
}
```

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observation/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observation/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/properties/observation`

