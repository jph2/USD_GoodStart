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
    "010_ASS_USD/geo",
    "010_ASS_USD/mat",
    "020_TEX",
    "030_USD_LYR",
    "040_SIM_LYR",
    "050_VAR_LYR",
    "060_META_LYR"
]


# ============================================================================
# USD File Templates
# ============================================================================

def get_root_template(product_name: str, default_prim: str, include_samples: bool, sublayers: List[str]) -> str:
    """Generate root USD file template."""
    sublayers_str = ",\n        ".join([f"@{layer}@" for layer in sublayers])
    
    # Default: Lock ALL persistent layers and use Session Layer as active authoring layer
    # This is the "safe mode" pattern to prevent layer pollution
    # Session layer is in-memory only and cannot be referenced by file path in metadata
    
    # Lock ALL persistent layers (all sublayers)
    locked_layers = []
    for layer in sublayers:
        locked_layers.append(f'                bool "{layer}" = 1')
    if locked_layers:
        locked_str = "\n".join(locked_layers)
    else:
        locked_str = ""
    
    # Session layer is in-memory, so we omit authoring_layer entirely
    # User should set Session Layer as active in Omniverse UI (safe mode default)
    # Omit authoring_layer line - Session Layer should be set manually in Omniverse UI
    authoring_layer_line = ""
    
    return f'''#usda 1.0
(
    customLayerData = {{
        dictionary cameraSettings = {{
            dictionary Front = {{
                double3 position = (0, 0, 50000)
                double radius = 500
            }}
            dictionary Perspective = {{
                double3 position = (0, 0, 1000)
                double3 target = (0, 0, 0)
            }}
            dictionary Right = {{
                double3 position = (-50000, 0, 0)
                double radius = 500
            }}
            dictionary Top = {{
                double3 position = (0, 50000, 0)
                double radius = 500
            }}
            string boundCamera = "/OmniverseKit_Persp"
        }}
        dictionary omni_layer = {{
{authoring_layer_line}
            dictionary locked = {{
{locked_str}
            }}
            dictionary muteness = {{
            }}
        }}
        # Safe Mode Default: All persistent layers are locked by default.
        # Set Session Layer as active authoring layer in Omniverse UI to prevent layer pollution.
        # (Session Layer is in-memory only and cannot be referenced by file path in metadata)
        dictionary renderSettings = {{
        }}
    }}
    defaultPrim = "{default_prim}"
    endTimeCode = 100
    metersPerUnit = 0.01
    startTimeCode = 0
    subLayers = [
        {sublayers_str}
    ]
    timeCodesPerSecond = 60
    upAxis = "Y"
)

def Xform "Environment"
{{
    int ground:size = 1400
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
        float3[] extent = [(-1400, -1400, 0), (1400, 1400, 0)]
        int[] faceVertexCounts = [4]
        int[] faceVertexIndices = [0, 1, 3, 2]
        rel material:binding = </Environment/Looks/Grid> (
            bindMaterialAs = "weakerThanDescendants"
        )
        normal3f[] normals = [(0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1)] (
            interpolation = "faceVarying"
        )
        point3f[] points = [(-700, -700, 0), (700, -700, 0), (-700, 700, 0), (700, 700, 0)]
        bool primvars:isMatteObject = 0
        texCoord2f[] primvars:st = [(0, 0), (14, 0), (14, 14), (0, 14)] (
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

def Xform "{default_prim}"
{{
    def Scope "Geo"
    {{
        # Add your product geometry here
        # Example: def Xform "ProductName" (references = @../010_ASS_USD/geo/product_GEO.usda@) {{ }}
    }}

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
    templates = {
        "opinion": f'''#usda 1.0
(
    doc = "Opinion/override layer for {layer_name}. This is the default authoring layer."
)

def "{default_prim}"
{{
    # Add your opinions, overrides, and modifications here.
    # This layer sits at the top (strongest) and can override anything from lower layers.
}}
''',
        "abc_opinion": f'''#usda 1.0
(
    doc = "Opinion layer abc - overrides shader ball position for alternative layout."
)

over "{default_prim}"
{{
    over "Geo"
    {{
        over "nvidia_shader_ball"
        {{
            double3 xformOp:rotateXYZ = (0, 0, 0)
            double3 xformOp:scale = (1, 1, 1)
            double3 xformOp:translate = (17.46904850038133, 176.23009685101712, 126.57352712500494)
            uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
        }}
    }}
}}
''',
        "xyz_opinion": f'''#usda 1.0
(
    doc = "Opinion layer xyz - overrides variant selection and environment."
)

over "{default_prim}"
{{
    over "Geo"
    {{
        # Shader ball - no variant set, just a simple reference
        # (Variants removed due to compatibility issues)
    }}
}}

over "Environment"
{{
    over "ground"
    {{
        float3[] extent = [(-1400, -1400, 0), (1400, 1400, 0)]
        point3f[] points = [(-700, -700, 0), (700, -700, 0), (-700, 700, 0), (700, 700, 0)]
        bool primvars:isMatteObject = 0
        texCoord2f[] primvars:st = [(0, 0), (14, 0), (14, 14), (0, 14)]
        token visibility = "inherited"
    }}
}}
''',
        "ass_import": f'''#usda 1.0
(
    doc = "Asset import layer for {layer_name}. References and payloads assets from 010_ASS_USD/."
)

def "{default_prim}"
{{
    def Scope "Geo"
    {{
        def Xform "Cube" (
            references = @../010_ASS_USD/geo/0_CUBE_GEO.usda@
        )
        {{
            double3 xformOp:rotateXYZ = (0, 0, 0)
            double3 xformOp:scale = (1, 1, 1)
            double3 xformOp:translate = (447.30697944709954, 0, 0)
            uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]

            over "Geo"
            {{
                over "Cube"
                {{
                    token visibility = "inherited"
                }}
            }}
        }}

        def Xform "nvidia_shader_ball" (
            references = @../010_ASS_USD/geo/0_Shader_Ball_GEO.usda@
        )
        {{
            double3 xformOp:rotateXYZ = (0, 0, 0)
            double3 xformOp:scale = (1, 1, 1)
            double3 xformOp:translate = (0, 0, 0)
            uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
        }}
    }}
}}
''',
        "mtl_import": f'''#usda 1.0
(
    doc = "Material import layer for {layer_name}. References material libraries from 010_ASS_USD/mat/."
)

def "{default_prim}"
{{
    def Scope "Looks"
    {{
        def Material "Material_Blue"
        {{
            token outputs:mdl:displacement.connect = </{default_prim}/Looks/Material_Blue/Shader.outputs:out>
            token outputs:mdl:surface.connect = </{default_prim}/Looks/Material_Blue/Shader.outputs:out>
            token outputs:mdl:volume.connect = </{default_prim}/Looks/Material_Blue/Shader.outputs:out>

            def Shader "Shader"
            {{
                uniform token info:implementationSource = "sourceAsset"
                uniform asset info:mdl:sourceAsset = @OmniPBR.mdl@
                uniform token info:mdl:sourceAsset:subIdentifier = "OmniPBR"
                color3f inputs:diffuse_color_constant = (0.0, 0.2, 1.0)
                float inputs:reflection_roughness_constant = 0.5
                token outputs:out (
                    renderType = "material"
                )
            }}
        }}

        def Material "Material_Red"
        {{
            token outputs:mdl:displacement.connect = </{default_prim}/Looks/Material_Red/Shader.outputs:out>
            token outputs:mdl:surface.connect = </{default_prim}/Looks/Material_Red/Shader.outputs:out>
            token outputs:mdl:volume.connect = </{default_prim}/Looks/Material_Red/Shader.outputs:out>

            def Shader "Shader"
            {{
                uniform token info:implementationSource = "sourceAsset"
                uniform asset info:mdl:sourceAsset = @OmniPBR.mdl@
                uniform token info:mdl:sourceAsset:subIdentifier = "OmniPBR"
                color3f inputs:diffuse_color_constant = (1.0, 0.0, 0.0)
                float inputs:reflection_roughness_constant = 0.5
                token outputs:out (
                    renderType = "material"
                )
            }}
        }}
    }}
}}
''',
        "var": f'''#usda 1.0
(
    doc = "Variant/configuration layer for {layer_name}."
)

over "{default_prim}"
{{
    over "Geo"
    {{
        over "Cube" (
            variants = {{
                string MaterialVariant = "Blue"
            }}
            prepend variantSets = "MaterialVariant"
        )
        {{
            variantSet "MaterialVariant" = {{
                "Blue" {{
                    over "Geo"
                    {{
                        over "Cube" (
                            prepend apiSchemas = ["MaterialBindingAPI"]
                        )
                        {{
                            rel material:binding = </{default_prim}/Looks/Material_Blue> (
                                bindMaterialAs = "weakerThanDescendants"
                            )
                        }}
                    }}
                }}
                "Red" {{
                    over "Geo"
                    {{
                        over "Cube" (
                            prepend apiSchemas = ["MaterialBindingAPI"]
                        )
                        {{
                            rel material:binding = </{default_prim}/Looks/Material_Red> (
                                bindMaterialAs = "weakerThanDescendants"
                            )
                        }}
                    }}
                }}
            }}
        }}

    }}
}}
''',
        "sim": f'''#usda 1.0
(
    doc = "Simulation layer for {layer_name}. Physics, collisions, articulations, sensors."
)

def "{default_prim}"
{{
    # Add simulation properties here:
    # - PhysicsCollisionAPI
    # - PhysicsRigidBodyAPI
    # - ArticulationRootAPI
    # - Sensor definitions
}}
''',
        "meta": f'''#usda 1.0
(
    doc = "Metadata layer for {layer_name}. PLM/ERP/AAS/OPC UA metadata."
)

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

**Purpose:** USD assets (converted from CAD or created in DCC).

## Folder Structure
- `geo/` - Geometry assets
- `mat/` - Material libraries

See the main README.md for detailed usage instructions.
''',
    "020_TEX": '''# 020_TEX

**Purpose:** Global textures shared across multiple assets.

Place shared texture files here. Asset-specific textures can live with their assets in `010_ASS_USD/`.
''',
    "030_USD_LYR": '''# 030_USD_LYR

**Purpose:** General USD layers (visual, layout, material, opinion layers).

See the main README.md for detailed usage instructions.
''',
    "040_SIM_LYR": '''# 040_SIM_LYR

**Purpose:** Simulation layers (physics, collisions, articulations, sensors).

See the main README.md for detailed usage instructions.
''',
    "050_VAR_LYR": '''# 050_VAR_LYR

**Purpose:** Variant/configuration layers.

See the main README.md for detailed usage instructions.
''',
    "060_META_LYR": '''# 060_META_LYR

**Purpose:** Metadata and standards layers (PLM/ERP/AAS/OPC UA).

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


def ask_product_name() -> str:
    """Ask for product name."""
    while True:
        name = input("Enter product name (used for root file and default prim): ").strip()
        if name:
            # Sanitize for filename
            safe_name = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in name)
            return safe_name
        print("Product name cannot be empty.")


def ask_default_prim(product_name: str) -> str:
    """Ask for default prim name, defaulting to product name or 'World'."""
    default = product_name if product_name else "World"
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


def create_root_file(base_path: Path, product_name: str, default_prim: str, 
                     include_samples: bool, sub_assemblies: List[str]):
    """Create the root USD file."""
    print("\nCreating root USD file...")
    
    # Build sublayers list (strongest first, weakest last)
    # In USD, first in array = strongest (applied last, overrides others)
    # Last in array = weakest (applied first, can be overridden)
    # Note: This matches the order in GoodStart_ROOT.usda
    sublayers = []
    
    if include_samples:
        # Match exact order from GoodStart_ROOT.usda
        sublayers.extend([
            "./040_SIM_LYR/sample_SIM_LYR.usda",  # First = strongest
            "./060_META_LYR/sample_META_LYR.usda",
            "./030_USD_LYR/sample_USD_LYR.usda",
            "./050_VAR_LYR/sample_VAR_LYR.usda",
            "./030_USD_LYR/your very Personal opinion_LYR.usda",  # Authoring layer (unlocked)
            "./050_VAR_LYR/VAR_LYR.usda",
            "./030_USD_LYR/abc_Opinion_LYR.usda",
            "./030_USD_LYR/xyz_Opinion_LYR.usda",
        ])
    else:
        # Production setup (no samples)
        # Opinion layer first (strongest), then variant, then imports
        sublayers.extend([
            "./030_USD_LYR/Opinion_LYR.usda",  # Strongest
            "./050_VAR_LYR/VAR_LYR.usda",
        ])
    
    # Material and asset import (always at bottom - weakest)
    # These are applied first and can be overridden by layers above
    sublayers.extend([
        "./030_USD_LYR/Mtl_import_LYR.usda",
        "./030_USD_LYR/Ass_import_LYR.usda"  # Weakest - must be last
    ])
    
    root_content = get_root_template(product_name, default_prim, include_samples, sublayers)
    root_filename = f"{product_name}_ROOT.usda"
    root_path = base_path / root_filename
    root_path.write_text(root_content, encoding='utf-8')
    print(f"  [OK] {root_filename}")


def create_layer_files(base_path: Path, include_samples: bool, default_prim: str):
    """Create layer USD files.
    
    Args:
        base_path: Base path for the project
        include_samples: Whether to include sample layers
        default_prim: Default prim name to use in all layers (for consistency)
    """
    print("\nCreating layer files...")
    
    layers_to_create = []
    
    if include_samples:
        # Sample layers
        layers_to_create.extend([
            ("030_USD_LYR", "sample_USD_LYR.usda", "opinion"),
            ("040_SIM_LYR", "sample_SIM_LYR.usda", "sim"),
            ("050_VAR_LYR", "sample_VAR_LYR.usda", "var"),
            ("060_META_LYR", "sample_META_LYR.usda", "meta"),
            # User layers with specific opinions
            ("030_USD_LYR", "your very Personal opinion_LYR.usda", "opinion"),
            ("030_USD_LYR", "abc_Opinion_LYR.usda", "abc_opinion"),
            ("030_USD_LYR", "xyz_Opinion_LYR.usda", "xyz_opinion"),
        ])
    
    # Production layers (always created)
    layers_to_create.extend([
        ("030_USD_LYR", "Opinion_LYR.usda", "opinion"),
        ("030_USD_LYR", "Ass_import_LYR.usda", "ass_import"),
        ("030_USD_LYR", "Mtl_import_LYR.usda", "mtl_import"),
        ("050_VAR_LYR", "VAR_LYR.usda", "var"),
    ])
    
    for folder, filename, layer_type in layers_to_create:
        layer_path = base_path / folder / filename
        content = get_layer_template(layer_type, filename.replace("_LYR.usda", ""), default_prim)
        layer_path.write_text(content, encoding='utf-8')
        print(f"  [OK] {folder}/{filename}")


def create_sub_assembly_files(base_path: Path, product_name: str, sub_assemblies: List[str]):
    """Create sub-assembly USD files for complex products."""
    if not sub_assemblies:
        return
    
    print("\nCreating sub-assembly files...")
    for assembly in sub_assemblies:
        safe_name = assembly.replace(" ", "_")
        filename = f"{safe_name}_ASSEMBLY.usda"
        file_path = base_path / "010_ASS_USD" / filename
        content = get_sub_assembly_template(assembly, product_name)
        file_path.write_text(content, encoding='utf-8')
        print(f"  [OK] 010_ASS_USD/{filename}")


def create_sample_assets(base_path: Path, include_samples: bool, default_prim: str):
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
    
    # Cube geometry - matches the structure from 0_CUBE_GEO.usda
    cube_content = f'''#usda 1.0
(
    doc = "Sample cube geometry"
    defaultPrim = "{default_prim}"
    metersPerUnit = 0.01
    upAxis = "Y"
)

def Xform "Environment"
{{
    int ground:size = 1400
    string ground:type = "On"
    token visibility = "inherited"
    double3 xformOp:rotateXYZ = (0, 0, 0)
    double3 xformOp:scale = (1, 1, 1)
    double3 xformOp:translate = (0, 0, 0)
    uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
}}

over "{default_prim}"
{{
    def Scope "Geo"
    {{
        def Mesh "Cube"
        {{
            float3[] extent = [(-50, -50, -50), (50, 50, 50)]
            int[] faceVertexCounts = [4, 4, 4, 4, 4, 4]
            int[] faceVertexIndices = [0, 1, 3, 2, 4, 5, 7, 6, 0, 1, 5, 4, 2, 3, 7, 6, 0, 2, 6, 4, 1, 3, 7, 5]
            normal3f[] normals = [(0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, -1), (0, 0, -1), (0, 0, -1), (0, 0, -1), (0, 1, 0), (0, 1, 0), (0, 1, 0), (0, 1, 0), (0, -1, 0), (0, -1, 0), (0, -1, 0), (0, -1, 0), (-1, 0, 0), (-1, 0, 0), (-1, 0, 0), (-1, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0)] (
                interpolation = "faceVarying"
            )
            point3f[] points = [(-50, -50, 50), (50, -50, 50), (-50, 50, 50), (50, 50, 50), (-50, -50, -50), (50, -50, -50), (-50, 50, -50), (50, 50, -50)]
            texCoord2f[] primvars:st = [(0, 0), (1, 0), (1, 1), (0, 1), (1, 0), (1, 1), (0, 1), (0, 0), (0, 1), (0, 0), (1, 0), (1, 1), (0, 0), (1, 0), (1, 1), (0, 1), (0, 0), (1, 0), (1, 1), (0, 1), (1, 0), (1, 1), (0, 1), (0, 0)] (
                interpolation = "faceVarying"
            )
            uniform token subdivisionScheme = "none"
            double3 xformOp:rotateXYZ = (0, 0, 0)
            double3 xformOp:scale = (1, 1, 1)
            double3 xformOp:translate = (0, 50, 0)
            uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
        }}
    }}

    def Scope "Looks"
    {{
    }}
}}
'''
    cube_path = base_path / "010_ASS_USD" / "geo" / "0_CUBE_GEO.usda"
    cube_path.write_text(cube_content, encoding='utf-8')
    print(f"  [OK] 010_ASS_USD/geo/0_CUBE_GEO.usda")
    
    # Shader ball geometry - programmatically generated sphere for material testing
    # Uses USD Sphere primitive for clean, simple geometry
    shader_ball_content = f'''#usda 1.0
(
    doc = "Shader ball geometry for material testing"
    defaultPrim = "{default_prim}"
    metersPerUnit = 0.01
    upAxis = "Y"
)

def Xform "Environment"
{{
    int ground:size = 1400
    string ground:type = "On"
    token visibility = "inherited"
    double3 xformOp:rotateXYZ = (0, 0, 0)
    double3 xformOp:scale = (1, 1, 1)
    double3 xformOp:translate = (0, 0, 0)
    uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
}}

over "{default_prim}"
{{
    def Scope "Geo"
    {{
        def Xform "nvidia_shader_ball_09"
        {{
            def Sphere "geo_shaderball_mat_01_All" (
                prepend apiSchemas = ["MaterialBindingAPI"]
            )
            {{
                float3[] extent = [(-50, -50, -50), (50, 50, 50)]
                double radius = 50
                token visibility = "inherited"
                double3 xformOp:rotateXYZ = (0, 0, 0)
                double3 xformOp:scale = (1, 1, 1)
                double3 xformOp:translate = (0, 0, 0)
                uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
            }}
        }}
    }}

    def Scope "Looks"
    {{
    }}
}}
'''
    shader_ball_path = base_path / "010_ASS_USD" / "geo" / "0_Shader_Ball_GEO.usda"
    shader_ball_path.write_text(shader_ball_content, encoding='utf-8')
    print(f"  [OK] 010_ASS_USD/geo/0_Shader_Ball_GEO.usda")


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
    product_name = ask_product_name()
    print(f"[OK] Product name: {product_name}")
    
    default_prim = ask_default_prim(product_name)
    print(f"[OK] Default prim: {default_prim}")
    
    include_samples = ask_include_samples()
    print(f"[OK] Include samples: {'Yes' if include_samples else 'No'}")
    
    # Simple Product setup - no sub-assemblies
    sub_assemblies = []
    
    print("\n" + "=" * 70)
    print("  Generating project structure...")
    print("=" * 70)
    
    # Generate structure
    try:
        create_folder_structure(base_path)
        create_readme_files(base_path)
        create_root_file(base_path, product_name, default_prim, include_samples, sub_assemblies)
        create_layer_files(base_path, include_samples, default_prim)
        create_sub_assembly_files(base_path, product_name, sub_assemblies)
        create_sample_assets(base_path, include_samples, default_prim)
        
        print("\n" + "=" * 70)
        print("  [OK] Project setup complete!")
        print("=" * 70)
        print(f"\nRoot file: {base_path / f'{product_name}_ROOT.usda'}")
        print(f"\nNext steps:")
        print(f"  1. Open {product_name}_ROOT.usda in Omniverse Composer")
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
