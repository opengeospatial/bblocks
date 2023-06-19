
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
    "Point": "geojson:Point",
    "MultiLineString": "geojson:MultiLineString",
    "Feature": "geojson:Feature",
    "features": "geojson:features",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "MultiPoint": "geojson:MultiPoint",
    "Polygon": "geojson:Polygon",
    "LineString": "geojson:LineString",
    "MultiPolygon": "geojson:MultiPolygon",
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
    "hasMember": "sosa:hasMember",
    "Observation": "sosa:Observation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "Sample": "sosa:Sample",
    "isProxyFor": "ssn:isProxyFor",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "inCondition": "ssn-system:inCondition",
    "isHostedBy": "sosa:isHostedBy"
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

