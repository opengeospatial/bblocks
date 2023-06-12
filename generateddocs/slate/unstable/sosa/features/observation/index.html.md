---
title: SOSA Observation Feature (Schema)

language_tabs:
  - json: JSON
  - ttl: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>SOSA Observation Feature</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: SOSA Observation Feature (Schema)
---


# SOSA Observation Feature `ogc.unstable.sosa.features.observation`

This building blocks defines a GeoJSON feature containing a SOSA Observation

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/unstable/sosa/features/observation/" target="_blank">valid</a></strong>
</aside>

# Examples

## Example of SOSA observation

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


# JSON Schema

```yaml--schema
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
  hasMember: http://www.w3.org/ns/sosa/hasMember
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  isObservedBy: http://www.w3.org/ns/sosa/isObservedBy
  resultTime: http://www.w3.org/ns/sosa/resultTime
  Observation: http://www.w3.org/ns/sosa/Observation
  isSampleOf: http://www.w3.org/ns/sosa/isSampleOf
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  hasFeatureOfInterest: http://www.w3.org/ns/sosa/hasFeatureOfInterest
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  forProperty: http://www.w3.org/ns/ssn/forProperty
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  hasSample: http://www.w3.org/ns/sosa/hasSample
  detects: http://www.w3.org/ns/ssn/detects
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  madeByActuator: http://www.w3.org/ns/sosa/madeByActuator
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  isActedOnBy: http://www.w3.org/ns/sosa/isActedOnBy
  actsOnProperty: http://www.w3.org/ns/sosa/actsOnProperty
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  hasInput: http://www.w3.org/ns/ssn/hasInput
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  observes: http://www.w3.org/ns/sosa/observes
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  implements: http://www.w3.org/ns/ssn/implements
  Sample: http://www.w3.org/ns/sosa/Sample
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  madeSampling: http://www.w3.org/ns/sosa/madeSampling
  madeBySensor: http://www.w3.org/ns/sosa/madeBySensor
  hasResult: http://www.w3.org/ns/sosa/hasResult
  madeObservation: http://www.w3.org/ns/sosa/madeObservation
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  madeBySampler: http://www.w3.org/ns/sosa/madeBySampler
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  isFeatureOfInterestOf: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
  madeActuation: http://www.w3.org/ns/sosa/madeActuation
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  hosts: http://www.w3.org/ns/sosa/hosts
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.json</a>


# JSON-LD Context

```json--ldContext
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
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "Feature": "geojson:Feature",
    "Polygon": "geojson:Polygon",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPolygon": "geojson:MultiPolygon",
    "MultiPoint": "geojson:MultiPoint",
    "features": "geojson:features",
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
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "hasMember": "sosa:hasMember",
    "hasProperty": "ssn:hasProperty",
    "isObservedBy": "sosa:isObservedBy",
    "Observation": "sosa:Observation",
    "isSampleOf": "sosa:isSampleOf",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "isPropertyOf": "ssn:isPropertyOf",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "forProperty": "ssn:forProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasSample": "sosa:hasSample",
    "detects": "ssn:detects",
    "inDeployment": "ssn:inDeployment",
    "madeByActuator": "sosa:madeByActuator",
    "hasOutput": "ssn:hasOutput",
    "isActedOnBy": "sosa:isActedOnBy",
    "actsOnProperty": "sosa:actsOnProperty",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "hasInput": "ssn:hasInput",
    "deployedSystem": "ssn:deployedSystem",
    "observes": "sosa:observes",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "implements": "ssn:implements",
    "Sample": "sosa:Sample",
    "hasDeployment": "ssn:hasDeployment",
    "madeSampling": "sosa:madeSampling",
    "madeObservation": "sosa:madeObservation",
    "inCondition": "ssn-system:inCondition",
    "implementedBy": "ssn:implementedBy",
    "madeBySampler": "sosa:madeBySampler",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "madeActuation": "sosa:madeActuation",
    "isResultOf": "sosa:isResultOf",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "isProxyFor": "ssn:isProxyFor",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "hosts": "sosa:hosts",
    "isHostedBy": "sosa:isHostedBy",
    "hasSubSystem": "ssn:hasSubSystem"
  }
}
```

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path: `_sources/features/observation`

