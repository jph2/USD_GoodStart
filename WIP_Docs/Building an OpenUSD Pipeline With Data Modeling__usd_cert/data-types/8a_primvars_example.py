"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 5 (primvars fundamentals + interpolation choices)

Why this script exists:
- It demonstrates PrimvarsAPI on a simple mesh.
- This is the minimum pattern before scaling to PointInstancer workflows.

How to run:
- From the __usd_cert folder:
  python data-types/8a_primvars_example.py

What to observe:
1) Creation of displayColor primvar with explicit type/interpolation.
2) Constant-value primvar authoring and read-back.
3) How primvars live alongside mesh topology attributes.
"""

import os
from pxr import Usd, UsdGeom, Sdf, Gf

def create_mesh_with_primvars_api():
    # 1. Setup Stage
    # Save to usd_root/_assets/
    usd_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    assets_dir = os.path.join(usd_root, '_assets')
    os.makedirs(assets_dir, exist_ok=True)
    output_path = os.path.join(assets_dir, 'primvars_example.usda')
    stage = Usd.Stage.CreateNew(output_path)
    
    # 2. Define the Mesh
    mesh = UsdGeom.Mesh.Define(stage, '/pvexample')
    
    # 3. Geometry Attributes
    mesh.CreateExtentAttr([Gf.Vec3f(-1, 0, 0), Gf.Vec3f(1, 1, 0)])
    mesh.CreatePointsAttr([
        Gf.Vec3f(-1, 0, 0), Gf.Vec3f(-1, 1, 0), Gf.Vec3f(0, 1, 0), 
        Gf.Vec3f(0, 0, 0), Gf.Vec3f(1, 1, 0), Gf.Vec3f(1, 0, 0)
    ])
    mesh.CreateFaceVertexCountsAttr([4, 4])
    mesh.CreateFaceVertexIndicesAttr([3, 2, 1, 0, 5, 4, 2, 3])
    
    # 4. Using PrimvarsAPI for displayColor
    # We initialize the API on the mesh prim
    primvars_api = UsdGeom.PrimvarsAPI(mesh)
    
    # Create the 'displayColor' primvar
    # Args: Name, TypeName, Interpolation
    display_color = primvars_api.CreatePrimvar(
        "displayColor", 
        Sdf.ValueTypeNames.Color3fArray, 
        UsdGeom.Tokens.constant
        # UsdGeom.Tokens.faceVarying
    )
    
    # Set the primvar value Constant
    display_color.Set([Gf.Vec3f(1, 0, 0)]) # Red

    # faceVarying: one colour per face-vertex (2 faces x 4 verts = 8 values)
    # display_color.Set([
    #     Gf.Vec3f(1, 0, 0),    # face 0, vert 0 - red
    #     Gf.Vec3f(0, 1, 0),    # face 0, vert 1 - green
    #     Gf.Vec3f(0, 0, 1),    # face 0, vert 2 - blue
    #     Gf.Vec3f(1, 1, 0),    # face 0, vert 3 - yellow
    #     Gf.Vec3f(1, 0, 1),    # face 1, vert 0 - magenta
    #     Gf.Vec3f(0, 1, 1),    # face 1, vert 1 - cyan
    #     Gf.Vec3f(1, 0.5, 0),  # face 1, vert 2 - orange
    #     Gf.Vec3f(0.5, 0, 1),  # face 1, vert 3 - purple
    # ])

    # Get primvar value
    print(f"Primvar value: {display_color.Get()}")  

    # 5. Transformations
    translate_op = mesh.AddTranslateOp(UsdGeom.XformOp.PrecisionDouble)
    translate_op.Set(Gf.Vec3d(0, 0, -10))
    
    # 6. Save and Inspect
    stage.GetRootLayer().Save()
    print("USD authored successfully with PrimvarsAPI.")

if __name__ == "__main__":
    create_mesh_with_primvars_api()