# Area Query

## Overview

The Area query returns data within the polygon defined by the `coords`
parameter. **Logic for identifying the best match for the requested area
will depend on the [collection](#collection-definition) and is at the
discretion of the query service implementer**. The height or time of the
area are specified through separate parameters. The results are further
filtered by the constraints defined by the following query parameters:

<table>
<caption>Area query structure</caption>
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
<td><p><strong>coords</strong></p>
<ul>
<li><p><a href="#req_edr_coords-definition">definition</a></p></li>
<li><p><a href="#req_edr_polygon-coords-response">rules</a></p></li>
</ul></td>
<td><p>WKT string</p></td>
<td><p><strong>Yes</strong></p></td>
<td><p>The coordinates are defined by a Polygon Well Known Text (WKT) string</p></td>
<td><ul>
<li><p><code>coords=POLYGON((-6.1 50.3,-4.35 51.4,-2.6 51.6,-2.8 50.6,-5.3 49.9,-6.1 50.3))</code></p></li>
<li><p><code>coords=MULTIPOLYGON(((-15 48.8,-15 60.95,5 60.85,5 48.8,-15 48.8)),
-6.1 50.3,-4.35 51.4,-2.6 51.6,-2.8 50.6,-5.3 49.9,-6.1 50.3
-6.1 50.3,-4.35 51.4,-2.6 51.6,-2.8 50.6,-5.3 49.9,-6.1 50.3)</code></p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>z</strong></p>
<ul>
<li><p><a href="#req_edr_z-definition">definition</a></p></li>
<li><p><a href="#req_edr_z-response">rules</a></p></li>
</ul></td>
<td><p>String</p></td>
<td><p>No</p></td>
<td><p>The vertical level to return data for (available options defined in the vertical attribute of the extent section in the <a href="#collection_metadata_desc">collections</a> metadata response</p></td>
<td><ul>
<li><p><code>z=850</code></p></li>
<li><p><code>z=1000,900,850,700</code></p></li>
<li><p><code>z=2/100</code></p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>datetime</strong></p>
<ul>
<li><p><a href="#req_collections_rc-time-definition">definition</a></p></li>
<li><p><a href="#req_core_rc-time-response">rules</a></p></li>
</ul></td>
<td><p>String</p></td>
<td><p>No</p></td>
<td><p>Datetime range to return data (the available range is defined in the the temporal attribute of the extent section in the <a href="#collection_metadata_desc">collections</a> metadata response)</p></td>
<td><ul>
<li><p><code>datetime=2018-02-12T00:00Z</code></p></li>
<li><p><code>datetime=2018-02-12T00:00/2018-03-18T12:31Z</code></p></li>
<li><p><code>datetime=2018-02-12T00:00Z,2018-02-12T01:00Z,2018-02-14T12:00Z</code></p></li>
</ul></td>
</tr>
<tr class="odd">
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
<tr class="even">
<td><p><strong>crs</strong></p>
<ul>
<li><p><a href="#req_edr_crs-definition">definition</a></p></li>
<li><p><a href="#req_edr_crs-response">rules</a></p></li>
</ul></td>
<td><p>String</p></td>
<td><p>No</p></td>
<td><p>coordinate reference system identifier for the <strong>coords</strong> values and output data (available options listed in the <a href="#collection_metadata_desc">collections</a> metadata response</p></td>
<td><ul>
<li><p><code>crs=EPSG:4326</code></p></li>
<li><p><code>crs=A_CUSTOM_LABEL</code></p></li>
</ul></td>
</tr>
<tr class="odd">
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

*If a client request has a **coords** value which includes a height
value and defines a **z** query parameter the **z** query parameter will
be the requested height value*

## Source Reference

It is defined in the [OGC API-EDR V1.0.1 specification,
Section 8.2.3](https://docs.ogc.org/is/19-086r5/19-086r5.htm) which is
maintained by the OGC EDR API Standard Working Group using this [OGC
GitHub
repository](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval).

## Maturity

Stable

## Model (UML) TBD

## Model (OWL, or at least a formal and stable mapping of concepts to URIs) TBD

## JSON schema

Currently the schema is [defined in
YAML](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/standard/openapi/request-bodies/area.yaml)

## JSON-LD context TBD e.g. <https://github.com/covjson/specification/blob/master/contexts/context.jsonld>

## Validator

[OGC API - Environmental Data Retrieval 1.0 Conformance Test Suite,
Beta,
Version 0.5, 2022-11-08](https://cite.opengeospatial.org/te2/about/ogcapi-edr10/1.0/site/).

## Examples

See the Examples in the [Standard,
Clause 8.2.3](https://opengeospatial.github.io/ogcna-auto-review/19-086r5.html#parameter-name).

### Example 1 Request data within a specified area for a single level and single time

    .../area?coords=POLYGON((-6.1 50.3,-4.35 51.4,-2.6 51.6,-2.8 50.6,-5.3 49.9,-6.1 50.3))0&z=850&datetime=2018-02-12T00:00Z

### Example 2 Request data within a specified area, with an interior hole, for a single level and single time

    .../area?coords=POLYGON((-6.1 50.3,-4.35 51.4,-2.6 51.6,-2.8 50.6,-5.3 49.9,-6.1 50.3),(-5.0 50.2,-4.8 50.4,-5.0 50.4,-5.0 50.2))0&z=850&datetime=2018-02-12T00:00Z

### Example 3 Request data within a specified area for a single level and a range of times

    .../area?coords=POLYGON((-6.1 50.3,-4.35 51.4,-2.6 51.6,-2.8 50.6,-5.3 49.9,-6.1 50.3))p&z=850&datetime=2018-02-12T00:00/2018-03-18T12:31Z

### Example 4 Request data within a specified area for a single time and for several levels

    .../area?coords=POLYGON((-6.1 50.3,-4.35 51.4,-2.6 51.6,-2.8 50.6,-5.3 49.9,-6.1 50.3))&datetime=2018-02-12T00:00Z&z=1000,900,850,700

### Example 5 Request data within several specified areas and for a single level and single time

    .../area?coords=MULTIPOLYGON\(((-15 48.8,-15 60.95,5 60.85,5 48.8,-15 48.8)),((-6.1 50.3,-4.35 51.4,-2.6 51.6,-2.8 50.6,-5.3 49.9,-6.1 50.3)))&z=2&datetime=2018-03-18T12:31Z

## Further guidance

See the Examples in the
[Standard](https://opengeospatial.github.io/ogcna-auto-review/19-086r5.html).

## Media type

application/json

## Link relation types

Link relation types do not seem applicable for a Cube Query. Possibly
\`describedby\`could be useful.
