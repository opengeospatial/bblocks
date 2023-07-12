
# SOSA Observation Feature (Schema)

`ogc.unstable.sosa.features.observation` *v1.0*

This building blocks defines a GeoJSON feature containing a SOSA Observation

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Examples

### Example of SOSA observation
#### json
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

#### turtle
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

## Schema

```yaml
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
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
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
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  implements: http://www.w3.org/ns/ssn/implements
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  Sample: http://www.w3.org/ns/sosa/Sample
  resultTime: http://www.w3.org/ns/sosa/resultTime
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasMember: http://www.w3.org/ns/sosa/hasMember
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  observes: http://www.w3.org/ns/sosa/observes
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  hosts: http://www.w3.org/ns/sosa/hosts
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.yaml)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/features/observation`

