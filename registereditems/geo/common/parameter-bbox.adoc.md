Version: 1.0.1

# Overview

The `bbox` query parameter provides a simple mechanism for filtering
resources based on their location. It selects all resources that
intersect a rectangle (map view) or box (including height information).

[**Maturity**](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity):
Mature

# Examples

The following bounding box parameter includes the 48 contiguous states
of the United States of America.

``` TEXT
bbox=-124.7844079,24.7433195,-66.9513812,49.3457868
```

# Description

`bbox` is a query parameter that may be applied in GET requests on a
collection of resources.

The parameter, if provided, selects the resources with a spatial extent
that intersects the specified [bounding box](json-bbox.adoc).

The coordinates of the bounding box are in longitude, latitude and
optionally ellipsoidal height unless a different coordinate reference
system is specified in the [query parameter
`bbox-crs`](parameter-bbox-crs.adoc).

The `bbox` parameter matches all resources in the collection that are
not associated with a spatial geometry, too.

If a resource has multiple spatial geometry properties, it is the
decision of the server whether only a single spatial geometry property
is used to determine the spatial extent or all relevant geometries.

# OpenAPI 3.0 specification

``` YAML
name: bbox
in: query
required: false
style: form
explode: false
schema:
  type: array
  oneOf:
  - minItems: 4
    maxItems: 4
  - minItems: 6
    maxItems: 6
  items:
    type: number
```

## Source Reference

[OGC API - Features, Part 1, 7.15.3: Parameter
bbox](http://www.opengis.net/doc/IS/ogcapi-features-1/1.0#_parameter_bbox)
