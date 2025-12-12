# 040_LYR_SIM

**Version:** 0.9.4-beta
**Last Updated:** 12.12.2025

## Purpose

This folder contains **simulation-specific USD layer files** for physics, robotics, and sensors.  
These layers add or override **simulation behavior** without touching base geometry or visual layers.

## Typical Layers

- `Collision_LYR.usda` – Collision geometry and `PhysicsCollisionAPI` setup  
- `Physics_LYR.usda` – Rigid bodies, physics materials, gravity settings  
- `Articulation_LYR.usda` – Robot joints, articulation roots, joint limits  
- `Sensors_LYR.usda` – Camera, LiDAR, IMU, and other sensor definitions

> Visual layers (layout, materials, variants) live in `030_LYR_USD/`.  
> Simulation logic lives here in `040_LYR_SIM/` to keep concerns separated.

## Usage

1. Create a new `.usda` file in this folder with a descriptive name ending in `_LYR`.
2. Add it to the `subLayers` array in `Asset_ROOT.usda` / `GoodStart_ROOT.usda` **above** `AssetImport_LYR.usda`.
3. Author simulation properties using USD physics and robotics schemas (see Chapter 11 of the Best Practices Guide).

## Best Practices

- Keep **geometry** in payloads in `010_ASS_USD/`, not in simulation layers.
- Use `040_LYR_SIM/` only for:
  - Physics APIs (`PhysicsRigidBodyAPI`, `PhysicsCollisionAPI`, `PhysicsMaterialAPI`, `ArticulationRootAPI`, joints).
  - Sensor APIs (camera, LiDAR, IMU, etc.).
- Keep sim layers modular:
  - One layer for collisions,
  - One for joints,
  - One for sensors, etc., when helpful.
- Always use **relative paths** when referencing assets from this folder.


