"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 6 (extract -> transform pipeline shape)
- Chapter 7 (convenience-layer helper patterns)
- Chapter 8 (validation and production hardening)

Why this script exists:
- It is an advanced conversion example with explicit pipeline phases.
- It shows how to keep extraction faithful, then apply controlled transforms.

How to run:
- Requires additional dependencies: assimp_py, usdex.core, and local common.*
- From the __usd_cert folder:
  python additional-examples/obj2usd.py <input.obj> -o <output.usda>

What to observe:
1) Extraction phase reads source geometry/material data.
2) Transform phase sets default prim and up-axis normalization.
3) Result is a structured stage suited for downstream validation.
"""

import argparse
import logging
import math
import sys
from enum import Enum
from pathlib import Path

import assimp_py
from pxr import Gf, Sdf, Tf, Usd, UsdGeom, UsdShade

import common.commandLine
import common.usdUtils
import usdex.core


logger = logging.getLogger("obj2usd")


class UpAxis(Enum):
    Y = UsdGeom.Tokens.y
    Z = UsdGeom.Tokens.z

    def __str__(self):
        return self.value

# ADD CODE BELOW HERE
# vvvvvvvvvvvvvvvvvvv

def extract(input_file: Path, output_file: Path) -> Usd.Stage:
    logger.info("Executing extraction phase...")
    process_flags = 0
    # Load the obj using Assimp 
    scene = assimp_py.ImportFile(str(input_file), process_flags)
    # Define the stage where the output will go 
    stage: Usd.Stage = Usd.Stage.CreateNew(str(output_file))
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
    # Assume linear units as meters.
    UsdGeom.SetStageMetersPerUnit(stage, UsdGeom.LinearUnits.meters)

    for mesh in scene.meshes:
        # Replace any invalid characters with underscores.
        sanitized_mesh_name = Tf.MakeValidIdentifier(mesh.name)
        usd_mesh = UsdGeom.Mesh.Define(stage, f"/{sanitized_mesh_name}")
        # You can use the Vt APIs here instead of Python lists.
        # Especially keep this in mind for C++ implementations.
        face_vertex_counts = []
        face_vertex_indices = []
        for indices in mesh.indices:
            # Convert the indices to a flat list
            face_vertex_indices.extend(indices)
            # Append the number of vertices for each face
            face_vertex_counts.append(len(indices))
        
        usd_mesh.CreatePointsAttr(mesh.vertices)
        usd_mesh.CreateFaceVertexCountsAttr().Set(face_vertex_counts)
        usd_mesh.CreateFaceVertexIndicesAttr().Set(face_vertex_indices)
        # Treat the mesh as a polygonal mesh and not a subdivision surface.
        # Respect the normals or lack of normals from OBJ.
        usd_mesh.CreateSubdivisionSchemeAttr(UsdGeom.Tokens.none)
        if mesh.normals:
            usd_mesh.CreateNormalsAttr(mesh.normals)
        
        # Get the mesh's material by index
        # scene.materials is a dictionary consisting of assimp material properties
        mtl = scene.materials[mesh.material_index]
        if not mtl:
            continue
        sanitized_mat_name = Tf.MakeValidIdentifier(mtl["NAME"])
        material_path = Sdf.Path(f"/{sanitized_mat_name}")
        # Get colors and convert specular shininess to roughness.
        diffuse_color = mtl["COLOR_DIFFUSE"]
        emissive_color = mtl["COLOR_EMISSIVE"]
        specular_color = mtl["COLOR_SPECULAR"]
        roughness = 1 - math.sqrt(mtl["SHININESS"] / 1000.0)

        # Create a UsdPreviewSurface material and bind it to the mesh.
        # definePreviewMaterial creates the Material prim and a connected UsdPreviewSurface shader.
        material: UsdShade.Material = usdex.core.definePreviewMaterial(
            stage=stage,
            path=material_path,
            color=Gf.Vec3f(diffuse_color),
            roughness=roughness,
        )
        # Switch to specular workflow and author the additional specular/emissive inputs
        # on the underlying UsdPreviewSurface shader via usdUtils.addPrimvarShader helper.
        shader: UsdShade.Shader = usdex.core.computeEffectivePreviewSurfaceShader(material)
        shader.CreateInput("useSpecularWorkflow", Sdf.ValueTypeNames.Int).Set(1)
        shader.CreateInput("specularColor", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3f(specular_color))
        shader.CreateInput("emissiveColor", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3f(emissive_color))
        usdex.core.bindMaterial(usd_mesh.GetPrim(), material)

    return stage


def set_default_prim(stage: Usd.Stage):
    """Set a default prim to make this stage referenceable

    OBJ has no notion of a scene graph hierarchy or a scene root.
    This is a mandatory chaser to move all prims under a default prim
    to make this asset referenceable.
    Args:
        stage (Usd.Stage): The stage to modify
    """

    # Get the prim in the root namespace that we want to reparent under the default prim.
    root_prims = stage.GetPseudoRoot().GetChildren()
    world_prim = UsdGeom.Xform.Define(stage, "/World").GetPrim()
    stage.SetDefaultPrim(world_prim)
    editor = Usd.NamespaceEditor(stage)
    for prim in root_prims:
        editor.ReparentPrim(prim, world_prim)
        editor.ApplyEdits()


def set_up_axis(stage: Usd.Stage, up_axis: UpAxis):
    """Set the specified up-axis for the stage.

    OBJ is Y-up by default. This is an optional chaser to allow
    users to change the up-axis to suit their pipeline. Corrective
    transformations are applied.

    Args:
        stage (Usd.Stage): The stage to modify
        up_axis (UpAxis): The up-axis value to set.
    """
    if up_axis == UpAxis.Y:
        UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
    else:
        UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
        xformable = UsdGeom.Xformable(stage.GetDefaultPrim())
        xformable.AddRotateXOp(opSuffix="unitsResolve").Set(90.0)


def transform(stage: Usd.Stage, args: argparse.Namespace):
    logger.info("Executing transformation phase...")
    set_default_prim(stage)
    set_up_axis(stage, args.up_axis)


def main(args: argparse.Namespace):
    # Extract the .obj
    stage: Usd.Stage = extract(args.input, args.output)
    # Transformations to be applied to the scene hierarchy
    transform(stage, args)
    # Save the Stage after editing
    stage.Save()

# ^^^^^^^^^^^^^^^^^^^^
# ADD CODE ABOVE HERE


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(
        "obj2usd", description="An OBJ to USD converter script."
    )
    parser.add_argument("input", help="Input OBJ file", type=Path)
    parser.add_argument("-o", "--output", help="Specify an output USD file", type=Path)
    export_opts = parser.add_argument_group("Export Options")
    export_opts.add_argument(
        "-u",
        "--up-axis",
        help="Specify the up axis for the exported USD stage.",
        type=UpAxis,
        choices=list(UpAxis),
        default=UpAxis.Y,
    )

    args = parser.parse_args()
    if args.output is None:
        args.output = args.input.parent / f"{args.input.stem}.usda"

    logger.info(f"Converting {args.input}...")
    main(args)
    logger.info(f"Converted results output as: {args.output}.")
    logger.info(f"Done.")