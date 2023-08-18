---
title: JSON-FG Feature - Lenient (Schema)

toc_footers:
  - Version 0.1
  - <a href='#'>JSON-FG Feature - Lenient</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: JSON-FG Feature - Lenient (Schema)
---


# JSON-FG Feature - Lenient `ogc.geo.json-fg.feature-lenient`

A OGC Features and Geometries JSON (JSON-FG) Feature that does not require the "time" and "place" properties.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/stable" target="_blank" data-rainbow-uri>Stable</a>
</p>

<aside class="success">
This building block is <strong>valid</strong>
</aside>

# Description

OGC Features and Geometries JSON (JSON-FG) extends GeoJSON to support a limited set of additional capabilities that are
out-of-scope for GeoJSON, but that are essential or important for a variety of use cases involving feature data.

This Building Block extends the standard JSON-FG one by removing the requirement to provide values for the 
"time" and "place" properties.


# JSON Schema

```yaml--schema
allOf:
- $ref: ../../features/feature/schema.yaml
- type: object
  required:
  - type
  - geometry
  - properties
  properties:
    type:
      type: string
      enum:
      - Feature
      x-jsonld-id: '@type'
    id:
      oneOf:
      - type: number
      - type: string
      x-jsonld-id: '@id'
    featureType:
      $ref: https://beta.schemas.opengis.net/json-fg/featuretype.json
    links:
      type: array
      items:
        $ref: https://beta.schemas.opengis.net/json-fg/link.json
    time:
      $ref: https://beta.schemas.opengis.net/json-fg/time.json
    coordRefSys:
      $ref: https://beta.schemas.opengis.net/json-fg/coordrefsys.json
    place:
      $ref: https://beta.schemas.opengis.net/json-fg/place.json
    geometry:
      $ref: https://beta.schemas.opengis.net/json-fg/geometry.json
      x-jsonld-id: https://purl.org/geojson/vocab#geometry
    properties:
      oneOf:
      - type: 'null'
      - type: object
      x-jsonld-id: https://purl.org/geojson/vocab#properties
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  GeometryCollection: https://purl.org/geojson/vocab#GeometryCollection
  LineString: https://purl.org/geojson/vocab#LineString
  MultiLineString: https://purl.org/geojson/vocab#MultiLineString
  MultiPoint: https://purl.org/geojson/vocab#MultiPoint
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
  Point: https://purl.org/geojson/vocab#Point
  Polygon: https://purl.org/geojson/vocab#Polygon
  bbox:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#bbox
  coordinates:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#coordinates
  features:
    x-jsonld-container: '@set'
    x-jsonld-id: https://purl.org/geojson/vocab#features
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;data=allOf%3A%0A-+%24ref%3A+..%2F..%2Ffeatures%2Ffeature%2Fschema.yaml%0A-+type%3A+object%0A++required%3A%0A++-+type%0A++-+geometry%0A++-+properties%0A++properties%3A%0A++++type%3A%0A++++++type%3A+string%0A++++++enum%3A%0A++++++-+Feature%0A++++++x-jsonld-id%3A+%27%40type%27%0A++++id%3A%0A++++++oneOf%3A%0A++++++-+type%3A+number%0A++++++-+type%3A+string%0A++++++x-jsonld-id%3A+%27%40id%27%0A++++featureType%3A%0A++++++%24ref%3A+https%3A%2F%2Fbeta.schemas.opengis.net%2Fjson-fg%2Ffeaturetype.json%0A++++links%3A%0A++++++type%3A+array%0A++++++items%3A%0A++++++++%24ref%3A+https%3A%2F%2Fbeta.schemas.opengis.net%2Fjson-fg%2Flink.json%0A++++time%3A%0A++++++%24ref%3A+https%3A%2F%2Fbeta.schemas.opengis.net%2Fjson-fg%2Ftime.json%0A++++coordRefSys%3A%0A++++++%24ref%3A+https%3A%2F%2Fbeta.schemas.opengis.net%2Fjson-fg%2Fcoordrefsys.json%0A++++place%3A%0A++++++%24ref%3A+https%3A%2F%2Fbeta.schemas.opengis.net%2Fjson-fg%2Fplace.json%0A++++geometry%3A%0A++++++%24ref%3A+https%3A%2F%2Fbeta.schemas.opengis.net%2Fjson-fg%2Fgeometry.json%0A++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23geometry%0A++++properties%3A%0A++++++oneOf%3A%0A++++++-+type%3A+%27null%27%0A++++++-+type%3A+object%0A++++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23properties%0Ax-jsonld-extra-terms%3A%0A++Feature%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23Feature%0A++FeatureCollection%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23FeatureCollection%0A++GeometryCollection%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23GeometryCollection%0A++LineString%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23LineString%0A++MultiLineString%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23MultiLineString%0A++MultiPoint%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23MultiPoint%0A++MultiPolygon%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23MultiPolygon%0A++Point%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23Point%0A++Polygon%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23Polygon%0A++bbox%3A%0A++++x-jsonld-container%3A+%27%40list%27%0A++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23bbox%0A++coordinates%3A%0A++++x-jsonld-container%3A+%27%40list%27%0A++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23coordinates%0A++features%3A%0A++++x-jsonld-container%3A+%27%40set%27%0A++++x-jsonld-id%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23features%0Ax-jsonld-prefixes%3A%0A++geojson%3A+https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23%0A">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature-lenient/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature-lenient/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature-lenient/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature-lenient/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "type": "@type",
    "id": "@id",
    "properties": "geojson:properties",
    "geometry": {
      "@id": "geojson:geometry",
      "@context": {}
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "features": {
      "@container": "@set",
      "@id": "geojson:features"
    },
    "links": {
      "@id": "rdfs:seeAlso",
      "@context": {
        "href": "@id",
        "title": "rdfs:label"
      }
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=%7B%0A++%22%40context%22%3A+%7B%0A++++%22type%22%3A+%22%40type%22%2C%0A++++%22id%22%3A+%22%40id%22%2C%0A++++%22properties%22%3A+%22geojson%3Aproperties%22%2C%0A++++%22geometry%22%3A+%7B%0A++++++%22%40id%22%3A+%22geojson%3Ageometry%22%2C%0A++++++%22%40context%22%3A+%7B%7D%0A++++%7D%2C%0A++++%22bbox%22%3A+%7B%0A++++++%22%40container%22%3A+%22%40list%22%2C%0A++++++%22%40id%22%3A+%22geojson%3Abbox%22%0A++++%7D%2C%0A++++%22Feature%22%3A+%22geojson%3AFeature%22%2C%0A++++%22FeatureCollection%22%3A+%22geojson%3AFeatureCollection%22%2C%0A++++%22GeometryCollection%22%3A+%22geojson%3AGeometryCollection%22%2C%0A++++%22LineString%22%3A+%22geojson%3ALineString%22%2C%0A++++%22MultiLineString%22%3A+%22geojson%3AMultiLineString%22%2C%0A++++%22MultiPoint%22%3A+%22geojson%3AMultiPoint%22%2C%0A++++%22MultiPolygon%22%3A+%22geojson%3AMultiPolygon%22%2C%0A++++%22Point%22%3A+%22geojson%3APoint%22%2C%0A++++%22Polygon%22%3A+%22geojson%3APolygon%22%2C%0A++++%22features%22%3A+%7B%0A++++++%22%40container%22%3A+%22%40set%22%2C%0A++++++%22%40id%22%3A+%22geojson%3Afeatures%22%0A++++%7D%2C%0A++++%22links%22%3A+%7B%0A++++++%22%40id%22%3A+%22rdfs%3AseeAlso%22%2C%0A++++++%22%40context%22%3A+%7B%0A++++++++%22href%22%3A+%22%40id%22%2C%0A++++++++%22title%22%3A+%22rdfs%3Alabel%22%0A++++++%7D%0A++++%7D%2C%0A++++%22coordinates%22%3A+%7B%0A++++++%22%40container%22%3A+%22%40list%22%2C%0A++++++%22%40id%22%3A+%22geojson%3Acoordinates%22%0A++++%7D%2C%0A++++%22geojson%22%3A+%22https%3A%2F%2Fpurl.org%2Fgeojson%2Fvocab%23%22%2C%0A++++%22rdfs%22%3A+%22http%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%22%2C%0A++++%22%40version%22%3A+1.1%0A++%7D%0A%7D">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature-lenient/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature-lenient/context.jsonld</a>

# References

* [OGC Testbed-17: OGC Features and Geometries JSON Engineering Report](http://docs.ogc.org/per/21-017r1.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path:
<code><a href="https://github.com/opengeospatial/bblocks/blob/HEAD/registereditems/geo/json-fg/feature-lenient" target="_blank">registereditems/geo/json-fg/feature-lenient</a></code>

