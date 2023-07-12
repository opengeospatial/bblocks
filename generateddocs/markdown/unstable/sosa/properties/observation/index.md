
# SOSA Observation (Schema)

`ogc.unstable.sosa.properties.observation` *v1.0*

This building block defines the set of properties for an observation according to the SOSA/SSN specification. These properties may be directly included into a root element of a JSON object or used in the properties container of a GeoJSON feature.

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Description

## SOSA Observation

An observation is "the Act of carrying out an (Observation) Procedure to estimate or calculate a value 
of a property of a FeatureOfInterest. Links to a Sensor to describe what made the Observation and how;
links to an ObservableProperty to describe what the result is an estimate of, and to a FeatureOfInterest
to detail what that property was associated with."
## Examples

### Example of SOSA observation
#### json
```json
{ 
  "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
  "hasSimpleResult": 33,
  "resultTime": "2022-05-01T22:33:44Z"
}
```

#### turtle
```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
_:a1 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 33 ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
.
```

## Schema

```yaml
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

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observation/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observation/schema.yaml)


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
    "hasResult": "sosa:hasResult",
    "hasSimpleResult": "sosa:hasSimpleResult",
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
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observation/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/properties/observation`

