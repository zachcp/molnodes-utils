import bpy
import mathutils
import molecularnodes
import molnodes

# register molecular nodes
try:
    molecularnodes.register()
except:
    pass
try:
    molnodes.register()
except:
    pass


from . import wiggle

wiggle.register()


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


# import .wiggle as wiggle
# usernodes.load_pdb("1FAP")
# usernodes.set_camera(1.5) # try this a few different times
# import blendersynth as bsyn
