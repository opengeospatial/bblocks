If the `bbox-crs` parameter is specified, then the values of the `bbox` parameter are assumed to be in the specified
coordinate reference system and the server will perform the necessary internal transformations to properly fetch data
from within the specified bounding box.

Otherwise, the values for the `bbox` parameter shall be assumed to be WGS 84 longitude-latitude for coordinates
without height and WGS 84 longitude-latitude-height for coordinates with height.