
# SOSA ObservationCollection (Schema)

`ogc.unstable.sosa.properties.observationCollection` *v1.0*

This building blocks defines an ObservationCollection according to the SOSA/SSN v1.1 specification.

[*Status*](http://www.opengis.net/def/status): Invalid

## Description

## SOSA ObservationCollection

Collection of one or more observations, whose members share a common value for one or more properties.
## Examples

### Example of SOSA ObservationCollection
#### json
```json
{ 
  "hasMember": [
    "_:a1"
  ],
  "observedProperty": "_:p1",
  "resultTime": "2022-05-01T22:33:44Z"
}
```


### Example of SOSA ObservationCollection
#### json
```json
{ 
  "observedProperty": "p1",
  "resultTime": "2022-05-01T22:33:44Z",
  "hasMember": [
    { 
      "@id": "a1",
      "@type": "sosa:Observation",
      "comment": "Example of an inline membership - would entail hasMember relations",
      "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
      "hasSimpleResult": 1995.2,
      "phenomenonTime": "2022-05-01T22:33:40Z"
    }
  ]
}
```


### Turtle example of SOSA ObservationCollection
#### ttl
```ttl
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix eg: <http://example.org/my-feature/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

eg:c1 a sosa:ObservationCollection ;
  sosa:hasMember eg:a1 ;
  sosa:observedProperty eg:p1 ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
  sosa:phenomenonTime "2022-05-01T22:33:40Z"^^xsd:dateTime ;
.

eg:a1 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 33 ;
.
eg:p1 a skos:Concept;
  skos:prefLabel "Some Observable Property";
.
```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: SOSA ObservationCollection
$defs:
  collection:
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
        x-jsonld-type: '@id'
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
      hasMember:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/collection'
          - $ref: ../observation/schema.yaml
          - $ref: ../../../../../registereditems/unstable/ogc-utils/iri-or-curie/schema.yaml
        x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
allOf:
- $ref: '#/$defs/collection'
- not:
    anyOf:
    - required:
      - hasResult
    - required:
      - hasSimpleResult
x-jsonld-extra-terms:
  Observation: http://www.w3.org/ns/sosa/Observation
  Sample: http://www.w3.org/ns/sosa/Sample
  observes:
    x-jsonld-id: http://www.w3.org/ns/sosa/observes
    x-jsonld-type: '@id'
  isObservedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isObservedBy
    x-jsonld-type: '@id'
  madeObservation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
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
  isFeatureOfInterestOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    x-jsonld-type: '@id'
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
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
  features: http://www.w3.org/ns/sosa/hasMember
  properties: '@nest'
  featureType: '@type'
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn: http://www.w3.org/ns/ssn/
  ssn-system: http://www.w3.org/ns/ssn/systems/

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.yaml)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/properties/observationCollection`

