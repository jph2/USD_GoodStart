Those URLs (Pixar USD docs, OpenUSD, and the old Omniverse connectors marketing page) have either moved into the new OpenUSD / Learn OpenUSD site structure or into newer Omniverse docs. You can fix your “dead links” by pointing to the current equivalents below.[1][2][3][4]

## Replacements for each dead link

- **Old:** `https://www.nvidia.com/en-us/omniverse/connectors/` → 404  
  **Use instead (technical connectors info):**  
  - Omniverse connectors overview and download in NGC catalog:  
    `https://catalog.ngc.nvidia.com/orgs/nvidia/teams/omniverse/collections/omni_connectors`[1]
  - Or, for documentation: Omniverse Connect “Third Party Connectors”:  
    `https://docs.omniverse.nvidia.com/connect/latest/3rd-party-connectors.html`[5]

- **Old:** `https://graphics.pixar.com/usd/release/api/_usd__page__composition__arch.html#Usd_Page_Composition_Arcs_Sublayers` → 403  
  **Use instead (sublayers in current Learn OpenUSD docs):**  
  - `https://docs.nvidia.com/learn-openusd/latest/creating-composition-arcs/sublayers/what-are-sublayers.html`[2]
  - Entry page for composition arcs:  
    `https://docs.nvidia.com/learn-openusd/latest/creating-composition-arcs/index.html`[3]

- **Old:** `https://graphics.pixar.com/usd/release/api/_usd__page__value_resolution.html` → 403  
  **Use instead (value resolution in Learn OpenUSD):**  
  - `https://docs.nvidia.com/learn-openusd/latest/beyond-basics/value-resolution.html`[4]

- **Old:** `https://openusd.com/` → Status 0 (likely blocked / redirected in your checker)  
  **Use instead (stable entry point you can link to):**  
  - Explainer for OpenUSD on AOUSD site:  
    `https://aousd.org/blog/explainer-series-what-is-openusd/`[6]
  - Or the general Learn OpenUSD portal:  
    `https://docs.nvidia.com/learn-openusd/latest/`[3]

## Suggested updated snippet for your doc

In your `OpenUSD_Best_Practices_Guide` file, replace the broken links with:

- Connectors: `https://catalog.ngc.nvidia.com/orgs/nvidia/teams/omniverse/collections/omni_connectors` or `https://docs.omniverse.nvidia.com/connect/latest/3rd-party-connectors.html`.[5][1]
- Sublayers / composition arcs: `https://docs.nvidia.com/learn-openusd/latest/creating-composition-arcs/sublayers/what-are-sublayers.html`.[2]
- Value resolution: `https://docs.nvidia.com/learn-openusd/latest/beyond-basics/value-resolution.html`.[4]
- OpenUSD home / intro: `https://docs.nvidia.com/learn-openusd/latest/` or `https://aousd.org/blog/explainer-series-what-is-openusd/`.[6][3]

[1](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/omniverse/collections/omni_connectors)
[2](https://docs.nvidia.com/learn-openusd/latest/creating-composition-arcs/sublayers/what-are-sublayers.html)
[3](https://docs.nvidia.com/learn-openusd/latest/creating-composition-arcs/index.html)
[4](https://docs.nvidia.com/learn-openusd/latest/beyond-basics/value-resolution.html)
[5](https://docs.omniverse.nvidia.com/connect/latest/3rd-party-connectors.html)
[6](https://aousd.org/blog/explainer-series-what-is-openusd/)
[7](https://aousd.org/blog/announcing-openusd-v25-05-key-features-and-improvements/)
[8](https://github.com/PixarAnimationStudios/OpenUSD/blob/dev/CHANGELOG.md)
[9](https://docs.omniverse.nvidia.com/connect/latest/blender/nucleus-connector.html)
[10](https://github.com/NVIDIA-Omniverse/connect-samples)




Omniverse and Siemens Tecnomatix Plant Simulation are integrated via a dedicated Tecnomatix–Omniverse connector that exports geometry and simulation studies into OpenUSD and can maintain a live, synchronized link between the tools. Plant Simulation itself does not natively “speak OpenUSD” in the sense of direct USD file authoring; instead, USD is used on the Omniverse side as the scene and data representation that the connector publishes into.[1][3][7]

## What the integration is

Siemens offers a “Tecnomatix Connector for NVIDIA Omniverse” as an add‑on for Process Simulate X and Plant Simulation X. Key capabilities are:[1]

- Export of study and model geometry from Plant Simulation / Process Simulate into Omniverse for high‑end visualization and collaboration.[1]
- Export of simulation runs (discrete‑event behavior, motions, etc.) so that simulations can be run or replayed inside Omniverse experiences.[4][1]
- A live connection mode in which changes or running simulations in Plant Simulation are reflected immediately in Omniverse, enabling synchronized views of the digital twin.[3][1]

From the Siemens side this is positioned as part of the Tecnomatix / Xcelerator portfolio, and from the NVIDIA side as an OpenUSD‑based industrial metaverse workflow where Omniverse connects multiple Siemens tools (Teamcenter, NX, Tecnomatix, etc.).[5][7]

## How exchange typically works

Conceptually, the connector workflow looks like this:

- Plant Simulation / Process Simulate holds the manufacturing model and the discrete‑event or process logic, remaining the “system of record” for process behavior.[3][1]
- The connector publishes geometry, layout, and state from these tools into an Omniverse Nucleus server, where they become OpenUSD scenes that can be opened in Omniverse apps (for example, Composer).[7][1]
- For live mode, the connector streams updates (positions, states, KPIs) during simulation runs so that Omniverse can visualize them in real time; Omniverse is responsible for photoreal rendering, physics‑based visualization, and potentially additional simulation layers.[7][3][1]

Round‑trip editing is more limited: current material emphasizes “operate on it and make changes” in Omniverse and then update the study, but the primary direction is Plant Simulation → Omniverse for visualization and analysis rather than full bidirectional process authoring.[1]

## What Plant Simulation supports regarding OpenUSD

Plant Simulation X does not expose OpenUSD as a first‑class public file format; the OpenUSD integration is realized through the Tecnomatix–Omniverse connector. In practice this means:[1]

- You configure and run your models in Plant Simulation X; the connector translates models and simulation studies into an Omniverse‑compatible representation based on USD.[3][1]
- The OpenUSD structure (layers, prim hierarchy, metadata) is primarily managed by the connector and Omniverse; Siemens material highlights Omniverse’s OpenUSD‑based digital twin and uses the connector as the bridge rather than asking Plant Simulation users to work directly with USD.[7]

Recent Plant Simulation user conference material explicitly calls out the combination of NVIDIA Omniverse and Plant Simulation as an emerging standard pattern for 3D visualization and integration, with OpenUSD and Omniverse providing the scalable visualization and data‑fusion layer over Tecnomatix process models.[3][7]

## Practical evaluation / best‑practice takeaways

For an industrial digital‑twin pipeline:

- Treat Plant Simulation / Process Simulate as the authoritative source for process logic and discrete‑event behavior, and Omniverse (OpenUSD) as the authoritative source for 3D scene aggregation, high‑fidelity visualization, and additional analytics or AI layers.[7][1]
- Use the Tecnomatix–Omniverse connector (rather than ad‑hoc exports) whenever you need ongoing synchronization or live simulation visualization; it is explicitly designed for “live connection” and industrial‑metaverse scenarios.[3][1]
- Structure your USD side (once in Omniverse) according to OpenUSD asset‑structure and layering best practices, and treat Plant Simulation‑origin layers as one data domain among others (for example, combining them with CAD, PLC/OPC UA, AAS layers) in the same USD stage.[7]

Today, the “OpenUSD support” you get is therefore: Plant Simulation X can participate in an OpenUSD‑centric digital twin via the Tecnomatix connector, rather than Plant Simulation itself being a general USD DCC.

[1](https://plm.sw.siemens.com/en-US/tecnomatix/products/tecnomatix-connector-nvidia-omniverse/)
[2](https://forums.developer.nvidia.com/t/omniverse-connector-for-siemens-plant-simulation-and-process-simulate/241952)
[3](https://blogs.sw.siemens.com/tecnomatix/plant-simulation-user-conference-2025-recap-python-integration-ai-industrial-metaverse-and-more/)
[4](https://www.youtube.com/watch?v=sk-2dJIR5R8)
[5](https://www.youtube.com/watch?v=s_INA4ChbmI)
[6](https://www.rcrwireless.com/20211115/internet-of-things/siemens-energy-to-use-nvidia-omniverse-platform-for-predictive-maintenance)
[7](https://www.youtube.com/watch?v=t6ppwWZUSEc)
[8](https://forums.developer.nvidia.com/t/omniverse-and-tecnomatix-plant-simulation-and-tecnomatix-process-simulate/248715)
[9](https://plant-simulation.de/umstellung-auf-3d-in-plant-simulation/)
[10](https://www.youtube.com/watch?v=UO0GaY8WLW8)





Omniverse and Siemens Tecnomatix Plant Simulation are integrated via a dedicated Tecnomatix–Omniverse connector that exports geometry and simulation studies into OpenUSD and can maintain a live, synchronized link between the tools. Plant Simulation itself does not natively “speak OpenUSD” in the sense of direct USD file authoring; instead, USD is used on the Omniverse side as the scene and data representation that the connector publishes into.[1][3][7]

## What the integration is

Siemens offers a “Tecnomatix Connector for NVIDIA Omniverse” as an add‑on for Process Simulate X and Plant Simulation X. Key capabilities are:[1]

- Export of study and model geometry from Plant Simulation / Process Simulate into Omniverse for high‑end visualization and collaboration.[1]
- Export of simulation runs (discrete‑event behavior, motions, etc.) so that simulations can be run or replayed inside Omniverse experiences.[4][1]
- A live connection mode in which changes or running simulations in Plant Simulation are reflected immediately in Omniverse, enabling synchronized views of the digital twin.[3][1]

From the Siemens side this is positioned as part of the Tecnomatix / Xcelerator portfolio, and from the NVIDIA side as an OpenUSD‑based industrial metaverse workflow where Omniverse connects multiple Siemens tools (Teamcenter, NX, Tecnomatix, etc.).[5][7]

## How exchange typically works

Conceptually, the connector workflow looks like this:

- Plant Simulation / Process Simulate holds the manufacturing model and the discrete‑event or process logic, remaining the “system of record” for process behavior.[3][1]
- The connector publishes geometry, layout, and state from these tools into an Omniverse Nucleus server, where they become OpenUSD scenes that can be opened in Omniverse apps (for example, Composer).[7][1]
- For live mode, the connector streams updates (positions, states, KPIs) during simulation runs so that Omniverse can visualize them in real time; Omniverse is responsible for photoreal rendering, physics‑based visualization, and potentially additional simulation layers.[7][3][1]

Round‑trip editing is more limited: current material emphasizes “operate on it and make changes” in Omniverse and then update the study, but the primary direction is Plant Simulation → Omniverse for visualization and analysis rather than full bidirectional process authoring.[1]

## What Plant Simulation supports regarding OpenUSD

Plant Simulation X does not expose OpenUSD as a first‑class public file format; the OpenUSD integration is realized through the Tecnomatix–Omniverse connector. In practice this means:[1]

- You configure and run your models in Plant Simulation X; the connector translates models and simulation studies into an Omniverse‑compatible representation based on USD.[3][1]
- The OpenUSD structure (layers, prim hierarchy, metadata) is primarily managed by the connector and Omniverse; Siemens material highlights Omniverse’s OpenUSD‑based digital twin and uses the connector as the bridge rather than asking Plant Simulation users to work directly with USD.[7]

Recent Plant Simulation user conference material explicitly calls out the combination of NVIDIA Omniverse and Plant Simulation as an emerging standard pattern for 3D visualization and integration, with OpenUSD and Omniverse providing the scalable visualization and data‑fusion layer over Tecnomatix process models.[3][7]

## Practical evaluation / best‑practice takeaways

For an industrial digital‑twin pipeline:

- Treat Plant Simulation / Process Simulate as the authoritative source for process logic and discrete‑event behavior, and Omniverse (OpenUSD) as the authoritative source for 3D scene aggregation, high‑fidelity visualization, and additional analytics or AI layers.[7][1]
- Use the Tecnomatix–Omniverse connector (rather than ad‑hoc exports) whenever you need ongoing synchronization or live simulation visualization; it is explicitly designed for “live connection” and industrial‑metaverse scenarios.[3][1]
- Structure your USD side (once in Omniverse) according to OpenUSD asset‑structure and layering best practices, and treat Plant Simulation‑origin layers as one data domain among others (for example, combining them with CAD, PLC/OPC UA, AAS layers) in the same USD stage.[7]

Today, the “OpenUSD support” you get is therefore: Plant Simulation X can participate in an OpenUSD‑centric digital twin via the Tecnomatix connector, rather than Plant Simulation itself being a general USD DCC.

[1](https://plm.sw.siemens.com/en-US/tecnomatix/products/tecnomatix-connector-nvidia-omniverse/)
[2](https://forums.developer.nvidia.com/t/omniverse-connector-for-siemens-plant-simulation-and-process-simulate/241952)
[3](https://blogs.sw.siemens.com/tecnomatix/plant-simulation-user-conference-2025-recap-python-integration-ai-industrial-metaverse-and-more/)
[4](https://www.youtube.com/watch?v=sk-2dJIR5R8)
[5](https://www.youtube.com/watch?v=s_INA4ChbmI)
[6](https://www.rcrwireless.com/20211115/internet-of-things/siemens-energy-to-use-nvidia-omniverse-platform-for-predictive-maintenance)
[7](https://www.youtube.com/watch?v=t6ppwWZUSEc)
[8](https://forums.developer.nvidia.com/t/omniverse-and-tecnomatix-plant-simulation-and-tecnomatix-process-simulate/248715)
[9](https://plant-simulation.de/umstellung-auf-3d-in-plant-simulation/)
[10](https://www.youtube.com/watch?v=UO0GaY8WLW8)




Omniverse and Siemens Tecnomatix Plant Simulation are integrated via a dedicated Tecnomatix–Omniverse connector that exports geometry and simulation studies into OpenUSD and can maintain a live, synchronized link between the tools. Plant Simulation itself does not natively “speak OpenUSD” in the sense of direct USD file authoring; instead, USD is used on the Omniverse side as the scene and data representation that the connector publishes into.[1][3][7]

## What the integration is

Siemens offers a “Tecnomatix Connector for NVIDIA Omniverse” as an add‑on for Process Simulate X and Plant Simulation X. Key capabilities are:[1]

- Export of study and model geometry from Plant Simulation / Process Simulate into Omniverse for high‑end visualization and collaboration.[1]
- Export of simulation runs (discrete‑event behavior, motions, etc.) so that simulations can be run or replayed inside Omniverse experiences.[4][1]
- A live connection mode in which changes or running simulations in Plant Simulation are reflected immediately in Omniverse, enabling synchronized views of the digital twin.[3][1]

From the Siemens side this is positioned as part of the Tecnomatix / Xcelerator portfolio, and from the NVIDIA side as an OpenUSD‑based industrial metaverse workflow where Omniverse connects multiple Siemens tools (Teamcenter, NX, Tecnomatix, etc.).[5][7]

## How exchange typically works

Conceptually, the connector workflow looks like this:

- Plant Simulation / Process Simulate holds the manufacturing model and the discrete‑event or process logic, remaining the “system of record” for process behavior.[3][1]
- The connector publishes geometry, layout, and state from these tools into an Omniverse Nucleus server, where they become OpenUSD scenes that can be opened in Omniverse apps (for example, Composer).[7][1]
- For live mode, the connector streams updates (positions, states, KPIs) during simulation runs so that Omniverse can visualize them in real time; Omniverse is responsible for photoreal rendering, physics‑based visualization, and potentially additional simulation layers.[7][3][1]

Round‑trip editing is more limited: current material emphasizes “operate on it and make changes” in Omniverse and then update the study, but the primary direction is Plant Simulation → Omniverse for visualization and analysis rather than full bidirectional process authoring.[1]

## What Plant Simulation supports regarding OpenUSD

Plant Simulation X does not expose OpenUSD as a first‑class public file format; the OpenUSD integration is realized through the Tecnomatix–Omniverse connector. In practice this means:[1]

- You configure and run your models in Plant Simulation X; the connector translates models and simulation studies into an Omniverse‑compatible representation based on USD.[3][1]
- The OpenUSD structure (layers, prim hierarchy, metadata) is primarily managed by the connector and Omniverse; Siemens material highlights Omniverse’s OpenUSD‑based digital twin and uses the connector as the bridge rather than asking Plant Simulation users to work directly with USD.[7]

Recent Plant Simulation user conference material explicitly calls out the combination of NVIDIA Omniverse and Plant Simulation as an emerging standard pattern for 3D visualization and integration, with OpenUSD and Omniverse providing the scalable visualization and data‑fusion layer over Tecnomatix process models.[3][7]

## Practical evaluation / best‑practice takeaways

For an industrial digital‑twin pipeline:

- Treat Plant Simulation / Process Simulate as the authoritative source for process logic and discrete‑event behavior, and Omniverse (OpenUSD) as the authoritative source for 3D scene aggregation, high‑fidelity visualization, and additional analytics or AI layers.[7][1]
- Use the Tecnomatix–Omniverse connector (rather than ad‑hoc exports) whenever you need ongoing synchronization or live simulation visualization; it is explicitly designed for “live connection” and industrial‑metaverse scenarios.[3][1]
- Structure your USD side (once in Omniverse) according to OpenUSD asset‑structure and layering best practices, and treat Plant Simulation‑origin layers as one data domain among others (for example, combining them with CAD, PLC/OPC UA, AAS layers) in the same USD stage.[7]

Today, the “OpenUSD support” you get is therefore: Plant Simulation X can participate in an OpenUSD‑centric digital twin via the Tecnomatix connector, rather than Plant Simulation itself being a general USD DCC.

[1](https://plm.sw.siemens.com/en-US/tecnomatix/products/tecnomatix-connector-nvidia-omniverse/)
[2](https://forums.developer.nvidia.com/t/omniverse-connector-for-siemens-plant-simulation-and-process-simulate/241952)
[3](https://blogs.sw.siemens.com/tecnomatix/plant-simulation-user-conference-2025-recap-python-integration-ai-industrial-metaverse-and-more/)
[4](https://www.youtube.com/watch?v=sk-2dJIR5R8)
[5](https://www.youtube.com/watch?v=s_INA4ChbmI)
[6](https://www.rcrwireless.com/20211115/internet-of-things/siemens-energy-to-use-nvidia-omniverse-platform-for-predictive-maintenance)
[7](https://www.youtube.com/watch?v=t6ppwWZUSEc)
[8](https://forums.developer.nvidia.com/t/omniverse-and-tecnomatix-plant-simulation-and-tecnomatix-process-simulate/248715)
[9](https://plant-simulation.de/umstellung-auf-3d-in-plant-simulation/)
[10](https://www.youtube.com/watch?v=UO0GaY8WLW8)




Realtime data is streamed into Omniverse / Isaac Sim / Isaac Lab by having external systems publish data over a protocol or SDK, which is then bound to USD prims and attributes inside a running Kit-based app. The app reacts to those messages (Python, ActionGraph, extensions) and updates the stage in place.

## Core mechanisms in a nutshell

- **Message transport**  
  - Commonly via **ROS / ROS2** (especially for Isaac Sim / Lab robotics workflows).  
  - Also via **custom TCP/UDP/websocket services**, gRPC/REST backends, or field-bus / OPC UA bridges that your extension talks to.  
  - For cloud/enterprise setups, Omniverse Cloud APIs (USD Write / USD Notify / Omniverse Channel) expose an event-style interface so external apps can push changes and subscribe to scene updates in near real time.[4]

- **Binding to the USD stage**  
  - Incoming messages are handled by Omniverse extensions or Isaac components, which map message payloads to **USD paths and attributes** (for example, `/Robot/base_link.xformOp:translate` or `float sensor:temperature`).  
  - Updates run in the Kit event loop: Python callbacks, ActionGraph nodes, or robotics middleware bindings directly write to those attributes, so transforms, states, and metadata change live inside the stage.

- **Streaming visuals vs streaming data**  
  - Visual output (Omniverse or Isaac viewport) is streamed to clients via pixel streaming (WebRTC-based, GDN/streaming client), but this is **frame streaming**, not data streaming.[1][3][7][10]
  - Realtime *data* (commands, telemetry, sensor values) is separate: it flows through ROS2, custom protocols, or Omniverse Cloud APIs into the server, which then mutates the USD; the updated USD is what drives what you see and what downstream consumers can query.[7][4]

## Isaac Sim / Isaac Lab specifics

- Isaac Sim and Isaac Lab ship with **ROS/ROS2 bridges, robot “articulation” components, and sensor publishers**. These let:  
  - External stacks publish joint targets, velocity commands, or sensor inputs; Isaac updates robot prims accordingly in real time.  
  - Isaac publish simulated sensor data (RGB, depth, LiDAR, IMU) back out over ROS2 or other channels for external processing.  
- Under the hood, it is the same pattern: a Kit app with extensions that translate messages ↔ USD attributes, running in a tight physics/render loop so the stage stays synchronized with the data stream.

## Mental model

- Think of Omniverse / Isaac as a **USD scene plus a set of live “adapters”**.  
- Realtime data arrives via your chosen protocol → adapter code decodes it → writes to USD prims → physics/render loop consumes those prim values each frame.  
- In the other direction, you can subscribe to USD changes (file or live stage) or use robotics bridges to stream simulated data out to the rest of your stack.

[1](https://docs.omniverse.nvidia.com/omniverse-dgxc/latest/overview/technical_summary/streaming_technology.html)
[2](https://www.innoactive.io/nvidia-omniverse)
[3](https://docs.omniverse.nvidia.com/avp/latest/index.html)
[4](https://aecmag.com/visualisation/nvidia-to-extend-reach-of-omniverse-with-new-cloud-apis/)
[5](https://forums.developer.nvidia.com/t/how-to-obtain-video-streaming-from-virtual-cameras-in-omniverse/336245)
[6](https://www.algoryx.se/mainpage/wp-content/uploads/2021/04/Thesis-Martin.Vikdahl-Streaming.data_.models.for-distributed.physics.simulation.workflows.pdf)
[7](https://www.nttdata.com/global/en/insights/focus/2023/utilizing-nvidia-omniverse-for-digital-twin-projects-at-the-ntt-data-innovation-center)
[8](https://www.linkedin.com/posts/monkeyway_gdn-omniverse-realtime3dstreaming-activity-7322573483111010306-IqU2)
[9](https://www.youtube.com/watch?v=RbsZ-Qj--2w)
[10](https://www.nvidia.com/en-us/omniverse/)





USD schemas are defined in the core Pixar OpenUSD codebase as declarative `.usda` files that describe custom prim types (typed schemas) or APIs (applied schemas), which are then registered via plugins to enable codegen, validation, and introspection.[1][2][3]

## Where schemas are defined

Schemas live in the USD source tree under `pxr/usd/usd/schemas/` (or similar paths in your build), with built-in ones like `UsdGeomSphereSchema` in files such as `usdGeom/schema.usda`. Custom schemas follow the same structure: you author a `.usda` file that declares the prim type, its properties, metadata, and relationships, then build/register it as a plugin.

## How to define a new schema

1. **Author the schema.usda**: Write a `.usda` file defining your prim or API, specifying `apiSchemas` or `primType` with typed properties (e.g., `float my:custom:value = 1.0 (schemaComment = "My prop")`).[3][1]
2. **Build the plugin**: Place it in a plugin directory, use `usdGenSchema` (older) or just the `.usda` + plugin manifest for codeless schemas (since USD 21.08).[3]
3. **Register**: Set `PXR_PLUGINPATH_NAME` to include your plugin dir; USD auto-discovers and loads schemas at stage open.[2]

Example minimal typed schema:
```
#schema.usda
#usda 1.1
(
    autoApplyApi = "/MyDomain/MySchemaAPI"
)
class "MyPrim" (
    token my:info:purpose = "guide" 
    rel my:target = []
)
```

## Best practices

- **Name namespaces**: Use reverse-domain like `mycompany:domain:prop` to avoid collisions.[5]
- **Prefer codeless schemas** unless you need custom C++ behavior; just `.usda` + plugin is simpler and works everywhere.[3]
- **Single schema per file**, unique names (e.g., `MySchema.schema.usda`); use search paths for includes.[2]
- **Document with metadata**: `schemaComment`, `page`, `hidden`; define defaults and allowed values.[1]
- **Version schemas**: Append version suffixes; deprecate old ones gracefully.

## Pixar, Omniverse, or AOUSD?

- **Pixar core**: The schema system originated in Pixar USD; all official schemas (UsdGeom, UsdShade, etc.) are Pixar-defined in the reference implementation.[4][1]
- **AOUSD**: Alliance for OpenUSD (aousd.org) governs the spec/process but doesn't "own" schemas—it's a standards body promoting Pixar USD upstream.
- **NVIDIA Omniverse**: Ships Pixar schemas + NVIDIA extensions (OmniPxr, Isaac schemas for robots/sensors); you define customs the same way, Omniverse just provides extra tools like schema editors in Kit Composer.[7]

Schemas are a **Pixar USD language feature**—platform-agnostic once registered. Omniverse/others add domain schemas (e.g., IsaacRobot), but the definition mechanism is universal Pixar USD.

[1](https://extra-ordinary.tv/2023/04/11/universal-scene-description-usd-format-from-pixar/)
[2](https://github.com/PixarAnimationStudios/USD/issues/158)
[3](https://remedy-entertainment.github.io/USDBook/terminology/schemas.html)
[4](https://developer.apple.com/videos/play/wwdc2022/10129/)
[5](https://www.sidefx.com/docs/houdini/solaris/usd.html)
[6](https://www.buildingsmart.org/wp-content/uploads/2024/10/2024-08-30-IFC-and-USD-clean.pdf)
[7](https://developer.apple.com/documentation/usd/usd-schemas-for-ar)
[8](https://rystorm.com/blog/i-would-like-usd-to-succeed)




You do not need schemas to add arbitrary metadata to USD prims; you can directly author custom attributes using prefixed names (e.g., `float opcua:runtime:temperature = 55.0`) anywhere in your USD files or stages.

## When you don't need schemas

For simple data injection or prototyping, raw custom attributes work fine:

- Just write `namespace:domain:property = value` on any prim. USD treats these as generic `token`, `float`, etc., with no validation or special behavior.
- Perfect for quick integration (OPC UA data, AAS metadata, runtime states) where you control both writer and reader.
- No plugin registration, no codegen—pure data authoring.

Your earlier examples (`opcua:runtime:temperature`, `aas:submodel:identification`) are exactly this: ad-hoc prefixed attributes without schemas.

## When and why you need schemas

Schemas become necessary when you want **structure, tooling, and guarantees** beyond raw attributes:

- **Validation and discovery**: Schemas define allowed types, ranges, defaults, and relationships (e.g., `opcua:runtime:temperature` must be `float >= 0`). Tools can validate, auto-complete, and query them.
- **Introspection and traversal**: `UsdSchema` APIs let you discover all `Pump` prims with your `OpcUaRuntimeSchema` applied, or enumerate properties programmatically.
- **UI and editors**: Omniverse Composer, USDView, or custom apps show schema properties in structured panels with previews, not as generic "unknown attributes".
- **Composition safety**: Schemas enable `autoApplyApi` (automatic application to matching prims) and typed inheritance.
- **Interoperability**: Downstream consumers (other teams, apps) understand your data model without reverse-engineering prefixes.

## Benefits in practice

| Use Case | Raw Attributes | Schemas |
|----------|----------------|---------|
| **Quick prototypes** | ✅ Simple, no setup | ❌ Overhead |
| **Team workflows** | ⚠️ Brittle naming | ✅ Structured discovery |
| **Tool integration** | ❌ No UI/validation | ✅ Editors recognize properties |
| **Large pipelines** | ⚠️ Manual prefix discipline | ✅ Enforced contracts |
| **External consumers** | ❌ Documentation needed | ✅ Self-describing via metadata |

## Best practice decision tree

- **Use raw attributes if**: Single team, simple data, full control over readers/writers, prototyping.
- **Define schemas if**: Multiple teams/tools, need validation/UI, want programmatic access (`GetMySchemaAttr()`), plan to distribute (plugins/extensions), or data model stabilizes.

**Hybrid pattern** (most common): Start with raw prefixed attributes for speed, promote to schemas once the properties stabilize and you need tooling. Your OPC UA/AAS layers can stay raw attributes; only schema-ify if you build a `PumpRuntimeSchema` that multiple apps consume.

Schemas are **optional structure on top of the generic attribute system**—not required for data integration, but essential for production pipelines with tooling and collaboration.

[1](https://aecmag.com/features/usd-and-the-aec-industry/)
[2](https://www.buildingsmart.org/wp-content/uploads/2024/10/2024-08-30-IFC-and-USD-clean.pdf)
[3](https://aousd.org/blog/explainer-series-for-developers-what-are-openusd-schemas/)
[4](https://developer.apple.com/br/videos/play/wwdc2022/10129/)
[5](https://yelzkizi.org/open-usd-3d-workflows/)
[6](https://docs.omniverse.nvidia.com/usd/latest/usd_schemas.html)
[7](https://www.sidefx.com/docs/houdini/solaris/usd.html)
[8](https://cgrebel.com/2023/02/adopting-universal-scene-description/)



