"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 3 (type safety as a pipeline feature)

Why this script exists:
- It gives a compact catalog of common USD value types.
- It demonstrates why token/asset/role/array choices reduce data drift.

How to run:
- From the __usd_cert folder:
  python data-types/7a_value_types.py

What to observe:
1) Mixed scalar and specialized typed attributes on one prim.
2) Role type semantics (Point3f vs Vector3f vs Normal3f).
3) Array authoring patterns for time-series and point data.
"""

from pxr import Usd, Sdf, Tf, UsdGeom

# Create an in-memory stage
stage = Usd.Stage.CreateInMemory()
prim = stage.DefinePrim("/InfrastructureObject", "Xform")

# 1. Basic Scalar Types
# bool, int, float, double, string
prim.CreateAttribute("isActive", Sdf.ValueTypeNames.Bool).Set(True)
prim.CreateAttribute("sensorID", Sdf.ValueTypeNames.Int).Set(1024)
prim.CreateAttribute("precisionValue", Sdf.ValueTypeNames.Double).Set(0.0000045)
prim.CreateAttribute("description", Sdf.ValueTypeNames.String).Set("Data center rack")

# 2. Specialized String Types (Token and Asset)
# Use Token for repeated keywords/enums, Asset for file paths
prim.CreateAttribute("status", Sdf.ValueTypeNames.Token).Set("Maintenance")
prim.CreateAttribute("schematicPath", Sdf.ValueTypeNames.Asset).Set("./docs/layout.pdf")

# 3. Geometric Role Types (3D Vectors)
# These tell USD how to treat the 3D data during transforms
prim.CreateAttribute("position", Sdf.ValueTypeNames.Point3f).Set((10.0, 5.0, 0.0))
prim.CreateAttribute("velocity", Sdf.ValueTypeNames.Vector3f).Set((0.0, 1.0, 0.0))
prim.CreateAttribute("surfaceNormal", Sdf.ValueTypeNames.Normal3f).Set((0.0, 0.0, 1.0))
prim.CreateAttribute("displayColor", Sdf.ValueTypeNames.Color3f).Set((0.2, 0.8, 0.2))

# 4. Matrix Types
# Standard 4x4 matrix for transformations
from pxr import Gf
matrix = Gf.Matrix4d(1.0) # Identity matrix
prim.CreateAttribute("transformMatrix", Sdf.ValueTypeNames.Matrix4d).Set(matrix)

# 5. Array Types
# Simply add 'Array' to the end of the type name
prim.CreateAttribute("tempReadings", Sdf.ValueTypeNames.FloatArray).Set([22.5, 23.1, 22.8])
prim.CreateAttribute("pointCloud", Sdf.ValueTypeNames.Point3fArray).Set([(0,0,0), (1,1,1), (2,2,2)])

# Inspect the result in USDA format
print(stage.GetRootLayer().ExportToString())
#print(dir(UsdGeom.Tokens))