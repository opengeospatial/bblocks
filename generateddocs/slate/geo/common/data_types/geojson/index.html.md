---
title: GeoJSON (Schema)

toc_footers:
  - Version 1.0
  - <a href='#'>GeoJSON</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: GeoJSON (Schema)
---

# Overview

A GeoJSON object

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

# Description

A feature is an abstraction of real world phenomena [ISO 19101-1:2014].

The GeoJSON representation is the currently recommended representation that all APIs should support, where GeoJSON can
be used for the data.

Each GeoJSON feature includes the following JSON members:

* `type`: fixed value "Feature".
* `geometry`: the primary geometry of the feature describing its location as a GeoJSON geometry object. `null`, if the
  feature has no spatial geometry.
* `properties`: an object with a member for each feature property.
# Schema

[schema.yaml](https://opengeospatial.github.io/bblocks/registereditems/geo/common/data_types/geojson/schema.yaml)
# Sources

* [IETF RFC 7946 - The GeoJSON Format](https://datatracker.ietf.org/doc/html/rfc7946)
