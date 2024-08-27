bl_info = {
	"name" : "Set Color",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Set_Color(bpy.types.Operator):
	bl_idname = "node.set_color"
	bl_label = "Set Color"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize set_color node group
		def set_color_node_group():
			set_color = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Set Color")

			set_color.color_tag = 'GEOMETRY'
			set_color.description = ""

			set_color.is_modifier = True
			
			#set_color interface
			#Socket Atoms
			atoms_socket = set_color.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "Atomic geometry with an updated `Color` attribute"
			
			#Socket Atoms
			atoms_socket_1 = set_color.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			atoms_socket_1.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket = set_color.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = True
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Color
			color_socket = set_color.interface.new_socket(name = "Color", in_out='INPUT', socket_type = 'NodeSocketColor')
			color_socket.default_value = (0.16151699423789978, 0.6239609718322754, 0.19560199975967407, 1.0)
			color_socket.attribute_domain = 'POINT'
			color_socket.description = "Color to apply to the selected atoms"
			
			
			#initialize set_color nodes
			#node Group Input
			group_input = set_color.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Store Named Attribute
			store_named_attribute = set_color.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_COLOR'
			store_named_attribute.domain = 'POINT'
			#Name
			store_named_attribute.inputs[2].default_value = "Color"
			
			#node Group Output
			group_output = set_color.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			
			
			
			#Set locations
			group_input.location = (-460.0, -80.0)
			store_named_attribute.location = (-260.0, -20.0)
			group_output.location = (-100.0, -20.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			
			#initialize set_color links
			#store_named_attribute.Geometry -> group_output.Atoms
			set_color.links.new(store_named_attribute.outputs[0], group_output.inputs[0])
			#group_input.Atoms -> store_named_attribute.Geometry
			set_color.links.new(group_input.outputs[0], store_named_attribute.inputs[0])
			#group_input.Selection -> store_named_attribute.Selection
			set_color.links.new(group_input.outputs[1], store_named_attribute.inputs[1])
			#group_input.Color -> store_named_attribute.Value
			set_color.links.new(group_input.outputs[2], store_named_attribute.inputs[3])
			return set_color

		set_color = set_color_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Set Color", type = 'NODES')
		mod.node_group = set_color
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Set_Color.bl_idname)
			
def register():
	bpy.utils.register_class(Set_Color)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Set_Color)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
