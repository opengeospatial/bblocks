
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
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  implements: http://www.w3.org/ns/ssn/implements
  observes: http://www.w3.org/ns/sosa/observes
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  hasInput: http://www.w3.org/ns/ssn/hasInput
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  Sample: http://www.w3.org/ns/sosa/Sample
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  detects: http://www.w3.org/ns/ssn/detects
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  hasSample: http://www.w3.org/ns/sosa/hasSample
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  resultTime: http://www.w3.org/ns/sosa/resultTime
  hosts: http://www.w3.org/ns/sosa/hosts
  hasMember: http://www.w3.org/ns/sosa/hasMember
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  Observation: http://www.w3.org/ns/sosa/Observation
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  forProperty: http://www.w3.org/ns/ssn/forProperty
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty

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
    "GeometryCollection": "geojson:GeometryCollection",
    "features": "geojson:features",
    "FeatureCollection": "geojson:FeatureCollection",
    "MultiLineString": "geojson:MultiLineString",
    "Polygon": "geojson:Polygon",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Feature": "geojson:Feature",
    "MultiPoint": "geojson:MultiPoint",
    "LineString": "geojson:LineString",
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
    "madeObservation": "sosa:madeObservation",
    "isHostedBy": "sosa:isHostedBy",
    "implements": "ssn:implements",
    "observes": "sosa:observes",
    "hasInput": "ssn:hasInput",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "isProxyFor": "ssn:isProxyFor",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "Sample": "sosa:Sample",
    "madeActuation": "sosa:madeActuation",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "isActedOnBy": "sosa:isActedOnBy",
    "madeSampling": "sosa:madeSampling",
    "hasDeployment": "ssn:hasDeployment",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "detects": "ssn:detects",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "inCondition": "ssn-system:inCondition",
    "deployedSystem": "ssn:deployedSystem",
    "hasSample": "sosa:hasSample",
    "madeByActuator": "sosa:madeByActuator",
    "hosts": "sosa:hosts",
    "hasMember": "sosa:hasMember",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasProperty": "ssn:hasProperty",
    "inDeployment": "ssn:inDeployment",
    "isResultOf": "sosa:isResultOf",
    "Observation": "sosa:Observation",
    "isObservedBy": "sosa:isObservedBy",
    "implementedBy": "ssn:implementedBy",
    "madeBySampler": "sosa:madeBySampler",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "forProperty": "ssn:forProperty",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasSubSystem": "ssn:hasSubSystem",
    "isSampleOf": "sosa:isSampleOf",
    "hasOutput": "ssn:hasOutput",
    "actsOnProperty": "sosa:actsOnProperty"
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

