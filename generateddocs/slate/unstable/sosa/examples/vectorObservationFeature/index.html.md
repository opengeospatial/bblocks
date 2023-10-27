---
title: Example SOSA Vector Observation Feature (Schema)


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

## VectorObservation - specialisation example.



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
                -111.71,
                40.156709946862874
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
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/unstable/sosa/examples/vectorObservationFeature/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Funstable%2Fsosa%2Fexamples%2FvectorObservationFeature%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>



## VectorObservationCollection



```json
{
    "@context": {
    "resultschema": "http://example.org/resultschema/",
    "pose": "resultschema:pose",
    "distance": {
      "@id": "resultschema:distance"
    }
  },
  "@id": "c1",
  "type": "FeatureCollection",
  "featureType": "sosa:ObservationCollection",
  "properties": {
    "resultTime": "1999"
  },
  "features": [
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
  ]
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/unstable/sosa/examples/vectorObservationFeature/example_2_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Funstable%2Fsosa%2Fexamples%2FvectorObservationFeature%2Fexample_2_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>



# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: Example SOSA Observation Specialisation - a vector bearing and distance
$defs:
  VectorObservation:
    allOf:
    - $ref: ../../features/observation/schema.yaml
    - type: object
      properties:
        properties:
          $ref: ../vectorObservation/schema.yaml
  VectorObservationCollection:
    allOf:
    - $ref: ../../features/observationCollection/schema.yaml
    - type: object
      properties:
        features:
          type: array
          items:
            $ref: '#/$defs/VectorObservation'
anyOf:
- $ref: '#/$defs/VectorObservation'
- $ref: '#/$defs/VectorObservationCollection'

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Funstable%2Fsosa%2Fexamples%2FvectorObservationFeature%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/examples/vectorObservationFeature/schema.json</a>

# Validation

## SHACL Shapes

The following SHACL shapes are used for validating this building block:

* [https://opengeospatial.github.io/bblocks/registereditems/unstable/sosa/_sources/examples/vectorObservationFeature/rules.shacl](https://opengeospatial.github.io/bblocks/registereditems/unstable/sosa/_sources/examples/vectorObservationFeature/rules.shacl)
* [https://opengeospatial.github.io/bblocks/registereditems/unstable/sosa/_sources/properties/observation/rules.shacl](https://opengeospatial.github.io/bblocks/registereditems/unstable/sosa/_sources/properties/observation/rules.shacl)

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path:
<code><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/HEAD/_sources/examples/vectorObservationFeature" target="_blank">_sources/examples/vectorObservationFeature</a></code>

