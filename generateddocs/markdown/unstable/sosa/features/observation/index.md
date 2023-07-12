
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
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  forProperty: http://www.w3.org/ns/ssn/forProperty
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  hasSample: http://www.w3.org/ns/sosa/hasSample
  hasInput: http://www.w3.org/ns/ssn/hasInput
  resultTime: http://www.w3.org/ns/sosa/resultTime
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  observes: http://www.w3.org/ns/sosa/observes
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  hosts: http://www.w3.org/ns/sosa/hosts
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hasResult: http://www.w3.org/ns/sosa/hasResult
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  Observation: http://www.w3.org/ns/sosa/Observation
  hasMember: http://www.w3.org/ns/sosa/hasMember
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  detects: http://www.w3.org/ns/ssn/detects
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  implements: http://www.w3.org/ns/ssn/implements
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  features: http://www.w3.org/ns/sosa/hasMember
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  Sample: http://www.w3.org/ns/sosa/Sample

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

