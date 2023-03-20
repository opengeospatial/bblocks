The EDR API Items query is an [OGC API - Features](#OGC17-069r3)
endpoint that may be used to catalog pre-existing EDR sampling features.
The pre-existence of an EDR sampling feature may be because a particular
query has been cached for later use,such as a monitoring location. Or
there may be a catalog of spatiotemporal sampling features such as
domains of anomalies in a dataset. A [GeoJSON-compatible
JSON-Schema](http://schemas.opengis.net/ogcapi/edr/1.0/openapi/EDR_OpenAPI.yaml)
is specified to document an EDR API query endpoint and valid query
parameters including time range, parameters, and spatial
characteristics.

Unresolved directive in json-query-item.adoc -
include::../../../recommendations/core/REC\_edr-geojson.adoc\[\]

# Parameter itemId

If an itemId is not specified, the query will return a list of the
available itemId’s. This behavior is specified in [OGC API -
Features](#OGC17-069r3). All other parameters for use with the Items
query are defined by OGC API - Features.

The filter constraints are defined by the following query parameters:

<table>
<caption>Items query structure</caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 22%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Query Parameter</p></td>
<td><p>Type</p></td>
<td><p>Required</p></td>
<td><p>Description</p></td>
<td><p>Examples</p></td>
</tr>
<tr class="even">
<td><p><strong>bbox</strong></p>
<ul>
<li><p><a href="#req_core_rc-bbox-definition">definition</a></p></li>
<li><p><a href="#req_core_rc-bbox-response">rules</a></p></li>
</ul></td>
<td><p>String</p></td>
<td><p><strong>Yes</strong></p></td>
<td><p>The coordinates are defined by a BBOX string Only data that has a geometry that intersects the <a href="#area-definition">area</a> defined by the <a href="#req_core_rc-bbox-definition">bbox</a> are selected.</p>
<ul>
<li><p>Lower left corner, coordinate axis 1</p></li>
<li><p>Lower left corner, coordinate axis 2</p></li>
<li><p>Upper right corner, coordinate axis 1</p></li>
<li><p>Upper right corner, coordinate axis 2</p></li>
</ul>
<p>bbox=minx,miny,maxx,maxy</p>
<p>The X and Y coordinates are values in the coordinate system defined by the <code>crs</code> query parameter. If <code>crs</code> is not defined, the values will be assumed to be WGS84 longitude/latitude coordinates and heights will be assumed to be in meters above mean sea level.</p></td>
<td><ul>
<li><p><code>bbox=-6.0,50.0,-4.35,52.0</code></p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>datetime</strong></p>
<ul>
<li><p><a href="#req_collections_rc-time-definition">definition</a></p></li>
<li><p><a href="#req_core_rc-time-response">rules</a></p></li>
</ul></td>
<td><p>String</p></td>
<td><p>No</p></td>
<td><p>Datetime range to return data (the available range is defined in the temporal attribute of the extent section in the <a href="#collection_metadata_desc">collections</a> metadata response)</p></td>
<td><ul>
<li><p><code>datetime=2018-02-12T00:00Z</code></p></li>
<li><p><code>datetime=2018-02-12T00:00/2018-03-18T12:31Z</code></p></li>
<li><p><code>datetime=2018-02-12T00:00Z,2018-02-12T01:00Z,2018-02-14T12:00Z</code></p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>limit</strong></p>
<ul>
<li><p><a href="#req_edr_rc-limit-definition">definition</a></p></li>
<li><p><a href="#req_edr_rc-limit-response">rules</a></p></li>
</ul></td>
<td><p>String</p></td>
<td><p>No</p></td>
<td><p>Maximum number of items to return</p></td>
<td><ul>
<li><p><code>limit=10</code></p></li>
</ul></td>
</tr>
</tbody>
</table>

To retrieve an item, specify the required Item identifier:

`/collections/{collectionId}/items/{itemId}`

The following example returns information for the requested item with an
id of KIAD\_2020-05-19T00Z from the Metar
[collection](#collection-definition). Returned data would include a
location query end point, time range, a list of available parameters,
and a representative geometry for the KIAD METAR station.

`/collections/metar/items/KIAD_2020-05-19T00Z`

The following example returns information for the requested item with an
id of warning\_12345 from the forecast
[collection](#collection-definition). Returned data would include an
[area](#area-definition) query end point, time range, a list of
available parameters and a representative geometry for the
warning\_12345 warning area.

`/collections/forecast/items/warning_12345`
