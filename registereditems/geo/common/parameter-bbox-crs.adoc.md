Version: 1.0.0

# Overview

The `bbox-crs` query parameter can be used to assert the coordinate
reference system that is used for the coordinate values of the [`bbox`
parameter](bbox.adoc).

[**Maturity**](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity):
Stable

# Examples

The coordinates in the following bounding box are in the coordinate
reference system ETRS89 / UTM zone 32N that is used, for example, in
Germany.

``` TEXT
...
&bbox=32507317,5224265,33427450,5603836
&bbox-crs=http%3A%2F%2Fwww.opengis.net%2Fdef%2Fcrs%2FEPSG%2F0%2F25832
```

# Description

If the `bbox-crs` parameter is specified, then the values of the `bbox`
parameter are assumed to be in the specified coordinate reference system
and the server will perform the necessary internal transformations to
properly fetch data from within the specified bounding box.

# OpenAPI 3.0 specification

``` YAML
name: bbox-crs
in: query
required: false
schema:
  type: string
  format: uri
style: form
explode: false
```

## Source Reference

[OGC API - Features, Part 2, 6.3.1: Parameter
bbox-crs](http://www.opengis.net/doc/IS/ogcapi-features-2/1.0#_parameter_bbox_crs)
