#!/usr/bin/env python
"""Simple animation example"""
import blendersynth as bsyn
bsyn.run_this_script()

comp = bsyn.Compositor()  # Create a new compositor - this manages all the render layers

monkey = bsyn.Mesh.from_primitive('monkey')

# Set some render settings
bsyn.render.set_cycles_samples(10)
bsyn.render.set_resolution(512, 512)
num_frames = 100

# Set the 'animation' to be the rotation of the camera
camera = bsyn.Camera()
camera.track_to(monkey)  # look at monkey
circular_path = bsyn.Curve('circle', scale=5, location=(0, 0, 1))
camera.follow_path(circular_path, frames=(0, num_frames), fracs=(0, 0.5))  # set to follow circular path

# Also animate the position, rotation and scale of the monkey
monkey.set_location((0, 0, -2), frame=0)
monkey.set_location((0, 0, 2), frame=num_frames)
monkey.set_scale(1, frame=0)
monkey.set_scale(2, frame=num_frames)
monkey.set_rotation_euler((0, 0, 0), frame=0)
monkey.set_rotation_euler((0, 0, 3.14159/2), frame=num_frames)

# animate camera FOV
camera.set_fov(60, frame=0)
camera.set_fov(120, frame=num_frames)

normal_aov = bsyn.aov.NormalsAOV(ref_frame='CAMERA', polarity=[-1, 1, -1])
monkey.assign_aov(normal_aov)

# Define data outputs
comp.define_output('Image', directory='outputs/animation/rgb', file_name='rgb')
comp.define_output(normal_aov, directory='outputs/animation/normal', file_name='normals')

comp.render(animation=True, frame_end=num_frames)

# convert rendered frames to video
bsyn.file.frames_to_video(directory='outputs/animation/rgb', output_loc='outputs/animation/rgb.gif', frame_rate=24, delete_images=False, output_fmt='gif')
bsyn.file.frames_to_video(directory='outputs/animation/normal', output_loc='outputs/animation/normal.gif', frame_rate=24, delete_images=False, output_fmt='gif')

# combine into one gif for visualisation
bsyn.file.hstack(['outputs/animation/rgb.gif', 'outputs/animation/normal.gif'], 'outputs/animation/animation_output.gif')
