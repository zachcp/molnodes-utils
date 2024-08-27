bl_info = {
	"name" : "MN_assembly_center",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_assembly_center(bpy.types.Operator):
	bl_idname = "node.mn_assembly_center"
	bl_label = "MN_assembly_center"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize mn_assembly_center node group
		def mn_assembly_center_node_group():
			mn_assembly_center = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_assembly_center")

			mn_assembly_center.color_tag = 'GEOMETRY'
			mn_assembly_center.description = ""

			mn_assembly_center.is_modifier = True
			
			#mn_assembly_center interface
			#Socket Assembly Instances
			assembly_instances_socket = mn_assembly_center.interface.new_socket(name = "Assembly Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			assembly_instances_socket.attribute_domain = 'POINT'
			assembly_instances_socket.description = "The translated assembly"
			
			#Socket Old Centre
			old_centre_socket = mn_assembly_center.interface.new_socket(name = "Old Centre", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			old_centre_socket.default_value = (0.0, 0.0, 0.0)
			old_centre_socket.min_value = -3.4028234663852886e+38
			old_centre_socket.max_value = 3.4028234663852886e+38
			old_centre_socket.subtype = 'NONE'
			old_centre_socket.attribute_domain = 'POINT'
			old_centre_socket.description = "The old centre point of the assembly"
			
			#Socket Transform Vector
			transform_vector_socket = mn_assembly_center.interface.new_socket(name = "Transform Vector", in_out='OUTPUT', socket_type = 'NodeSocketVector')
			transform_vector_socket.default_value = (0.0, 0.0, 0.0)
			transform_vector_socket.min_value = -3.4028234663852886e+38
			transform_vector_socket.max_value = 3.4028234663852886e+38
			transform_vector_socket.subtype = 'NONE'
			transform_vector_socket.attribute_domain = 'POINT'
			transform_vector_socket.description = "The transformation that was applied to the assembly"
			
			#Socket Assembly Instances
			assembly_instances_socket_1 = mn_assembly_center.interface.new_socket(name = "Assembly Instances", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			assembly_instances_socket_1.attribute_domain = 'POINT'
			assembly_instances_socket_1.description = "The instances of an assembly, the result of `MN_assembly`"
			
			#Socket Center
			center_socket = mn_assembly_center.interface.new_socket(name = "Center", in_out='INPUT', socket_type = 'NodeSocketBool')
			center_socket.default_value = True
			center_socket.attribute_domain = 'POINT'
			center_socket.description = "Whether to center the assembly"
			
			#Socket Translation
			translation_socket = mn_assembly_center.interface.new_socket(name = "Translation", in_out='INPUT', socket_type = 'NodeSocketVector')
			translation_socket.default_value = (0.0, 0.0, 0.0)
			translation_socket.min_value = -3.4028234663852886e+38
			translation_socket.max_value = 3.4028234663852886e+38
			translation_socket.subtype = 'TRANSLATION'
			translation_socket.attribute_domain = 'POINT'
			translation_socket.description = "Additional translation to apply to the centered assembly"
			
			
			#initialize mn_assembly_center nodes
			#node Realize Instances
			realize_instances = mn_assembly_center.nodes.new("GeometryNodeRealizeInstances")
			realize_instances.name = "Realize Instances"
			#Selection
			realize_instances.inputs[1].default_value = True
			#Realize All
			realize_instances.inputs[2].default_value = True
			#Depth
			realize_instances.inputs[3].default_value = 0
			
			#node Bounding Box
			bounding_box = mn_assembly_center.nodes.new("GeometryNodeBoundBox")
			bounding_box.name = "Bounding Box"
			
			#node Bounding Box.001
			bounding_box_001 = mn_assembly_center.nodes.new("GeometryNodeBoundBox")
			bounding_box_001.name = "Bounding Box.001"
			
			#node Reroute
			reroute = mn_assembly_center.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Switch
			switch = mn_assembly_center.nodes.new("GeometryNodeSwitch")
			switch.name = "Switch"
			switch.input_type = 'GEOMETRY'
			
			#node Group Output
			group_output = mn_assembly_center.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Mix
			mix = mn_assembly_center.nodes.new("ShaderNodeMix")
			mix.name = "Mix"
			mix.blend_type = 'MIX'
			mix.clamp_factor = True
			mix.clamp_result = False
			mix.data_type = 'VECTOR'
			mix.factor_mode = 'UNIFORM'
			#Factor_Float
			mix.inputs[0].default_value = 0.5
			
			#node Transform
			transform = mn_assembly_center.nodes.new("GeometryNodeTransform")
			transform.name = "Transform"
			transform.mode = 'COMPONENTS'
			#Rotation
			transform.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Vector Math
			vector_math = mn_assembly_center.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SCALE'
			#Scale
			vector_math.inputs[3].default_value = -1.0
			
			#node Group Input
			group_input = mn_assembly_center.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Vector Math.001
			vector_math_001 = mn_assembly_center.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'ADD'
			
			
			
			
			#Set locations
			realize_instances.location = (-251.50982666015625, -44.62482452392578)
			bounding_box.location = (-411.50982666015625, -44.62482452392578)
			bounding_box_001.location = (-91.50982666015625, -44.62482452392578)
			reroute.location = (-381.8795471191406, -19.754844665527344)
			switch.location = (653.526611328125, 204.82861328125)
			group_output.location = (862.0359497070312, 127.03370666503906)
			mix.location = (68.49017333984375, -44.62482452392578)
			transform.location = (498.4442443847656, -47.385963439941406)
			vector_math.location = (240.0, -40.0)
			group_input.location = (-680.0, -160.0)
			vector_math_001.location = (240.0, -180.0)
			
			#Set dimensions
			realize_instances.width, realize_instances.height = 140.0, 100.0
			bounding_box.width, bounding_box.height = 140.0, 100.0
			bounding_box_001.width, bounding_box_001.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			switch.width, switch.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			mix.width, mix.height = 140.0, 100.0
			transform.width, transform.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			
			#initialize mn_assembly_center links
			#group_input.Assembly Instances -> reroute.Input
			mn_assembly_center.links.new(group_input.outputs[0], reroute.inputs[0])
			#reroute.Output -> bounding_box.Geometry
			mn_assembly_center.links.new(reroute.outputs[0], bounding_box.inputs[0])
			#bounding_box.Bounding Box -> realize_instances.Geometry
			mn_assembly_center.links.new(bounding_box.outputs[0], realize_instances.inputs[0])
			#realize_instances.Geometry -> bounding_box_001.Geometry
			mn_assembly_center.links.new(realize_instances.outputs[0], bounding_box_001.inputs[0])
			#bounding_box_001.Min -> mix.A
			mn_assembly_center.links.new(bounding_box_001.outputs[1], mix.inputs[4])
			#bounding_box_001.Max -> mix.B
			mn_assembly_center.links.new(bounding_box_001.outputs[2], mix.inputs[5])
			#mix.Result -> vector_math.Vector
			mn_assembly_center.links.new(mix.outputs[1], vector_math.inputs[0])
			#reroute.Output -> transform.Geometry
			mn_assembly_center.links.new(reroute.outputs[0], transform.inputs[0])
			#transform.Geometry -> switch.True
			mn_assembly_center.links.new(transform.outputs[0], switch.inputs[2])
			#group_input.Assembly Instances -> switch.False
			mn_assembly_center.links.new(group_input.outputs[0], switch.inputs[1])
			#group_input.Center -> switch.Switch
			mn_assembly_center.links.new(group_input.outputs[1], switch.inputs[0])
			#switch.Output -> group_output.Assembly Instances
			mn_assembly_center.links.new(switch.outputs[0], group_output.inputs[0])
			#mix.Result -> group_output.Old Centre
			mn_assembly_center.links.new(mix.outputs[1], group_output.inputs[1])
			#vector_math.Vector -> group_output.Transform Vector
			mn_assembly_center.links.new(vector_math.outputs[0], group_output.inputs[2])
			#vector_math.Vector -> vector_math_001.Vector
			mn_assembly_center.links.new(vector_math.outputs[0], vector_math_001.inputs[0])
			#group_input.Translation -> vector_math_001.Vector
			mn_assembly_center.links.new(group_input.outputs[2], vector_math_001.inputs[1])
			#vector_math_001.Vector -> transform.Translation
			mn_assembly_center.links.new(vector_math_001.outputs[0], transform.inputs[1])
			return mn_assembly_center

		mn_assembly_center = mn_assembly_center_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_assembly_center", type = 'NODES')
		mod.node_group = mn_assembly_center
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_assembly_center.bl_idname)
			
def register():
	bpy.utils.register_class(MN_assembly_center)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_assembly_center)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
