
# Conformance Classes schema (Schema)

`ogc.api.common.confClasses` *v0.1*

Alias of the OGC API - Common confClasses schema, published in the OGC API Common building blocks register.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

This block is an alias of the [Conformance Classes schema](bblocks://ogc.api.common.part1.schemas.confClasses)
defined in the OGC API - Common building blocks register. It exists so that other blocks in this
register can depend on it directly, without importing the OGC API - Common register themselves.

## Schema

```yaml
$ref: https://ogcincubator.github.io/bblocks-ogcapi-common/build/annotated/api/common/part1/schemas/confClasses/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/api/common/confClasses/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/api/common/confClasses/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "conformsTo": {
      "@id": "dct:conformsTo",
      "@type": "@id",
      "@container": "@set"
    },
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/api/common/confClasses/context.jsonld)

## Sources

* [OGC API - Common - Part 1: Core](https://docs.ogc.org/is/19-072/19-072.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/api/common/confClasses`

