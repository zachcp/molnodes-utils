#!/usr/bin/env python
"""Script showing the basics of using BlenderSynth"""

import bpy
import blendersynth as bsyn
from blendersynth.run.load_blend import load_blend
import molecularnodes
from molecularnodes.entities.molecule.ui import load_local, fetch


def load_MN(blend_file_path =  "./assets/MN_data_file_4.2.blend"):
    bpy.ops.wm.open_mainfile(filepath=blend_file_path)
    bpy.utils.refresh_script_paths()
    bpy.context.scene.render.engine = 'CYCLES'
    # remove the cube
    objs = bpy.data.objects
    objs.remove(objs["StorageCube"], do_unlink=True)


bsyn.run_this_script(open_blender=False)  # If called from Python, this will run the current script in Blender
#bsyn.world.set_color((0.8, 0.7, 0.8))

molecularnodes.register()
load_MN()

#mol = load_local("/Users/zcpowers/Desktop/molnodes/assets/1BNA.pdb", name="1BNA").create_object("1BNA")
mol =  fetch("1FAP", style="cartoon").create_object("1FAP")
#mol.scale[0] = 3
#mol.scale[1] = 3
#mol.scale[2] = 3


camera = bsyn.Camera()

# camera.look_at_object(mol)
# camera.set_scale(2.0)
# look at the molcule
camera.location *= 0.5
#bsyn.camera.zoom_out(factor=2)

comp = bsyn.Compositor()  # Create a new compositor - this manages all the render layers
# Generate some basic scene components. Alternatively, use bsyn.load_blend to load a .blend file
light = bsyn.Light.create('POINT', location=(0, -5, 0), intensity=100)  # Create a new light
# Set some render settings
bsyn.render.set_cycles_samples(10)
bsyn.render.set_resolution(512, 512)
# bsyn.render.set_transparent()
comp.define_output('Image', directory='outputs/quickstart', file_name='rgb')  # render RGB layer
comp.render()  # render the result
