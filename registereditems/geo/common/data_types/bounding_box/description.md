A bounding box is provided as an array of four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth):

* Lower left corner, coordinate axis 1
* Lower left corner, coordinate axis 2
* Minimum value, coordinate axis 3 (optional)
* Upper right corner, coordinate axis 1
* Upper right corner, coordinate axis 2
* Maximum value, coordinate axis 3 (optional)

If the value consists of four numbers, the coordinate reference system is WGS 84 longitude/latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate reference system is specified.

If the value consists of six numbers, the coordinate reference system is WGS 84 longitude/latitude/height (http://www.opengis.net/def/crs/OGC/0/CRS84h) unless a different coordinate reference system is specified.

How a different coordinate reference system is specified depends on the context in which the bounding box is used.

For WGS 84 longitude/latitude the values are in most cases the sequence of minimum longitude, minimum latitude, maximum longitude and maximum latitude. However, in cases where the box spans the antimeridian the first value (west-most box edge) is larger than the third value (east-most box edge).

If the vertical axis is included, the third and the sixth number are the bottom and the top of the 3-dimensional bounding box.

The text representation of a bounding box is based on the JSON representation and represents the array as comma-separated values.
