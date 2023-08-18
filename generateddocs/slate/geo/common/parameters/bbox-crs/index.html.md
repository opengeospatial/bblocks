---
title: bbox-crs (Parameter)


toc_footers:
  - Version 1.0
  - <a href='#'>bbox-crs</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: bbox-crs (Parameter)
---


# bbox-crs `ogc.geo.common.parameters.bbox-crs`

The bbox-crs query parameter can be used to assert the coordinate reference system that is used for the coordinate values of the bbox parameter.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/stable" target="_blank" data-rainbow-uri>Stable</a>
</p>

<aside class="success">
This building block is <strong>valid</strong>
</aside>

# Description

If the `bbox-crs` parameter is specified, then the values of the `bbox` parameter are assumed to be in the specified
coordinate reference system and the server will perform the necessary internal transformations to properly fetch data
from within the specified bounding box.

Otherwise, the values for the `bbox` parameter shall be assumed to be WGS 84 longitude-latitude for coordinates
without height and WGS 84 longitude-latitude-height for coordinates with height.
# Examples

## Bounding box parameter example

The coordinates in the following bounding box are in the coordinate reference system ETRS89 / UTM zone 32N that is used, for example, in Germany.



```python
import urllib.parse
import urllib.request

params = {
  'bbox': '-124.7844079,24.7433195,-66.9513812,49.3457868',
  'bbox-crs': 'http://www.opengis.net/def/crs/EPSG/0/25832'
}

url = 'https://demo.pygeoapi.io/master/collections/lakes/items?' \
    + urllib.parse.urlencode(params)

contents = urllib.request.urlopen(url)

print(contents.read())

```


# JSON Schema

```yaml--schema
name: bbox-crs
in: query
required: false
schema:
  type: string
  format: uri
style: form
explode: false

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;data=name%3A+bbox-crs%0Ain%3A+query%0Arequired%3A+false%0Aschema%3A%0A++type%3A+string%0A++format%3A+uri%0Astyle%3A+form%0Aexplode%3A+false%0A">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox-crs/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox-crs/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox-crs/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox-crs/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%7B%0A++++%22%40version%22%3A+1.1%0A++%7D%0A%7D">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox-crs/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox-crs/context.jsonld</a>

# References

* [OGC API - Features, Part 2, 6.3.1: Parameter bbox-crs](http://www.opengis.net/doc/IS/ogcapi-features-2/1.0#_parameter_bbox_crs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path:
<code><a href="https://github.com/opengeospatial/bblocks/blob/HEAD/registereditems/geo/common/parameters/bbox-crs" target="_blank">registereditems/geo/common/parameters/bbox-crs</a></code>

