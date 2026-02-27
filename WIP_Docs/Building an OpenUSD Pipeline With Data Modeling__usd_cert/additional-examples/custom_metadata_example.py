"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 4 (metadata and customData conventions)

Why this script exists:
- It shows practical metadata authoring on an attribute.
- It includes nested customData, which is common for app-specific context.

How to run:
- From the __usd_cert folder:
  python additional-examples/custom_metadata_example.py

What to observe:
1) Registered metadata keys vs customData payload.
2) Difference between all metadata and authored metadata.
3) Accessing nested values in customData for downstream usage.
"""

from pxr import Sdf, Usd, UsdGeom

stage = Usd.Stage.CreateInMemory()
prim_path = Sdf.Path("/bicycle")
prim = stage.DefinePrim(prim_path, "Xform")
attr = prim.CreateAttribute("tire:size", Sdf.ValueTypeNames.Float)
attr.Set(10)

# Add various custom metadata (using registered USD metadata keys)
attr.SetMetadata("interpolation", UsdGeom.Tokens.constant)
attr.SetMetadata("comment", "This is the tire size in inches")  # String metadata
attr.SetMetadata("documentation", "Tire size specification for bicycle wheels")  # String metadata
attr.SetMetadata("displayName", "Tire Size")  # String metadata for UI display
attr.SetMetadata("hidden", False)  # Boolean metadata

# customData allows you to store arbitrary custom key-value pairs
attr.SetMetadata("customData", {
    "manufacturer": "Acme Tires Inc.",
    "model": "RoadMaster 3000",
    "year": 2024,
    "certifications": ["ISO-9001", "CE"],
    "specifications": {
        "maxPressure": 65,
        "minPressure": 35,
        "material": "rubber composite"
    }
})

print("=" * 60)
print("ATTRIBUTE INFORMATION")
print("=" * 60)
print(f"Attribute Name: {attr.GetName()}")
print(f"Attribute Value: {attr.Get()}")
print(f"Attribute Type: {attr.GetTypeName()}")

print("\n" + "=" * 60)
print("ALL METADATA (Key: Value)")
print("=" * 60)
for key in sorted(attr.GetAllMetadata().keys()):
    value = attr.GetMetadata(key)
    print(f"  {key:20s}: {value}")

print("\n" + "=" * 60)
print("AUTHORED METADATA ONLY (Key: Value)")
print("=" * 60)
for key in sorted(attr.GetAllAuthoredMetadata().keys()):
    value = attr.GetMetadata(key)
    print(f"  {key:20s}: {value}")

print("\n" + "=" * 60)
print("ACCESSING SPECIFIC METADATA")
print("=" * 60)
print(f"Comment: {attr.GetMetadata('comment')}")
print(f"Documentation: {attr.GetMetadata('documentation')}")
print(f"Display Name: {attr.GetMetadata('displayName')}")
print(f"Hidden: {attr.GetMetadata('hidden')}")

print("\n" + "=" * 60)
print("ACCESSING CUSTOMDATA")
print("=" * 60)
custom_data = attr.GetMetadata('customData')
print(f"Full customData: {custom_data}")
print(f"\nManufacturer: {custom_data.get('manufacturer')}")
print(f"Model: {custom_data.get('model')}")
print(f"Year: {custom_data.get('year')}")
print(f"Certifications: {custom_data.get('certifications')}")
print(f"Max Pressure: {custom_data.get('specifications', {}).get('maxPressure')} PSI")
print(f"Material: {custom_data.get('specifications', {}).get('material')}")
