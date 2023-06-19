
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
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  observes: http://www.w3.org/ns/sosa/observes
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  hasInput: http://www.w3.org/ns/ssn/hasInput
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  implements: http://www.w3.org/ns/ssn/implements
  hosts: http://www.w3.org/ns/sosa/hosts
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasSample: http://www.w3.org/ns/sosa/hasSample
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  resultTime: http://www.w3.org/ns/sosa/resultTime
  detects: http://www.w3.org/ns/ssn/detects
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  forProperty: http://www.w3.org/ns/ssn/forProperty
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  hasMember: http://www.w3.org/ns/sosa/hasMember
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  Observation: http://www.w3.org/ns/sosa/Observation
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  Sample: http://www.w3.org/ns/sosa/Sample
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy

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
    "isPropertyOf": "ssn:isPropertyOf",
    "hasDeployment": "ssn:hasDeployment",
    "isResultOf": "sosa:isResultOf",
    "madeSampling": "sosa:madeSampling",
    "implementedBy": "ssn:implementedBy",
    "observes": "sosa:observes",
    "hasSubSystem": "ssn:hasSubSystem",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "madeBySampler": "sosa:madeBySampler",
    "hasInput": "ssn:hasInput",
    "isActedOnBy": "sosa:isActedOnBy",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasProperty": "ssn:hasProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "isObservedBy": "sosa:isObservedBy",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "implements": "ssn:implements",
    "hosts": "sosa:hosts",
    "madeByActuator": "sosa:madeByActuator",
    "hasSample": "sosa:hasSample",
    "deployedSystem": "ssn:deployedSystem",
    "detects": "ssn:detects",
    "inDeployment": "ssn:inDeployment",
    "madeActuation": "sosa:madeActuation",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "actsOnProperty": "sosa:actsOnProperty",
    "hasOutput": "ssn:hasOutput",
    "madeObservation": "sosa:madeObservation",
    "forProperty": "ssn:forProperty",
    "isSampleOf": "sosa:isSampleOf",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "Observation": "sosa:Observation",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "Sample": "sosa:Sample",
    "hasResult": "sosa:hasResult",
    "isProxyFor": "ssn:isProxyFor",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "inCondition": "ssn-system:inCondition",
    "isHostedBy": "sosa:isHostedBy"
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

