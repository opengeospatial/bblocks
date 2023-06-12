
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

#### ttl
```ttl
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
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  implements: http://www.w3.org/ns/ssn/implements
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  detects: http://www.w3.org/ns/ssn/detects
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  Sample: http://www.w3.org/ns/sosa/Sample
  observes: http://www.w3.org/ns/sosa/observes
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasResult: http://www.w3.org/ns/sosa/hasResult
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasInput: http://www.w3.org/ns/ssn/hasInput
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  forProperty: http://www.w3.org/ns/ssn/forProperty
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  hasSample: http://www.w3.org/ns/sosa/hasSample
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  hosts: http://www.w3.org/ns/sosa/hosts
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  Observation: http://www.w3.org/ns/sosa/Observation
  hasMember: http://www.w3.org/ns/sosa/hasMember
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observation/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observation/schema.yaml)


# JSON-LD Context

```jsonld
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
    "madeByActuator": "sosa:madeByActuator",
    "isPropertyOf": "ssn:isPropertyOf",
    "implements": "ssn:implements",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "madeBySampler": "sosa:madeBySampler",
    "detects": "ssn:detects",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "Sample": "sosa:Sample",
    "observes": "sosa:observes",
    "isActedOnBy": "sosa:isActedOnBy",
    "madeActuation": "sosa:madeActuation",
    "hasSubSystem": "ssn:hasSubSystem",
    "isProxyFor": "ssn:isProxyFor",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasDeployment": "ssn:hasDeployment",
    "deployedSystem": "ssn:deployedSystem",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "isResultOf": "sosa:isResultOf",
    "hasProperty": "ssn:hasProperty",
    "actsOnProperty": "sosa:actsOnProperty",
    "madeSampling": "sosa:madeSampling",
    "inCondition": "ssn-system:inCondition",
    "hasInput": "ssn:hasInput",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "forProperty": "ssn:forProperty",
    "implementedBy": "ssn:implementedBy",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "madeObservation": "sosa:madeObservation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "inDeployment": "ssn:inDeployment",
    "hasSample": "sosa:hasSample",
    "isObservedBy": "sosa:isObservedBy",
    "isSampleOf": "sosa:isSampleOf",
    "hosts": "sosa:hosts",
    "hasOutput": "ssn:hasOutput",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "Observation": "sosa:Observation",
    "hasMember": "sosa:hasMember",
    "isHostedBy": "sosa:isHostedBy"
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

