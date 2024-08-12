#!/usr/bin/env python
"""Script showing the basics of using BlenderSynth"""

import bpy
import blendersynth as bsyn
from blendersynth.run.load_blend import load_blend

# bsyn.run_this_script(open_blender=False)  # If called from Python, this will run the current script in Blender
bsyn.run_this_script(open_blender=True)  # If called from Python, this will run the current script in Blender


# load_blend("assets/MN_data_file_4.2.blend")
f = bpy.ops.wm.open_mainfile(filepath="assets/MN_data_file_4.2.blend")
bpy.context.scene.render.engine = 'CYCLES'


comp = bsyn.Compositor()  # Create a new compositor - this manages all the render layers

# Generate some basic scene components. Alternatively, use bsyn.load_blend to load a .blend file
monkey = bsyn.Mesh.from_primitive('monkey', scale=1, rotation_euler=(0, 0, 0.5))  # Create a new mesh from a primitive
light = bsyn.Light.create('POINT', location=(0, -5, 0), intensity=100)  # Create a new light

# add a basic material
monkey.material = bsyn.Material()
monkey.material.set_bdsf_property("Base Color", (0, 0.8, 0.2, 1))

# Set some render settings
bsyn.render.set_cycles_samples(10)
bsyn.render.set_resolution(256, 256)
bsyn.render.set_transparent()

comp.define_output('Image', directory='outputs/quickstart', file_name='rgb01')  # render RGB layer
comp.render()  # render the result
