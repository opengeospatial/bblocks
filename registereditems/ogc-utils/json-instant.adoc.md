Version: 1.0.1

# Description

Temporal instants are either a date or timestamp in the Gregorian
calendar as specified by
[RFC 3339](https://tools.ietf.org/html/rfc3339). See the syntax of
`full-date` and `date-time` in
[section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6).

All timestamps include a timezone. The use of UTC ("Z") is recommended.

This describes the initial range of instant values. This range may be
extended in the future to support additional use cases. Clients
processing instant values must be prepared to receive other values.
Clients may ignore values that they do not understand.

An instant is embedded as a string in JSON representations of OGC API
resources.

[**Maturity**](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity):
Mature

## Examples

``` JSON
"2017-08-17"
```

``` JSON
"2017-08-17T08:05:32Z"
```

## Schema

``` YAML
Unresolved directive in json-instant.adoc - include::instant.yaml[]
```

# Alternate Representation: Text

The text representation is identical to the RFC 3339 string.

## Examples

``` TEXT
2017-08-17
```

``` TEXT
2017-08-17T08:05:32Z
```
