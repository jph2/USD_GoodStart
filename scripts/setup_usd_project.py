#!/usr/bin/env python3
"""
USD GoodStart Project Setup Script

Creates a USD_GoodStart project with folder structure and one root scene (m, cm, or mm scale).
Based on USD_GoodStart_m_ROOT.usda, USD_GoodStart_cm_ROOT.usda, USD_GoodStart_mm_ROOT.usda
and folders: 000_SOURCE, 010_ASS_USD, 020_BASE_LYR, 030_SIM_LYR, 040_DATA_LYRs.

Usage:
    python scripts/setup_usd_project.py [target_directory]
    python scripts/setup_usd_project.py --version

If no directory is provided, the script runs in the current directory.
"""

__version__ = "0.9.3"

import sys
from pathlib import Path
from typing import List, Optional

# ============================================================================
# Configuration
# ============================================================================

FOLDER_STRUCTURE = [
    "000_SOURCE",
    "010_ASS_USD",
    "010_ASS_USD/USD_Endpoint",
    "010_ASS_USD/MatLib",
    "010_ASS_USD/tex",
    "010_ASS_USD/Envs",
    "020_BASE_LYR",
    "030_SIM_LYR",
    "040_DATA_LYRs",
]

# Sublayer paths (strongest first). Must match roots USD_GoodStart_*_ROOT.usda.
SUBLAYERS = [
    "./020_BASE_LYR/OPIN_LYR.usda",
    "./020_BASE_LYR/CAM_LYR.usda",
    "./020_BASE_LYR/ENV_LYR.usda",
    "./030_SIM_LYR/SIM_LYR.usda",
    "./040_DATA_LYRs/DATA_LYRs.usda",
    "./020_BASE_LYR/ACTGR_LYR.usda",
    "./020_BASE_LYR/ANIM_LYR.usda",
    "./020_BASE_LYR/VAR_LYR.usda",
    "./020_BASE_LYR/MTL_LYR.usda",
    "./020_BASE_LYR/ASS_LYR.usda",
]

# Layers to create (folder, filename). All get minimal content: #usda 1.0
LAYERS_TO_CREATE = [
    ("020_BASE_LYR", "OPIN_LYR.usda"),
    ("020_BASE_LYR", "CAM_LYR.usda"),
    ("020_BASE_LYR", "ENV_LYR.usda"),
    ("020_BASE_LYR", "ASS_LYR.usda"),
    ("020_BASE_LYR", "MTL_LYR.usda"),
    ("020_BASE_LYR", "VAR_LYR.usda"),
    ("020_BASE_LYR", "ACTGR_LYR.usda"),
    ("020_BASE_LYR", "ANIM_LYR.usda"),
    ("020_BASE_LYR", "PHY_LYR.usda"),
    ("030_SIM_LYR", "SIM_LYR.usda"),
    ("040_DATA_LYRs", "DATA_LYRs.usda"),
]

# Scale options: (suffix, metersPerUnit value, display)
SCALE_OPTIONS = [
    ("m", 1.0, "Meters"),
    ("cm", 0.01, "Centimeters"),
    ("mm", 0.001, "Millimeters"),
]

# Layer templates for files that need more than just #usda 1.0
# Use {default_prim} placeholder for the default prim name
LAYER_TEMPLATES = {
    "ASS_LYR.usda": '''#usda 1.0

over "{default_prim}"
{{
    def Xform "A" (
        references = <>
    )
    {{
        double3 xformOp:rotateXYZ = (0, 0, 0)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, 0, 0)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
    }}

    def Xform "B" (
        references = <>
    )
    {{
        double3 xformOp:rotateXYZ = (0, 0, 0)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, 0, 0)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
    }}
}}

''',
    "CAM_LYR.usda": '''#usda 1.0

over "{default_prim}"
{{
    def Camera "Camera"
    {{
        float2 clippingRange = (1, 10000000)
        float focalLength = 18.147562
        float focusDistance = 400
        double3 xformOp:rotateYXZ = (0, -0, -0)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, 270, 360)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateYXZ", "xformOp:scale"]
    }}
}}

''',
}

README_TEMPLATES = {
    "000_SOURCE": """# 000_SOURCE

**Purpose:** Original CAD/DCC source files before USD conversion.

Place your source files here (CAD files, DCC project files, etc.) before converting to USD format.
""",
    "010_ASS_USD": """# 010_ASS_USD

**Purpose:** USD assets (converted from CAD or created in DCC + Textrurs from that were created in 2D Apps) | 

## Folder Structure
- `USD_Endpoint/` - Geometry assets -> Exports froM CAD / DCC as stable Endpoints, the name Stays constant
- `MatLib/` - Material libraries
- `tex/` - Global textures shared across multiple assets Place shared texture files here. Asset-specific textures can live with their assets in `USD_Endpoint/`
- `Envs/` -  Environments 

See the main README.md for detailed usage instructions.
""",
    "020_BASE_LYR": """# 020_BASE_LYR

**Purpose:** Base USD layers (opinion, asset import, material import, variant, action, animation layers).

# 020_BASE_LYR

**Purpose:** General USD layers (visual, layout, material, opinion layers).


ACTGR_LYR.usda -> Action Graphs
ANIM_LYR.usda -> Animation tracks
ASS_LYR.usda -> Assets | Local | Reference | Payloads
CAM_LYR.usda -> Cameras
ENV_LYR.usda -> Environment
MTL_LYR.usda -> Material Libaries | Local materials 
OPIN_LYR.usda -> Opinions
PHY_LYR.usda -> Physics simulation
VAR_LYR.usda -> Variants

See the main README.md for detailed usage instructions.
""",
    "030_SIM_LYR": """# 030_SIM_LYR

**Purpose:** Simulation layers (external simulations e.g. ansys)

See the main README.md for detailed usage instructions.
""",
    "040_DATA_LYRs": """# 040_DATA_LYRs

**Purpose:** Data layers for data-driven digital twin integration (PLM/ERP/AAS/OPC UA / sensor / data metadata).

See the main README.md for detailed usage instructions.
""",
}

# ============================================================================
# Root template: based on USD_GoodStart_m_ROOT.usda
# {root_filename}, {mpu_str}, and {default_prim} are substituted.
# ============================================================================

def _get_root_template_content(root_filename: str, mpu_str: str, default_prim: str) -> str:
    """Return root USDA content. Template uses root_filename, mpu_str, and default_prim."""
    sublayers_str = ",\n        ".join([f"@{p}@" for p in SUBLAYERS])
    return f'''#usda 1.0
(
    customLayerData = {{
        dictionary cameraSettings = {{
            dictionary Front = {{
                double3 position = (0, 0, 50000)
                double radius = 500
            }}
            dictionary Perspective = {{
                double3 position = (764.2241942381814, 633.5855099124096, 796.3182160588008)
                double3 target = (-26.46817790205455, 225.2060805154992, 84.34472110960974)
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
            string authoring_layer = "./{root_filename}"
            dictionary locked = {{
                bool "./020_BASE_LYR/ACTGR_LYR.usda" = 1
                bool "./020_BASE_LYR/ANIM_LYR.usda" = 1
                bool "./020_BASE_LYR/ASS_LYR.usda" = 1
                bool "./020_BASE_LYR/CAM_LYR.usda" = 1
                bool "./020_BASE_LYR/ENV_LYR.usda" = 1
                bool "./020_BASE_LYR/MTL_LYR.usda" = 1
                bool "./020_BASE_LYR/OPIN_LYR.usda" = 1
                bool "./020_BASE_LYR/VAR_LYR.usda" = 1
                bool "./030_SIM_LYR/SIM_LYR.usda" = 1
                bool "./040_DATA_LYRs/DATA_LYRs.usda" = 1
            }}
            dictionary muteness = {{
            }}
        }}
        dictionary renderSettings = {{
            double "rtx:directLighting:sampledLighting:maxRayUnexposedIntensity" = 6399.9990234375
            double "rtx:indirectDiffuse:maxRayUnexposedIntensity" = 6399.9990234375
            double "rtx:pathtracing:fireflyFilter:maxPerEmissiveUnexposedIntensity" = 3199.99951171875
            double "rtx:pathtracing:fireflyFilter:maxUnexposedIntensityPerSample" = 3199.99951171875
            double "rtx:pathtracing:fireflyFilter:maxUnexposedIntensityPerSampleDiffuse" = 3199.99951171875
            double "rtx:post:lensFlares:flareScale" = 0.075
            double "rtx:raytracing:inscattering:maxRTSampleUnexposedIntensity" = 204799.96875
            float3 "rtx:sceneDb:ambientLightColor" = (0, 0, 0)
            double "rtx:translucency:maxRayUnexposedIntensity" = 19199.998046875
        }}
    }}
    defaultPrim = "{default_prim}"
    endTimeCode = 100
    metersPerUnit = {mpu_str}
    startTimeCode = 0
    subLayers = [
        {sublayers_str}
    ]
    timeCodesPerSecond = 60
    upAxis = "Y"
)

def Xform "{default_prim}"
{{
    def Mesh "Cube"
    {{
        float3[] extent = [(-50, -50, -50), (50, 50, 50)]
        int[] faceVertexCounts = [4, 4, 4, 4, 4, 4]
        int[] faceVertexIndices = [0, 1, 3, 2, 4, 6, 7, 5, 6, 2, 3, 7, 4, 5, 1, 0, 4, 0, 2, 6, 5, 7, 3, 1]
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
        double3 xformOp:translate = (0, 267.6749425311719, 0)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
    }}
}}

def Xform "Environment"
{{
    int ground:size = 1400
    string ground:type = "On"
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
        float inputs:shaping:cone:softness
        float inputs:shaping:focus
        color3f inputs:shaping:focusTint
        asset inputs:shaping:ies:file
        token visibility = "inherited"
        double3 xformOp:rotateXYZ = (0, 180, 0)
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
        float inputs:exposure = 12
        float inputs:intensity = 1
        bool inputs:normalize = 1
        float inputs:shaping:cone:angle = 180
        float inputs:shaping:cone:softness
        float inputs:shaping:focus
        color3f inputs:shaping:focusTint
        asset inputs:shaping:ies:file
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
        texCoord2f[] primvars:st = [(0, 0), (14, 0), (14, 14), (0, 14)] (
            interpolation = "faceVarying"
        )
        uniform token subdivisionScheme = "none"
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
                prepend apiSchemas = ["OmniRtxSettingsCommonAdvancedAPI_1", "OmniRtxSettingsRtAdvancedAPI_1", "OmniRtxSettingsPtAdvancedAPI_1", "OmniRtxPostColorGradingAPI_1", "OmniRtxPostChromaticAberrationAPI_1", "OmniRtxPostBloomPhysicalAPI_1", "OmniRtxPostMatteObjectAPI_1", "OmniRtxPostCompositingAPI_1", "OmniRtxPostDofAPI_1", "OmniRtxPostMotionBlurAPI_1", "OmniRtxPostTvNoiseAPI_1", "OmniRtxPostTonemapIrayReinhardAPI_1", "OmniRtxPostDebugSettingsAPI_1", "OmniRtxDebugSettingsAPI_1"]
                hide_in_stage_window = true
                no_delete = true
            )
            {{
                rel camera = </OmniverseKit_Persp>
                token omni:rtx:ambientOcclusion:denoiserMode = "none"
                token omni:rtx:background:source:texture:textureMode = "repeatMirrored"
                token omni:rtx:background:source:type = "domeLight"
                bool omni:rtx:debug:view:pixelDebug:enableFixedTextPos = 1
                token omni:rtx:directLighting:sampledLighting:denoisingTechnique = "None"
                bool omni:rtx:dlss:frameGeneration = 1
                bool omni:rtx:indirectDiffuse:denoiser:enabled = 0
                float omni:rtx:post:bloom:scale = 0.075
                bool omni:rtx:post:registeredCompositing:invertColorCorrection = 1
                bool omni:rtx:post:registeredCompositing:invertToneMap = 1
                int omni:rtx:pt:maxSamplesPerLaunch = 2073600
                int omni:rtx:pt:mgpu:maxPixelsPerRegionExponent = 12
                bool omni:rtx:reflections:denoiser:enabled = 0
                token omni:rtx:rendermode = "RealTimePathTracing"
                bool omni:rtx:rt:demoire = 0
                bool omni:rtx:rt:lightcache:spatialCache:dontResolveConflicts = 1
                int omni:rtx:rt:sss:samples = 1
                int omni:rtx:rtpt:maxVolumeBounces = 15
                float omni:rtx:rtpt:modulatingRoughnessThreshold = 0.08
                uint omni:rtx:viewTile:limit = 4294967295
                rel orderedVars = </Render/Vars/LdrColor>
                custom bool overrideClipRange = 0
                uniform int2 resolution = (2160, 1135)
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
'''


# ============================================================================
# Interactive
# ============================================================================

def print_header():
    print("\n" + "=" * 70)
    print("  USD GoodStart Project Setup")
    print("=" * 70)
    print()


def ask_scale() -> int:
    """Return 0=m, 1=cm, 2=mm."""
    print("Select scale (root file metersPerUnit):")
    for i, (suffix, _, label) in enumerate(SCALE_OPTIONS):
        print(f"  [{i + 1}] {label} ({suffix}) – metersPerUnit = {SCALE_OPTIONS[i][1]}")
    while True:
        choice = input("Enter choice (1–3, default: 1): ").strip() or "1"
        if choice in ("1", "2", "3"):
            return int(choice) - 1
        print("Please enter 1, 2, or 3.")


def ask_default_prim() -> str:
    """Ask for the default prim name. Returns 'World' if empty."""
    print("\nDefault prim name (the root Xform that holds your scene):")
    print("  This name will be used in the root file and all layer files.")
    print("  Examples: World, MyProduct, Scene, Assembly")
    name = input("Enter default prim name (default: World): ").strip()
    if not name:
        return "World"
    # Basic validation: must be a valid USD prim name (no spaces, starts with letter)
    if not name[0].isalpha():
        print("Warning: Prim name should start with a letter. Using 'World' instead.")
        return "World"
    # Replace spaces and invalid chars with underscores
    import re
    clean_name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
    if clean_name != name:
        print(f"Note: Prim name adjusted to '{clean_name}' (removed invalid characters)")
    return clean_name


# ============================================================================
# File generation
# ============================================================================

def create_folder_structure(base_path: Path):
    print("\nCreating folder structure...")
    for folder in FOLDER_STRUCTURE:
        folder_path = base_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"  [OK] {folder}")


def create_readme_files(base_path: Path):
    print("\nCreating README files...")
    for folder in FOLDER_STRUCTURE:
        top = folder.split("/")[0]
        if top in README_TEMPLATES:
            readme_path = base_path / top / "README.md"
            readme_path.write_text(README_TEMPLATES[top], encoding="utf-8")
            print(f"  [OK] {top}/README.md")


def create_layer_files(base_path: Path, default_prim: str):
    """Create all sublayer USDA files. Uses templates for ASS_LYR and CAM_LYR, minimal for others."""
    print("\nCreating layer files...")
    minimal_content = "#usda 1.0\n"
    for folder, filename in LAYERS_TO_CREATE:
        path = base_path / folder / filename
        # Use template if available, otherwise minimal
        template = LAYER_TEMPLATES.get(filename)
        if template:
            content = template.format(default_prim=default_prim)
        else:
            content = minimal_content
        path.write_text(content, encoding="utf-8")
        print(f"  [OK] {folder}/{filename}")


def create_root_file(base_path: Path, scale_index: int, default_prim: str) -> str:
    """Create root USDA. If this script lives in USD_GoodStart/scripts and the
    reference root exists in repo root, copy it; else generate from template.
    Replaces 'World' with default_prim in all cases.
    Returns the root filename.
    """
    import re
    suffix, mpu_val, _ = SCALE_OPTIONS[scale_index]
    # Use default_prim in the filename instead of USD_GoodStart
    root_filename = f"{default_prim}_{suffix}_ROOT.usda"
    path = base_path / root_filename

    # Prefer copying reference root from repo when available (same dir as script -> parent = repo root)
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    # Reference roots in repo are named USD_GoodStart_*_ROOT.usda
    reference_root = repo_root / f"USD_GoodStart_{suffix}_ROOT.usda"
    if reference_root.exists():
        content = reference_root.read_text(encoding="utf-8")
        # Update authoring_layer to point at the new filename
        content = re.sub(
            r'(string authoring_layer = )"[^"]*"',
            f'\\1"./{root_filename}"',
            content,
        )
        # Replace default prim name if not "World"
        if default_prim != "World":
            content = re.sub(r'defaultPrim = "World"', f'defaultPrim = "{default_prim}"', content)
            content = re.sub(r'def Xform "World"', f'def Xform "{default_prim}"', content)
        path.write_text(content, encoding="utf-8")
        print(f"  [OK] {root_filename} (copied from repo)")
        return root_filename

    mpu_str = "1" if mpu_val == 1.0 else str(mpu_val)
    content = _get_root_template_content(root_filename, mpu_str, default_prim)
    path.write_text(content, encoding="utf-8")
    print(f"  [OK] {root_filename}")
    return root_filename


# ============================================================================
# Main
# ============================================================================

def setup_project(target_dir: Optional[Path] = None) -> bool:
    print_header()

    if target_dir is not None:
        base_path = Path(target_dir).resolve()
    else:
        base_path = Path.cwd()
        script_markers = ["setup_usd_project.py", "setup_usd_project.bat", "SETUP_STANDALONE.md"]
        if all((base_path / f).exists() for f in script_markers):
            base_path = base_path.parent
            print("Detected setup script folder. Creating project in parent directory.")

    print(f"Target directory: {base_path}\n")

    if base_path.exists() and any(base_path.iterdir()):
        response = input("Directory is not empty. Continue? (y/n): ").strip().lower()
        if response != "y":
            print("Setup cancelled.")
            return False

    scale_index = ask_scale()
    suffix = SCALE_OPTIONS[scale_index][0]
    print(f"[OK] Scale: {SCALE_OPTIONS[scale_index][2]} ({suffix})")

    default_prim = ask_default_prim()
    print(f"[OK] Default prim: {default_prim}\n")

    print("=" * 70)
    print("  Generating project structure...")
    print("=" * 70)

    try:
        create_folder_structure(base_path)
        create_readme_files(base_path)
        create_layer_files(base_path, default_prim)
        root_name = create_root_file(base_path, scale_index, default_prim)

        print("\n" + "=" * 70)
        print("  [OK] Project setup complete!")
        print("=" * 70)
        print(f"\nRoot file: {base_path / root_name}")
        print(f"Default prim: {default_prim}")
        print("\nNext steps:")
        print("  1. Open the root file in Omniverse Composer")
        print("  2. Add assets under 010_ASS_USD/USD_Endpoint/")
        print("  3. Author content in 020_BASE_LYR, 030_SIM_LYR, 040_DATA_LYRs as needed")
        print()
        return True
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    args = sys.argv[1:]
    if args and args[0] in ("--version", "-v"):
        print(f"USD GoodStart Setup Script v{__version__}")
        sys.exit(0)
    target = Path(args[0]) if args else None
    ok = setup_project(target)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
