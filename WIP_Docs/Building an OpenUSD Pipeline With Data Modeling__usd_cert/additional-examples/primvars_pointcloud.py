"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 5 (PointInstancer + per-instance visualization data)

Why this script exists:
- It provides a compact point-cloud-style instancer example.
- This mirrors the Station 7 sensor overlay pattern at practical scale.

How to run:
- From the __usd_cert folder:
  python additional-examples/primvars_pointcloud.py

What to observe:
1) Prototype list and protoIndices mapping.
2) Per-instance displayColor primvar authoring with varying interpolation.
3) Stage structure suitable for usdview inspection and iteration.
"""

from pxr import Usd, UsdGeom, Sdf, Gf, Vt

def create_instancer_with_primvars():
    stage = Usd.Stage.CreateNew('_assets/point_cloud_instancer.usda')
    
    # 1. Create the PointInstancer prim
    instancer = UsdGeom.PointInstancer.Define(stage, '/Scene/Instancer')
    
    # 2. Define Prototypes (The objects we want to instance)
    # These are usually hidden or placed under a 'Prototypes' scope
    proto_scope = UsdGeom.Scope.Define(stage, '/Scene/Instancer/Prototypes')
    
    cube_a = UsdGeom.Cube.Define(stage, '/Scene/Instancer/Prototypes/CubeA')
    cube_b = UsdGeom.Cube.Define(stage, '/Scene/Instancer/Prototypes/CubeB')
    
    # Add the prototypes to the instancer's relationship list
    instancer.GetPrototypesRel().SetTargets([cube_a.GetPath(), cube_b.GetPath()])
    
    # 3. Define the Point Cloud Data (Positions and Indices)
    positions = Vt.Vec3fArray([
        (0,0,0), (2,0,0), (4,0,0), 
        (0,2,0), (2,2,0), (4,2,0)
    ])
    # protoIndices: which prototype to use for each point (0=CubeA, 1=CubeB)
    proto_indices = Vt.IntArray([0, 1, 0, 1, 0, 1])
    
    instancer.CreatePositionsAttr(positions)
    instancer.CreateProtoIndicesAttr(proto_indices)
    
    # 4. Author Primvars for Instance Variation
    # We use PrimvarsAPI to create a primvar that varies per instance
    primvars_api = UsdGeom.PrimvarsAPI(instancer)
    
    # Example: Custom 'displayColor' per instance
    # For PointInstancers, 'varying' interpolation often maps to each point
    colors = Vt.Vec3fArray([
        (1,0,0), (0,1,0), (0,0,1), 
        (1,1,0), (1,0,1), (0,1,1)
    ])
    color_pv = primvars_api.CreatePrimvar(
        "displayColor", 
        Sdf.ValueTypeNames.Color3fArray, 
        UsdGeom.Tokens.varying
    )
    color_pv.Set(colors)

    # 5. Save the result
    stage.GetRootLayer().Save()
    print("Point Cloud Instancer created successfully.")

if __name__ == "__main__":
    create_instancer_with_primvars()