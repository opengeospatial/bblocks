
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

#### ttl
```ttl
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
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasSample: http://www.w3.org/ns/sosa/hasSample
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  hasResult: http://www.w3.org/ns/sosa/hasResult
  hasInput: http://www.w3.org/ns/ssn/hasInput
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  implements: http://www.w3.org/ns/ssn/implements
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  forProperty: http://www.w3.org/ns/ssn/forProperty
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  observes: http://www.w3.org/ns/sosa/observes
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  hasMember: http://www.w3.org/ns/sosa/hasMember
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  detects: http://www.w3.org/ns/ssn/detects
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  Observation: http://www.w3.org/ns/sosa/Observation
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  resultTime: http://www.w3.org/ns/sosa/resultTime
  hosts: http://www.w3.org/ns/sosa/hosts
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  Sample: http://www.w3.org/ns/sosa/Sample
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem

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
    "Feature": "geojson:Feature",
    "MultiPoint": "geojson:MultiPoint",
    "GeometryCollection": "geojson:GeometryCollection",
    "MultiPolygon": "geojson:MultiPolygon",
    "features": "geojson:features",
    "FeatureCollection": "geojson:FeatureCollection",
    "Polygon": "geojson:Polygon",
    "Point": "geojson:Point",
    "MultiLineString": "geojson:MultiLineString",
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
    "hasOutput": "ssn:hasOutput",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "isProxyFor": "ssn:isProxyFor",
    "hasSample": "sosa:hasSample",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasInput": "ssn:hasInput",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "implements": "ssn:implements",
    "isPropertyOf": "ssn:isPropertyOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "madeObservation": "sosa:madeObservation",
    "isResultOf": "sosa:isResultOf",
    "forProperty": "ssn:forProperty",
    "hasDeployment": "ssn:hasDeployment",
    "observes": "sosa:observes",
    "isActedOnBy": "sosa:isActedOnBy",
    "hasMember": "sosa:hasMember",
    "detects": "ssn:detects",
    "inDeployment": "ssn:inDeployment",
    "madeSampling": "sosa:madeSampling",
    "madeBySampler": "sosa:madeBySampler",
    "inCondition": "ssn-system:inCondition",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "actsOnProperty": "sosa:actsOnProperty",
    "Observation": "sosa:Observation",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hosts": "sosa:hosts",
    "isHostedBy": "sosa:isHostedBy",
    "implementedBy": "ssn:implementedBy",
    "madeByActuator": "sosa:madeByActuator",
    "madeActuation": "sosa:madeActuation",
    "isSampleOf": "sosa:isSampleOf",
    "isObservedBy": "sosa:isObservedBy",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "Sample": "sosa:Sample",
    "hasProperty": "ssn:hasProperty",
    "deployedSystem": "ssn:deployedSystem",
    "hasSubSystem": "ssn:hasSubSystem"
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

