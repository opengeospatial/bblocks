# Cube Query

## Overview

The `Cube` query returns a data cube defined by the `bbox` and `z`
parameters. The results are further filtered by the constraints defined
by the following query parameters:

<table>
<caption>Cube query structure</caption>
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
<p>The X and Y coordinates are values in the coordinate system defined by the crs query parameter. If crs is not defined, the values will be assumed to be WGS84 longitude/latitude coordinates and heights will be assumed to be in metres above mean sea level.</p></td>
<td><ul>
<li><p><code>bbox=-6.0,50.0,-4.35,52.0</code></p></li>
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
<td><p>coordinate reference system identifier for the <strong>coords</strong> values and output data (available options listed in the <a href="#collection_metadata_desc">collections</a> metadata response)</p></td>
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

*If a client request has a **bbox** value which includes height values
and defines a **z** query parameter the **z** query parameter will be
the definition of the requested height value*

## Source Reference

It is defined in the [OGC API-EDR V1.0.1 specification,
Section 8.2.4](https://docs.ogc.org/is/19-086r5/19-086r5.htm) which is
maintained by the OGC EDR API Standard Working Group using this [OGC
GitHub
repository](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval).

## Maturity

Stable

## Model (UML) TBD

## Model (OWL, or at least a formal and stable mapping of concepts to URIs) TBD

## JSON schema

Currently the schema is [defined in
YAML](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/standard/openapi/request-bodies/cube.yaml)

## JSON-LD context TBD e.g. <https://github.com/covjson/specification/blob/master/contexts/context.jsonld>

## Validator

[OGC API - Environmental Data Retrieval 1.0 Conformance Test Suite,
Beta,
Version 0.5, 2022-11-08](https://cite.opengeospatial.org/te2/about/ogcapi-edr10/1.0/site/).

## Examples

See the Examples in the [Standard,
Clause 8.2.4](https://opengeospatial.github.io/ogcna-auto-review/19-086r5.html#parameter-name).

### Example 1 Request data within a specified `bbox` for a single level and single time

    .../cube?bbox=-6.0,50.0,-4.35,52.0&z=850&datetime=2018-02-12T00:00Z

### Example 2 Request data within a specified `bbox` for a single level and a range of times

    .../cube?bbox=-6.0,50.0,-4.35,52.0&z=850&datetime=2018-02-12T00:00/2018-03-18T12:31Z

### Example 3 Request data within a specified `bbox` for a single time and for several levels

    .../cube?bbox=-6.0,50.0,-4.35,52.0&datetime=2018-02-12T00:00Z&z=1000,900,850,700

### Example 4 Request data within a specified `bbox` for a range of levels and a range of times

    .../cube?bbox=-6.0,50.0,-4.35,52.0&z=2/100&datetime=2018-02-12T00:00/2018-03-18T12:31Z

## Further guidance

See the Examples in the
[Standard](https://opengeospatial.github.io/ogcna-auto-review/19-086r5.html).

## Media type

application/json

## Link relation types

Link relation types do not seem applicable for a Cube Query. Possibly
\`describedby\`could be useful.
