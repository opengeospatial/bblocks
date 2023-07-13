GeoPose 1.0 is an OGC Implementation Standard for exchanging the location and orientation of real or virtual geometric
objects (“Poses”) within reference frames anchored to the earth’s surface (“Geo”) or within other astronomical
coordinate systems.

The Basic-YPR Target has a simple structure with no options. Position is specified as a point in an LTP-ENU frame and
rotation is specified by yaw, pitch, and roll angles specified in decimal degrees.

The Basic_YPR.position attribute shall represent the outer frame, specified by an implicit WGS-84 CRS and an implicit
EPSG 4461-CS (LTP-ENU) coordinate system and explicit parameters to define the tangent point.

The Basic_YPR.angles attribute shall represent the inner frame, which is a rotation-only transformation with Yaw, Pitch,
and Roll (YPR) angles, which expressed as three consecutive rotations of a reference frame oriented East-North-Up (ENU)
coordinate system (where the coordinate axes East, North, and Up correspond to the axes X, Y, Z) about the local (
rotated) axes z, y, and x, applied in that order, corresponding to the conventional Yaw, Pitch, and Roll angles. The
unit of measure SHALL be the degree and the angles represented as signed real number values.