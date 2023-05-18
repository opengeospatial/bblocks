Version: 1.0.1

# Overview

The `limit` query parameter provides a mechanism for a client to limit
the maximum number of items in a response from an API resource that is
some kind of a collection of items.

[**Maturity**](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity):
Mature

# Examples

The number of resources returned depends on the server and the parameter
`limit`.

  - The client can request a limit it is interested in.

  - The server likely has a default value for the limit, and a maximum
    limit.

Using default/maximum values of 10/10000:

  - If you ask for 10, you will get 0 to 10 (as requested) and if there
    are more, a `next` link;

  - If you don’t specify a limit, you will get 0 to 10 (default) and if
    there are more, a `next` link;

  - If you ask for 50000, you might get up to 10000 (server-limited) and
    if there are more, a `next` link;

  - If you follow the `next` link from the previous response, you might
    get up to 10000 additional features and if there are more, a next
    link.

# Description

`limit` is a query parameter that may be applied in GET requests on a
collection of resources.

The response will not contain more resources than specified by the
`limit` parameter, if provided.

If the API definition specifies a maximum value for the `limit`
parameter, the response will not contain more features than this maximum
value.

Only resources are counted that are on the first level of the
collection. Any nested resources contained within the explicitly
requested resources will not be counted.

If the request selects more resources than is returned in the response
(the number it returns is less than or equal to the
requested/default/maximum limit) then the response will include a link
to the next set of resources (the next "page") with a link relation type
`next`.

# OpenAPI 3.0 specification

``` YAML
Unresolved directive in parameter-limit.adoc - include::limit.yaml[]
```

The values for `minimum`, `maximum` and `default` are only examples and
may be changed.
