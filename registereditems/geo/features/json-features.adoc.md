Version: 1.0.1

# Overview

The features in an [OGC Collection](../common/json-collection.adoc).

This resource supports spatial filtering with the [`bbox`
parameter](../../common/parameters/bbox.adoc), temporal filtering with
the [`datetime` parameter](../common/parameters-datetime.adoc).

To avoid overloading clients and servers, both clients and servers can
limit the maximum number of features in a representation of the
resource. In this case, paging is supported to provide access to all the
features in the collection that match the specified filter conditions.

[**Maturity**](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity):
Mature

# Pre-defined properties

| Property       | Type                                         | Description                                                                                                                                                                                                                                                                                                                                 |
| -------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| links          | \[ [Link](../../ogc-utils/json-link.adoc) \] | **REQUIRED**. Links to other resources. See [Link relation types](#link-relations) for typical link relations of this resource type.                                                                                                                                                                                                        |
| features       | \[ [Feature](json-feature.adoc) \]           | **REQUIRED**. The features in the collection.                                                                                                                                                                                                                                                                                               |
| timeStamp      | string                                       | The RFC 3339 time stamp when the resource representation was generated.                                                                                                                                                                                                                                                                     |
| numberMatched  | integer                                      | **RECOMMENDED**. If a property `numberMatched` is included in the response, the value is the number of features in the feature collections that match the filter parameters like `bbox`, `datetime`, etc. Servers can omit this information, if the information about the number of matching features is not known or difficult to compute. |
| numberReturned | integer                                      | **RECOMMENDED**. If a property `numberReturned` is included in the response, the value is the number of features in the response document. Servers can omit this information, if the information about the number of features is not known or difficult to compute.                                                                         |

Properties

# Link relation types

The following link relation types are commonly used in links from a
Features resource:

| Link relation type | Description                                                                                                                                  |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`             | **REQUIRED**. Link to the resource in the current representation.                                                                            |
| `alternate`        | **REQUIRED**. Link to the resource in every other media type supported by the server.                                                        |
| `next`             | **CONDITIONAL**. If the response is a page of a paged response and there is another page, a link will reference that next page.              |
| `prev`             | If the response is a page of a paged response and there is a previous page, a link may reference that previous page.                         |
| `first`            | If the response is a page of a paged response, a link may reference the first page.                                                          |
| `last`             | If the response is a page of a paged response, a link may reference the last page.                                                           |
| `license`          | **RECOMMENDED**. Refers to the license associated with the data.                                                                             |
| `describedby`      | Refers to a resource providing information about the data, for example, a schema for the feature collection or a separate metadata resource. |

Outgoing link relation types

The following link relation types are commonly used in links to a
Features resource:

<table>
<caption>Incoming link relation types</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Link relation type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>items</code></p></td>
<td><p>From a <a href="../common/json-collection.adoc">OGC Collection resource</a>.</p>
<p>This link relation type will not be registered with IANA. In the future, it may be superseded by the <code>search</code> link relation type.</p></td>
</tr>
<tr class="even">
<td><p><code>search</code></p></td>
<td><p>From any resource that wants to link to a resource that supports searching the features, e.g. from a <a href="../../common/resources/collection.adoc">OGC Collection resource</a>.</p>
<p>This link relation type is expected to supersede the use of the <code>items</code> link relation type.</p></td>
</tr>
</tbody>
</table>

# Representation: GeoJSON

The GeoJSON representation is the currently recommended representation
that all APIs should support, where GeoJSON can be used for the data.

In addition to the pre-defined properties listed above, each GeoJSON
feature collection includes a JSON member with the key `type` and the
value "FeatureCollection".

## Example

``` JSON
{
   "type":"FeatureCollection",
   "links":[
      {
         "href":"https://demo.ldproxy.net/zoomstack/collections/airports/items?f=json",
         "rel":"self",
         "type":"application/geo+json",
         "title":"This document"
      },
      {
         "href":"https://demo.ldproxy.net/zoomstack/collections/airports/items?f=html",
         "rel":"alternate",
         "type":"text/html",
         "title":"This document as HTML"
      },
      {
         "href":"https://demo.ldproxy.net/zoomstack/collections/airports/items?f=json&offset=10",
         "rel":"next",
         "type":"application/geo+json",
         "title":"Next page"
      }
   ],
   "numberReturned":10,
   "timeStamp":"2021-07-07T12:38:27Z",
   "features":[
      {
         "type":"Feature",
         "id":1,
         "geometry":{
            "type":"Point",
            "coordinates":[
               -1.6930015,
               60.3216821
            ]
         },
         "properties":{
            "name":"Papa Stour Airstrip"
         }
      },
      {
         "type":"Feature",
         "id":2,
         "geometry":{
            "type":"Point",
            "coordinates":[
               -1.2922268,
               59.8782666
            ]
         },
         "properties":{
            "name":"Sumburgh Airport"
         }
      },
      {
         "type":"Feature",
         "id":3,
         "geometry":{
            "type":"Point",
            "coordinates":[
               -1.2439112,
               60.1917461
            ]
         },
         "properties":{
            "name":"Tingwall Airport"
         }
      },
      {
         "type":"Feature",
         "id":4,
         "geometry":{
            "type":"Point",
            "coordinates":[
               -2.8997054,
               58.9579609
            ]
         },
         "properties":{
            "name":"Kirkwall Airport"
         }
      },
      {
         "type":"Feature",
         "id":5,
         "geometry":{
            "type":"Point",
            "coordinates":[
               -6.3295079,
               58.2139012
            ]
         },
         "properties":{
            "name":"Port-Adhair Steòrnabhaigh/Stornoway Airport"
         }
      },
      {
         "type":"Feature",
         "id":6,
         "geometry":{
            "type":"Point",
            "coordinates":[
               -3.094033,
               58.4583627
            ]
         },
         "properties":{
            "name":"Wick John O'Groats Airport"
         }
      },
      {
         "type":"Feature",
         "id":7,
         "geometry":{
            "type":"Point",
            "coordinates":[
               -7.3604149,
               57.4838089
            ]
         },
         "properties":{
            "name":"Benbecula Airport"
         }
      },
      {
         "type":"Feature",
         "id":8,
         "geometry":{
            "type":"Point",
            "coordinates":[
               -7.4485984,
               57.0255697
            ]
         },
         "properties":{
            "name":"Barra Airport"
         }
      },
      {
         "type":"Feature",
         "id":9,
         "geometry":{
            "type":"Point",
            "coordinates":[
               -4.0493516,
               57.5431467
            ]
         },
         "properties":{
            "name":"Inverness Airport"
         }
      },
      {
         "type":"Feature",
         "id":10,
         "geometry":{
            "type":"Point",
            "coordinates":[
               -2.2001789,
               57.2023588
            ]
         },
         "properties":{
            "name":"Aberdeen International Airport"
         }
      }
   ]
}
```

## Media type

`application/geo+json`

## Schema

``` YAML
allOf:
  - $ref: https://geojson.org/schema/FeatureCollection.json
  - type: object
    properties:
      links:
        type: array
        items:
          $ref: ../../../ogc-utils/schemas/json-link.yaml
      timeStamp:
        type: string
        format: date-time
      numberMatched:
        type: integer
        minimum: 0
      numberReturned:
        type: integer
        minimum: 0
```

# Representation: HTML

Providing an HTML representation is recommended so that the resource can
be displayed in a web browser and indexed by search engines.

The HTML representation should include all information that is part of
the JSON representation.

## Media type

`text/html`

# Source References

  - [OGC API - Features, Part 1, 7.15.7: Features
    response](http://www.opengis.net/doc/IS/ogcapi-features-1/1.0#_response_6)

  - [OGC API - Features, Part 1, 8.3:
    GeoJSON](http://www.opengis.net/doc/IS/ogcapi-features-1/1.0#_requirements_class_geojson)
