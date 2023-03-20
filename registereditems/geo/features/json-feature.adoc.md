Version: 1.0.1

# Overview

A feature. Every feature is a sub-resource of an [OGC
Collection](../common/json-collection.adoc).

[**Maturity**](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity):
Mature

# Pre-defined properties

| Property | Type                                         | Description                                                                                                                          |
| -------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| links    | \[ [Link](../../ogc-utils/json-link.adoc) \] | **REQUIRED**. Links to other resources. See [Link relation types](#link-relations) for typical link relations of this resource type. |
| id       | string or integer                            | **REQUIRED**. The feature identifier in the collection.                                                                              |

Properties

In addition, there will be properties that describe the real-world
entity that the feature represents plus optionally properties that are
metadata.

# Link relation types

The following link relation types are commonly used in links from a
Feature:

| Link relation type | Description                                                                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `self`             | **REQUIRED**. Link to the resource in the current representation.                                                                 |
| `alternate`        | **REQUIRED**. Link to the resource in every other media type supported by the server.                                             |
| `collection`       | **REQUIRED**. Link to the OGC Collection that this feature belongs to.                                                            |
| `describedby`      | Refers to a resource providing information about the data, for example, a schema for the feature or a separate metadata resource. |
| `type`             | Refers to the canonical URI of a feature type that the feature implements.                                                        |
| `canonical`        | Refers to a persistent URI of this feature that will not change between API changes.                                              |

Outgoing link relation types

The following link relation types are commonly used in links to a
Feature:

| Link relation type | Description                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------ |
| `item`             | May by used to point to the feature from a static [OGC Collection resource](../common/json-collection.adoc). |

Incoming link relation types

# Representation: GeoJSON

The GeoJSON representation is the currently recommended representation
that all APIs should support, where GeoJSON can be used for the data.

In addition to the pre-defined properties listed above, each GeoJSON
feature includes the following JSON members:

  - `type`: fixed value "Feature".

  - `geometry`: the primary geometry of the feature describing its
    location as a GeoJSON geometry object. `null`, if the feature has no
    spatial geometry.

  - `properties`: an object with a member for each feature property.

## Example

``` JSON
{
   "type":"Feature",
   "links":[
      {
         "href":"https://demo.ldproxy.net/zoomstack/collections/airports/items/8?f=json",
         "rel":"self",
         "type":"application/geo+json",
         "title":"This document"
      },
      {
         "href":"https://demo.ldproxy.net/zoomstack/collections/airports/items/8?f=html",
         "rel":"alternate",
         "type":"text/html",
         "title":"This document as HTML"
      },
      {
         "href":"https://demo.ldproxy.net/zoomstack/collections/airports?f=json",
         "rel":"collection",
         "type":"application/json",
         "title":"The collection the feature belongs to"
      }
   ],
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
}
```

## Media type

`application/geo+json`

## Schema

``` YAML
allOf:
  - $ref: https://geojson.org/schema/Feature.json
  - type: object
    properties:
      links:
        type: array
        items:
          $ref: ../../../ogc-utils/schemas/json-link.yaml
```

# Representation: HTML

Providing an HTML representation is recommended so that the resource can
be displayed in a web browser and indexed by search engines.

The HTML representation should include all information that is part of
the JSON representation.

## Media type

`text/html`

# Source References

  - [OGC API - Features, Part 1, 7.16.2: Feature
    response](http://www.opengis.net/doc/IS/ogcapi-features-1/1.0#_response_7)

  - [OGC API - Features, Part 1, 8.3:
    GeoJSON](http://www.opengis.net/doc/IS/ogcapi-features-1/1.0#_requirements_class_geojson)
