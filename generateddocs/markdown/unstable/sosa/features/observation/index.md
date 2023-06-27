
# SOSA Observation Feature (Schema)

`ogc.unstable.sosa.features.observation` *v1.0*

This building blocks defines a GeoJSON feature containing a SOSA Observation

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Examples

### Example of SOSA observation
#### json
```json
{ 
  "@id": "_:a1",
  "type": "Feature",
  "featureType": "sosa:Observation",
  "geometry": {
    "type": "Point",
    "coordinates": [43.457475012484124, -3.7684047847661435]
  },
  "properties": {
    "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
    "hasSimpleResult": 33,
    "resultTime": "2022-05-01T22:33:44Z"
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
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  resultTime: http://www.w3.org/ns/sosa/resultTime
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  detects: http://www.w3.org/ns/ssn/detects
  hasInput: http://www.w3.org/ns/ssn/hasInput
  forProperty: http://www.w3.org/ns/ssn/forProperty
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  implements: http://www.w3.org/ns/ssn/implements
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  observes: http://www.w3.org/ns/sosa/observes
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  hasResult: http://www.w3.org/ns/sosa/hasResult
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  hasSample: http://www.w3.org/ns/sosa/hasSample
  hasMember: http://www.w3.org/ns/sosa/hasMember
  Observation: http://www.w3.org/ns/sosa/Observation
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  Sample: http://www.w3.org/ns/sosa/Sample
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  hosts: http://www.w3.org/ns/sosa/hosts
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "http://www.w3.org/ns/ssn/systems/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
    "type": "@type",
    "id": "@id",
    "properties": "geojson:properties",
    "geometry": {
      "@context": {
        "type": "@type",
        "coordinates": "geojson:coordinates"
      },
      "@id": "geojson:geometry"
    },
    "bbox": "geojson:bbox",
    "MultiPoint": "geojson:MultiPoint",
    "Polygon": "geojson:Polygon",
    "GeometryCollection": "geojson:GeometryCollection",
    "Point": "geojson:Point",
    "Feature": "geojson:Feature",
    "MultiPolygon": "geojson:MultiPolygon",
    "MultiLineString": "geojson:MultiLineString",
    "LineString": "geojson:LineString",
    "FeatureCollection": "geojson:FeatureCollection",
    "features": "geojson:features",
    "links": "rdfs:seeAlso",
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
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "madeSampling": "sosa:madeSampling",
    "isResultOf": "sosa:isResultOf",
    "implementedBy": "ssn:implementedBy",
    "inDeployment": "ssn:inDeployment",
    "madeBySampler": "sosa:madeBySampler",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "detects": "ssn:detects",
    "hasInput": "ssn:hasInput",
    "forProperty": "ssn:forProperty",
    "madeObservation": "sosa:madeObservation",
    "implements": "ssn:implements",
    "hasDeployment": "ssn:hasDeployment",
    "observes": "sosa:observes",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "isSampleOf": "sosa:isSampleOf",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSubSystem": "ssn:hasSubSystem",
    "isObservedBy": "sosa:isObservedBy",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "isProxyFor": "ssn:isProxyFor",
    "isPropertyOf": "ssn:isPropertyOf",
    "madeActuation": "sosa:madeActuation",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasSample": "sosa:hasSample",
    "hasMember": "sosa:hasMember",
    "Observation": "sosa:Observation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "Sample": "sosa:Sample",
    "inCondition": "ssn-system:inCondition",
    "hasProperty": "ssn:hasProperty",
    "madeByActuator": "sosa:madeByActuator",
    "hasOutput": "ssn:hasOutput",
    "isHostedBy": "sosa:isHostedBy",
    "hosts": "sosa:hosts",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "actsOnProperty": "sosa:actsOnProperty",
    "deployedSystem": "ssn:deployedSystem"
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/features/observation`

