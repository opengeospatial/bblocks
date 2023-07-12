
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
    "isActedOnBy": "sosa:isActedOnBy"
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

