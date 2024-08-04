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

<blockquote class="lang-specific shell">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/common/parameters/bbox/example_2_1.shell">Open in new window</a>
</blockquote>




```python
import urllib.parse
import urllib.request

params = {'bbox': '-124.7844079,24.7433195,-66.9513812,49.3457868'}

url = 'https://demo.pygeoapi.io/master/collections/lakes/items?' \
    + urllib.parse.urlencode(params)

contents = urllib.request.urlopen(url)

print(contents.read())
```

<blockquote class="lang-specific python">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/common/parameters/bbox/example_2_2.python">Open in new window</a>
</blockquote>




```javascript
bbox = [-124.7844079,24.7433195,-66.9513812,49.3457868];

url = 'https://demo.pygeoapi.io/master/collections/lakes/items?';

fetch(url + `bbox=${bbox.join(',')}`)
  .then((response) => response.json())
  .then((json) => console.log(json));
```

<blockquote class="lang-specific javascript">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/common/parameters/bbox/example_2_3.javascript">Open in new window</a>
</blockquote>



# JSON Schema

```yaml--schema
name: bbox
in: query
description: 'Only features that have a geometry that intersects the bounding box
  are selected.

  The bounding box is provided as four or six numbers, depending on whether the

  coordinate reference system includes a vertical axis (height or depth):


  * Lower left corner, coordinate axis 1

  * Lower left corner, coordinate axis 2

  * Minimum value, coordinate axis 3 (optional)

  * Upper right corner, coordinate axis 1

  * Upper right corner, coordinate axis 2

  * Maximum value, coordinate axis 3 (optional)


  If the value consists of four numbers, the coordinate reference system is

  WGS 84 longitude/latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84)

  unless a different coordinate reference system is specified in the parameter `bbox-crs`.


  If the value consists of six numbers, the coordinate reference system is WGS 84

  longitude/latitude/ellipsoidal height (http://www.opengis.net/def/crs/OGC/0/CRS84h)

  unless a different coordinate reference system is specified in the parameter `bbox-crs`.


  The query parameter `bbox-crs` is specified in OGC API - Features - Part 2: Coordinate

  Reference Systems by Reference.


  For WGS 84 longitude/latitude the values are in most cases the sequence of

  minimum longitude, minimum latitude, maximum longitude and maximum latitude.

  However, in cases where the box spans the antimeridian the first value

  (west-most box edge) is larger than the third value (east-most box edge).


  If the vertical axis is included, the third and the sixth number are the

  bottom and the top of the 3-dimensional bounding box.


  If a feature has multiple spatial geometry properties, it is the decision of the

  server whether only a single spatial geometry property is used to determine

  the extent or all relevant geometries.'
required: false
schema:
  type: array
  oneOf:
  - minItems: 4
    maxItems: 4
  - minItems: 6
    maxItems: 6
  items:
    type: number
style: form
explode: false

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Fcommon%2Fparameters%2Fbbox%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/common/parameters/bbox/schema.json</a>

# References

* [OGC API - Features, Part 1, 7.15.3: Parameter bbox](https://docs.ogc.org/is/17-069r3/17-069r3.html#_parameter_bbox)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path:
<code><a href="https://github.com/opengeospatial/bblocks/blob/HEAD/registereditems/geo/common/parameters/bbox" target="_blank">registereditems/geo/common/parameters/bbox</a></code>

