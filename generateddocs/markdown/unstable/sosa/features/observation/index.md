
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
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  implements: http://www.w3.org/ns/ssn/implements
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  detects: http://www.w3.org/ns/ssn/detects
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  Sample: http://www.w3.org/ns/sosa/Sample
  observes: http://www.w3.org/ns/sosa/observes
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasResult: http://www.w3.org/ns/sosa/hasResult
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasInput: http://www.w3.org/ns/ssn/hasInput
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  forProperty: http://www.w3.org/ns/ssn/forProperty
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  hasSample: http://www.w3.org/ns/sosa/hasSample
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  hosts: http://www.w3.org/ns/sosa/hosts
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  Observation: http://www.w3.org/ns/sosa/Observation
  hasMember: http://www.w3.org/ns/sosa/hasMember
  resultTime: http://www.w3.org/ns/sosa/resultTime
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
    "MultiPoint": "geojson:MultiPoint",
    "Feature": "geojson:Feature",
    "LineString": "geojson:LineString",
    "MultiPolygon": "geojson:MultiPolygon",
    "GeometryCollection": "geojson:GeometryCollection",
    "FeatureCollection": "geojson:FeatureCollection",
    "Polygon": "geojson:Polygon",
    "features": "geojson:features",
    "Point": "geojson:Point",
    "MultiLineString": "geojson:MultiLineString",
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
    "madeByActuator": "sosa:madeByActuator",
    "isPropertyOf": "ssn:isPropertyOf",
    "implements": "ssn:implements",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "madeBySampler": "sosa:madeBySampler",
    "detects": "ssn:detects",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "Sample": "sosa:Sample",
    "observes": "sosa:observes",
    "isActedOnBy": "sosa:isActedOnBy",
    "madeActuation": "sosa:madeActuation",
    "hasSubSystem": "ssn:hasSubSystem",
    "isProxyFor": "ssn:isProxyFor",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasDeployment": "ssn:hasDeployment",
    "deployedSystem": "ssn:deployedSystem",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "isResultOf": "sosa:isResultOf",
    "hasProperty": "ssn:hasProperty",
    "actsOnProperty": "sosa:actsOnProperty",
    "madeSampling": "sosa:madeSampling",
    "inCondition": "ssn-system:inCondition",
    "hasInput": "ssn:hasInput",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "forProperty": "ssn:forProperty",
    "implementedBy": "ssn:implementedBy",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "madeObservation": "sosa:madeObservation",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "inDeployment": "ssn:inDeployment",
    "hasSample": "sosa:hasSample",
    "isObservedBy": "sosa:isObservedBy",
    "isSampleOf": "sosa:isSampleOf",
    "hosts": "sosa:hosts",
    "hasOutput": "ssn:hasOutput",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "Observation": "sosa:Observation",
    "hasMember": "sosa:hasMember",
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

