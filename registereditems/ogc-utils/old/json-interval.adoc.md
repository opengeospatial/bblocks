Version: 1.0.1

# Description

Temporal intervals are described by the start and end
[instants](instant.adoc).

Both start and end instants are included in the interval.

Open ranges at the start or end are supported.

The interval is embedded as an array with two items (start, end) in JSON
representations of OGC API resources.

Open ranges at the start or end are represented by a `null` value for
the start/end.

[**Maturity**](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity):
Mature

## Examples

``` JSON
[ "1969-07-16", "1969-07-24" ]
```

``` JSON
[ "1969-07-16T05:32:00Z", "1969-07-24T16:50:35Z" ]
```

``` JSON
[ "2019-10-14", null ]
```

## Schema

``` YAML
Unresolved directive in json-interval.adoc - include::interval.yaml[]
```

# Alternate Representation: Text

The text representation of an interval values does not use the standard
representation of an array, that is as comma-separated values. The text
representation is based on ISO 8601 and the two instants are separated
by a solidus ("/"). Open ranges at the start or end are represented
using a double-dot (".."). An empty string ("") represents an unknown
value for the start/end and may be used, too.

## Examples

``` TEXT
1969-07-16/1969-07-24
```

``` TEXT
1969-07-16T05:32:00Z/1969-07-24T16:50:35Z
```

``` TEXT
2019-10-14/..
```
