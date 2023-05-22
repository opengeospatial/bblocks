---
title: SOSA ObservationCollection (Schema)

language_tabs:
  - json
  - ttl

toc_footers:
  - Version 1.0
  - <a href='#'>SOSA ObservationCollection</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: SOSA ObservationCollection (Schema)
---

# Overview

This building blocks defines an ObservationCollection according to the SOSA/SSN v1.1 specification.

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Development

# Description

## SOSA ObservationCollection

Collection of one or more observations, whose members share a common value for one or more properties.
# Examples

## Example of SOSA ObservationCollection

```json
{ 
  "@id": "c1",
  "type": "Feature",
  "featureType": "sosa:ObservationCollection",
  "properties": {
    "hasMember": "_:a1",
    "observedProperty": "_:p1",
    "resultTime": "2022-05-01T22:33:44Z"
  },
}
```

```json
{ 
  "@id": "c1",
  "type": "Feature",
  "featureType": "sosa:ObservationCollection",
  "properties": {
    "observedProperty": "p1",
    "resultTime": "2022-05-01T22:33:44Z",
    "hasMember": [
      { 
        "@id": "a1",
        "comment": "Example of an inline membership - would entail hasMember relations",
        "hasFeatureOfInterest": "http://example.com/fois/1",
      }
    ]
  },
}
```

```ttl
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix eg: <http://example.org/my-feature/> .

eg:c1 a sosa:ObservationCollection ;
  sosa:hasMember eg:a1 ;
  sosa:observedProperty eg:p1 ;
  sosa:resultTime "2022-05-01T22:33:44Z"^^xsd:dateTime ;
.

eg:a1 a sosa:Observation ;
  sosa:hasFeatureOfInterest <http://example.com/fois/1> ;
  sosa:hasSimpleResult 33 ;
.
eg:p1 a skos:Concept;
  skos:prefLabel "Some Observable Property";
.
```

# Schema

[schema.yaml](https://opengeospatial.github.io/bblocks/registereditems/unstable/sosa/_sources/properties/observationCollection/schema.yaml)
# Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)
* [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/)