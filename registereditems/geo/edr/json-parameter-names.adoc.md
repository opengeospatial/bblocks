# Parameter-Name Object

## Overview

The `parameter-name` object provides information about a data parameter
supported by a Collection. The Collection may expose several
`parameter-name` objects, as a set of key-value pairs, where the key is
the name of the parameter and the value is a
[Parameter-Name](#col-parameter) object.

There is also a very similar, compatible, JSON object defined in the
[CoverageJSON
specification](https://opengeospatial.github.io/ogcna-auto-review/21-069.html#toc22)
called `parameter`.

This building block is called `parameter-name` to try to avoid confusion
with the JSON use of `parameter`.

## Source Reference

It is defined in the [OGC API-EDR V1.0.1 specification,
Section 8.2.1.3](https://docs.ogc.org/is/19-086r5/19-086r5.htm) which is
maintained by the OGC EDR API Standard Working Group using this [OGC
GitHub
repository](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval).

## Maturity

Stable

## Pre-defined Properties of the Parameter-Name Object

| Field Name           | Type                                              | Required | Description                                                                                                              |
| -------------------- | ------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| id                   | String                                            | No       | parameter id                                                                                                             |
| **type**             | String                                            | **Yes**  | Always 'Parameter'                                                                                                       |
| label                | String                                            | No       | A short text label for the parameter                                                                                     |
| description          | String                                            | No       | A description of the parameter                                                                                           |
| data-type            | String                                            | No       | The data type of the parameter values \[integer, float, string\]                                                         |
| unit                 | [unit](#col-unit) object                          | No       | A description of the units of the parameter values                                                                       |
| **observedProperty** | [observedProperty](#col-observed_property) object | **Yes**  | A formal definition of the parameter                                                                                     |
| extent               | [Extent](#col-extent) object                      | No       | Information on the spatio-temporal extent of the parameter values (if different from other parameters in the collection) |
| measurementType      | [measurementType](#col-measurement_type) object   | No       | Information on how the value was derived                                                                                 |

Parameter-Name Object

## Model (UML) TBD

## Model (OWL, or at least a formal and stable mapping of concepts to URIs) TBD

## JSON schema

Currently the schema is [defined in
YAML](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/blob/master/standard/openapi/schemas/collections/parameterNames.yaml)

## JSON-LD context TBD e.g. <https://github.com/covjson/specification/blob/master/contexts/context.jsonld>

## Validator

[OGC API - Environmental Data Retrieval 1.0 Conformance Test Suite,
Beta,
Version 0.5, 2022-11-08](https://cite.opengeospatial.org/te2/about/ogcapi-edr10/1.0/site/).

## Examples

See some Examples in the [Standard,
Clause 8.2.1.3](https://opengeospatial.github.io/ogcna-auto-review/19-086r5.html#parameter-name).

Also, some examples from an implementation

### Example 1, Height of the Maximum Wind (for aviation)

    "max_wind_ht":{
       "type":"Parameter",
       "id":"max_wind_ht",
       "description":"Height at which the maximum wind speed occurs",
       "unit":{
          "symbol":{
             "value":"m",
             "type":"http://codes.wmo.int/common/unit/_m"
          },
          "label":"m"
       },
       "observedProperty":{
          "id":"http://codes.wmo.int/grib2/codeflag/4.2/_0-3-3",
          "label":"ICAO Standard Atmosphere Reference Height [m]"
       }
    },

### Example 2, Geopotential Height, measured in geopotential meters

    "geo_pot_ht":{
                   "type":"Parameter",
                   "id":"geo_pot_ht",
                   "description":"Geopotential height [gpm]",
                   "unit":{
                      "symbol":{
                         "value":"gpm",
                         "type":"http://codes.wmo.int/common/unit/_gpm"
                      },
                      "label":"gpm"
                   },
                   "observedProperty":{
                      "id":"http://codes.wmo.int/grib2/codeflag/4.2/_0-3-5",
                      "label":"Geopotential height [gpm]"
                      }
                  },

### Example 3, Relative Humidity, as a percentage

``` 
            "rh":{
               "type":"Parameter",
               "id":"rh",
               "description":"Relative humidity [%]",
               "unit":{
                  "symbol":{
                     "value":"%",
                     "type":"http://codes.wmo.int/common/unit/percent"
                  },
                  "label":"%"
               },
               "observedProperty":{
                  "id":"http://codes.wmo.int/grib2/codeflag/4.2/_0-1-1",
                  "label":"Relative humidity [%]"
               }
            }
```

## Further guidance

See the Examples in the
[Standard](https://opengeospatial.github.io/ogcna-auto-review/19-086r5.html).

## Media type

application/json

## Link relation types

Link relation types do not seem applicable for a Parameter Name Object.
Possibly \`describedby\`old be useful.
