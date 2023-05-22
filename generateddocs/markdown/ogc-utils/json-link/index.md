# JSON Link (Schema)

*Version 0.1*

Web linking according to <a href=''></a> is used to express relationships between resources. The JSON object representation of links described here is used consistently in OGC API’s.

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Mature

## Schema

[schema.yaml](https://opengeospatial.github.io/bblocks/registereditems/ogc-utils/json-link/schema.yaml)

```yaml
"$schema": https://json-schema.org/draft/2020-12/schema
description: 'JSON Link'
type: object
required:
  - href
  - rel
properties:
  href:
    type: string
    format: uri-reference
  rel:
    type: string
  anchor:
    type: string
  type:
    type: string
  hreflang:
    type: string
  title:
    type: string
  length:
    type: integer

```
## Sources

* [IETF RFC 8288 - Web Linking](https://www.rfc-editor.org/rfc/rfc8288.txt)