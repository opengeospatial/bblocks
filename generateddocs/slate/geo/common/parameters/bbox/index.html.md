---
title: bbox (Parameter)

language_tabs:
  - shell
  - python: Python
  - javascript: Javascript

toc_footers:
  - Version 1.0
  - <a href='#'>bbox</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: bbox (Parameter)
---


# bbox `ogc.geo.common.parameters.bbox`

The bbox query parameter provides a simple mechanism for filtering resources based on their location. It selects all resources that intersect a rectangle (map view) or box (including height information).

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/stable" target="_blank" data-rainbow-uri>Stable</a>
</p>

<aside class="success">
This building block is <strong>valid</strong>
</aside>

# Description

`bbox` is a query parameter that may be applied in GET requests on a collection of resources.

The parameter, if provided, selects the resources with a spatial extent that intersects the specified bounding box.

The coordinates of the bounding box are in longitude, latitude and optionally ellipsoidal height unless a different
coordinate reference system is specified in the query parameter `bbox-crs`.

The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a
vertical axis (height or depth):

* Lower left corner, coordinate axis 1
* Lower left corner, coordinate axis 2
* Minimum value, coordinate axis 3 (optional)
* Upper right corner, coordinate axis 1
* Upper right corner, coordinate axis 2
* Maximum value, coordinate axis 3 (optional)

The `bbox` parameter matches all resources in the collection that are not associated with a spatial geometry, too.

If a resource has multiple spatial geometry properties, it is the decision of the server whether only a single spatial
geometry property is used to determine the spatial extent or all relevant geometries.

# Examples

## The following bounding box parameter includes the 48 contiguous states of the United States of America.

`bbox=-124.7844079,24.7433195,-66.9513812,49.3457868`

![Bounding box for the continental US states](https://opengeospatial.github.io/bblocks/registereditems/geo/common/parameters/bbox/assets/example.png)


## Using a bounding box parameter in a request

```shell
curl \
"https://demo.pygeoapi.io/master/collections/lakes/items?\
bbox=-124.7844079,24.7433195,-66.9513812,49.3457868"
```

```python
import urllib.parse
import urllib.request

params = {'bbox': '-124.7844079,24.7433195,-66.9513812,49.3457868'}

url = 'https://demo.pygeoapi.io/master/collections/lakes/items?' \
    + urllib.parse.urlencode(params)

contents = urllib.request.urlopen(url)

print(contents.read())
```

```javascript
bbox = [-124.7844079,24.7433195,-66.9513812,49.3457868];

url = 'https://demo.pygeoapi.io/master/collections/lakes/items?';

fetch(url + `bbox=${bbox.join(',')}`)
  .then((response) => response.json())
  .then((json) => console.log(json));
```


# JSON Schema

```yaml--schema
name: bbox
in: query
required: false
style: form
explode: false
schema:
  type: array
  oneOf:
  - minItems: 4
    maxItems: 4
  - minItems: 6
    maxItems: 6
  items:
    type: number

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox/schema.json</a>

# References

* [OGC API - Features, Part 1, 7.15.3: Parameter bbox](https://docs.ogc.org/is/17-069r3/17-069r3.html#_parameter_bbox)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path: `registereditems/geo/common/parameters/bbox`

