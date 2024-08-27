bl_info = {
	"name" : ".MN_utils_bio_assembly",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class _MN_utils_bio_assembly(bpy.types.Operator):
	bl_idname = "node._mn_utils_bio_assembly"
	bl_label = ".MN_utils_bio_assembly"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_utils_bio_assembly node group
		def _mn_utils_bio_assembly_node_group():
			_mn_utils_bio_assembly = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_utils_bio_assembly")

			_mn_utils_bio_assembly.color_tag = 'NONE'
			_mn_utils_bio_assembly.description = ""

			_mn_utils_bio_assembly.is_modifier = True
			
			#_mn_utils_bio_assembly interface
			#Socket Instances
			instances_socket = _mn_utils_bio_assembly.interface.new_socket(name = "Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			instances_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket = _mn_utils_bio_assembly.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket RotTransMat
			rottransmat_socket = _mn_utils_bio_assembly.interface.new_socket(name = "RotTransMat", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			rottransmat_socket.attribute_domain = 'POINT'
			
			#Socket Scale Rotation
			scale_rotation_socket = _mn_utils_bio_assembly.interface.new_socket(name = "Scale Rotation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_rotation_socket.default_value = 1.0
			scale_rotation_socket.min_value = -10000.0
			scale_rotation_socket.max_value = 10000.0
			scale_rotation_socket.subtype = 'NONE'
			scale_rotation_socket.attribute_domain = 'POINT'
			
			#Socket Scale Translation
			scale_translation_socket = _mn_utils_bio_assembly.interface.new_socket(name = "Scale Translation", in_out='INPUT', socket_type = 'NodeSocketFloat')
			scale_translation_socket.default_value = 1.0
			scale_translation_socket.min_value = -10000.0
			scale_translation_socket.max_value = 10000.0
			scale_translation_socket.subtype = 'NONE'
			scale_translation_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_utils_bio_assembly nodes
			#node Frame.001
			frame_001 = _mn_utils_bio_assembly.nodes.new("NodeFrame")
			frame_001.label = "Handle the Instances"
			frame_001.name = "Frame.001"
			frame_001.label_size = 20
			frame_001.shrink = True
			
			#node Frame
			frame = _mn_utils_bio_assembly.nodes.new("NodeFrame")
			frame.label = "Transfer and Scale th e Rotations and Transformations"
			frame.name = "Frame"
			frame.label_size = 20
			frame.shrink = True
			
			#node Group Output
			group_output = _mn_utils_bio_assembly.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Reroute.002
			reroute_002 = _mn_utils_bio_assembly.nodes.new("NodeReroute")
			reroute_002.name = "Reroute.002"
			#node Named Attribute.001
			named_attribute_001 = _mn_utils_bio_assembly.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'FLOAT_VECTOR'
			#Name
			named_attribute_001.inputs[0].default_value = "rot"
			
			#node Reroute.001
			reroute_001 = _mn_utils_bio_assembly.nodes.new("NodeReroute")
			reroute_001.name = "Reroute.001"
			#node Domain Size
			domain_size = _mn_utils_bio_assembly.nodes.new("GeometryNodeAttributeDomainSize")
			domain_size.name = "Domain Size"
			domain_size.component = 'POINTCLOUD'
			
			#node Geometry to Instance
			geometry_to_instance = _mn_utils_bio_assembly.nodes.new("GeometryNodeGeometryToInstance")
			geometry_to_instance.name = "Geometry to Instance"
			
			#node Group Input
			group_input = _mn_utils_bio_assembly.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Reroute
			reroute = _mn_utils_bio_assembly.nodes.new("NodeReroute")
			reroute.name = "Reroute"
			#node Duplicate Elements
			duplicate_elements = _mn_utils_bio_assembly.nodes.new("GeometryNodeDuplicateElements")
			duplicate_elements.name = "Duplicate Elements"
			duplicate_elements.domain = 'INSTANCE'
			#Selection
			duplicate_elements.inputs[1].default_value = True
			
			#node Sample Index.001
			sample_index_001 = _mn_utils_bio_assembly.nodes.new("GeometryNodeSampleIndex")
			sample_index_001.name = "Sample Index.001"
			sample_index_001.clamp = True
			sample_index_001.data_type = 'FLOAT_VECTOR'
			sample_index_001.domain = 'POINT'
			
			#node Index.001
			index_001 = _mn_utils_bio_assembly.nodes.new("GeometryNodeInputIndex")
			index_001.name = "Index.001"
			
			#node Index
			index = _mn_utils_bio_assembly.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			#node Position
			position = _mn_utils_bio_assembly.nodes.new("GeometryNodeInputPosition")
			position.name = "Position"
			
			#node Sample Index
			sample_index = _mn_utils_bio_assembly.nodes.new("GeometryNodeSampleIndex")
			sample_index.name = "Sample Index"
			sample_index.clamp = True
			sample_index.data_type = 'FLOAT_VECTOR'
			sample_index.domain = 'POINT'
			
			#node Vector Math.001
			vector_math_001 = _mn_utils_bio_assembly.nodes.new("ShaderNodeVectorMath")
			vector_math_001.name = "Vector Math.001"
			vector_math_001.operation = 'SCALE'
			
			#node Reroute.005
			reroute_005 = _mn_utils_bio_assembly.nodes.new("NodeReroute")
			reroute_005.name = "Reroute.005"
			#node Vector Math
			vector_math = _mn_utils_bio_assembly.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'SCALE'
			
			#node Reroute.003
			reroute_003 = _mn_utils_bio_assembly.nodes.new("NodeReroute")
			reroute_003.name = "Reroute.003"
			#node Rotate Instances
			rotate_instances = _mn_utils_bio_assembly.nodes.new("GeometryNodeRotateInstances")
			rotate_instances.name = "Rotate Instances"
			#Selection
			rotate_instances.inputs[1].default_value = True
			#Pivot Point
			rotate_instances.inputs[3].default_value = (0.0, 0.0, 0.0)
			#Local Space
			rotate_instances.inputs[4].default_value = True
			
			#node Translate Instances
			translate_instances = _mn_utils_bio_assembly.nodes.new("GeometryNodeTranslateInstances")
			translate_instances.name = "Translate Instances"
			#Selection
			translate_instances.inputs[1].default_value = True
			#Local Space
			translate_instances.inputs[3].default_value = False
			
			
			
			#Set parents
			reroute_002.parent = frame
			named_attribute_001.parent = frame
			reroute_001.parent = frame
			domain_size.parent = frame_001
			geometry_to_instance.parent = frame_001
			group_input.parent = frame_001
			reroute.parent = frame_001
			duplicate_elements.parent = frame_001
			sample_index_001.parent = frame
			index_001.parent = frame
			index.parent = frame
			position.parent = frame
			sample_index.parent = frame
			vector_math_001.parent = frame
			reroute_005.parent = frame
			vector_math.parent = frame
			reroute_003.parent = frame
			rotate_instances.parent = frame_001
			translate_instances.parent = frame_001
			
			#Set locations
			frame_001.location = (-30.0, 10.0)
			frame.location = (101.3235855102539, -114.33607482910156)
			group_output.location = (1200.7205810546875, 342.195556640625)
			reroute_002.location = (50.0, -590.0)
			named_attribute_001.location = (-110.0, -470.0)
			reroute_001.location = (-270.0, -590.0)
			domain_size.location = (-670.0, 210.0)
			geometry_to_instance.location = (-670.0, 310.0)
			group_input.location = (-1010.0, 90.0)
			reroute.location = (-750.0, 50.0)
			duplicate_elements.location = (-350.0, 250.0)
			sample_index_001.location = (-110.0, -250.0)
			index_001.location = (-301.3235778808594, -365.6639404296875)
			index.location = (78.6764144897461, -525.6639404296875)
			position.location = (78.6764144897461, -465.6639404296875)
			sample_index.location = (78.6764144897461, -245.66392517089844)
			vector_math_001.location = (78.6764144897461, -105.66392517089844)
			reroute_005.location = (58.676414489746094, -245.66392517089844)
			vector_math.location = (-121.3235855102539, -105.66392517089844)
			reroute_003.location = (-121.3235855102539, -245.66392517089844)
			rotate_instances.location = (50.0, 210.0)
			translate_instances.location = (230.0, 210.0)
			
			#Set dimensions
			frame_001.width, frame_001.height = 1440.0, 428.0
			frame.width, frame.height = 580.0, 558.3360595703125
			group_output.width, group_output.height = 140.0, 100.0
			reroute_002.width, reroute_002.height = 16.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			reroute_001.width, reroute_001.height = 16.0, 100.0
			domain_size.width, domain_size.height = 140.0, 100.0
			geometry_to_instance.width, geometry_to_instance.height = 160.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			reroute.width, reroute.height = 16.0, 100.0
			duplicate_elements.width, duplicate_elements.height = 140.0, 100.0
			sample_index_001.width, sample_index_001.height = 140.0, 100.0
			index_001.width, index_001.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			position.width, position.height = 140.0, 100.0
			sample_index.width, sample_index.height = 140.0, 100.0
			vector_math_001.width, vector_math_001.height = 140.0, 100.0
			reroute_005.width, reroute_005.height = 16.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			reroute_003.width, reroute_003.height = 16.0, 100.0
			rotate_instances.width, rotate_instances.height = 140.0, 100.0
			translate_instances.width, translate_instances.height = 140.0, 100.0
			
			#initialize _mn_utils_bio_assembly links
			#geometry_to_instance.Instances -> duplicate_elements.Geometry
			_mn_utils_bio_assembly.links.new(geometry_to_instance.outputs[0], duplicate_elements.inputs[0])
			#reroute.Output -> domain_size.Geometry
			_mn_utils_bio_assembly.links.new(reroute.outputs[0], domain_size.inputs[0])
			#domain_size.Point Count -> duplicate_elements.Amount
			_mn_utils_bio_assembly.links.new(domain_size.outputs[0], duplicate_elements.inputs[2])
			#duplicate_elements.Geometry -> rotate_instances.Instances
			_mn_utils_bio_assembly.links.new(duplicate_elements.outputs[0], rotate_instances.inputs[0])
			#reroute_001.Output -> sample_index_001.Geometry
			_mn_utils_bio_assembly.links.new(reroute_001.outputs[0], sample_index_001.inputs[0])
			#named_attribute_001.Attribute -> sample_index_001.Value
			_mn_utils_bio_assembly.links.new(named_attribute_001.outputs[0], sample_index_001.inputs[1])
			#reroute_002.Output -> sample_index.Geometry
			_mn_utils_bio_assembly.links.new(reroute_002.outputs[0], sample_index.inputs[0])
			#position.Position -> sample_index.Value
			_mn_utils_bio_assembly.links.new(position.outputs[0], sample_index.inputs[1])
			#vector_math_001.Vector -> translate_instances.Translation
			_mn_utils_bio_assembly.links.new(vector_math_001.outputs[0], translate_instances.inputs[2])
			#rotate_instances.Instances -> translate_instances.Instances
			_mn_utils_bio_assembly.links.new(rotate_instances.outputs[0], translate_instances.inputs[0])
			#translate_instances.Instances -> group_output.Instances
			_mn_utils_bio_assembly.links.new(translate_instances.outputs[0], group_output.inputs[0])
			#group_input.RotTransMat -> reroute.Input
			_mn_utils_bio_assembly.links.new(group_input.outputs[1], reroute.inputs[0])
			#reroute.Output -> reroute_001.Input
			_mn_utils_bio_assembly.links.new(reroute.outputs[0], reroute_001.inputs[0])
			#reroute_001.Output -> reroute_002.Input
			_mn_utils_bio_assembly.links.new(reroute_001.outputs[0], reroute_002.inputs[0])
			#sample_index_001.Value -> vector_math.Vector
			_mn_utils_bio_assembly.links.new(sample_index_001.outputs[0], vector_math.inputs[0])
			#vector_math.Vector -> rotate_instances.Rotation
			_mn_utils_bio_assembly.links.new(vector_math.outputs[0], rotate_instances.inputs[2])
			#sample_index.Value -> vector_math_001.Vector
			_mn_utils_bio_assembly.links.new(sample_index.outputs[0], vector_math_001.inputs[0])
			#group_input.Scale Rotation -> vector_math.Scale
			_mn_utils_bio_assembly.links.new(group_input.outputs[2], vector_math.inputs[3])
			#reroute_005.Output -> vector_math_001.Scale
			_mn_utils_bio_assembly.links.new(reroute_005.outputs[0], vector_math_001.inputs[3])
			#group_input.Geometry -> geometry_to_instance.Geometry
			_mn_utils_bio_assembly.links.new(group_input.outputs[0], geometry_to_instance.inputs[0])
			#reroute_003.Output -> reroute_005.Input
			_mn_utils_bio_assembly.links.new(reroute_003.outputs[0], reroute_005.inputs[0])
			#index_001.Index -> sample_index_001.Index
			_mn_utils_bio_assembly.links.new(index_001.outputs[0], sample_index_001.inputs[2])
			#index.Index -> sample_index.Index
			_mn_utils_bio_assembly.links.new(index.outputs[0], sample_index.inputs[2])
			#group_input.Scale Translation -> reroute_003.Input
			_mn_utils_bio_assembly.links.new(group_input.outputs[3], reroute_003.inputs[0])
			return _mn_utils_bio_assembly

		_mn_utils_bio_assembly = _mn_utils_bio_assembly_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = ".MN_utils_bio_assembly", type = 'NODES')
		mod.node_group = _mn_utils_bio_assembly
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(_MN_utils_bio_assembly.bl_idname)
			
def register():
	bpy.utils.register_class(_MN_utils_bio_assembly)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(_MN_utils_bio_assembly)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
