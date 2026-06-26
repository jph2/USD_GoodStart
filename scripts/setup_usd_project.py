#!/usr/bin/env python3
"""
USD GoodStart Project Setup Script

Creates a USD_GoodStart project with folder structure and one root scene (m, cm, or mm scale).
Based on USD_GoodStart_m_ROOT.usda, USD_GoodStart_cm_ROOT.usda, USD_GoodStart_mm_ROOT.usda
and folders: 000_SOURCE, 010_ASS_USD, 020_BASE_LYR, 030_SIM_LYR, 035_RUNTIME_LYR, 040_DATA_LYRs.

Usage:
    python scripts/setup_usd_project.py [target_directory]
    python scripts/setup_usd_project.py --version

If no directory is provided, the script runs in the current directory.
"""

# Version: 0.9.5.2 | Date: 27.06.2026 | Time: 00:17 | GlobalID: 20260627_0017_USDGoodStart_Setup
__version__ = "0.9.5.2"

import sys
from pathlib import Path
from typing import List, Optional

# ============================================================================
# Configuration
# ============================================================================

FOLDER_STRUCTURE = [
    "000_SOURCE",
    "010_ASS_USD",
    "010_ASS_USD/USD_Startpoint",
    "010_ASS_USD/MatLib",
    "010_ASS_USD/tex",
    "010_ASS_USD/Envs",
    "020_BASE_LYR",
    "030_SIM_LYR",
    "035_RUNTIME_LYR",
    "040_DATA_LYRs",
]

# Sublayer paths (strongest first). Must match roots USD_GoodStart_*_ROOT.usda.
SUBLAYERS = [
    "./020_BASE_LYR/OPIN_LYR.usda",
    "./020_BASE_LYR/CAM_LYR.usda",
    "./020_BASE_LYR/ENV_LYR.usda",
    "./035_RUNTIME_LYR/RUNTIME_LYR.usda",
    "./030_SIM_LYR/SIM_LYR.usda",
    "./040_DATA_LYRs/DATA_LYRs.usda",
    "./020_BASE_LYR/ACTGR_LYR.usda",
    "./020_BASE_LYR/ANIM_LYR.usda",
    "./020_BASE_LYR/VAR_LYR.usda",
    "./020_BASE_LYR/MTL_LYR.usda",
    "./020_BASE_LYR/PHY_LYR.usda",
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
    ("035_RUNTIME_LYR", "RUNTIME_LYR.usda"),
    ("040_DATA_LYRs", "DATA_LYRs.usda"),
]

# Scale options: (suffix, metersPerUnit value, display). Order: cm first (default for Omniverse Composer).
SCALE_OPTIONS = [
    ("cm", 0.01, "Centimeters"),
    ("m", 1.0, "Meters"),
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
- `USD_Startpoint/` - Geometry assets -> Exports froM CAD / DCC as stable Startpoints, the name Stays constant
- `MatLib/` - Material libraries
- `tex/` - Global textures shared across multiple assets Place shared texture files here. Asset-specific textures can live with their assets in `USD_Startpoint/`
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
    "035_RUNTIME_LYR": """# 035_RUNTIME_LYR

**Purpose:** Runtime/session-backed layer slot for live digital twin state such as MQTT, OPC UA, or other shopfloor telemetry.

Keep live telemetry in a session layer or runtime signal store by default. Use `RUNTIME_LYR.usda` only for explicit runtime opinions or snapshots that should be persisted.

Static metadata belongs in `040_DATA_LYRs/`.

See the main README.md for detailed usage instructions.
""",
    "040_DATA_LYRs": """# 040_DATA_LYRs

**Purpose:** Static and slow-changing data layers for data-driven digital twin integration (PLM/ERP/AAS/OPC UA / metadata).

Live telemetry belongs in a session layer or `035_RUNTIME_LYR/`, not here by default.

See the main README.md for detailed usage instructions.
""",
}

# ============================================================================
# Root template: keeps the starter scene physically consistent across unit choices.
# Numeric values are authored in the selected stage unit.
# ============================================================================

def _fmt_usd_number(value: float) -> str:
    """Format numeric USDA values without noisy trailing precision."""
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.15g}"


def _stage_units(meters: float, meters_per_unit: float) -> str:
    """Convert a physical meter value to the selected stage unit."""
    return _fmt_usd_number(meters / meters_per_unit)


def _stage_tuple(values_meters: tuple[float, float, float], meters_per_unit: float) -> str:
    return ", ".join(_stage_units(value, meters_per_unit) for value in values_meters)


def _get_root_template_content(root_filename: str, mpu_val: float, default_prim: str) -> str:
    """Return root USDA content with starter geometry scaled by metersPerUnit."""
    mpu_str = "1" if mpu_val == 1.0 else str(mpu_val)
    sublayers_str = ",\n        ".join([f"@{p}@" for p in SUBLAYERS])
    cube_half = _stage_units(0.5, mpu_val)
    ground_half = _stage_units(7.0, mpu_val)
    ground_size = _stage_units(14.0, mpu_val)
    light_height = _stage_units(3.05, mpu_val)
    camera_far = _stage_units(500.0, mpu_val)
    camera_radius = _stage_units(5.0, mpu_val)
    persp_position = _stage_tuple((-6.486169164847129, 7.196822390878303, 20.611666836476675), mpu_val)
    persp_target = _stage_tuple((0.8683254870102121, -0.7283014643907768, 0.3723306848790707), mpu_val)
    return f'''#usda 1.0
(
    customLayerData = {{
        dictionary cameraSettings = {{
            dictionary Front = {{
                double3 position = (0, 0, {camera_far})
                double radius = {camera_radius}
            }}
            dictionary Perspective = {{
                double3 position = ({persp_position})
                double3 target = ({persp_target})
            }}
            dictionary Right = {{
                double3 position = (-{camera_far}, 0, 0)
                double radius = {camera_radius}
            }}
            dictionary Top = {{
                double3 position = (0, {camera_far}, 0)
                double radius = {camera_radius}
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
                bool "./020_BASE_LYR/PHY_LYR.usda" = 1
                bool "./020_BASE_LYR/VAR_LYR.usda" = 1
                bool "./030_SIM_LYR/SIM_LYR.usda" = 1
                bool "./035_RUNTIME_LYR/RUNTIME_LYR.usda" = 1
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
        float3[] extent = [(-{cube_half}, -{cube_half}, -{cube_half}), ({cube_half}, {cube_half}, {cube_half})]
        int[] faceVertexCounts = [4, 4, 4, 4, 4, 4]
        int[] faceVertexIndices = [0, 1, 3, 2, 4, 6, 7, 5, 6, 2, 3, 7, 4, 5, 1, 0, 4, 0, 2, 6, 5, 7, 3, 1]
        normal3f[] normals = [(0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, -1), (0, 0, -1), (0, 0, -1), (0, 0, -1), (0, 1, 0), (0, 1, 0), (0, 1, 0), (0, 1, 0), (0, -1, 0), (0, -1, 0), (0, -1, 0), (0, -1, 0), (-1, 0, 0), (-1, 0, 0), (-1, 0, 0), (-1, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0)] (
            interpolation = "faceVarying"
        )
        point3f[] points = [(-{cube_half}, -{cube_half}, {cube_half}), ({cube_half}, -{cube_half}, {cube_half}), (-{cube_half}, {cube_half}, {cube_half}), ({cube_half}, {cube_half}, {cube_half}), (-{cube_half}, -{cube_half}, -{cube_half}), ({cube_half}, -{cube_half}, -{cube_half}), (-{cube_half}, {cube_half}, -{cube_half}), ({cube_half}, {cube_half}, -{cube_half})]
        texCoord2f[] primvars:st = [(0, 0), (1, 0), (1, 1), (0, 1), (1, 0), (1, 1), (0, 1), (0, 0), (0, 1), (0, 0), (1, 0), (1, 1), (0, 0), (1, 0), (1, 1), (0, 1), (0, 0), (1, 0), (1, 1), (0, 1), (1, 0), (1, 1), (0, 1), (0, 0)] (
            interpolation = "faceVarying"
        )
        uniform token subdivisionScheme = "none"
        double3 xformOp:rotateXYZ = (0, 0, 0)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, {cube_half}, 0)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
    }}
}}

def Xform "Environment"
{{
    int ground:size = {ground_size}
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
        double3 xformOp:translate = (0, {light_height}, 0)
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
        double3 xformOp:translate = (0, {light_height}, 0)
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
        float3[] extent = [(-{ground_half}, -{ground_half}, 0), ({ground_half}, {ground_half}, 0)]
        int[] faceVertexCounts = [4]
        int[] faceVertexIndices = [0, 1, 3, 2]
        rel material:binding = </Environment/Looks/Grid> (
            bindMaterialAs = "weakerThanDescendants"
        )
        normal3f[] normals = [(0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1)] (
            interpolation = "faceVarying"
        )
        point3f[] points = [(-{ground_half}, -{ground_half}, 0), ({ground_half}, -{ground_half}, 0), (-{ground_half}, {ground_half}, 0), ({ground_half}, {ground_half}, 0)]
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
    print("  *** IMPORTANT: Stage scale defaults differ by app ***")
    print("  Isaac Sim and Isaac Lab use METERS as the default stage unit.")
    print("  Omniverse Composer uses CENTIMETERS as the default.")
    print("  Choose the scale that matches your target app.")
    print()


def ask_scale() -> int:
    """Return 0=cm, 1=m, 2=mm. Default is 0 (Centimeters) for Omniverse Composer."""
    print("Select scale (root file metersPerUnit):")
    print()
    print("Please note!")
    print("- Isaac Sim and Isaac Lab have a default scene scale of 1 meter")
    print("- Omniverse Composer has a default scale of 1 centimeter")
    print()
    print("  [1] (Composer default)\t\t  -> Centimeters (cm)\t– metersPerUnit = 0.01 [default]")
    print()
    print("  [2] (IsaacSim / Lab default)\t\t  -> Meters (m)\t– metersPerUnit = 1.0")
    print()
    print("  [3] (are you nuts? / special interest!) -> Millimeters (mm)\t– metersPerUnit = 0.001")
    print()
    print("Special Note:")
    print("The starter cube, ground, lights, and camera guides are authored in the selected stage")
    print("unit so their physical size stays consistent across meters, centimeters, and millimeters.")
    print()
    print("Omniverse may still show transform scale as 1 because scale is a multiplier on the authored")
    print("geometry, not the same thing as the stage unit. Debug physical size via metersPerUnit plus")
    print("authored point/translate values, not by xformOp:scale alone.")
    print()
    while True:
        choice = input("Enter choice (1–3, default: 1 = Centimeters): ").strip() or "1"
        if choice in ("1", "2", "3"):
            return int(choice) - 1
        print("Please enter 1, 2, or 3.")


def ask_scale_confirm(scale_index: int) -> bool:
    """Require user to type the unit suffix (cm, m, mm) to confirm. Returns True if confirmed."""
    suffix, _, label = SCALE_OPTIONS[scale_index]
    print()
    print("  Referring to Isaac Sim and Isaac Lab: choose the scale that matches your target app.")
    prompt = f"Are you sure you want to use {label}? Type '{suffix}' to confirm (or 'q' to choose again): "
    while True:
        typed = input(prompt).strip().lower()
        if typed == "q":
            return False
        if typed == suffix:
            return True
        print(f"  You typed '{typed}'. Please type exactly '{suffix}' to confirm, or 'q' to pick another scale.")


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

    content = _get_root_template_content(root_filename, mpu_val, default_prim)
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

    while True:
        scale_index = ask_scale()
        if ask_scale_confirm(scale_index):
            break
        print("  Scale not confirmed. Please choose again.\n")

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
        print("  2. Add assets under 010_ASS_USD/USD_Startpoint/")
        print("  3. Author content in 020_BASE_LYR, 035_RUNTIME_LYR, 030_SIM_LYR, 040_DATA_LYRs as needed")
        print()
        print("  --- Note: Stage scale (metersPerUnit) ---")
        print("  Isaac Sim and Isaac Lab handle stage scale in METERS by default.")
        print("  Omniverse Composer uses CENTIMETERS by default.")
        print("  When sharing USD between these apps, use the same scale or convert.")
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
