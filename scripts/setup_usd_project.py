#!/usr/bin/env python3
"""
USD GoodStart Project Setup Script

Interactive script to generate a USD_GoodStart project structure with configurable templates.

Usage:
    python scripts/setup_usd_project.py [target_directory]

If no directory is provided, the script will run in the current directory.
"""

import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# Try to import USD libraries (optional - script can work without them for file generation)
try:
    from pxr import Usd, Sdf
    USD_AVAILABLE = True
except ImportError:
    USD_AVAILABLE = False
    print("Note: USD libraries not available. Script will generate files but cannot validate USD syntax.")


# ============================================================================
# Configuration & Templates
# ============================================================================

# Simple Product setup - single product with no sub-assemblies

FOLDER_STRUCTURE = [
    "000_SOURCE",
    "010_ASS_USD/USD_Endpoint",
    "010_ASS_USD/MatLib",
    "010_ASS_USD/tex",
    "010_ASS_USD/Envs",
    "020_BASE_LYR",
    "030_SIM_LYR",
    "040_DATA_LYRs",
]


# ============================================================================
# USD File Templates
# ============================================================================

def get_root_template(product_name: str, default_prim: str, include_samples: bool, sublayers: List[str], meters_per_unit: float = 1.0) -> str:
    """Generate root USD file template."""
    sublayers_str = ",\n        ".join([f"@{layer}@" for layer in sublayers])
    
    # Calculate ground plane size: 10x10 meters
    # Half-size in scene units: 5 meters / meters_per_unit
    ground_half_size = 5.0 / meters_per_unit
    
    # Camera near clipping: 1 cm = 0.01 meters in scene units
    camera_near = 0.01 / meters_per_unit
    # Camera far clipping: reasonable for 10m scene, use 100 meters
    camera_far = 100.0 / meters_per_unit
    
    return f'''#usda 1.0
(
    customLayerData = {{
        dictionary cameraSettings = {{
            dictionary Front = {{
                double3 position = (0, 0, {ground_half_size * 2})
                double radius = {ground_half_size * 1.5}
                double2 clippingRange = ({camera_near}, {camera_far})
            }}
            dictionary Perspective = {{
                double3 position = (0, {ground_half_size * 0.5}, {ground_half_size * 2})
                double3 target = (0, 0, 0)
                double2 clippingRange = ({camera_near}, {camera_far})
            }}
            dictionary Right = {{
                double3 position = (-{ground_half_size * 2}, 0, 0)
                double radius = {ground_half_size * 1.5}
                double2 clippingRange = ({camera_near}, {camera_far})
            }}
            dictionary Top = {{
                double3 position = (0, {ground_half_size * 2}, 0)
                double radius = {ground_half_size * 1.5}
                double2 clippingRange = ({camera_near}, {camera_far})
            }}
            string boundCamera = "/OmniverseKit_Persp"
        }}
        dictionary omni_layer = {{
            dictionary locked = {{
                bool "./020_BASE_LYR/ACTGR_LYR.usda" = 1
                bool "./020_BASE_LYR/ACTION_LYR.usda" = 1
                bool "./020_BASE_LYR/ANIM_LYR.usda" = 1
                bool "./020_BASE_LYR/ASS_LYR.usda" = 1
                bool "./020_BASE_LYR/ENV_LYR.usda" = 1
                bool "./020_BASE_LYR/MTL_LYR.usda" = 1
                bool "./020_BASE_LYR/OPIN_LYR.usda" = 1
                bool "./020_BASE_LYR/VAR_LYR.usda" = 1
                bool "./030_SIM_LYR/SIM_LYR.usda" = 1
                bool "./030_USD_LYR/Ass_import_LYR.usda" = 0
                bool "./030_USD_LYR/Mtl_import_LYR.usda" = 0
                bool "./030_USD_LYR/sample_USD_LYR.usda" = 0
                bool "./030_USD_LYR/your very Personal opinion_LYR.usda" = 0
                bool "./040_DATA_LYRs/DATA_LYRs.usda" = 1
                bool "./040_SIM_LYR/sample_SIM_LYR.usda" = 0
                bool "./050_VAR_LYR/sample_VAR_LYR.usda" = 0
                bool "./060_META_LYR/sample_META_LYR.usda" = 1
            }}
            dictionary muteness = {{
            }}
        }}
        dictionary renderSettings = {{
        }}
    }}
    defaultPrim = "{default_prim}"
    endTimeCode = 100
    metersPerUnit = {meters_per_unit}
    startTimeCode = 0
    subLayers = [
        {sublayers_str}
    ]
    timeCodesPerSecond = 60
    upAxis = "Y"
)

def Xform "Environment"
{{
    # Ground plane: 10x10 meters
    int ground:size = {int(ground_half_size * 2)}
    string ground:type = "On"
    token visibility = "inherited"
    double3 xformOp:rotateXYZ = (0, 0, 0)
    double3 xformOp:scale = (1, 1, 1)
    double3 xformOp:translate = (0, 0, 0)
    uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]

    def DomeLight "Sky" (
        prepend apiSchemas = ["ShapingAPI"]
    )
    {{
        float inputs:colorTemperature = 6250
        bool inputs:enableColorTemperature = 1
        float inputs:exposure = 9
        float inputs:intensity = 1
        float inputs:shaping:cone:angle = 180
        token visibility = "inherited"
        double3 xformOp:rotateXYZ = (0, -90, -90)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, 305, 0)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
    }}

    def DistantLight "DistantLight" (
        prepend apiSchemas = ["ShapingAPI"]
    )
    {{
        float inputs:angle = 2.5
        float inputs:colorTemperature = 7250
        bool inputs:enableColorTemperature = 1
        float inputs:exposure = 10
        float inputs:intensity = 1
        token visibility = "inherited"
        double3 xformOp:rotateXYZ = (-105, 0, 0)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, 305, 0)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
    }}

    def Scope "Looks"
    {{
        def Material "Grid"
        {{
            token outputs:mdl:displacement.connect = </Environment/Looks/Grid/Shader.outputs:out>
            token outputs:mdl:surface.connect = </Environment/Looks/Grid/Shader.outputs:out>
            token outputs:mdl:volume.connect = </Environment/Looks/Grid/Shader.outputs:out>

            def Shader "Shader"
            {{
                uniform token info:implementationSource = "sourceAsset"
                uniform asset info:mdl:sourceAsset = @OmniPBR.mdl@
                uniform token info:mdl:sourceAsset:subIdentifier = "OmniPBR"
                float inputs:albedo_add = 0
                float inputs:albedo_brightness = 0.52
                float inputs:albedo_desaturation = 1
                bool inputs:project_uvw = 0
                float inputs:reflection_roughness_constant = 0.333
                token outputs:out (
                    renderType = "material"
                )
            }}
        }}
    }}

    def Mesh "ground" (
        prepend apiSchemas = ["MaterialBindingAPI"]
    )
    {{
        float3[] extent = [(-{ground_half_size}, -{ground_half_size}, 0), ({ground_half_size}, {ground_half_size}, 0)]
        int[] faceVertexCounts = [4]
        int[] faceVertexIndices = [0, 1, 3, 2]
        rel material:binding = </Environment/Looks/Grid> (
            bindMaterialAs = "weakerThanDescendants"
        )
        normal3f[] normals = [(0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1)] (
            interpolation = "faceVarying"
        )
        point3f[] points = [(-{ground_half_size}, -{ground_half_size}, 0), ({ground_half_size}, -{ground_half_size}, 0), (-{ground_half_size}, {ground_half_size}, 0), ({ground_half_size}, {ground_half_size}, 0)]
        bool primvars:isMatteObject = 0
        texCoord2f[] primvars:st = [(0, 0), (10, 0), (10, 10), (0, 10)] (
            interpolation = "faceVarying"
        )
        uniform token subdivisionScheme = "none"
        token visibility = "inherited"
        double3 xformOp:rotateXYZ = (0, -90, -90)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, 0, 0)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
    }}

    def Plane "groundCollider" (
        prepend apiSchemas = ["PhysicsCollisionAPI"]
    )
    {{
        uniform token axis = "Y"
        uniform token purpose = "guide"
        token visibility = "invisible"
    }}
}}

def "Render" (
    hide_in_stage_window = true
    no_delete = true
)
{{
    def "OmniverseKit"
    {{
        def "HydraTextures" (
            hide_in_stage_window = true
            no_delete = true
        )
        {{
            def RenderProduct "omni_kit_widget_viewport_ViewportTexture_0" (
                prepend apiSchemas = ["OmniRtxSettingsCommonAdvancedAPI_1"]
                hide_in_stage_window = true
                no_delete = true
            )
            {{
                rel camera = </OmniverseKit_Persp>
                uniform int2 resolution = (1920, 1080)
            }}
        }}
    }}

    def RenderSettings "OmniverseGlobalRenderSettings" (
        prepend apiSchemas = ["OmniRtxSettingsGlobalRtAdvancedAPI_1", "OmniRtxSettingsGlobalPtAdvancedAPI_1"]
        no_delete = true
    )
    {{
        rel products = </Render/OmniverseKit/HydraTextures/omni_kit_widget_viewport_ViewportTexture_0>
    }}

    def "Vars"
    {{
        def RenderVar "LdrColor" (
            hide_in_stage_window = true
            no_delete = true
        )
        {{
            uniform string sourceName = "LdrColor"
        }}
    }}
}}

over "OmniverseKit_Persp"
{{
    double2 clippingRange = ({camera_near}, {camera_far})
}}

def Xform "{default_prim}"
{{
    # Add your product geometry here
    # Example: def Xform "ProductName" (references = @../010_ASS_USD/USD_Endpoint/product_GEO.usda@) {{ }}

    def Scope "Looks"
    {{
        # Add materials here
        # Example: def Material "MaterialName" {{ ... }}
    }}
}}
'''


def get_layer_template(layer_type: str, layer_name: str, default_prim: str = "World") -> str:
    """Generate layer file template based on type.
    
    Args:
        layer_type: Type of layer (opinion, ass_import, mtl_import, var, sim, meta, etc.)
        layer_name: Name identifier for the layer
        default_prim: Default prim name to use (defaults to "World" for backward compatibility)
    """
    header = f'''#usda 1.0
(
    customLayerData = {{
        dictionary cameraSettings = {{
            dictionary Front = {{
                double2 clippingRange = (0.01, 100)
                double3 position = (0, 0, 10)
                double radius = 7.5
            }}
            dictionary Perspective = {{
                double2 clippingRange = (0.01, 100)
                double3 position = (6.19289454004624, 7.024767839765761, 13.420619843416928)
                double3 target = (0.0649537519511938, -0.16707580451681903, 0.05387260142201633)
            }}
            dictionary Right = {{
                double2 clippingRange = (0.01, 100)
                double3 position = (-10, 0, 0)
                double radius = 7.5
            }}
            dictionary Top = {{
                double2 clippingRange = (0.01, 100)
                double3 position = (0, 10, 0)
                double radius = 7.5
            }}
            string boundCamera = "/OmniverseKit_Persp"
        }}
        dictionary omni_layer = {{
            string authoring_layer = "./GoodStart_ROOT.usda"
            dictionary locked = {{
                bool "./020_BASE_LYR/ACTGR_LYR.usda" = 1
                bool "./020_BASE_LYR/ACTION_LYR.usda" = 1
                bool "./020_BASE_LYR/ANIM_LYR.usda" = 1
                bool "./020_BASE_LYR/ASS_LYR.usda" = 1
                bool "./020_BASE_LYR/ENV_LYR.usda" = 1
                bool "./020_BASE_LYR/MTL_LYR.usda" = 1
                bool "./020_BASE_LYR/OPIN_LYR.usda" = 1
                bool "./020_BASE_LYR/VAR_LYR.usda" = 1
                bool "./030_SIM_LYR/SIM_LYR.usda" = 1
                bool "./030_USD_LYR/Ass_import_LYR.usda" = 0
                bool "./030_USD_LYR/Mtl_import_LYR.usda" = 0
                bool "./030_USD_LYR/sample_USD_LYR.usda" = 0
                bool "./030_USD_LYR/your very Personal opinion_LYR.usda" = 0
                bool "./040_DATA_LYRs/DATA_LYRs.usda" = 1
                bool "./040_SIM_LYR/sample_SIM_LYR.usda" = 0
                bool "./050_VAR_LYR/sample_VAR_LYR.usda" = 0
                bool "./060_META_LYR/sample_META_LYR.usda" = 1
            }}
            dictionary muteness = {{
            }}
        }}
        dictionary renderSettings = {{
        }}
    }}
    defaultPrim = "{default_prim}"
    endTimeCode = 100
    metersPerUnit = 1
    startTimeCode = 0
    timeCodesPerSecond = 60
    upAxis = "Y"
)
'''

    templates = {
        "opinion": f'''{header}

over "{default_prim}"
{{
}}
''',
        "abc_opinion": f'''{header}

over "{default_prim}"
{{
    # Add opinions here for {layer_name}
}}
''',
        "xyz_opinion": f'''{header}

over "{default_prim}"
{{
    # Add opinions here for {layer_name}
}}
''',
        "ass_import": f'''{header}

def "{default_prim}"
{{
    def Xform "Cube" (
        references = @../010_ASS_USD/USD_Endpoint/0_CUBE_GEO.usda@
    )
    {{
        double3 xformOp:rotateXYZ = (0, 0, 0)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, 0, 0)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
    }}

    def Xform "Ball" (
        references = @../010_ASS_USD/USD_Endpoint/0_Shader_Ball_GEO.usda@
    )
    {{
        double3 xformOp:rotateXYZ = (0, 0, 0)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, 0, 0)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
    }}
}}
''',
        "mtl_import": f'''{header}

def "{default_prim}"
{{
    def Scope "Looks"
    {{
        # Add materials here (MatLib from 010_ASS_USD/MatLib)
    }}
}}
''',
        "var": f'''{header}

over "{default_prim}"
{{
    # Add variants here (e.g. VariantSets for configuration)
}}
''',
        "sim": f'''{header}

def "{default_prim}"
{{
    # Add simulation properties here:
    # - PhysicsCollisionAPI
    # - PhysicsRigidBodyAPI
    # - ArticulationRootAPI
    # - Sensor definitions
}}
''',
        "action": f'''{header}

over "{default_prim}"
{{
    # Add action-related prims or bindings here
}}
''',
        "anim": f'''{header}

over "{default_prim}"
{{
    # Add animation prims, clips, or bindings here
}}
''',
        "data": f'''{header}

over "{default_prim}"
{{
    # Attach metadata to prims:
    # string plm:id = "PLM-001"
    # string cad:partNumber = "PART-123"
    # dictionary customData = {{
    #     string digitalTwin:assetId = "DT-001"
    # }}
}}
'''
    }
    return templates.get(layer_type, templates["opinion"])


def get_sub_assembly_template(assembly_name: str, product_name: str) -> str:
    """Generate sub-assembly USD file template."""
    safe_name = assembly_name.replace(" ", "_")
    return f'''#usda 1.0
(
    doc = "{assembly_name} sub-assembly for {product_name}"
    defaultPrim = "{assembly_name}"
)

def Xform "{assembly_name}"
{{
    # Add {assembly_name.lower()} geometry, materials, and configuration here
    # This file can be referenced from the main product root file
}}
'''


# ============================================================================
# README Templates
# ============================================================================

README_TEMPLATES = {
    "000_SOURCE": '''# 000_SOURCE

**Purpose:** Original CAD/DCC source files before USD conversion.

Place your source files here (CAD files, DCC project files, etc.) before converting to USD format.
''',
    "010_ASS_USD": '''# 010_ASS_USD

**Purpose:** USD assets (converted from CAD or created in DCC + Textures from 2D Apps)

## Folder Structure
- `USD_Endpoint/` - Geometry assets -> Exports from CAD / DCC as stable Endpoints, the name stays constant
- `MatLib/` - Material libraries
- `tex/` - Global textures shared across multiple assets. Place shared texture files here. Asset-specific textures can live with their assets in `USD_Endpoint/`

See the main README.md for detailed usage instructions.
''',
    "020_BASE_LYR": '''# 020_BASE_LYR

**Purpose:** Base USD layers (opinion, asset import, material import, variant, action, animation layers).

See the main README.md for detailed usage instructions.
''',
    "030_SIM_LYR": '''# 030_SIM_LYR

**Purpose:** Simulation layers (physics, collisions, articulations, sensors).

See the main README.md for detailed usage instructions.
''',
    "040_DATA_LYRs": '''# 040_DATA_LYRs

**Purpose:** Data layers for data-driven digital twin integration (PLM/ERP/AAS/OPC UA / sensor / data metadata).

See the main README.md for detailed usage instructions.
'''
}


# ============================================================================
# Interactive Questions
# ============================================================================

def print_header():
    """Print welcome header."""
    print("\n" + "=" * 70)
    print("  USD GoodStart Project Setup")
    print("=" * 70)
    print()


def ask_default_prim_name() -> str:
    """Ask for default prim name, defaulting to 'World'."""
    default = "World"
    response = input(f"Enter default prim name (default: '{default}'): ").strip()
    return response if response else default


def ask_include_samples() -> bool:
    """Ask if user wants to include sample scene files."""
    while True:
        response = input("Include sample scene files? (y/n, default: y): ").strip().lower()
        if not response or response == 'y':
            return True
        elif response == 'n':
            return False
        print("Please enter 'y' or 'n'.")


def ask_unit_system() -> float:
    """Ask user to select unit system (mm/cm/m) and return metersPerUnit value."""
    print("\nSelect unit system:")
    print("  [1] Millimeters (mm)")
    print("  [2] Centimeters (cm)")
    print("  [3] Meters (m) - default")
    
    unit_map = {
        "1": 0.001,  # millimeters
        "2": 0.01,   # centimeters
        "3": 1.0     # meters
    }
    
    unit_names = {
        "1": "millimeters",
        "2": "centimeters", 
        "3": "meters"
    }
    
    while True:
        choice = input("Enter choice (1-3, default: 3): ").strip()
        if not choice:
            choice = "3"
        if choice in unit_map:
            unit_name = unit_names[choice]
            print(f"[OK] Selected: {unit_name}")
            return unit_map[choice]
        print("Invalid choice. Please enter 1, 2, or 3.")


# ============================================================================
# File Generation
# ============================================================================

def create_folder_structure(base_path: Path):
    """Create all required folders."""
    print("\nCreating folder structure...")
    for folder in FOLDER_STRUCTURE:
        folder_path = base_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"  [OK] {folder}")


def create_readme_files(base_path: Path):
    """Create README.md files in each folder."""
    print("\nCreating README files...")
    for folder in FOLDER_STRUCTURE:
        folder_name = folder.split('/')[0]  # Get base folder name
        if folder_name in README_TEMPLATES:
            readme_path = base_path / folder_name / "README.md"
            readme_path.write_text(README_TEMPLATES[folder_name], encoding='utf-8')
            print(f"  [OK] {folder_name}/README.md")


def create_root_file(base_path: Path, default_prim: str, 
                     include_samples: bool, sub_assemblies: List[str], meters_per_unit: float):
    """Create the root USD file."""
    print("\nCreating root USD file...")
    
    # Build sublayers list (strongest first, weakest last)
    # In USD, first in array = strongest (applied last, overrides others)
    # Last in array = weakest (applied first, can be overridden)
    # Match the order from user's new structure
    sublayers = []
    
    if include_samples:
        # Sample layers (if needed in future)
        # For now, use production structure
        pass
    
    # Production setup - match user's structure exactly
    # Strongest to weakest order:
    sublayers.extend([
        "./020_BASE_LYR/OPIN_LYR.usda",      # Strongest - opinions/overrides
        "./020_BASE_LYR/ENV_LYR.usda",       # Environment (lighting, ground, render defaults)
        "./030_SIM_LYR/SIM_LYR.usda",        # Simulation
        "./040_DATA_LYRs/DATA_LYRs.usda",    # Data/metadata
        "./020_BASE_LYR/ACTGR_LYR.usda",     # Action graph / behavior
        "./020_BASE_LYR/ANIM_LYR.usda",      # Animation
        "./020_BASE_LYR/VAR_LYR.usda",       # Variants
        "./020_BASE_LYR/MTL_LYR.usda",       # Materials
        "./020_BASE_LYR/ASS_LYR.usda",       # Weakest - asset imports
    ])
    
    # Root file is always named USD_GoodStart_ROOT.usda
    root_content = get_root_template("USD_GoodStart", default_prim, include_samples, sublayers, meters_per_unit)
    root_filename = "USD_GoodStart_ROOT.usda"
    root_path = base_path / root_filename
    root_path.write_text(root_content, encoding='utf-8')
    print(f"  [OK] {root_filename}")


def create_layer_files(base_path: Path, include_samples: bool, default_prim: str):
    """Create layer USD files.
    
    Args:
        base_path: Base path for the project
        include_samples: Whether to include sample layers (not used in new structure)
        default_prim: Default prim name to use in all layers (for consistency)
    """
    print("\nCreating layer files...")
    
    layers_to_create = []
    
    # Base layers (always created) - match user's new structure
    layers_to_create.extend([
        ("020_BASE_LYR", "OPIN_LYR.usda", "opinion"),
        ("020_BASE_LYR", "ENV_LYR.usda", "opinion"),
        ("020_BASE_LYR", "ASS_LYR.usda", "ass_import"),
        ("020_BASE_LYR", "MTL_LYR.usda", "mtl_import"),
        ("020_BASE_LYR", "VAR_LYR.usda", "var"),
        ("020_BASE_LYR", "ACTGR_LYR.usda", "action"),
        ("020_BASE_LYR", "ANIM_LYR.usda", "anim"),
    ])
    
    # Simulation layer
    layers_to_create.extend([
        ("030_SIM_LYR", "SIM_LYR.usda", "sim"),
    ])
    
    # Data layers (plural folder name)
    layers_to_create.extend([
        ("040_DATA_LYRs", "DATA_LYRs.usda", "data"),
    ])
    
    for folder, filename, layer_type in layers_to_create:
        layer_path = base_path / folder / filename
        content = get_layer_template(layer_type, filename.replace("_LYR.usda", "").replace("_LYRs.usda", ""), default_prim)
        layer_path.write_text(content, encoding='utf-8')
        print(f"  [OK] {folder}/{filename}")


def create_sub_assembly_files(base_path: Path, sub_assemblies: List[str]):
    """Create sub-assembly USD files for complex products."""
    if not sub_assemblies:
        return
    
    print("\nCreating sub-assembly files...")
    for assembly in sub_assemblies:
        safe_name = assembly.replace(" ", "_")
        filename = f"{safe_name}_ASSEMBLY.usda"
        file_path = base_path / "010_ASS_USD" / filename
        content = get_sub_assembly_template(assembly, "USD_GoodStart")
        file_path.write_text(content, encoding='utf-8')
        print(f"  [OK] 010_ASS_USD/{filename}")


def create_sample_assets(base_path: Path, include_samples: bool, default_prim: str, meters_per_unit: float):
    """Create sample geometry assets programmatically.
    
    Generates all default assets (cube, shader ball) programmatically
    so the setup script creates a complete, working scene by default.
    
    Args:
        base_path: Base path for the project
        include_samples: Whether to include sample assets
        default_prim: Default prim name to use (for consistency with root layer)
    """
    # Always create default assets (cube and shader ball) for a working scene
    print("\nCreating default assets (programmatically generated)...")
    
    # Cube geometry - 1 meter edge length
    # Calculate half-extent: 0.5 meters in scene units
    # If metersPerUnit = 1.0, then 0.5 units = 0.5 meters
    # If metersPerUnit = 0.01 (cm), then 50 units = 0.5 meters
    # If metersPerUnit = 0.001 (mm), then 500 units = 0.5 meters
    half_extent = 0.5 / meters_per_unit
    
    cube_content = f'''#usda 1.0
(
    doc = "Sample cube geometry - 1 meter edge length"
    defaultPrim = "Geo"
    metersPerUnit = {meters_per_unit}
    upAxis = "Y"
)

def Xform "Geo" (
    assetInfo = {{
        string version = "1.0.0"
    }}
)
{{
    def Mesh "Cube"
    {{
        float3[] extent = [(-{half_extent}, -{half_extent}, -{half_extent}), ({half_extent}, {half_extent}, {half_extent})]
        int[] faceVertexCounts = [4, 4, 4, 4, 4, 4]
        int[] faceVertexIndices = [0, 1, 3, 2, 4, 5, 7, 6, 0, 1, 5, 4, 2, 3, 7, 6, 0, 2, 6, 4, 1, 3, 7, 5]
        normal3f[] normals = [(0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, -1), (0, 0, -1), (0, 0, -1), (0, 0, -1), (0, 1, 0), (0, 1, 0), (0, 1, 0), (0, 1, 0), (0, -1, 0), (0, -1, 0), (0, -1, 0), (0, -1, 0), (-1, 0, 0), (-1, 0, 0), (-1, 0, 0), (-1, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0)] (
            interpolation = "faceVarying"
        )
        point3f[] points = [(-{half_extent}, -{half_extent}, {half_extent}), ({half_extent}, -{half_extent}, {half_extent}), (-{half_extent}, {half_extent}, {half_extent}), ({half_extent}, {half_extent}, {half_extent}), (-{half_extent}, -{half_extent}, -{half_extent}), ({half_extent}, -{half_extent}, -{half_extent}), (-{half_extent}, {half_extent}, -{half_extent}), ({half_extent}, {half_extent}, -{half_extent})]
        texCoord2f[] primvars:st = [(0, 0), (1, 0), (1, 1), (0, 1), (1, 0), (1, 1), (0, 1), (0, 0), (0, 1), (0, 0), (1, 0), (1, 1), (0, 0), (1, 0), (1, 1), (0, 1), (0, 0), (1, 0), (1, 1), (0, 1), (1, 0), (1, 1), (0, 1), (0, 0)] (
            interpolation = "faceVarying"
        )
        uniform token subdivisionScheme = "none"
        double3 xformOp:rotateXYZ = (0, 0, 0)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, 0, 0)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
    }}
}}
'''
    cube_path = base_path / "010_ASS_USD" / "USD_Endpoint" / "0_CUBE_GEO.usda"
    cube_path.write_text(cube_content, encoding='utf-8')
    print(f"  [OK] 010_ASS_USD/USD_Endpoint/0_CUBE_GEO.usda")
    
    # Ball geometry - 1 meter diameter (radius 0.5 meters)
    # Calculate radius: 0.5 meters in scene units
    ball_radius = 0.5 / meters_per_unit
    
    shader_ball_content = f'''#usda 1.0
(
    doc = "Ball geometry - 1 meter diameter"
    defaultPrim = "Geo"
    metersPerUnit = {meters_per_unit}
    upAxis = "Y"
)

def Xform "Geo" (
    assetInfo = {{
        string version = "1.0.0"
    }}
)
{{
    def Sphere "Ball"
    {{
        float3[] extent = [(-{ball_radius}, -{ball_radius}, -{ball_radius}), ({ball_radius}, {ball_radius}, {ball_radius})]
        double radius = {ball_radius}
        token visibility = "inherited"
        double3 xformOp:rotateXYZ = (0, 0, 0)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, 0, 0)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
    }}
}}
'''
    shader_ball_path = base_path / "010_ASS_USD" / "USD_Endpoint" / "0_Shader_Ball_GEO.usda"
    shader_ball_path.write_text(shader_ball_content, encoding='utf-8')
    print(f"  [OK] 010_ASS_USD/USD_Endpoint/0_Shader_Ball_GEO.usda")


def create_envs_dummy(base_path: Path):
    """Create a dummy environment file under 010_ASS_USD/Envs.

    This is a parking place for alternate environments that ENV_LYR.usda can load.
    The default content is intentionally minimal; real projects can replace or add
    additional environment stages here.
    """
    print("\nCreating dummy environment in 010_ASS_USD/Envs/ ...")

    env_content = '''#usda 1.0
(
    doc = "Dummy environment placeholder for USD_GoodStart Envs/ folder."
    defaultPrim = "Environment"
    metersPerUnit = 1
    upAxis = "Y"
)

def Xform "Environment"
{
}
'''
    env_path = base_path / "010_ASS_USD" / "Envs" / "Environment.usda"
    env_path.write_text(env_content, encoding='utf-8')
    print("  [OK] 010_ASS_USD/Envs/Environment.usda")


# ============================================================================
# Main Setup Function
# ============================================================================

def setup_project(target_dir: Optional[Path] = None):
    """Main setup function."""
    print_header()
    
    # Determine target directory
    if target_dir:
        base_path = Path(target_dir).resolve()
    else:
        current_dir = Path.cwd()
        
        # Check if we're running from an extracted zip folder
        # (contains setup script files - indicates this is the zip extraction location)
        script_files = [
            "setup_usd_project.py",
            "setup_usd_project.bat",
            "setup_usd_project.ps1",
            "SETUP_STANDALONE.md",
            "README_STANDALONE.txt"
        ]
        
        # If current directory contains setup script files, use parent directory
        if all((current_dir / f).exists() for f in script_files):
            base_path = current_dir.parent
            print(f"Detected setup script folder. Creating project in parent directory.")
        else:
            base_path = current_dir
    
    print(f"Target directory: {base_path}")
    print()
    
    # Confirm directory
    if base_path.exists() and any(base_path.iterdir()):
        response = input(f"Directory is not empty. Continue? (y/n): ").strip().lower()
        if response != 'y':
            print("Setup cancelled.")
            return False
    
    # Interactive questions
    default_prim = ask_default_prim_name()
    print(f"[OK] Default prim: {default_prim}")
    
    include_samples = ask_include_samples()
    print(f"[OK] Include samples: {'Yes' if include_samples else 'No'}")
    
    meters_per_unit = ask_unit_system()
    
    # Simple Product setup - no sub-assemblies
    sub_assemblies = []
    
    print("\n" + "=" * 70)
    print("  Generating project structure...")
    print("=" * 70)
    
    # Generate structure
    try:
        create_folder_structure(base_path)
        create_readme_files(base_path)
        create_root_file(base_path, default_prim, include_samples, sub_assemblies, meters_per_unit)
        create_layer_files(base_path, include_samples, default_prim)
        create_sub_assembly_files(base_path, sub_assemblies)
        create_sample_assets(base_path, include_samples, default_prim, meters_per_unit)
        create_envs_dummy(base_path)
        
        print("\n" + "=" * 70)
        print("  [OK] Project setup complete!")
        print("=" * 70)
        print(f"\nRoot file: {base_path / 'USD_GoodStart_ROOT.usda'}")
        print(f"\nNext steps:")
        print(f"  1. Open USD_GoodStart_ROOT.usda in Omniverse Composer")
        print(f"  2. Set Session Layer as active authoring layer (see README.md)")
        print(f"  3. Start adding your assets to 010_ASS_USD/")
        print()
        
        return True
        
    except Exception as e:
        print(f"\n[ERROR] Error during setup: {e}")
        import traceback
        traceback.print_exc()
        return False


# ============================================================================
# CLI Entry Point
# ============================================================================

def main():
    """Main entry point."""
    target_dir = None
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    
    success = setup_project(target_dir)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
