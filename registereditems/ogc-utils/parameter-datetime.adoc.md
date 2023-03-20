Version: 1.0.1

# Overview

The `datetime` query parameter provides a simple mechanism for filtering
resources based on their temporal extent. It selects all resources that
intersect an temporal instant or interval.

[**Maturity**](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity):
Mature

# Examples

February 12, 2018, 23:20:52 UTC:

``` TEXT
datetime=2018-02-12T23%3A20%3A52Z
```

February 12, 2018, 00:00:00 UTC to March 18, 2018, 12:31:12 UTC:

``` TEXT
datetime=2018-02-12T00%3A00%3A00Z%2F2018-03-18T12%3A31%3A12Z
```

February 12, 2018, 00:00:00 UTC or later:

``` TEXT
datetime=2018-02-12T00%3A00%3A00Z%2F..
```

March 18, 2018, 12:31:12 UTC or earlier:

``` TEXT
datetime=..%2F2018-03-18T12%3A31%3A12Z
```

# Description

`datetime` is a query parameter that may be applied in GET requests on a
collection of resources.

The parameter, if provided, selects the resources with a temporal extent
that intersects the specified temporal
[instant](../schemas/instant.adoc) or
[interval](../schemas/interval.adoc).

The `datetime` parameter matches all resources in the collection that
are not associated with a temporal extent, too.

All instants in the `datetime` parameter have to be timestamps with a
timezone.

For intervals, the text representation is used. The interval notation is
taken from ISO 8601-2:2019. ISO 8601-2 distinguishes open start/end
timestamps (double-dot) and unknown start/end timestamps (empty string).
For queries, an unknown start/end has the same effect as an open
start/end.

"Intersects" means that the time (instant or interval) specified in the
parameter `datetime` includes a timestamp that is part of the temporal
geometry of the resource (again, a time instant or interval). For time
intervals this includes the start and end time.

If a resource has multiple temporal geometry properties, it is the
decision of the server whether only a single temporal geometry property
is used to determine the temporal extent or all relevant geometries.

# OpenAPI 3.0 specification

``` YAML
Unresolved directive in parameter-datetime.adoc - include::datetime.yaml[]
```
