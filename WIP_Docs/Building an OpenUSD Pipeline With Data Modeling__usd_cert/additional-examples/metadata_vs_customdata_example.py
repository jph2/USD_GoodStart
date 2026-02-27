"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 4 (metadata semantics)
- Chapter 8 (debugging metadata misuse)

Why this script exists:
- It clarifies a common confusion: SetMetadata vs SetCustomData.
- This is essential for keeping governance and app-specific data clean.

How to run:
- From the __usd_cert folder:
  python additional-examples/metadata_vs_customdata_example.py

What to observe:
1) SetCustomData is a convenience for metadata key "customData".
2) GetCustomData is equivalent to GetMetadata("customData").
3) Key-level customData APIs for controlled updates.
"""

from pxr import Sdf, Usd, UsdGeom

stage = Usd.Stage.CreateInMemory()
prim_path = Sdf.Path("/bicycle")
prim = stage.DefinePrim(prim_path, "Xform")

print("=" * 70)
print("DIFFERENCE BETWEEN SetMetadata() AND SetCustomData()")
print("=" * 70)

# ============================================================
# METHOD 1: prim.SetMetadata("key", value)
# ============================================================
print("\n1. prim.SetMetadata('key', value)")
print("-" * 70)
print("   - Sets INDIVIDUAL metadata fields")
print("   - Can set ANY registered metadata key")
print("   - Examples: comment, documentation, hidden, kind, active, etc.")
print()

# Set individual metadata fields
prim.SetMetadata("comment", "Main bicycle transform")
prim.SetMetadata("documentation", "Root transform for the bicycle")
prim.SetMetadata("hidden", False)
prim.SetMetadata("kind", "component")

print("   Set metadata:")
print(f"     comment: {prim.GetMetadata('comment')}")
print(f"     documentation: {prim.GetMetadata('documentation')}")
print(f"     hidden: {prim.GetMetadata('hidden')}")
print(f"     kind: {prim.GetMetadata('kind')}")

# ============================================================
# METHOD 2: prim.SetCustomData({...})
# ============================================================
print("\n2. prim.SetCustomData({...})")
print("-" * 70)
print("   - Sets the ENTIRE 'customData' metadata field")
print("   - 'customData' is ONE specific metadata key")
print("   - Replaces ALL existing customData")
print("   - Used for application-specific data")
print()

# Set custom data (this is actually setting metadata key 'customData')
prim.SetCustomData({
    "assetId": "BIKE-001",
    "version": 1,
    "owner": "Design Team"
})

print("   Set customData:")
print(f"     assetId: {prim.GetCustomDataByKey('assetId')}")
print(f"     version: {prim.GetCustomDataByKey('version')}")
print(f"     owner: {prim.GetCustomDataByKey('owner')}")

# ============================================================
# IMPORTANT: SetCustomData() is equivalent to SetMetadata("customData", {...})
# ============================================================
print("\n" + "=" * 70)
print("EQUIVALENCE DEMONSTRATION")
print("=" * 70)

# Create another prim to demonstrate equivalence
prim2 = stage.DefinePrim("/test1", "Xform")
prim3 = stage.DefinePrim("/test2", "Xform")

# These two are EQUIVALENT:
prim2.SetCustomData({"foo": "bar", "num": 42})
prim3.SetMetadata("customData", {"foo": "bar", "num": 42})

print("\nThese two methods are EQUIVALENT:")
print("  prim2.SetCustomData({'foo': 'bar', 'num': 42})")
print("  prim3.SetMetadata('customData', {'foo': 'bar', 'num': 42})")
print()
print(f"  prim2 customData: {prim2.GetCustomData()}")
print(f"  prim3 customData: {prim3.GetCustomData()}")
print(f"  Are they equal? {prim2.GetCustomData() == prim3.GetCustomData()}")

# ============================================================
# METHOD 3: prim.GetMetadata("key")
# ============================================================
print("\n" + "=" * 70)
print("DIFFERENCE BETWEEN GetMetadata() AND GetCustomData()")
print("=" * 70)

print("\n1. prim.GetMetadata('key')")
print("-" * 70)
print("   - Gets ANY metadata field by key")
print("   - Generic method for all metadata")
print()

print("   Examples:")
print(f"     GetMetadata('comment'): {prim.GetMetadata('comment')}")
print(f"     GetMetadata('kind'): {prim.GetMetadata('kind')}")
print(f"     GetMetadata('customData'): {prim.GetMetadata('customData')}")

# ============================================================
# METHOD 4: prim.GetCustomData()
# ============================================================
print("\n2. prim.GetCustomData()")
print("-" * 70)
print("   - Shortcut for GetMetadata('customData')")
print("   - Returns the entire customData dictionary")
print()

print("   Examples:")
print(f"     GetCustomData(): {prim.GetCustomData()}")
print(f"     GetMetadata('customData'): {prim.GetMetadata('customData')}")
print(f"     Are they equal? {prim.GetCustomData() == prim.GetMetadata('customData')}")

# ============================================================
# ADDITIONAL CUSTOMDATA METHODS
# ============================================================
print("\n" + "=" * 70)
print("ADDITIONAL CUSTOMDATA CONVENIENCE METHODS")
print("=" * 70)

print("\n1. prim.GetCustomDataByKey('key')")
print("   - Gets a SPECIFIC value from customData dictionary")
print(f"   - Example: {prim.GetCustomDataByKey('assetId')}")

print("\n2. prim.HasCustomDataKey('key')")
print("   - Checks if a key exists in customData")
print(f"   - Has 'assetId': {prim.HasCustomDataKey('assetId')}")
print(f"   - Has 'nonexistent': {prim.HasCustomDataKey('nonexistent')}")

print("\n3. prim.SetCustomDataByKey('key', value)")
print("   - Sets a SINGLE key in customData without replacing all")

# Set a single key without replacing existing customData
prim.SetCustomDataByKey("newField", "newValue")
print(f"   - After SetCustomDataByKey('newField', 'newValue'):")
print(f"     customData: {prim.GetCustomData()}")

print("\n4. prim.ClearCustomDataByKey('key')")
print("   - Removes a specific key from customData")

prim.ClearCustomDataByKey("newField")
print(f"   - After ClearCustomDataByKey('newField'):")
print(f"     customData: {prim.GetCustomData()}")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("""
SetMetadata("key", value):
  - Generic method to set ANY metadata field
  - Works for: comment, documentation, hidden, kind, customData, etc.
  
SetCustomData({...}):
  - Convenience method specifically for 'customData' field
  - Equivalent to: SetMetadata("customData", {...})
  - REPLACES entire customData dictionary

GetMetadata("key"):
  - Generic method to get ANY metadata field
  - Works for: comment, documentation, hidden, kind, customData, etc.
  
GetCustomData():
  - Convenience method specifically for 'customData' field
  - Equivalent to: GetMetadata("customData")
  - Returns the entire customData dictionary

Additional CustomData Methods:
  - GetCustomDataByKey('key')      - Get single value from customData
  - SetCustomDataByKey('key', val) - Set single value in customData
  - HasCustomDataKey('key')        - Check if key exists
  - ClearCustomDataByKey('key')    - Remove single key from customData
""")
