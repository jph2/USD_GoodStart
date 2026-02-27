"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 5 (PointInstancer + varying primvars at larger scale)

Why this script exists:
- It turns the primvar concept into a dense instanced grid.
- This closely mirrors the Station 7 "many sensors, one pattern" model.

How to run:
- From the __usd_cert folder:
  python data-types/8b_primvars_pointcloud_cloth.py

What to observe:
1) Prototype registration for PointInstancer.
2) Generated 31x31 positions with per-instance protoIndices.
3) Varying displayColor primvar mapping one value per instance.
4) Resulting stage scale and structure in usdview.
"""

from pxr import Usd, UsdGeom, Sdf, Gf, Vt

def create_cloth_instancer():
    # 1. Create a new USD stage
    stage = Usd.Stage.CreateNew('_assets/cloth_point_grid.usda')
    
    # 2. Create the PointInstancer prim
    instancer = UsdGeom.PointInstancer.Define(stage, '/Scene/ClothInstancer')
    
    # 3. Define the Prototype (A small sphere representing a point in the cloth)
    proto_scope = UsdGeom.Scope.Define(stage, '/Scene/ClothInstancer/Prototypes')
    sphere_proto = UsdGeom.Sphere.Define(stage, '/Scene/ClothInstancer/Prototypes/ThreadPoint')
    sphere_proto.CreateRadiusAttr(0.02) # Make it small
    
    # Register the prototype with the instancer
    instancer.GetPrototypesRel().SetTargets([sphere_proto.GetPath()])
    
    # 4. Generate the 1x1 Grid (31x31 = 961 points)
    num_points_axis = 31
    step = 1.0 / (num_points_axis - 1)
    
    positions = []
    proto_indices = []
    display_colors = []
    
    for i in range(num_points_axis):
        for j in range(num_points_axis):
            # Calculate coordinates (0 to 1 range)
            x = i * step
            y = j * step
            z = 0 # Flat cloth
            
            positions.append(Gf.Vec3f(x, y, z))
            proto_indices.append(0) # All points use the same sphere prototype
            
            # Create a color gradient based on position
            display_colors.append(Gf.Vec3f(x, y, 0.5))
            
    # Apply geometry data to the instancer
    instancer.CreatePositionsAttr(Vt.Vec3fArray(positions))
    instancer.CreateProtoIndicesAttr(Vt.IntArray(proto_indices))
    
    # 5. Author Primvars for color variation
    # PointInstancer uses 'varying' interpolation to map data per-instance
    primvars_api = UsdGeom.PrimvarsAPI(instancer)
    color_pv = primvars_api.CreatePrimvar(
        "displayColor", 
        Sdf.ValueTypeNames.Color3fArray, 
        UsdGeom.Tokens.varying
    )
    color_pv.Set(Vt.Vec3fArray(display_colors))

    # 6. Save the result
    stage.GetRootLayer().Save()
    print(f"Cloth PointInstancer created with {len(positions)} points.")

if __name__ == "__main__":
    create_cloth_instancer()