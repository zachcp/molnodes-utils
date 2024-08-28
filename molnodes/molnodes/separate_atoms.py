bl_info = {
	"name" : "Separate Atoms",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Separate_Atoms(bpy.types.Operator):
	bl_idname = "node.separate_atoms"
	bl_label = "Separate Atoms"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize separate_atoms node group
		def separate_atoms_node_group():
			separate_atoms = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Separate Atoms")

			separate_atoms.color_tag = 'GEOMETRY'
			separate_atoms.description = ""

			separate_atoms.is_modifier = True
			
			#separate_atoms interface
			#Socket Atoms
			atoms_socket = separate_atoms.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "The selected atoms"
			
			#Socket Inverted
			inverted_socket = separate_atoms.interface.new_socket(name = "Inverted", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			inverted_socket.attribute_domain = 'POINT'
			inverted_socket.description = "The non-selected atoms"
			
			#Socket Index
			index_socket = separate_atoms.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
			index_socket.default_value = 0
			index_socket.min_value = -2147483648
			index_socket.max_value = 2147483647
			index_socket.subtype = 'NONE'
			index_socket.attribute_domain = 'POINT'
			index_socket.description = "Index of the atoms before they were separated"
			
			#Socket Atoms
			atoms_socket_1 = separate_atoms.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			atoms_socket_1.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket = separate_atoms.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = True
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection field for which atoms to separate"
			
			
			#initialize separate_atoms nodes
			#node Group Output
			group_output = separate_atoms.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = separate_atoms.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Capture Attribute
			capture_attribute = separate_atoms.nodes.new("GeometryNodeCaptureAttribute")
			capture_attribute.name = "Capture Attribute"
			capture_attribute.active_index = 0
			capture_attribute.capture_items.clear()
			capture_attribute.capture_items.new('FLOAT', "Value")
			capture_attribute.capture_items["Value"].data_type = 'INT'
			capture_attribute.domain = 'POINT'
			
			#node Separate Geometry
			separate_geometry = separate_atoms.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Index
			index = separate_atoms.nodes.new("GeometryNodeInputIndex")
			index.name = "Index"
			
			
			
			
			#Set locations
			group_output.location = (-140.0, 80.0)
			group_input.location = (-639.2076416015625, 73.4643783569336)
			capture_attribute.location = (-460.0, 80.0)
			separate_geometry.location = (-300.0, 80.0)
			index.location = (-640.0, -40.0)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			capture_attribute.width, capture_attribute.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			index.width, index.height = 140.0, 100.0
			
			#initialize separate_atoms links
			#separate_geometry.Selection -> group_output.Atoms
			separate_atoms.links.new(separate_geometry.outputs[0], group_output.inputs[0])
			#separate_geometry.Inverted -> group_output.Inverted
			separate_atoms.links.new(separate_geometry.outputs[1], group_output.inputs[1])
			#capture_attribute.Geometry -> separate_geometry.Geometry
			separate_atoms.links.new(capture_attribute.outputs[0], separate_geometry.inputs[0])
			#group_input.Atoms -> capture_attribute.Geometry
			separate_atoms.links.new(group_input.outputs[0], capture_attribute.inputs[0])
			#index.Index -> capture_attribute.Value
			separate_atoms.links.new(index.outputs[0], capture_attribute.inputs[1])
			#capture_attribute.Value -> group_output.Index
			separate_atoms.links.new(capture_attribute.outputs[1], group_output.inputs[2])
			#group_input.Selection -> separate_geometry.Selection
			separate_atoms.links.new(group_input.outputs[1], separate_geometry.inputs[1])
			return separate_atoms

		separate_atoms = separate_atoms_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Separate Atoms", type = 'NODES')
		mod.node_group = separate_atoms
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Separate_Atoms.bl_idname)
			
def register():
	bpy.utils.register_class(Separate_Atoms)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Separate_Atoms)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
