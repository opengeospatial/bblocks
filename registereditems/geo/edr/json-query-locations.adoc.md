The Locations query returns data for the named location. **Logic for
identifying the best match for the coordinate will depend on the
[collection](#collection-definition) and is at the discretion of the
query service implementer**. If a location id is not defined the API
**MUST** return a GeoJSON features array of valid location identifiers.

The filter constraints are defined by the following query parameters:

<table>
<caption>locations query structure</caption>
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
<td><p><strong>locationId</strong></p></td>
<td><p>String</p></td>
<td><p>No</p></td>
<td><p>A unique identifier for the required location, such as a <a href="http://en.wikipedia.org/wiki/Geohash">GeoHash</a>, a World Meteorological Organization (WMO) station identifier or place name.</p></td>
<td><ul>
<li><p><code>EGLL</code></p></li>
<li><p><code>Ottawa</code></p></li>
<li><p><code>limit.broom.flip</code></p></li>
<li><p><code>gbsvn</code></p></li>
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
<td><p><strong>parameter-name</strong></p>
<ul>
<li><p><a href="#req_edr_parameters-definition">definition</a></p></li>
<li><p><a href="#req_edr_parameters-response">rules</a></p></li>
</ul></td>
<td><p>String</p></td>
<td><p>No</p></td>
<td><p>Comma delimited list of parameter names available options listed in the <strong>parameter_names</strong> section of the <a href="#collection_metadata_desc">collections</a> metadata response</p></td>
<td><ul>
<li><p><code>parameter-name=Visibility,Air%20Temperature`</code></p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>crs</strong></p>
<ul>
<li><p><a href="#req_edr_crs-definition">definition</a></p></li>
<li><p><a href="#req_edr_crs-response">rules</a></p></li>
</ul></td>
<td><p>String</p></td>
<td><p>No</p></td>
<td><p>Coordinate reference system identifier for the <strong>coords</strong> values and output data (available options listed in the <a href="#collection_metadata_desc">collections</a> metadata response</p></td>
<td><ul>
<li><p><code>crs=EPSG:4326</code></p></li>
<li><p><code>crs=A_CUSTOM_LABEL</code></p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>f</strong></p>
<ul>
<li><p><a href="#req_edr_f-definition">definition</a></p></li>
<li><p><a href="#req_edr_f-response">rules</a></p></li>
</ul></td>
<td><p>String</p></td>
<td><p>No</p></td>
<td><p>Data format for the output data (available options listed in the <a href="#collection_metadata_desc">collections</a> response), schemas describing JSON and XML outputs can be defined in the OpenAPI documentation (see <a href="https://swagger.io/docs/specification/data-models/">https://swagger.io/docs/specification/data-models/</a>)</p></td>
<td><ul>
<li><p><code>f=GeoJSON</code></p></li>
<li><p><code>f=netCDF4</code></p></li>
<li><p><code>f=CoverageJSON</code></p></li>
<li><p><code>f=CSV</code></p></li>
</ul></td>
</tr>
</tbody>
</table>
