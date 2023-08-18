---
title: SOSA ObservationCollection (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 1.0
  - <a href='#'>SOSA ObservationCollection</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: SOSA ObservationCollection (Schema)
---


# SOSA ObservationCollection `ogc.unstable.sosa.properties.observationCollection`

This building blocks defines an ObservationCollection according to the SOSA/SSN v1.1 specification.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/invalid" target="_blank" data-rainbow-uri>Invalid</a>
</p>

<aside class="warning">
Validation for this building block has <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/unstable/sosa/properties/observationCollection/" target="_blank">failed</a></strong>
</aside>

# Description

## SOSA ObservationCollection

Collection of one or more observations, whose members share a common value for one or more properties.
# Examples

## Example of SOSA ObservationCollection


```json
{ 
  "hasMember": [
    "_:a1"
  ],
  "observedProperty": "_:p1",
  "resultTime": "2022-05-01T22:33:44Z"
}
```

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;data=%7B+%0A++%22hasMember%22%3A+%5B%0A++++%22_%3Aa1%22%0A++%5D%2C%0A++%22observedProperty%22%3A+%22_%3Ap1%22%2C%0A++%22resultTime%22%3A+%222022-05-01T22%3A33%3A44Z%22%0A%7D">View on JSON Viewer</a></p>
</blockquote>



```jsonld
{
  "hasMember": [
    "_:a1"
  ],
  "observedProperty": "_:p1",
  "resultTime": "2022-05-01T22:33:44Z",
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22hasMember%22%3A+%5B%0A++++%22_%3Aa1%22%0A++%5D%2C%0A++%22observedProperty%22%3A+%22_%3Ap1%22%2C%0A++%22resultTime%22%3A+%222022-05-01T22%3A33%3A44Z%22%2C%0A++%22%40context%22%3A+%22https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Funstable%2Fsosa%2Fproperties%2FobservationCollection%2Fcontext.jsonld%22%0A%7D">View on JSON-LD Playground</a></p>
</blockquote>



```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .

[] sosa:hasMember "_:a1" ;
    sosa:observedProperty "_:p1" ;
    sosa:resultTime "2022-05-01T22:33:44Z" .


```


## Example of SOSA ObservationCollection


```json
{ 
  "observedProperty": "p1",
  "resultTime": "2022-05-01T22:33:44Z",
  "hasMember": [
    { 
      "@id": "a1",
      "comment": "Example of an inline membership - would entail hasMember relations",
      "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
      "hasSimpleResult": 1995.2,
      "phenomenonTime": "2022-05-01T22:33:40Z"
    }
  ]
}
```

<blockquote class="lang-specific json">
<p><a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;data=%7B+%0A++%22observedProperty%22%3A+%22p1%22%2C%0A++%22resultTime%22%3A+%222022-05-01T22%3A33%3A44Z%22%2C%0A++%22hasMember%22%3A+%5B%0A++++%7B+%0A++++++%22%40id%22%3A+%22a1%22%2C%0A++++++%22comment%22%3A+%22Example+of+an+inline+membership+-+would+entail+hasMember+relations%22%2C%0A++++++%22hasFeatureOfInterest%22%3A+%22https%3A%2F%2Fdemo.pygeoapi.io%2Fmaster%2Fcollections%2Futah_city_locations%2Fitems%2FSalem%22%2C%0A++++++%22hasSimpleResult%22%3A+1995.2%2C%0A++++++%22phenomenonTime%22%3A+%222022-05-01T22%3A33%3A40Z%22%0A++++%7D%0A++%5D%0A%7D">View on JSON Viewer</a></p>
</blockquote>



```jsonld
{
  "observedProperty": "p1",
  "resultTime": "2022-05-01T22:33:44Z",
  "hasMember": [
    {
      "@id": "a1",
      "comment": "Example of an inline membership - would entail hasMember relations",
      "hasFeatureOfInterest": "https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem",
      "hasSimpleResult": 1995.2,
      "phenomenonTime": "2022-05-01T22:33:40Z"
    }
  ],
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
<p><a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22observedProperty%22%3A+%22p1%22%2C%0A++%22resultTime%22%3A+%222022-05-01T22%3A33%3A44Z%22%2C%0A++%22hasMember%22%3A+%5B%0A++++%7B%0A++++++%22%40id%22%3A+%22a1%22%2C%0A++++++%22comment%22%3A+%22Example+of+an+inline+membership+-+would+entail+hasMember+relations%22%2C%0A++++++%22hasFeatureOfInterest%22%3A+%22https%3A%2F%2Fdemo.pygeoapi.io%2Fmaster%2Fcollections%2Futah_city_locations%2Fitems%2FSalem%22%2C%0A++++++%22hasSimpleResult%22%3A+1995.2%2C%0A++++++%22phenomenonTime%22%3A+%222022-05-01T22%3A33%3A40Z%22%0A++++%7D%0A++%5D%2C%0A++%22%40context%22%3A+%22https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Funstable%2Fsosa%2Fproperties%2FobservationCollection%2Fcontext.jsonld%22%0A%7D">View on JSON-LD Playground</a></p>
</blockquote>



```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://example.com/a1> sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
    sosa:hasSimpleResult 1.9952e+03 ;
    sosa:phenomenonTime "2022-05-01T22:33:40Z" .

[] sosa:hasMember <http://example.com/a1> ;
    sosa:observedProperty "p1" ;
    sosa:resultTime "2022-05-01T22:33:44Z" .


```


## Turtle example of SOSA ObservationCollection


```turtle
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix eg: <http://example.org/my-feature/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

eg:c1 a sosa:ObservationCollection ;
  sosa:hasMember eg:a1 ;
  sosa:observedProperty eg:p1 ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
  sosa:phenomenonTime "2022-05-01T22:33:40Z"^^xsd:dateTime ;
.

eg:a1 a sosa:Observation ;
  sosa:hasFeatureOfInterest <https://demo.pygeoapi.io/master/collections/utah_city_locations/items/Salem> ;
  sosa:hasSimpleResult 33 ;
.
eg:p1 a skos:Concept;
  skos:prefLabel "Some Observable Property";
.
```


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: SOSA ObservationCollection
type: object
properties:
  resultTime:
    type: string
    format: date-time
    x-jsonld-id: http://www.w3.org/ns/sosa/resultTime
  phenomenonTime:
    type:
    - object
    - string
    x-jsonld-id: http://www.w3.org/ns/sosa/phenomenonTime
  hasFeatureOfInterest:
    type:
    - object
    - string
    x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    x-jsonld-type: '@id'
  observedProperty:
    type:
    - object
    - string
    x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
  usedProcedure:
    type:
    - object
    - string
    x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
    x-jsonld-type: '@id'
  madeBySensor:
    type:
    - object
    - string
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
    x-jsonld-type: '@id'
not:
  anyOf:
  - required:
    - hasResult
  - required:
    - hasSimpleResult
x-jsonld-extra-terms:
  Observation: http://www.w3.org/ns/sosa/Observation
  Sample: http://www.w3.org/ns/sosa/Sample
  observes:
    x-jsonld-id: http://www.w3.org/ns/sosa/observes
    x-jsonld-type: '@id'
  isObservedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isObservedBy
    x-jsonld-type: '@id'
  madeObservation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
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
  isFeatureOfInterestOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    x-jsonld-type: '@id'
  hasResult: http://www.w3.org/ns/sosa/hasResult
  isResultOf: http://www.w3.org/ns/sosa/isResultOf
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
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
  properties: '@nest'
  featureType: '@type'
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  ssn: http://www.w3.org/ns/ssn/
  ssn-system: http://www.w3.org/ns/ssn/systems/

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;data=%24schema%3A+https%3A%2F%2Fjson-schema.org%2Fdraft%2F2020-12%2Fschema%0Adescription%3A+SOSA+ObservationCollection%0Atype%3A+object%0Aproperties%3A%0A++resultTime%3A%0A++++type%3A+string%0A++++format%3A+date-time%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FresultTime%0A++phenomenonTime%3A%0A++++type%3A%0A++++-+object%0A++++-+string%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FphenomenonTime%0A++hasFeatureOfInterest%3A%0A++++type%3A%0A++++-+object%0A++++-+string%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FhasFeatureOfInterest%0A++++x-jsonld-type%3A+%27%40id%27%0A++observedProperty%3A%0A++++type%3A%0A++++-+object%0A++++-+string%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FobservedProperty%0A++usedProcedure%3A%0A++++type%3A%0A++++-+object%0A++++-+string%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FusedProcedure%0A++++x-jsonld-type%3A+%27%40id%27%0A++madeBySensor%3A%0A++++type%3A%0A++++-+object%0A++++-+string%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FmadeBySensor%0A++++x-jsonld-type%3A+%27%40id%27%0Anot%3A%0A++anyOf%3A%0A++-+required%3A%0A++++-+hasResult%0A++-+required%3A%0A++++-+hasSimpleResult%0Ax-jsonld-extra-terms%3A%0A++Observation%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FObservation%0A++Sample%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FSample%0A++observes%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2Fobserves%0A++++x-jsonld-type%3A+%27%40id%27%0A++isObservedBy%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FisObservedBy%0A++++x-jsonld-type%3A+%27%40id%27%0A++madeObservation%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FmadeObservation%0A++++x-jsonld-type%3A+%27%40id%27%0A++actsOnProperty%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FactsOnProperty%0A++++x-jsonld-type%3A+%27%40id%27%0A++isActedOnBy%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FisActedOnBy%0A++++x-jsonld-type%3A+%27%40id%27%0A++madeActuation%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FmadeActuation%0A++++x-jsonld-type%3A+%27%40id%27%0A++madeByActuator%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FmadeByActuator%0A++++x-jsonld-type%3A+%27%40id%27%0A++hasSample%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FhasSample%0A++++x-jsonld-type%3A+%27%40id%27%0A++isSampleOf%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FisSampleOf%0A++++x-jsonld-type%3A+%27%40id%27%0A++madeSampling%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FmadeSampling%0A++++x-jsonld-type%3A+%27%40id%27%0A++madeBySampler%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FmadeBySampler%0A++++x-jsonld-type%3A+%27%40id%27%0A++isFeatureOfInterestOf%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FisFeatureOfInterestOf%0A++++x-jsonld-type%3A+%27%40id%27%0A++hasResult%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FhasResult%0A++isResultOf%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FisResultOf%0A++hasSimpleResult%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FhasSimpleResult%0A++hosts%3A%0A++++x-jsonld-id%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2Fhosts%0A++++x-jsonld-type%3A+%27%40id%27%0A++isHostedBy%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FisHostedBy%0A++isProxyFor%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FisProxyFor%0A++wasOriginatedBy%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FwasOriginatedBy%0A++detects%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fdetects%0A++hasProperty%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FhasProperty%0A++isPropertyOf%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FisPropertyOf%0A++forProperty%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FforProperty%0A++implements%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fimplements%0A++implementedBy%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FimplementedBy%0A++hasInput%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FhasInput%0A++hasOutput%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FhasOutput%0A++hasSubSystem%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FhasSubSystem%0A++deployedSystem%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FdeployedSystem%0A++hasDeployment%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FhasDeployment%0A++deployedOnPlatform%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FdeployedOnPlatform%0A++inDeployment%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2FinDeployment%0A++inCondition%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FinCondition%0A++hasSystemCapability%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FhasSystemCapability%0A++hasSystemProperty%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FhasSystemProperty%0A++hasOperatingRange%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FhasOperatingRange%0A++hasOperatingProperty%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FhasOperatingProperty%0A++hasSurvivalRange%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FhasSurvivalRange%0A++hasSurvivalProperty%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FhasSurvivalProperty%0A++qualityOfObservation%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2FqualityOfObservation%0A++hasMember%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FhasMember%0A++features%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2FhasMember%0A++properties%3A+%27%40nest%27%0A++featureType%3A+%27%40type%27%0Ax-jsonld-prefixes%3A%0A++sosa%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2F%0A++ssn%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2F%0A++ssn-system%3A+http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2Fsystems%2F%0A">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
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
    "Observation": "sosa:Observation",
    "Sample": "sosa:Sample",
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
    "isFeatureOfInterestOf": {
      "@id": "sosa:isFeatureOfInterestOf",
      "@type": "@id"
    },
    "hasResult": "sosa:hasResult",
    "isResultOf": "sosa:isResultOf",
    "hasSimpleResult": "sosa:hasSimpleResult",
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
    "features": "sosa:hasMember",
    "properties": "@nest",
    "featureType": "@type",
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "ssn:systems/",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%7B%0A++++%22resultTime%22%3A+%22sosa%3AresultTime%22%2C%0A++++%22phenomenonTime%22%3A+%22sosa%3AphenomenonTime%22%2C%0A++++%22hasFeatureOfInterest%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AhasFeatureOfInterest%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22observedProperty%22%3A+%22sosa%3AobservedProperty%22%2C%0A++++%22usedProcedure%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AusedProcedure%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeBySensor%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeBySensor%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22Observation%22%3A+%22sosa%3AObservation%22%2C%0A++++%22Sample%22%3A+%22sosa%3ASample%22%2C%0A++++%22observes%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3Aobserves%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isObservedBy%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AisObservedBy%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeObservation%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeObservation%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22actsOnProperty%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AactsOnProperty%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isActedOnBy%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AisActedOnBy%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeActuation%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeActuation%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeByActuator%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeByActuator%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22hasSample%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AhasSample%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isSampleOf%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AisSampleOf%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeSampling%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeSampling%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22madeBySampler%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AmadeBySampler%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isFeatureOfInterestOf%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3AisFeatureOfInterestOf%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22hasResult%22%3A+%22sosa%3AhasResult%22%2C%0A++++%22isResultOf%22%3A+%22sosa%3AisResultOf%22%2C%0A++++%22hasSimpleResult%22%3A+%22sosa%3AhasSimpleResult%22%2C%0A++++%22hosts%22%3A+%7B%0A++++++%22%40id%22%3A+%22sosa%3Ahosts%22%2C%0A++++++%22%40type%22%3A+%22%40id%22%0A++++%7D%2C%0A++++%22isHostedBy%22%3A+%22sosa%3AisHostedBy%22%2C%0A++++%22isProxyFor%22%3A+%22ssn%3AisProxyFor%22%2C%0A++++%22wasOriginatedBy%22%3A+%22ssn%3AwasOriginatedBy%22%2C%0A++++%22detects%22%3A+%22ssn%3Adetects%22%2C%0A++++%22hasProperty%22%3A+%22ssn%3AhasProperty%22%2C%0A++++%22isPropertyOf%22%3A+%22ssn%3AisPropertyOf%22%2C%0A++++%22forProperty%22%3A+%22ssn%3AforProperty%22%2C%0A++++%22implements%22%3A+%22ssn%3Aimplements%22%2C%0A++++%22implementedBy%22%3A+%22ssn%3AimplementedBy%22%2C%0A++++%22hasInput%22%3A+%22ssn%3AhasInput%22%2C%0A++++%22hasOutput%22%3A+%22ssn%3AhasOutput%22%2C%0A++++%22hasSubSystem%22%3A+%22ssn%3AhasSubSystem%22%2C%0A++++%22deployedSystem%22%3A+%22ssn%3AdeployedSystem%22%2C%0A++++%22hasDeployment%22%3A+%22ssn%3AhasDeployment%22%2C%0A++++%22deployedOnPlatform%22%3A+%22ssn%3AdeployedOnPlatform%22%2C%0A++++%22inDeployment%22%3A+%22ssn%3AinDeployment%22%2C%0A++++%22inCondition%22%3A+%22ssn%3Asystems%2FinCondition%22%2C%0A++++%22hasSystemCapability%22%3A+%22ssn%3Asystems%2FhasSystemCapability%22%2C%0A++++%22hasSystemProperty%22%3A+%22ssn%3Asystems%2FhasSystemProperty%22%2C%0A++++%22hasOperatingRange%22%3A+%22ssn%3Asystems%2FhasOperatingRange%22%2C%0A++++%22hasOperatingProperty%22%3A+%22ssn%3Asystems%2FhasOperatingProperty%22%2C%0A++++%22hasSurvivalRange%22%3A+%22ssn%3Asystems%2FhasSurvivalRange%22%2C%0A++++%22hasSurvivalProperty%22%3A+%22ssn%3Asystems%2FhasSurvivalProperty%22%2C%0A++++%22qualityOfObservation%22%3A+%22ssn%3Asystems%2FqualityOfObservation%22%2C%0A++++%22hasMember%22%3A+%22sosa%3AhasMember%22%2C%0A++++%22features%22%3A+%22sosa%3AhasMember%22%2C%0A++++%22properties%22%3A+%22%40nest%22%2C%0A++++%22featureType%22%3A+%22%40type%22%2C%0A++++%22sosa%22%3A+%22http%3A%2F%2Fwww.w3.org%2Fns%2Fsosa%2F%22%2C%0A++++%22ssn%22%3A+%22http%3A%2F%2Fwww.w3.org%2Fns%2Fssn%2F%22%2C%0A++++%22ssn-system%22%3A+%22ssn%3Asystems%2F%22%2C%0A++++%22%40version%22%3A+1.1%0A++%7D%0A%7D">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/unstable/sosa/properties/observationCollection/context.jsonld</a>

# References

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/ogcapi-sosa" target="_blank">https://github.com/opengeospatial/ogcapi-sosa</a>
* Path:
<code><a href="https://github.com/opengeospatial/ogcapi-sosa/blob/HEAD/_sources/properties/observationCollection" target="_blank">_sources/properties/observationCollection</a></code>

