
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
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  resultTime: http://www.w3.org/ns/sosa/resultTime
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  hasInput: http://www.w3.org/ns/ssn/hasInput
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  hosts: http://www.w3.org/ns/sosa/hosts
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  detects: http://www.w3.org/ns/ssn/detects
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  Sample: http://www.w3.org/ns/sosa/Sample
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  Observation: http://www.w3.org/ns/sosa/Observation
  implements: http://www.w3.org/ns/ssn/implements
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hasMember: http://www.w3.org/ns/sosa/hasMember
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  forProperty: http://www.w3.org/ns/ssn/forProperty
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  observes: http://www.w3.org/ns/sosa/observes
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasSample: http://www.w3.org/ns/sosa/hasSample
  hasResult: http://www.w3.org/ns/sosa/hasResult
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  hasProperty: http://www.w3.org/ns/ssn/hasProperty

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
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
    "links": "http://www.w3.org/2000/01/rdf-schema#seeAlso",
    "features": "http://www.w3.org/ns/sosa/hasMember",
    "resultTime": "http://www.w3.org/ns/sosa/resultTime",
    "phenomenonTime": "http://www.w3.org/ns/sosa/phenomenonTime",
    "hasFeatureOfInterest": {
      "@id": "http://www.w3.org/ns/sosa/hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": "http://www.w3.org/ns/sosa/observedProperty",
    "usedProcedure": {
      "@id": "http://www.w3.org/ns/sosa/usedProcedure",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "http://www.w3.org/ns/sosa/madeBySensor",
      "@type": "@id"
    },
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "isHostedBy": "sosa:isHostedBy",
    "inDeployment": "ssn:inDeployment",
    "hasInput": "ssn:hasInput",
    "implementedBy": "ssn:implementedBy",
    "hosts": "sosa:hosts",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "detects": "ssn:detects",
    "madeByActuator": "sosa:madeByActuator",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "Sample": "sosa:Sample",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "Observation": "sosa:Observation",
    "implements": "ssn:implements",
    "madeActuation": "sosa:madeActuation",
    "hasOutput": "ssn:hasOutput",
    "actsOnProperty": "sosa:actsOnProperty",
    "isObservedBy": "sosa:isObservedBy",
    "isSampleOf": "sosa:isSampleOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasMember": "sosa:hasMember",
    "isActedOnBy": "sosa:isActedOnBy",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "forProperty": "ssn:forProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "observes": "sosa:observes",
    "isProxyFor": "ssn:isProxyFor",
    "hasDeployment": "ssn:hasDeployment",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasSample": "sosa:hasSample",
    "hasResult": "sosa:hasResult",
    "inCondition": "ssn-system:inCondition",
    "isResultOf": "sosa:isResultOf",
    "madeSampling": "sosa:madeSampling",
    "madeBySampler": "sosa:madeBySampler",
    "hasSubSystem": "ssn:hasSubSystem",
    "deployedSystem": "ssn:deployedSystem",
    "madeObservation": "sosa:madeObservation",
    "hasProperty": "ssn:hasProperty"
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

