---
title: OGC Features and Geometries JSON (Schema)

toc_footers:
  - Version 0.1
  - <a href='#'>OGC Features and Geometries JSON</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: OGC Features and Geometries JSON (Schema)
---


# OGC Features and Geometries JSON

A OGC Features and Geometries JSON (JSON-FG) Feature, extending GeoJSON to support a limited set of additional capabilities that are out-of-scope for GeoJSON, but that are important for a variety of use cases involving feature data.

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Proposal

# Description

OGC Features and Geometries JSON (JSON-FG) extends GeoJSON to support a limited set of additional capabilities that are
out-of-scope for GeoJSON, but that are essential or important for a variety of use cases involving feature data.
A **feature collection** contains a set of features from a dataset.

Information that can be represented as GeoJSON is encoded as GeoJSON. Additional information is mainly encoded in
additional top-level members of GeoJSON objects. The members use keys that do not conflict with GeoJSON including the
obsolete version that pre-dates the IETF standard. GeoJSON clients will be able to parse and understand all aspects that
are specified by GeoJSON, JSON-FG clients will also parse and understand the additional capabilities.

This Standard specifies the following minimal extensions to the GeoJSON Standard:

* The ability to use Coordinate Reference Systems (CRSs) other than WGS 84;
* The ability to use non-Euclidean metrics, in particular ellipsoidal metrics;
* Support for solids and prisms as geometry types;
* The ability to encode temporal characteristics of a feature; and
* The ability to declare the type and the schema of a feature.

Information that can be represented as GeoJSON is encoded as GeoJSON. Additional information is mainly encoded in
additional members of the GeoJSON objects. The additional members use keys that do not conflict with GeoJSON. This is so
existing and future GeoJSON clients will continue to parse and understand GeoJSON content. JSON-FG enabled clients will
also be able to parse and understand the additional members.

JSON Schema is used to formally specify the JSON-FG syntax.

# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2019-09/schema
$id: https://beta.schemas.opengis.net/json-fg/featurecollection.json
title: a JSON-FG Feature Collection
description: This JSON Schema is part of JSON-FG version 0.1.1
type: object
required:
- type
- features
properties:
  type:
    type: string
    enum:
    - FeatureCollection
  featureType:
    $ref: featuretype.json
  geometryDimension:
    type: integer
    minimum: 0
    maximum: 3
  coordRefSys:
    $ref: coordrefsys.json
  links:
    type: array
    items:
      $ref: link.json
  features:
    type: array
    items:
      $ref: feature.json

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.yaml" target="_blank">schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.json" target="_blank">schema.json</a>

# References

* [OGC Testbed-17: OGC Features and Geometries JSON Engineering Report](http://docs.ogc.org/per/21-017r1.html)