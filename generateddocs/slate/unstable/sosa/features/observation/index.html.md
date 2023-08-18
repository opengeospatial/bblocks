---
title: SOSA Observation Feature (Schema)

language_tabs:
  - json: JSON
  - turtle: RDF/Turtle
  - jsonld: JSON-LD

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

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/unstable/sosa/features/observation/" target="_blank">valid</a></strong>
</aside>

# Examples

## Example of SOSA observation


```json
{
  "@id": "pop1999",
  "type": "Feature",
  "featureType": "sosa:Observation",
  "geometry": null,
  "properties": {
    "observedProperty": "https://dbpedia.org/ontology/population",
    "resultTime": "1999",
    "comment": "Example of an inline membership - would entail hasMember relations",
    "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Spanish%20Fork",
    "hasSimpleResult": 15555.0
  }
}
```

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;data=%7B%0A++%22%40id%22%3A+%22pop1999%22%2C%0A++%22type%22%3A+%22Feature%22%2C%0A++%22featureType%22%3A+%22sosa%3AObservation%22%2C%0A++%22geometry%22%3A+null%2C%0A++%22properties%22%3A+%7B%0A++++%22observedProperty%22%3A+%22https%3A%2F%2Fdbpedia.org%2Fontology%2Fpopulation%22%2C%0A++++%22resultTime%22%3A+%221999%22%2C%0A++++%22comment%22%3A+%22Example+of+an+inline+membership+-+would+entail+hasMember+relations%22%2C%0A++++%22hasFeatureOfInterest%22%3A+%22https%3A%2F%2Fdemo.pygeoapi.io%2Fmaster%2Fcollections%2Futah_city_locations%2Fitems%2FSpanish%2520Fork%22%2C%0A++++%22hasSimpleResult%22%3A+15555.0%0A++%7D%0A%7D">View on JSON Viewer</a></p>
</blockquote>



```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
_:a1 a geojson:Feature, sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 33 ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime
.
```


```jsonld
{
  "@id": "pop1999",
  "type": "Feature",
  "featureType": "sosa:Observation",
  "geometry": null,
  "properties": {
    "observedProperty": "https://dbpedia.org/ontology/population",
    "resultTime": "1999",
    "comment": "Example of an inline membership - would entail hasMember relations",
    "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Spanish%20Fork",
    "hasSimpleResult": 15555.0
  },
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40id%22%3A+%22pop1999%22%2C%0A++%22type%22%3A+%22Feature%22%2C%0A++%22featureType%22%3A+%22sosa%3AObservation%22%2C%0A++%22geometry%22%3A+null%2C%0A++%22properties%22%3A+%7B%0A++++%22observedProperty%22%3A+%22https%3A%2F%2Fdbpedia.org%2Fontology%2Fpopulation%22%2C%0A++++%22resultTime%22%3A+%221999%22%2C%0A++++%22comment%22%3A+%22Example+of+an+inline+membership+-+would+entail+hasMember+relations%22%2C%0A++++%22hasFeatureOfInterest%22%3A+%22https%3A%2F%2Fdemo.pygeoapi.io%2Fmaster%2Fcollections%2Futah_city_locations%2Fitems%2FSpanish%2520Fork%22%2C%0A++++%22hasSimpleResult%22%3A+15555.0%0A++%7D%2C%0A++%22%40context%22%3A+%22https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Funstable%2Fsosa%2Ffeatures%2Fobservation%2Fcontext.jsonld%22%0A%7D">View on JSON-LD Playground</a></p>
</blockquote>



# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: SOSA Observation Feature
type: object
allOf:
- $ref: ../../../../geo/json-fg/feature-lenient/schema.yaml
- type: object
  properties:
    properties:
      $ref: ../../properties/observation/schema.yaml
      x-jsonld-id: '@nest'
x-jsonld-extra-terms:
  Observation: http://www.w3.org/ns/sosa/Observation
  Sample: http://www.w3.org/ns/sosa/Sample
  observedProperty: http://www.w3.org/ns/sosa/observedProperty
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  observes:
    x-jsonld-id: http://www.w3.org/ns/sosa/observes
    x-jsonld-type: '@id'
  isObservedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isObservedBy
    x-jsonld-type: '@id'
  madeObservation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
    x-jsonld-type: '@id'
  madeBySensor:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
    x-jsonld-type: '@id'
  actsOnProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/actsOnProperty
    x-jsonld-type: '@id'
  isActedOnBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isActedOnBy
    x-jsonld-type: '@id'
  madeActuation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeActuation
    x-jsonld-type: '@id'
  madeByActuator:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeByActuator
    x-jsonld-type: '@id'
  hasSample:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasSample
    x-jsonld-type: '@id'
  isSampleOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isSampleOf
    x-jsonld-type: '@id'
  madeSampling:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeSampling
    x-jsonld-type: '@id'
  madeBySampler:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySampler
    x-jsonld-type: '@id'
  hasFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    x-jsonld-type: '@id'
  isFeatureOfInterestOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    x-jsonld-type: '@id'
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  resultTime: http://www.w3.org/ns/sosa/resultTime
  usedProcedure:
    x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
    x-jsonld-type: '@id'
  hosts:
    x-jsonld-id: http://www.w3.org/ns/sosa/hosts
    x-jsonld-type: '@id'
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  isProxyFor: http://www.w3.org/ns/ssn/isProxyFor
  wasOriginatedBy: http://www.w3.org/ns/ssn/wasOriginatedBy
  detects: http://www.w3.org/ns/ssn/detects
  hasProperty: http://www.w3.org/ns/ssn/hasProperty
  isPropertyOf: http://www.w3.org/ns/ssn/isPropertyOf
  forProperty: http://www.w3.org/ns/ssn/forProperty
  implements: http://www.w3.org/ns/ssn/implements
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  hasInput: http://www.w3.org/ns/ssn/hasInput
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  inCondition: http://www.w3.org/ns/ssn/systems/inCondition
  hasSystemCapability: http://www.w3.org/ns/ssn/systems/hasSystemCapability
  hasSystemProperty: http://www.w3.org/ns/ssn/systems/hasSystemProperty
  hasOperatingRange: http://www.w3.org/ns/ssn/systems/hasOperatingRange
  hasOperatingProperty: http://www.w3.org/ns/ssn/systems/hasOperatingProperty
  hasSurvivalRange: http://www.w3.org/ns/ssn/systems/hasSurvivalRange
  hasSurvivalProperty: http://www.w3.org/ns/ssn/systems/hasSurvivalProperty
  qualityOfObservation: http://www.w3.org/ns/ssn/systems/qualityOfObservation
  hasMember: http://www.w3.org/ns/sosa/hasMember
  features: http://www.w3.org/ns/sosa/hasMember
  featureType: '@type'
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn: http://www.w3.org/ns/ssn/
  ssn-system: http://www.w3.org/ns/ssn/systems/

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;data=%24schema%3A+https%3A%2F%2Fjson-schema.org%2Fdraft%2F2020-12%2Fschema%0Adescription%3A+SOSA+Observation+Feature%0Atype%3A+object%0AallOf%3A%0A-+%24ref%3A+..%2F..%2F..%2F..%2Fgeo%2Fjson-fg%2Ffeature-lenient%2Fschema.yaml%0A-+type%3A+object%0A++properties%3A%0A++++properties%3A%0A++++++%24ref%3A+..%2F..%2Fproperties%2Fobservation%2Fschema.yaml%0A++++++x-jsonld-id%3A+%27%40nest%27%0Ax-jsonld-extra-terms%3A%0A++Observation%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FObservation%0A++Sample%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FSample%0A++observedProperty%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FobservedProperty%0A++phenomenonTime%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FphenomenonTime%0A++observes%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2Fobserves%0A++++x-jsonld-type%3A+%27%40id%27%0A++isObservedBy%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FisObservedBy%0A++++x-jsonld-type%3A+%27%40id%27%0A++madeObservation%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FmadeObservation%0A++++x-jsonld-type%3A+%27%40id%27%0A++madeBySensor%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FmadeBySensor%0A++++x-jsonld-type%3A+%27%40id%27%0A++actsOnProperty%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FactsOnProperty%0A++++x-jsonld-type%3A+%27%40id%27%0A++isActedOnBy%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FisActedOnBy%0A++++x-jsonld-type%3A+%27%40id%27%0A++madeActuation%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FmadeActuation%0A++++x-jsonld-type%3A+%27%40id%27%0A++madeByActuator%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FmadeByActuator%0A++++x-jsonld-type%3A+%27%40id%27%0A++hasSample%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FhasSample%0A++++x-jsonld-type%3A+%27%40id%27%0A++isSampleOf%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FisSampleOf%0A++++x-jsonld-type%3A+%27%40id%27%0A++madeSampling%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FmadeSampling%0A++++x-jsonld-type%3A+%27%40id%27%0A++madeBySampler%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FmadeBySampler%0A++++x-jsonld-type%3A+%27%40id%27%0A++hasFeatureOfInterest%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FhasFeatureOfInterest%0A++++x-jsonld-type%3A+%27%40id%27%0A++isFeatureOfInterestOf%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FisFeatureOfInterestOf%0A++++x-jsonld-type%3A+%27%40id%27%0A++hasResult%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FhasResult%0A++isResultOf%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FisResultOf%0A++hasSimpleResult%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FhasSimpleResult%0A++resultTime%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FresultTime%0A++usedProcedure%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FusedProcedure%0A++++x-jsonld-type%3A+%27%40id%27%0A++hosts%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2Fhosts%0A++++x-jsonld-type%3A+%27%40id%27%0A++isHostedBy%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FisHostedBy%0A++isProxyFor%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FisProxyFor%0A++wasOriginatedBy%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FwasOriginatedBy%0A++detects%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fdetects%0A++hasProperty%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FhasProperty%0A++isPropertyOf%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FisPropertyOf%0A++forProperty%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FforProperty%0A++implements%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fimplements%0A++implementedBy%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FimplementedBy%0A++hasInput%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FhasInput%0A++hasOutput%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FhasOutput%0A++hasSubSystem%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FhasSubSystem%0A++deployedSystem%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FdeployedSystem%0A++hasDeployment%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FhasDeployment%0A++deployedOnPlatform%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FdeployedOnPlatform%0A++inDeployment%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FinDeployment%0A++inCondition%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FinCondition%0A++hasSystemCapability%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FhasSystemCapability%0A++hasSystemProperty%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FhasSystemProperty%0A++hasOperatingRange%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FhasOperatingRange%0A++hasOperatingProperty%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FhasOperatingProperty%0A++hasSurvivalRange%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FhasSurvivalRange%0A++hasSurvivalProperty%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FhasSurvivalProperty%0A++qualityOfObservation%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FqualityOfObservation%0A++hasMember%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FhasMember%0A++features%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FhasMember%0A++featureType%3A+%27%40type%27%0Ax-jsonld-prefixes%3A%0A++sosa%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2F%0A++ssn%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2F%0A++ssn-system%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2F%0A">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/schema.json</a>


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
      "@id": "geojson:features"
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
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "ssn:systems/",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%7B%0A++++%22type%22%3A+%22%40type%22%2C%0A++++%22id%22%3A+%22%40id%22%2C%0A++++%22properties%22%3A+%7B%0A++++++%22%40id%22%3A+%22%40nest%22%2C%0A++++++%22%40context%22%3A+%7B%0A++++++++%22features%22%3A+%22sosa%3AhasMember%22%2C%0A++++++++%22properties%22%3A+%22%40nest%22%0A++++++%7D%0A++++%7D%2C%0A++++%22geometry%22%3A+%7B%0A++++++%22%40id%22%3A+%22geojson%3Ageometry%22%2C%0A++++++%22%40context%22%3A+%7B%7D%0A++++%7D%2C%0A++++%22bbox%22%3A+%7B%0A++++++%22%40container%22%3A+%22%40list%22%2C%0A++++++%22%40id%22%3A+%22geojson%3Abbox%22%0A++++%7D%2C%0A++++%22Feature%22%3A+%22geojson%3AFeature%22%2C%0A++++%22FeatureCollection%22%3A+%22geojson%3AFeatureCollection%22%2C%0A++++%22GeometryCollection%22%3A+%22geojson%3AGeometryCollection%22%2C%0A++++%22LineString%22%3A+%22geojson%3ALineString%22%2C%0A++++%22MultiLineString%22%3A+%22geojson%3AMultiLineString%22%2C%0A++++%22MultiPoint%22%3A+%22geojson%3AMultiPoint%22%2C%0A++++%22MultiPolygon%22%3A+%22geojson%3AMultiPolygon%22%2C%0A++++%22Point%22%3A+%22geojson%3APoint%22%2C%0A++++%22Polygon%22%3A+%22geojson%3APolygon%22%2C%0A++++%22features%22%3A+%7B%0A++++++%22%40container%22%3A+%22%40set%22%2C%0A++++++%22%40id%22%3A+%22geojson%3Afeatures%22%0A++++%7D%2C%0A++++%22links%22%3A+%7B%0A++++++%22%40id%22%3A+%22rdfs%3AseeAlso%22%2C%0A++++++%22%40context%22%3A+%7B%0A++++++++%22href%22%3A+%22%40id%22%2C%0A++++++++%22title%22%3A+%22rdfs%3Alabel%22%0A++++++%7D%0A++++%7D%2C%0A++++%22coordinates%22%3A+%7B%0A++++++%22%40container%22%3A+%22%40list%22%2C%0A++++++%22%40id%22%3A+%22geojson%3Acoordinates%22%0A++++%7D%2C%0A++++%22Observation%22%3A+%22sosa%3AObservation%22%2C%0A++++%22Sample%22%3A+%22sosa%3ASample%22%2C%0A++++%22observedProperty%22%3A+%22sosa%3AobservedProperty%22%2C%0A++++%22phenomenonTime%22%3A+%22sosa%3AphenomenonTime%22%2C%0A++++%22observes%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3Aobserves%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isObservedBy%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AisObservedBy%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeObservation%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeObservation%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeBySensor%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeBySensor%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22actsOnProperty%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AactsOnProperty%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isActedOnBy%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AisActedOnBy%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeActuation%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeActuation%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeByActuator%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeByActuator%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22hasSample%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AhasSample%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isSampleOf%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AisSampleOf%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeSampling%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeSampling%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeBySampler%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeBySampler%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22hasFeatureOfInterest%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AhasFeatureOfInterest%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isFeatureOfInterestOf%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AisFeatureOfInterestOf%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22hasResult%22%3A+%22sosa%3AhasResult%22%2C%0A++++%22isResultOf%22%3A+%22sosa%3AisResultOf%22%2C%0A++++%22hasSimpleResult%22%3A+%22sosa%3AhasSimpleResult%22%2C%0A++++%22resultTime%22%3A+%22sosa%3AresultTime%22%2C%0A++++%22usedProcedure%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AusedProcedure%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22hosts%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3Ahosts%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isHostedBy%22%3A+%22sosa%3AisHostedBy%22%2C%0A++++%22isProxyFor%22%3A+%22ssn%3AisProxyFor%22%2C%0A++++%22wasOriginatedBy%22%3A+%22ssn%3AwasOriginatedBy%22%2C%0A++++%22detects%22%3A+%22ssn%3Adetects%22%2C%0A++++%22hasProperty%22%3A+%22ssn%3AhasProperty%22%2C%0A++++%22isPropertyOf%22%3A+%22ssn%3AisPropertyOf%22%2C%0A++++%22forProperty%22%3A+%22ssn%3AforProperty%22%2C%0A++++%22implements%22%3A+%22ssn%3Aimplements%22%2C%0A++++%22implementedBy%22%3A+%22ssn%3AimplementedBy%22%2C%0A++++%22hasInput%22%3A+%22ssn%3AhasInput%22%2C%0A++++%22hasOutput%22%3A+%22ssn%3AhasOutput%22%2C%0A++++%22hasSubSystem%22%3A+%22ssn%3AhasSubSystem%22%2C%0A++++%22deployedSystem%22%3A+%22ssn%3AdeployedSystem%22%2C%0A++++%22hasDeployment%22%3A+%22ssn%3AhasDeployment%22%2C%0A++++%22deployedOnPlatform%22%3A+%22ssn%3AdeployedOnPlatform%22%2C%0A++++%22inDeployment%22%3A+%22ssn%3AinDeployment%22%2C%0A++++%22inCondition%22%3A+%22ssn%3Asystems%2FinCondition%22%2C%0A++++%22hasSystemCapability%22%3A+%22ssn%3Asystems%2FhasSystemCapability%22%2C%0A++++%22hasSystemProperty%22%3A+%22ssn%3Asystems%2FhasSystemProperty%22%2C%0A++++%22hasOperatingRange%22%3A+%22ssn%3Asystems%2FhasOperatingRange%22%2C%0A++++%22hasOperatingProperty%22%3A+%22ssn%3Asystems%2FhasOperatingProperty%22%2C%0A++++%22hasSurvivalRange%22%3A+%22ssn%3Asystems%2FhasSurvivalRange%22%2C%0A++++%22hasSurvivalProperty%22%3A+%22ssn%3Asystems%2FhasSurvivalProperty%22%2C%0A++++%22qualityOfObservation%22%3A+%22ssn%3Asystems%2FqualityOfObservation%22%2C%0A++++%22hasMember%22%3A+%22sosa%3AhasMember%22%2C%0A++++%22featureType%22%3A+%22%40type%22%2C%0A++++%22geojson%22%3A+%22https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23%22%2C%0A++++%22rdfs%22%3A+%22http%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%22%2C%0A++++%22sosa%22%3A+%22http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2F%22%2C%0A++++%22ssn%22%3A+%22http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2F%22%2C%0A++++%22ssn-system%22%3A+%22ssn%3Asystems%2F%22%2C%0A++++%22%40version%22%3A+1.1%0A++%7D%0A%7D">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/features/observation/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path:
<code><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/HEAD/_sources/features/observation" target="_blank">_sources/features/observation</a></code>

