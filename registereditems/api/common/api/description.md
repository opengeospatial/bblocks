This block is an alias of the [OGC API - Common](bblocks://ogc.api.common.part1.api) OpenAPI
document, defined in the OGC API - Common building blocks register. It exists so that other
blocks in this register can depend on it directly, without importing the OGC API - Common
register themselves.

**Note:** this alias resolves `$ref` at the root of the OpenAPI document, which is not a location
where `$ref` is normally valid per the OpenAPI specification. Verify this renders correctly
wherever the compiled document is consumed (e.g. the viewer, Swagger UI/Redoc) before relying on it.
