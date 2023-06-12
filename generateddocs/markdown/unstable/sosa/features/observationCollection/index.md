
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

#### ttl
```ttl
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
  sosa:resultTime "1999-01-01"^^xsd:dateTime
.

 eg:pop2000 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 4372.0 ;
  sosa:resultTime "2000"^^xsd:dateTime
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
  hasMember: http://www.w3.org/ns/sosa/hasMember
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  resultTime: http://www.w3.org/ns/sosa/resultTime
  Observation: http://www.w3.org/ns/sosa/Observation
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  forProperty: http://www.w3.org/ns/ssn/forProperty
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  hasSample: http://www.w3.org/ns/sosa/hasSample
  detects: http://www.w3.org/ns/ssn/detects
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  hasInput: http://www.w3.org/ns/ssn/hasInput
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  observes: http://www.w3.org/ns/sosa/observes
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  implements: http://www.w3.org/ns/ssn/implements
  Sample: http://www.w3.org/ns/sosa/Sample
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  hasResult: http://www.w3.org/ns/sosa/hasResult
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  hosts: http://www.w3.org/ns/sosa/hosts
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem

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
    "hasProperty": "ssn:hasProperty",
    "isObservedBy": "sosa:isObservedBy",
    "Observation": "sosa:Observation",
    "isSampleOf": "sosa:isSampleOf",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isPropertyOf": "ssn:isPropertyOf",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "forProperty": "ssn:forProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "hasSample": "sosa:hasSample",
    "detects": "ssn:detects",
    "inDeployment": "ssn:inDeployment",
    "madeByActuator": "sosa:madeByActuator",
    "hasOutput": "ssn:hasOutput",
    "isActedOnBy": "sosa:isActedOnBy",
    "actsOnProperty": "sosa:actsOnProperty",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasInput": "ssn:hasInput",
    "deployedSystem": "ssn:deployedSystem",
    "observes": "sosa:observes",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "implements": "ssn:implements",
    "Sample": "sosa:Sample",
    "hasDeployment": "ssn:hasDeployment",
    "madeSampling": "sosa:madeSampling",
    "hasResult": "sosa:hasResult",
    "madeObservation": "sosa:madeObservation",
    "inCondition": "ssn-system:inCondition",
    "implementedBy": "ssn:implementedBy",
    "madeBySampler": "sosa:madeBySampler",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "madeActuation": "sosa:madeActuation",
    "isResultOf": "sosa:isResultOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "isProxyFor": "ssn:isProxyFor",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "hosts": "sosa:hosts",
    "isHostedBy": "sosa:isHostedBy",
    "hasSubSystem": "ssn:hasSubSystem"
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

