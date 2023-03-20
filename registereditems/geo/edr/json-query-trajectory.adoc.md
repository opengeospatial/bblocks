# Trajectory Query

## Overview

The Trajectory query returns data along the path defined by the `coords`
parameter. **Logic for identifying the best matches for the requested
trajectory will depend on the [collection](#collection-definition) and
is at the discretion of the query service implementer** . The results
are further filtered by the constraints defined by the following query
parameters:

<table>
<caption>Trajectory query structure</caption>
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
<li><p><a href="#req_edr_linestring-coords-response">rules</a></p></li>
</ul></td>
<td><p>WKT string</p></td>
<td><p><strong>Yes</strong></p></td>
<td><p>The coordinates are defined by one of the following Well Known Text (WKT) strings:</p>
<ul>
<li><p>LINESTRING</p></li>
<li><p>LINESTRINGZ</p></li>
<li><p>LINESTRINGM</p></li>
<li><p>LINESTRINGZM</p></li>
<li><p>The <strong>Z</strong> in <code>LINESTRINGZ</code> and <code>LINESTRINGZM</code> refers to the height value. <code>If the specified CRS does not define the height units, the heights units will default to metres above mean sea level</code></p></li>
<li><p>The <strong>M</strong> in <code>LINESTRINGM</code> and <code>LINESTRINGZM</code> refers to the number of seconds that have elapsed since the Unix epoch, that is the time 00:00:00 UTC on 1 January 1970. See <a href="https://en.wikipedia.org/wiki/Unix_time">https://en.wikipedia.org/wiki/Unix_time</a></p></li>
</ul></td>
<td><ul>
<li><p>A Simple 2D corridor <code>coords=LINESTRING(-3.53 50.72,-3.35 50.92,-3.11 51.02,-2.85 51.42,-2.59 51.46)</code></p></li>
<li><p>A 2D corridor with mutiple segments: <code>coords=MULTILINESTRING
-3.53 50.72,-3.35 50.92),(-3.11 51.02,-2.85 51.42,-2.59 51.46
-3.53 50.72,-3.35 50.92),(-3.11 51.02,-2.85 51.42,-2.59 51.46</code></p></li>
<li><p>A 2D corridor with all waypoints at same time: <code>coords=LINESTRING(-3.53 50.72,-3.35 50.92,-3.11 51.02,-2.85 51.42,-2.59 51.46)&amp;datetime=2018-02-12T23:00:00Z</code></p></li>
<li><p>A 2D corridor, all waypoints at the same height : <code>coords=LINESTRING(-3.53 50.72,-3.35 50.92,-3.11 51.02,-2.85 51.42,-2.59 51.46)&amp;z=850</code></p></li>
<li><p>A 2D corridor, all waypoints at the same time and height: <code>coords=LINESTRING(51.14 -2.98, 51.36 -2.87, 51.03 -3.15, 50.74 -3.48, 50.9 -3.36)&amp;datetime=2018-02-12T23:00:00Z&amp;z=850</code></p></li>
<li><p>A 3D corridor each waypoint at a different time: <code>coords=LINESTRINGM(51.14 -2.98 1560507000, 51.36 -2.87 1560507600, 51.03 -3.15 1560508200, 50.74 -3.48 1560508500, 50.9 -3.36 1560510240)</code></p></li>
<li><p>A 3D corridor, each waypoint at a different time by at the same height: <code>coords=LINESTRINGM(51.14 -2.98 1560507000, 51.36 -2.87 1560507600, 51.03 -3.15 1560508200, 50.74 -3.48 1560508500, 50.9 -3.36 1560510240)&amp;z=200</code></p></li>
<li><p>A 3D corridor, each waypoint at a different height: <code>coords=LINESTRINGZ(-3.53 50.72 0.1,-3.35 50.92 0.2,-3.11 51.02 0.3,-2.85 51.42 0.4,-2.59 51.46 0.5)</code></p></li>
<li><p>A 3D corridor each waypoint at a different height but the same time: <code>coords=LINESTRINGZ(-3.53 50.72 0.1,-3.35 50.92 0.2,-3.11 51.02 0.3,-2.85 51.42 0.4,-2.59 51.46 0.5)&amp;datetime=2018-02-12T23:00:00Z</code></p></li>
<li><p>A 4D corridor, each waypoint at different heights and times: <code>coords=LINESTRINGZM (-3.53 50.72 0.1 1560507000,-3.35 50.92 0.2 1560508800,-3.11 51.02 0.3 1560510600,-2.85 51.42 0.41560513600,-2.59 51.46 0.5 1560515400)</code></p></li>
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
<td><p>The vertical level to return data for (available options defined in the vertical attribute of the extent section in the <a href="#collection_metadata_desc">collections</a> metadata response)</p></td>
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
<li><p><code>parameter-name=Visibility,Air%20Temperature</code></p></li>
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

*If any of the following occurs:*

  - client request contains coords=LINESTRINGZ(…​) and a **z** query
    parameter

  - client request contains coords=LINESTRINGM(…​) and a **datetime**
    query parameter

  - client request contains coords=LINESTRINGZM(…​) and **z** or
    **datetime** query parameters

*An error MUST be thrown by the server*

## Source Reference

It is defined in the [OGC API-EDR V1.0.1 specification,
Section 8.2.5](https://docs.ogc.org/is/19-086r5/19-086r5.htm) which is
maintained by the OGC EDR API Standard Working Group using this [OGC
GitHub
repository](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval).

## Maturity

Stable

## Model (UML) TBD

## Model (OWL, or at least a formal and stable mapping of concepts to URIs) TBD

## JSON schema

Currently the schema is [defined in
YAML](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/standard/openapi/request-bodies/trajectory.yaml)

## JSON-LD context TBD e.g. <https://github.com/covjson/specification/blob/master/contexts/context.jsonld>

## Validator

[OGC API - Environmental Data Retrieval 1.0 Conformance Test Suite,
Beta,
Version 0.5, 2022-11-08](https://cite.opengeospatial.org/te2/about/ogcapi-edr10/1.0/site/).

## Examples

See the Examples in the [Standard,
Clause 8.2.5](https://opengeospatial.github.io/ogcna-auto-review/19-086r5.html#parameter-name).

### Example 1 Request data along a specified simple 2D trajectory

    .../trajectory?coords=LINESTRING(-3.53 50.72,-3.35 50.92,-3.11 51.02,-2.85 51.42,-2.59 51.46)

### Example 2 Request data along a specified 2D trajectory with multiple discontinuous segments

    .../trajectory?coords=MULTILINESTRING((-3.53 50.72,-3.35 50.92),(-3.11 51.02,-2.85 51.42,-2.59 51.46))

### Example 3 Request data along a specified 2D trajectory with all waypoints at same time:

    .../trajectory?coords=LINESTRING(-3.53 50.72,-3.35 50.92,-3.11 51.02,-2.85 51.42,-2.59 51.46)&datetime=2018-02-12T23:00:00Z

### Example 4 Request data along a specified 2D trajectory with all waypoints at the same height

    ...trajectory?coords=LINESTRING(-3.53 50.72,-3.35 50.92,-3.11 51.02,-2.85 51.42,-2.59 51.46)&z=850

### Example 5 Request data along a specified 2D trajectory with all waypoints at the same time and height

    ...trajectory?coords=LINESTRING(51.14 -2.98, 51.36 -2.87, 51.03 -3.15, 50.74 -3.48, 50.9 -3.36)&datetime=2018-02-12T23:00:00Z&z=850

### Example 6 Request data along a specified 3D trajectory with each waypoint at a different time

    .../trajectory?coords=LINESTRINGM(51.14 -2.98 1560507000, 51.36 -2.87 1560507600, 51.03 -3.15 1560508200, 50.74 -3.48 1560508500, 50.9 -3.36 1560510240)

### Example 7 Request data along a specified 3D trajectory with each waypoint at a different time but at the same height

    .../trajectory?coords=LINESTRINGM(51.14 -2.98 1560507000, 51.36 -2.87 1560507600, 51.03 -3.15 1560508200, 50.74 -3.48 1560508500, 50.9 -3.36 1560510240)&z=200

### Example 8 Request data along a specified 3D trajectory with each waypoint at a different height

    .../trajectory?coords=LINESTRINGZ(-3.53 50.72 0.1,-3.35 50.92 0.2,-3.11 51.02 0.3,-2.85 51.42 0.4,-2.59 51.46 0.5)

### Example 9 Request data along a specified 3D trajectory with each waypoint at a different height but at the same time

    .../trajectory?coords=LINESTRINGZ(-3.53 50.72 0.1,-3.35 50.92 0.2,-3.11 51.02 0.3,-2.85 51.42 0.4,-2.59 51.46 0.5)&datetime=2018-02-12T23:00:00Z

### Example 10 Request data along a specified 4D trajectory with each waypoint at different heights and times

    .../trajectory?coords=LINESTRINGZM(-3.53 50.72 0.1 1560507000,-3.35 50.92 0.2 1560508800,-3.11 51.02 0.3 1560510600,-2.85 51.42 0.41560513600,-2.59 51.46 0.5 1560515400)

## Further guidance

See the Examples in the
[Standard](https://opengeospatial.github.io/ogcna-auto-review/19-086r5.html).

## Media type

application/json

## Link relation types

Link relation types do not seem applicable for a Cube Query. Possibly
\`describedby\`could be useful.
