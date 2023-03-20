Version: 1.0.0

# Overview

The `crs` query parameter can be used to request the coordinate
reference system to use for any coordinates included in the response.

[**Maturity**](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity):
Stable

# Examples

The following [Features request]() will return the building geometries
in the coordinate reference system NAD27 / UTM zone 3N that is used, for
example, in Canada.

``` TEXT
.../collections/buildings/items
?crs=http%3A%2F%2Fwww.opengis.net%2Fdef%2Fcrs%2FEPSG%2F0%2F26703
&...
```

# Description

If the `bbox-crs` parameter is specified, then the values of the `bbox`
parameter are assumed to be in the specified coordinate reference system
and the server will perform the necessary internal transformations to
properly fetch data from within the specified bounding box.

If the value of the `crs` parameter is not one of the supported
coordinate reference system identifiers for the resource, the server
will respond with a client error.

How the supported coordinate reference systems are specified, depends on
the resource type. For example, for a [Features
resource](../features/json-features.adoc), the supported coordinate
reference systems are listed in the parent [OGC API Collection
resource](json-collection.adoc).

# OpenAPI 3.0 specification

``` YAML
name: crs
in: query
required: false
schema:
  type: string
  format: uri
style: form
explode: false
```

## Source Reference

[OGC API - Features, Part 2, 6.3.2: Parameter
crs](http://www.opengis.net/doc/IS/ogcapi-features-2/1.0#_parameter_crs)
