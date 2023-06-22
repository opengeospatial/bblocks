
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
    "Polygon": "geojson:Polygon",
    "MultiLineString": "geojson:MultiLineString",
    "Feature": "geojson:Feature",
    "LineString": "geojson:LineString",
    "GeometryCollection": "geojson:GeometryCollection",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "features": "geojson:features",
    "FeatureCollection": "geojson:FeatureCollection",
    "MultiPoint": "geojson:MultiPoint",
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
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "inDeployment": "ssn:inDeployment",
    "implementedBy": "ssn:implementedBy",
    "actsOnProperty": "sosa:actsOnProperty",
    "deployedSystem": "ssn:deployedSystem",
    "Sample": "sosa:Sample",
    "madeObservation": "sosa:madeObservation",
    "isProxyFor": "ssn:isProxyFor",
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
    "hasMember": "sosa:hasMember",
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
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/features/observation`

