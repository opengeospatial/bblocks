Version: 1.0.1

# Overview

This JSON object provides information about the spatial and temporal
extent of a resource.

A typical resource type is a collection and the object describes the
extent of all items in the collection.

[**Maturity**](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity):
Mature

# Description

This object provides the axis-aligned extent of a resource.

Only spatial and temporal extents are specified. Additional members may
be added to represent other extents, for example, thermal or pressure
ranges.

# Pre-defined properties

| Property | Type                         | Description                                                                                                                    |
| -------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| spatial  | [Spatial Extent](#spatial)   | **CONDITIONAL**. The spatial extent of the resource. This property has to be provided, if the resource has a spatial extent.   |
| temporal | [Temporal Extent](#temporal) | **CONDITIONAL**. The temporal extent of the resource. This property has to be provided, if the resource has a temporal extent. |

Properties

For example, a feature collection where features have a spatial, but no
temporal property will only provide the `spatial` member.

Additional properties for other aspects may be added.

## Spatial Extent

<table>
<caption>Properties</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 10%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>bbox</p></td>
<td><p>[ <a href="json-bbox.adoc">Bounding Box</a> ]</p></td>
<td><p><strong>REQUIRED</strong>. The first bounding box in the array describes the overall spatial extent. All subsequent bounding boxes describe more precise extents, e.g., to identify clusters of data. Clients only interested in the overall extent will only access the first item in the array.</p>
<p>The extent information will typically be derived automatically and be the minimal axis-aligned bounding box of the resource.</p></td>
</tr>
<tr class="even">
<td><p>crs</p></td>
<td><p>URI</p></td>
<td><p>The spatial coordinate reference system of the coordinates in <code>bbox</code>.</p>
<p>If no value is provided, the default reference system is WGS 84 longitude/latitude ("http://www.opengis.net/def/crs/OGC/1.3/CRS84").</p></td>
</tr>
</tbody>
</table>

Additional properties for other descriptions of the spatial extent may
be added.

## Temporal Extent

<table>
<caption>Properties</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 10%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>interval</p></td>
<td><p>[ <a href="../../ogc-utils/json-interval.adoc">Interval</a> ]</p></td>
<td><p><strong>REQUIRED</strong>. The first interval in the array describes the overall temporal extent. All subsequent intervals describe more precise extents, e.g., to identify clusters of data. Clients only interested in the overall extent will only access the first item in the array.</p>
<p>The extent information will typically be derived automatically and be the minimal interval of the resource.</p></td>
</tr>
<tr class="even">
<td><p>trs</p></td>
<td><p>URI</p></td>
<td><p>The temporal coordinate reference system of instants in <code>interval</code>.</p>
<p>If no value is provided, the default reference system is the Gregorian calendar ("http://www.opengis.net/def/uom/ISO-8601/0/Gregorian").</p></td>
</tr>
</tbody>
</table>

Additional properties for other descriptions of the temporal extent may
be added.

## Example

The following extent can describe feature data in the United States of
America (excluding Territories) that covers the year 2020.

The first bounding box of the four bounding boxes is the union of the
three other bounding boxes representing the 48 contiguous states, Alaska
and Hawaii respectively - from the west-bound longitude of Alaska to the
east-bound longitude of the 48 contiguous states.

Note that the overall bounding box as well as the bounding box of Alaska
cross the anti-meridian.

``` JSON
{
  "spatial": {
    "bbox": [
      [172.461667, 18.910361, -66.9513812, 71.365162],
      [-124.7844079, 24.7433195, -66.9513812, 49.3457868],
      [172.461667, 51.214183, -129.979511, 71.365162],
      [-178.334698, 18.910361, -154.806773, 28.402123]
    ]
  },
  "temporal": {
     "interval": [ "2020-01-01", "2020-12-31" ]
  }
}
```

As can be seen in the example, there can be multiple ways to construct
the overall bounding box from its component bounding boxes since
longitudes are cyclic (that is, -180° is equal to 180°). Another union
of the component bounding boxes for the 48 contiguous states, Alaska and
Hawaii would be `[-124.7844079, 18.910361, -129.979511, 71.365162]` -
from the west-bound longitude of the 48 contiguous states to the
east-bound longitude of Alaska. The typical approach in such cases is to
select the option with the smallest area, as was done in the example.

## Schema

``` YAML
type: object
properties:
  spatial:
    type: object
    properties:
      bbox:
        type: array
        minItems: 1
        items:
          $ref: json-bbox.yaml
      crs:
        type: string
        default: 'http://www.opengis.net/def/crs/OGC/1.3/CRS84'
  temporal:
    type: object
    properties:
      interval:
        type: array
        minItems: 1
        items:
          $ref: ../../../ogc-utils/schemas/json-interval.yaml
      trs:
        type: string
        default: 'http://www.opengis.net/def/uom/ISO-8601/0/Gregorian'
```

## Source Reference

[OGC API - Features, Part 1, 7.13.2: Feature Collections
Response](http://www.opengis.net/doc/IS/ogcapi-features-1/1.0#_response_4)
