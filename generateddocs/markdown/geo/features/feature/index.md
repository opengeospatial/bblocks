# Feature (Schema)

*Version 1.0*

A feature. Every feature is a sub-resource of an OGC Collection.

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

## Description

A feature is an abstraction of real world phenomena [ISO 19101-1:2014].

The GeoJSON representation is the currently recommended representation that all APIs should support, where GeoJSON can
be used for the data.

Each GeoJSON feature includes the following JSON members:

* `type`: fixed value "Feature".
* `geometry`: the primary geometry of the feature describing its location as a GeoJSON geometry object. `null`, if the
  feature has no spatial geometry.
* `properties`: an object with a member for each feature property.
## Schema

[schema.yaml](https://opengeospatial.github.io/bblocks/registereditems/geo/features/feature/schema.yaml)

```yaml
allOf:
  - $ref: bblocks://r1.geo.common.data_types.geojson
  - type: object
    properties:
      links:
        type: array
        items:
          $ref: bblocks://r1.ogc-utils.json-link

```
## Sources

* [OGC API - Features, Part 1, 7.16.2: Feature Response](https://docs.ogc.org/is/17-069r3/17-069r3.html#_response_7)
* [ISO 19101-1:2014 - Geographic information - Reference model - Part 1: Fundamentals](https://www.iso.org/standard/59164.html)
