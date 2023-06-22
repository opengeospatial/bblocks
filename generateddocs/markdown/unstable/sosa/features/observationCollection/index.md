
# SOSA ObservationCollection Feature (Schema)

`ogc.unstable.sosa.features.observationCollection` *v1.0*

This building blocks defines an ObservationCollection Feature according to the SOSA/SSN v1.1 specification.

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Examples

### Example of SOSA ObservationCollection
#### json
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

#### json
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

#### turtle
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

## Schema

```yaml
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
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
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
  resultTime: http://www.w3.org/ns/sosa/resultTime
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
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
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
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
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observationCollection/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observationCollection/schema.yaml)


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
    "hasMember": "sosa:hasMember",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "inDeployment": "ssn:inDeployment",
    "implementedBy": "ssn:implementedBy",
    "actsOnProperty": "sosa:actsOnProperty",
    "deployedSystem": "ssn:deployedSystem",
    "Sample": "sosa:Sample",
    "madeObservation": "sosa:madeObservation",
    "isProxyFor": "ssn:isProxyFor",
    "hasResult": "sosa:hasResult",
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
    "hasSimpleResult": "sosa:hasSimpleResult",
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
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observationCollection/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/features/observationCollection`

