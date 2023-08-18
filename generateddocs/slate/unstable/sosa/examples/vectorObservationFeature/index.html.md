---
title: Example SOSA Vector Observation Feature (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>Example SOSA Vector Observation Feature</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Example SOSA Vector Observation Feature (Schema)
---


# Example SOSA Vector Observation Feature `ogc.unstable.sosa.examples.vectorObservationFeature`

This building block defines an example SOSA Observation Feature for a Vector Observation

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/unstable/sosa/examples/vectorObservationFeature/" target="_blank">valid</a></strong>
</aside>

# Examples

## Example 1


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

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;data=%7B%0A++%22%40id%22%3A+%22vector-obs-1%22%2C%0A++%22type%22%3A%22Feature%22%2C%0A++%22geometry%22%3A%7B%0A++++%22type%22%3A%22LineString%22%2C%0A++++%22coordinates%22%3A%5B%0A++++++%5B%0A++++++++-111.67183507997295%2C%0A++++++++40.056709946862874%0A++++++%5D%2C%0A++++++%5B%0A++++++++-111.67183507997295%2C%0A++++++++40.056709946862874%0A++++++%5D%0A++++%5D%0A++%7D%2C%0A++%22time%22%3Anull%2C%0A++%22place%22%3Anull%2C%0A++%22properties%22%3A%7B%0A++++%22hasFeatureOfInterest%22%3A%22eg%3ATraverse-P1-P2%22%2C%0A++++%22resultTime%22%3A%222023-05-22T16%3A41%3A00%2B2%22%2C%0A++++%22hasResult%22%3A%7B%0A++++++%22pose%22%3A%7B%0A++++++++%22position%22%3A%7B%0A++++++++++%22lat%22%3A-111.67183507997295%2C%0A++++++++++%22lon%22%3A40.056709946862874%2C%0A++++++++++%22h%22%3A0.5%0A++++++++%7D%2C%0A++++++++%22angles%22%3A%7B%0A++++++++++%22yaw%22%3A15.35%2C%0A++++++++++%22pitch%22%3A-0.01%2C%0A++++++++++%22roll%22%3A0%0A++++++++%7D%0A++++++%7D%2C%0A++++++%22distance%22%3A6889234.2%0A++++%7D%0A++%7D%0A%7D%0A">View on JSON Viewer</a></p>
</blockquote>



```jsonld
{
  "@id": "vector-obs-1",
  "type": "Feature",
  "geometry": {
    "type": "LineString",
    "coordinates": [
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
  "time": null,
  "place": null,
  "properties": {
    "hasFeatureOfInterest": "eg:Traverse-P1-P2",
    "resultTime": "2023-05-22T16:41:00+2",
    "hasResult": {
      "pose": {
        "position": {
          "lat": -111.67183507997295,
          "lon": 40.056709946862874,
          "h": 0.5
        },
        "angles": {
          "yaw": 15.35,
          "pitch": -0.01,
          "roll": 0
        }
      },
      "distance": 6889234.2
    }
  },
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40id%22%3A+%22vector-obs-1%22%2C%0A++%22type%22%3A+%22Feature%22%2C%0A++%22geometry%22%3A+%7B%0A++++%22type%22%3A+%22LineString%22%2C%0A++++%22coordinates%22%3A+%5B%0A++++++%5B%0A++++++++-111.67183507997295%2C%0A++++++++40.056709946862874%0A++++++%5D%2C%0A++++++%5B%0A++++++++-111.67183507997295%2C%0A++++++++40.056709946862874%0A++++++%5D%0A++++%5D%0A++%7D%2C%0A++%22time%22%3A+null%2C%0A++%22place%22%3A+null%2C%0A++%22properties%22%3A+%7B%0A++++%22hasFeatureOfInterest%22%3A+%22eg%3ATraverse-P1-P2%22%2C%0A++++%22resultTime%22%3A+%222023-05-22T16%3A41%3A00%2B2%22%2C%0A++++%22hasResult%22%3A+%7B%0A++++++%22pose%22%3A+%7B%0A++++++++%22position%22%3A+%7B%0A++++++++++%22lat%22%3A+-111.67183507997295%2C%0A++++++++++%22lon%22%3A+40.056709946862874%2C%0A++++++++++%22h%22%3A+0.5%0A++++++++%7D%2C%0A++++++++%22angles%22%3A+%7B%0A++++++++++%22yaw%22%3A+15.35%2C%0A++++++++++%22pitch%22%3A+-0.01%2C%0A++++++++++%22roll%22%3A+0%0A++++++++%7D%0A++++++%7D%2C%0A++++++%22distance%22%3A+6889234.2%0A++++%7D%0A++%7D%2C%0A++%22%40context%22%3A+%22https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Funstable%2Fsosa%2Fexamples%2FvectorObservationFeature%2Fcontext.jsonld%22%0A%7D">View on JSON-LD Playground</a></p>
</blockquote>



```turtle
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://example.com/properties/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://www.example.com/features/vector-obs-1> a geojson:Feature ;
    sosa:hasFeatureOfInterest <eg:Traverse-P1-P2> ;
    sosa:hasResult [ ns1:distance "6889234.2"^^xsd:float ] ;
    sosa:resultTime "2023-05-22T16:41:00+2" ;
    geojson:geometry [ a geojson:LineString ;
            geojson:coordinates ( ( -1.116718e+02 4.005671e+01 ) ( -1.116718e+02 4.005671e+01 ) ) ] .


```


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: Example SOSA Vector Observation
allOf:
- $ref: ../../features/observation/schema.yaml
- type: object
  properties:
    properties:
      $ref: ../vectorObservation/schema.yaml

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;data=%24schema%3A+https%3A%2F%2Fjson-schema.org%2Fdraft%2F2020-12%2Fschema%0Adescription%3A+Example+SOSA+Vector+Observation%0AallOf%3A%0A-+%24ref%3A+..%2F..%2Ffeatures%2Fobservation%2Fschema.yaml%0A-+type%3A+object%0A++properties%3A%0A++++properties%3A%0A++++++%24ref%3A+..%2FvectorObservation%2Fschema.yaml%0A">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "type": "@type",
    "id": "@id",
    "properties": {
      "@id": "@nest",
      "@context": {
        "features": "sosa:hasMember",
        "properties": "@nest"
      }
    },
    "geometry": {
      "@id": "geojson:geometry",
      "@context": {}
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
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
    "features": {
      "@container": "@set",
      "@id": "sosa:hasMember"
    },
    "links": {
      "@id": "rdfs:seeAlso",
      "@context": {
        "href": "@id",
        "title": "rdfs:label"
      }
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "Observation": "sosa:Observation",
    "Sample": "sosa:Sample",
    "observedProperty": "sosa:observedProperty",
    "phenomenonTime": "sosa:phenomenonTime",
    "observes": {
      "@id": "sosa:observes",
      "@type": "@id"
    },
    "isObservedBy": {
      "@id": "sosa:isObservedBy",
      "@type": "@id"
    },
    "madeObservation": {
      "@id": "sosa:madeObservation",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "sosa:madeBySensor",
      "@type": "@id"
    },
    "actsOnProperty": {
      "@id": "sosa:actsOnProperty",
      "@type": "@id"
    },
    "isActedOnBy": {
      "@id": "sosa:isActedOnBy",
      "@type": "@id"
    },
    "madeActuation": {
      "@id": "sosa:madeActuation",
      "@type": "@id"
    },
    "madeByActuator": {
      "@id": "sosa:madeByActuator",
      "@type": "@id"
    },
    "hasSample": {
      "@id": "sosa:hasSample",
      "@type": "@id"
    },
    "isSampleOf": {
      "@id": "sosa:isSampleOf",
      "@type": "@id"
    },
    "madeSampling": {
      "@id": "sosa:madeSampling",
      "@type": "@id"
    },
    "madeBySampler": {
      "@id": "sosa:madeBySampler",
      "@type": "@id"
    },
    "hasFeatureOfInterest": {
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "sosa:isFeatureOfInterestOf",
      "@type": "@id"
    },
    "hasResult": "sosa:hasResult",
    "isResultOf": "sosa:isResultOf",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "resultTime": "sosa:resultTime",
    "usedProcedure": {
      "@id": "sosa:usedProcedure",
      "@type": "@id"
    },
    "hosts": {
      "@id": "sosa:hosts",
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
    "inCondition": "ssn:systems/inCondition",
    "hasSystemCapability": "ssn:systems/hasSystemCapability",
    "hasSystemProperty": "ssn:systems/hasSystemProperty",
    "hasOperatingRange": "ssn:systems/hasOperatingRange",
    "hasOperatingProperty": "ssn:systems/hasOperatingProperty",
    "hasSurvivalRange": "ssn:systems/hasSurvivalRange",
    "hasSurvivalProperty": "ssn:systems/hasSurvivalProperty",
    "qualityOfObservation": "ssn:systems/qualityOfObservation",
    "hasMember": "sosa:hasMember",
    "featureType": "@type",
    "position": {
      "@id": "geopose:position",
      "@context": {
        "lat": "geo:lat",
        "lon": "geo:long",
        "h": "geopose:h"
      }
    },
    "angles": {
      "@id": "geopose:angles",
      "@context": {
        "yaw": "geopose:yaw",
        "pitch": "geopose:pitch",
        "roll": "geopose:roll"
      }
    },
    "distance": {
      "@id": "http://example.com/properties/distance",
      "@type": "http://www.w3.org/2001/XMLSchema#float"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "ssn:systems/",
    "geopose": "http://example.com/geopose/",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%7B%0A++++%22type%22%3A+%22%40type%22%2C%0A++++%22id%22%3A+%22%40id%22%2C%0A++++%22properties%22%3A+%7B%0A++++++%22%40id%22%3A+%22%40nest%22%2C%0A++++++%22%40context%22%3A+%7B%0A++++++++%22features%22%3A+%22sosa%3AhasMember%22%2C%0A++++++++%22properties%22%3A+%22%40nest%22%0A++++++%7D%0A++++%7D%2C%0A++++%22geometry%22%3A+%7B%0A++++++%22%40id%22%3A+%22geojson%3Ageometry%22%2C%0A++++++%22%40context%22%3A+%7B%7D%0A++++%7D%2C%0A++++%22bbox%22%3A+%7B%0A++++++%22%40container%22%3A+%22%40list%22%2C%0A++++++%22%40id%22%3A+%22geojson%3Abbox%22%0A++++%7D%2C%0A++++%22Feature%22%3A+%22geojson%3AFeature%22%2C%0A++++%22FeatureCollection%22%3A+%22geojson%3AFeatureCollection%22%2C%0A++++%22GeometryCollection%22%3A+%22geojson%3AGeometryCollection%22%2C%0A++++%22LineString%22%3A+%22geojson%3ALineString%22%2C%0A++++%22MultiLineString%22%3A+%22geojson%3AMultiLineString%22%2C%0A++++%22MultiPoint%22%3A+%22geojson%3AMultiPoint%22%2C%0A++++%22MultiPolygon%22%3A+%22geojson%3AMultiPolygon%22%2C%0A++++%22Point%22%3A+%22geojson%3APoint%22%2C%0A++++%22Polygon%22%3A+%22geojson%3APolygon%22%2C%0A++++%22features%22%3A+%7B%0A++++++%22%40container%22%3A+%22%40set%22%2C%0A++++++%22%40id%22%3A+%22sosa%3AhasMember%22%0A++++%7D%2C%0A++++%22links%22%3A+%7B%0A++++++%22%40id%22%3A+%22rdfs%3AseeAlso%22%2C%0A++++++%22%40context%22%3A+%7B%0A++++++++%22href%22%3A+%22%40id%22%2C%0A++++++++%22title%22%3A+%22rdfs%3Alabel%22%0A++++++%7D%0A++++%7D%2C%0A++++%22coordinates%22%3A+%7B%0A++++++%22%40container%22%3A+%22%40list%22%2C%0A++++++%22%40id%22%3A+%22geojson%3Acoordinates%22%0A++++%7D%2C%0A++++%22Observation%22%3A+%22sosa%3AObservation%22%2C%0A++++%22Sample%22%3A+%22sosa%3ASample%22%2C%0A++++%22observedProperty%22%3A+%22sosa%3AobservedProperty%22%2C%0A++++%22phenomenonTime%22%3A+%22sosa%3AphenomenonTime%22%2C%0A++++%22observes%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3Aobserves%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isObservedBy%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AisObservedBy%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeObservation%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeObservation%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeBySensor%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeBySensor%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22actsOnProperty%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AactsOnProperty%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isActedOnBy%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AisActedOnBy%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeActuation%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeActuation%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeByActuator%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeByActuator%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22hasSample%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AhasSample%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isSampleOf%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AisSampleOf%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeSampling%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeSampling%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeBySampler%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeBySampler%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22hasFeatureOfInterest%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AhasFeatureOfInterest%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isFeatureOfInterestOf%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AisFeatureOfInterestOf%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22hasResult%22%3A+%22sosa%3AhasResult%22%2C%0A++++%22isResultOf%22%3A+%22sosa%3AisResultOf%22%2C%0A++++%22hasSimpleResult%22%3A+%22sosa%3AhasSimpleResult%22%2C%0A++++%22resultTime%22%3A+%22sosa%3AresultTime%22%2C%0A++++%22usedProcedure%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AusedProcedure%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22hosts%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3Ahosts%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isHostedBy%22%3A+%22sosa%3AisHostedBy%22%2C%0A++++%22isProxyFor%22%3A+%22ssn%3AisProxyFor%22%2C%0A++++%22wasOriginatedBy%22%3A+%22ssn%3AwasOriginatedBy%22%2C%0A++++%22detects%22%3A+%22ssn%3Adetects%22%2C%0A++++%22hasProperty%22%3A+%22ssn%3AhasProperty%22%2C%0A++++%22isPropertyOf%22%3A+%22ssn%3AisPropertyOf%22%2C%0A++++%22forProperty%22%3A+%22ssn%3AforProperty%22%2C%0A++++%22implements%22%3A+%22ssn%3Aimplements%22%2C%0A++++%22implementedBy%22%3A+%22ssn%3AimplementedBy%22%2C%0A++++%22hasInput%22%3A+%22ssn%3AhasInput%22%2C%0A++++%22hasOutput%22%3A+%22ssn%3AhasOutput%22%2C%0A++++%22hasSubSystem%22%3A+%22ssn%3AhasSubSystem%22%2C%0A++++%22deployedSystem%22%3A+%22ssn%3AdeployedSystem%22%2C%0A++++%22hasDeployment%22%3A+%22ssn%3AhasDeployment%22%2C%0A++++%22deployedOnPlatform%22%3A+%22ssn%3AdeployedOnPlatform%22%2C%0A++++%22inDeployment%22%3A+%22ssn%3AinDeployment%22%2C%0A++++%22inCondition%22%3A+%22ssn%3Asystems%2FinCondition%22%2C%0A++++%22hasSystemCapability%22%3A+%22ssn%3Asystems%2FhasSystemCapability%22%2C%0A++++%22hasSystemProperty%22%3A+%22ssn%3Asystems%2FhasSystemProperty%22%2C%0A++++%22hasOperatingRange%22%3A+%22ssn%3Asystems%2FhasOperatingRange%22%2C%0A++++%22hasOperatingProperty%22%3A+%22ssn%3Asystems%2FhasOperatingProperty%22%2C%0A++++%22hasSurvivalRange%22%3A+%22ssn%3Asystems%2FhasSurvivalRange%22%2C%0A++++%22hasSurvivalProperty%22%3A+%22ssn%3Asystems%2FhasSurvivalProperty%22%2C%0A++++%22qualityOfObservation%22%3A+%22ssn%3Asystems%2FqualityOfObservation%22%2C%0A++++%22hasMember%22%3A+%22sosa%3AhasMember%22%2C%0A++++%22featureType%22%3A+%22%40type%22%2C%0A++++%22position%22%3A+%7B%0A++++++%22%40id%22%3A+%22geopose%3Aposition%22%2C%0A++++++%22%40context%22%3A+%7B%0A++++++++%22lat%22%3A+%22geo%3Alat%22%2C%0A++++++++%22lon%22%3A+%22geo%3Along%22%2C%0A++++++++%22h%22%3A+%22geopose%3Ah%22%0A++++++%7D%0A++++%7D%2C%0A++++%22angles%22%3A+%7B%0A++++++%22%40id%22%3A+%22geopose%3Aangles%22%2C%0A++++++%22%40context%22%3A+%7B%0A++++++++%22yaw%22%3A+%22geopose%3Ayaw%22%2C%0A++++++++%22pitch%22%3A+%22geopose%3Apitch%22%2C%0A++++++++%22roll%22%3A+%22geopose%3Aroll%22%0A++++++%7D%0A++++%7D%2C%0A++++%22distance%22%3A+%7B%0A++++++%22%40id%22%3A+%22http%3A%2F%2Fexample.com%2Fproperties%2Fdistance%22%2C%0A++++++%22%40type%22%3A+%22http%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%22%0A++++%7D%2C%0A++++%22geojson%22%3A+%22https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23%22%2C%0A++++%22rdfs%22%3A+%22http%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%22%2C%0A++++%22sosa%22%3A+%22http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2F%22%2C%0A++++%22ssn%22%3A+%22http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2F%22%2C%0A++++%22ssn-system%22%3A+%22ssn%3Asystems%2F%22%2C%0A++++%22geopose%22%3A+%22http%3A%2F%2Fexample.com%2Fgeopose%2F%22%2C%0A++++%22geo%22%3A+%22http%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23%22%2C%0A++++%22%40version%22%3A+1.1%0A++%7D%0A%7D">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path:
<code><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/HEAD/_sources/examples/vectorObservationFeature" target="_blank">_sources/examples/vectorObservationFeature</a></code>

