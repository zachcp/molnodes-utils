import bpy
import mathutils
import molecularnodes
import molnodes
import blendersynth as bsyn

# this one has the imports
import usernodes


## Dirty Just Getting it Done
def load_pdb(code):
    bpy.context.scene.MN_pdb_code = code
    bpy.context.scene.MN_import_style = "cartoon"
    bpy.context.scene.MN_import_centre = True
    bpy.ops.mn.import_wwpdb()


def set_camera(distance):
    camera = bpy.context.scene.camera
    camera.location = mathutils.Vector([distance, 0, 0])
    direction = mathutils.Vector([1, 0, 0])
    direction.normalize()
    up = mathutils.Vector([0, 0, 1])
    rotation = direction.to_track_quat("Z", "Y")
    camera.rotation_euler = rotation.to_euler()
    bpy.context.view_layer.update()


def replace_geometry_nodes_modifier(obj, node_group_name):
    existing_modifier = obj.modifiers.get("GeometryNodes")
    if existing_modifier:
        obj.modifiers.remove(existing_modifier)
    modifier = obj.modifiers.new(name="GeometryNodes", type="NODES")
    node_group = bpy.data.node_groups.get(node_group_name)
    if node_group:
        modifier.node_group = node_group
    else:
        print(f"Node group '{node_group_name}' not found")
    return modifier


def increase_lighting():
    # Create a new light if it doesn't exist
    if "Extra_Light" not in bpy.data.objects:
        light_data = bpy.data.lights.new(name="Extra_Light", type="SUN")
        light_object = bpy.data.objects.new(name="Extra_Light", object_data=light_data)
        bpy.context.collection.objects.link(light_object)
    else:
        light_object = bpy.data.objects["Extra_Light"]

    # Set light properties
    light_object.data.energy = 2.0  # Increase this value to make it brighter
    light_object.rotation_euler = (0.785, 0, 0.785)  # Adjust angle as needed

    # If you want to modify existing lights, you can do something like this:
    for obj in bpy.data.objects:
        if obj.type == "LIGHT":
            obj.data.energy *= 1.5  # Increase all light energies by 50%


load_pdb("1FAP")
set_camera(1.2)
increase_lighting()
obj = bpy.data.objects["1FAP"]
nm = obj.modifiers.get("MolecularNodes")
obj.modifiers.remove(nm)
bpy.ops.node.wiggleprot()  # invoke the ops  --> there definitely  a more delicate way here

# render settings

bpy.context.scene.render.engine = "CYCLES"
bpy.context.scene.render.film_transparent = True


comp = bsyn.Compositor()  # Create a new compositor - this manages all the render layers
bsyn.render.set_cycles_samples(10)
bsyn.render.set_resolution(512, 512)
num_frames = 24
comp.define_output("Image", directory="outputs/animation/prot_01", file_name="rgb")
comp.render(animation=True, frame_end=num_frames)

bsyn.file.frames_to_video(
    directory="outputs/animation/prot_01",
    output_loc="outputs/animation/prot_01.gif",
    frame_rate=24,
    delete_images=False,
    output_fmt="gif",
)
