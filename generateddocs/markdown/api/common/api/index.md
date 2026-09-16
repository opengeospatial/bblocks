
# OGC API - Common (Api)

`ogc.api.common.api` *v0.1*

Alias of the OGC API - Common OpenAPI document, published in the OGC API Common building blocks register.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

This block is an alias of the [OGC API - Common](bblocks://ogc.api.common.part1.api) OpenAPI
document, defined in the OGC API - Common building blocks register. It exists so that other
blocks in this register can depend on it directly, without importing the OGC API - Common
register themselves.

**Note:** this alias resolves `$ref` at the root of the OpenAPI document, which is not a location
where `$ref` is normally valid per the OpenAPI specification. Verify this renders correctly
wherever the compiled document is consumed (e.g. the viewer, Swagger UI/Redoc) before relying on it.

## Sources

* [OGC API - Common - Part 1: Core](https://docs.ogc.org/is/19-072/19-072.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/api/common/api`

