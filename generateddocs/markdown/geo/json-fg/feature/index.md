# JSON-FG Feature (Schema)

*Version 0.1*

A OGC Features and Geometries JSON (JSON-FG) Feature, extending GeoJSON to support a limited set of additional capabilities that are out-of-scope for GeoJSON, but that are important for a variety of use cases involving feature data.

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Proposal

## Description

OGC Features and Geometries JSON (JSON-FG) extends GeoJSON to support a limited set of additional capabilities that are
out-of-scope for GeoJSON, but that are essential or important for a variety of use cases involving feature data.

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
## Schema

```yaml
allOf:
- $ref: ../../features/feature/schema.yaml
- $ref: https://beta.schemas.opengis.net/json-fg/feature.json

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature/schema.yaml)

## Sources

* [OGC Testbed-17: OGC Features and Geometries JSON Engineering Report](http://docs.ogc.org/per/21-017r1.html)
