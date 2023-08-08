---
title: JSON-FG Feature Collection (Schema)

toc_footers:
  - Version 0.1
  - <a href='#'>JSON-FG Feature Collection</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: JSON-FG Feature Collection (Schema)
---


# JSON-FG Feature Collection `ogc.geo.json-fg.featureCollection`

A collection of OGC Features and Geometries JSON (JSON-FG) Features, extending GeoJSON to support a limited set of additional capabilities that are out-of-scope for GeoJSON, but that are important for a variety of use cases involving feature data.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/stable" target="_blank" data-rainbow-uri>Stable</a>
</p>

<aside class="success">
This building block is <strong>valid</strong>
</aside>

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
    x-jsonld-container: '@set'
    x-jsonld-id: https://purl.org/geojson/vocab#features
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.json</a>

# References

* [OGC Testbed-17: OGC Features and Geometries JSON Engineering Report](http://docs.ogc.org/per/21-017r1.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path: `registereditems/geo/json-fg/featureCollection`

