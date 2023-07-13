
# Example SOSA Vector Observation Feature (Schema)

`ogc.unstable.sosa.examples.vectorObservationFeature` *v1.0*

This building block defines an example SOSA Observation Feature for a Vector Observation

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

## Examples

### Example 1
#### json
```json
{
  "@id": "vector-obs-1",
  "type":"Feature",
  "geometry":{
    "type":"LineString",
    "coordinates":[
      [
        -111.67183507997295,
        40.056709946862874
      ],
      [
        -111.67183507997295,
        40.056709946862874
      ]
    ]
  },
  "time":null,
  "place":null,
  "properties":{
    "hasFeatureOfInterest":"eg:Traverse-P1-P2",
    "resultTime":"2023-05-22T16:41:00+2",
    "hasResult":{
      "pose":{
        "position":{
          "lat":-111.67183507997295,
          "lon":40.056709946862874,
          "h":0.5
        },
        "angles":{
          "yaw":15.35,
          "pitch":-0.01,
          "roll":0
        }
      },
      "distance":6889234.2
    }
  }
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Example SOSA Vector Observation
allOf:
- $ref: ../../features/observation/schema.yaml
- type: object
  properties:
    properties:
      $ref: ../vectorObservation/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "type": "@type",
    "id": "@id",
    "properties": "geojson:properties",
    "geometry": {
      "@id": "https://purl.org/geojson/vocab#geometry",
      "@context": {}
    },
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "bbox": {
      "@container": "@list",
      "@id": "https://purl.org/geojson/vocab#bbox"
    },
    "coordinates": {
      "@container": "@list",
      "@id": "https://purl.org/geojson/vocab#coordinates"
    },
    "features": {
      "@container": "@set",
      "@id": "http://www.w3.org/ns/sosa/hasMember"
    },
    "links": {
      "@id": "http://www.w3.org/2000/01/rdf-schema#seeAlso",
      "@context": {
        "href": "@id",
        "title": "rdfs:label"
      }
    },
    "resultTime": "sosa:resultTime",
    "phenomenonTime": "sosa:phenomenonTime",
    "observedProperty": "sosa:observedProperty",
    "hasResult": "sosa:hasResult",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "Observation": "sosa:Observation",
    "Sample": "sosa:Sample",
    "observes": {
      "@id": "http://www.w3.org/ns/sosa/observes",
      "@type": "@id"
    },
    "isObservedBy": {
      "@id": "http://www.w3.org/ns/sosa/isObservedBy",
      "@type": "@id"
    },
    "madeObservation": {
      "@id": "http://www.w3.org/ns/sosa/madeObservation",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "http://www.w3.org/ns/sosa/madeBySensor",
      "@type": "@id"
    },
    "actsOnProperty": {
      "@id": "http://www.w3.org/ns/sosa/actsOnProperty",
      "@type": "@id"
    },
    "isActedOnBy": {
      "@id": "http://www.w3.org/ns/sosa/isActedOnBy",
      "@type": "@id"
    },
    "madeActuation": {
      "@id": "http://www.w3.org/ns/sosa/madeActuation",
      "@type": "@id"
    },
    "madeByActuator": {
      "@id": "http://www.w3.org/ns/sosa/madeByActuator",
      "@type": "@id"
    },
    "hasSample": {
      "@id": "http://www.w3.org/ns/sosa/hasSample",
      "@type": "@id"
    },
    "isSampleOf": {
      "@id": "http://www.w3.org/ns/sosa/isSampleOf",
      "@type": "@id"
    },
    "madeSampling": {
      "@id": "http://www.w3.org/ns/sosa/madeSampling",
      "@type": "@id"
    },
    "madeBySampler": {
      "@id": "http://www.w3.org/ns/sosa/madeBySampler",
      "@type": "@id"
    },
    "hasFeatureOfInterest": {
      "@id": "http://www.w3.org/ns/sosa/hasFeatureOfInterest",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "http://www.w3.org/ns/sosa/isFeatureOfInterestOf",
      "@type": "@id"
    },
    "isResultOf": "sosa:isResultOf",
    "usedProcedure": {
      "@id": "http://www.w3.org/ns/sosa/usedProcedure",
      "@type": "@id"
    },
    "hosts": {
      "@id": "http://www.w3.org/ns/sosa/hosts",
      "@type": "@id"
    },
    "isHostedBy": "sosa:isHostedBy",
    "isProxyFor": "ssn:isProxyFor",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "detects": "ssn:detects",
    "hasProperty": "ssn:hasProperty",
    "isPropertyOf": "ssn:isPropertyOf",
    "forProperty": "ssn:forProperty",
    "implements": "ssn:implements",
    "implementedBy": "ssn:implementedBy",
    "hasInput": "ssn:hasInput",
    "hasOutput": "ssn:hasOutput",
    "hasSubSystem": "ssn:hasSubSystem",
    "deployedSystem": "ssn:deployedSystem",
    "hasDeployment": "ssn:hasDeployment",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "inDeployment": "ssn:inDeployment",
    "inCondition": "ssn-system:inCondition",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasMember": "sosa:hasMember",
    "position": {
      "@id": "http://example.com/geopose/position",
      "@context": {
        "lat": "geopose:lat",
        "lon": "geopose:lon",
        "h": "geopose:h",
        "position": "geopose:position",
        "angles": "geopose:angles",
        "yaw": "geopose:yaw",
        "pitch": "geopose:pitch",
        "roll": "geopose:roll"
      }
    },
    "angles": {
      "@id": "http://example.com/geopose/angles",
      "@context": {
        "yaw": "geopose:yaw",
        "pitch": "geopose:pitch",
        "roll": "geopose:roll",
        "position": "geopose:position",
        "angles": "geopose:angles",
        "lat": "geopose:lat",
        "lon": "geopose:lon",
        "h": "geopose:h"
      }
    },
    "longitude": "geo:long",
    "latitude": "geo:lat",
    "height": "geopose:height",
    "rotations": "geopose:rotations",
    "distance": {
      "@id": "http://example.com/properties/distance",
      "@type": "http://www.w3.org/2001/XMLSchema#float"
    }
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/context.jsonld)

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/ogcapi-sosa](https://github.com/opengeospatial/ogcapi-sosa)
* Path: `_sources/examples/vectorObservationFeature`

