
# bbox-crs (Parameter)

`ogc.geo.common.parameters.bbox-crs` *v1.0*

The bbox-crs query parameter can be used to assert the coordinate reference system that is used for the coordinate values of the bbox parameter.

[*Status*](http://www.opengis.net/def/status): Stable

## Description

If the `bbox-crs` parameter is specified, then the values of the `bbox` parameter are assumed to be in the specified
coordinate reference system and the server will perform the necessary internal transformations to properly fetch data
from within the specified bounding box.

Otherwise, the values for the `bbox` parameter shall be assumed to be WGS 84 longitude-latitude for coordinates
without height and WGS 84 longitude-latitude-height for coordinates with height.
## Examples

### Bounding box parameter example
The coordinates in the following bounding box are in the coordinate reference system ETRS89 / UTM zone 32N that is used, for example, in Germany.

#### python
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

## Schema

```yaml
name: bbox-crs
in: query
required: false
schema:
  type: string
  format: uri
style: form
explode: false

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox-crs/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox-crs/schema.yaml)

## Sources

* [OGC API - Features, Part 2, 6.3.1: Parameter bbox-crs](http://www.opengis.net/doc/IS/ogcapi-features-2/1.0#_parameter_bbox_crs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/geo/common/parameters/bbox-crs`

