import bpy
import math

# Clear existing objects
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

# Create a cube
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))

# Add a light
light_data = bpy.data.lights.new(name="Light", type="SUN")
light_object = bpy.data.objects.new(name="Light", object_data=light_data)
bpy.context.collection.objects.link(light_object)
light_object.location = (5, 5, 5)

# Add a camera
camera_data = bpy.data.cameras.new(name="Camera")
camera_object = bpy.data.objects.new(name="Camera", object_data=camera_data)
bpy.context.collection.objects.link(camera_object)
camera_object.location = (5, -5, 5)
camera_object.rotation_euler = (math.radians(60), 0, math.radians(45))
bpy.context.scene.camera = camera_object

# Set render settings
bpy.context.scene.render.engine = "CYCLES"
bpy.context.scene.render.resolution_x = 800
bpy.context.scene.render.resolution_y = 600

# Set output path
bpy.context.scene.render.filepath = "./outputs/00_render.png"

# Render
bpy.ops.render.render(write_still=True)
