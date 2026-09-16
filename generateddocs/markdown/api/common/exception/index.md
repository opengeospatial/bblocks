
# Exception schema (Schema)

`ogc.api.common.exception` *v0.1*

Alias of the OGC API - Common exception schema, published in the OGC API Common building blocks register.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

This block is an alias of the [Exception schema](bblocks://ogc.api.common.part1.schemas.exception)
defined in the OGC API - Common building blocks register. It exists so that other blocks in this
register can depend on it directly, without importing the OGC API - Common register themselves.

## Examples

### Example exception
#### json
```json
{
 "type": "https://example.net/validation-error",
 "title": "Your request parameters didn't validate.",
 "status": 400,
 "detail": "the 'age' and 'color' parameters do not validate",
 "instance": "urn:uuid:ebd2e7f0-1b27-11e8-accf-0ed5f89f718b"
 }
```

#### jsonld
```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/api/common/exception/context.jsonld",
  "type": "https://example.net/validation-error",
  "title": "Your request parameters didn't validate.",
  "status": 400,
  "detail": "the 'age' and 'color' parameters do not validate",
  "instance": "urn:uuid:ebd2e7f0-1b27-11e8-accf-0ed5f89f718b"
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix httpv: <http://www.w3.org/2011/http#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:uuid:ebd2e7f0-1b27-11e8-accf-0ed5f89f718b> a <https://example.net/validation-error> ;
    dct:description "the 'age' and 'color' parameters do not validate" ;
    dct:title "Your request parameters didn't validate." ;
    httpv:statusCodeNumber 400 .


```

## Schema

```yaml
$ref: https://ogcincubator.github.io/bblocks-ogcapi-common/build/annotated/api/common/part1/schemas/exception/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/api/common/exception/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/api/common/exception/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "type": "@type",
    "title": "dct:title",
    "status": "httpv:statusCodeNumber",
    "detail": "dct:description",
    "instance": "@id",
    "dct": "http://purl.org/dc/terms/",
    "httpv": "http://www.w3.org/2011/http#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/api/common/exception/context.jsonld)

## Sources

* [OGC API - Common - Part 1: Core](https://docs.ogc.org/is/19-072/19-072.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/api/common/exception`

