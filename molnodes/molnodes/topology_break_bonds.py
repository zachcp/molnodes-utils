bl_info = {
	"name" : "Topology Break Bonds",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Topology_Break_Bonds(bpy.types.Operator):
	bl_idname = "node.topology_break_bonds"
	bl_label = "Topology Break Bonds"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize _mn_world_scale node group
		def _mn_world_scale_node_group():
			_mn_world_scale = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".MN_world_scale")

			_mn_world_scale.color_tag = 'NONE'
			_mn_world_scale.description = ""

			
			#_mn_world_scale interface
			#Socket world_scale
			world_scale_socket = _mn_world_scale.interface.new_socket(name = "world_scale", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			world_scale_socket.subtype = 'NONE'
			world_scale_socket.default_value = 0.009999999776482582
			world_scale_socket.min_value = -3.4028234663852886e+38
			world_scale_socket.max_value = 3.4028234663852886e+38
			world_scale_socket.attribute_domain = 'POINT'
			
			
			#initialize _mn_world_scale nodes
			#node Group Input
			group_input = _mn_world_scale.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Value
			value = _mn_world_scale.nodes.new("ShaderNodeValue")
			value.label = "world_scale"
			value.name = "Value"
			
			value.outputs[0].default_value = 0.009999999776482582
			#node Group Output
			group_output = _mn_world_scale.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			
			
			
			#Set locations
			group_input.location = (-200.0, 0.0)
			value.location = (0.0, 0.0)
			group_output.location = (190.0, 0.0)
			
			#Set dimensions
			group_input.width, group_input.height = 140.0, 100.0
			value.width, value.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			
			#initialize _mn_world_scale links
			#value.Value -> group_output.world_scale
			_mn_world_scale.links.new(value.outputs[0], group_output.inputs[0])
			return _mn_world_scale

		_mn_world_scale = _mn_world_scale_node_group()

		#initialize mn_units node group
		def mn_units_node_group():
			mn_units = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN Units")

			mn_units.color_tag = 'NONE'
			mn_units.description = ""

			
			#mn_units interface
			#Socket Angstrom
			angstrom_socket = mn_units.interface.new_socket(name = "Angstrom", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			angstrom_socket.subtype = 'NONE'
			angstrom_socket.default_value = 0.0
			angstrom_socket.min_value = -3.4028234663852886e+38
			angstrom_socket.max_value = 3.4028234663852886e+38
			angstrom_socket.attribute_domain = 'POINT'
			
			#Socket Nanometre
			nanometre_socket = mn_units.interface.new_socket(name = "Nanometre", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
			nanometre_socket.subtype = 'NONE'
			nanometre_socket.default_value = 0.0
			nanometre_socket.min_value = -3.4028234663852886e+38
			nanometre_socket.max_value = 3.4028234663852886e+38
			nanometre_socket.attribute_domain = 'POINT'
			
			#Socket Value
			value_socket = mn_units.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
			value_socket.subtype = 'NONE'
			value_socket.default_value = 3.0
			value_socket.min_value = -10000.0
			value_socket.max_value = 10000.0
			value_socket.attribute_domain = 'POINT'
			value_socket.description = "A value which will be scaled appropriately for the world"
			
			
			#initialize mn_units nodes
			#node Group Output
			group_output_1 = mn_units.nodes.new("NodeGroupOutput")
			group_output_1.name = "Group Output"
			group_output_1.is_active_output = True
			
			#node Group Input
			group_input_1 = mn_units.nodes.new("NodeGroupInput")
			group_input_1.name = "Group Input"
			
			#node Math
			math = mn_units.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'MULTIPLY'
			math.use_clamp = False
			
			#node Math.001
			math_001 = mn_units.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'MULTIPLY'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 10.0
			
			#node Group
			group = mn_units.nodes.new("GeometryNodeGroup")
			group.name = "Group"
			group.node_tree = _mn_world_scale
			
			
			
			
			#Set locations
			group_output_1.location = (190.0, 0.0)
			group_input_1.location = (-240.0, 0.0)
			math.location = (-60.0, 0.0)
			math_001.location = (-60.0, -160.0)
			group.location = (-304.00421142578125, -104.114013671875)
			
			#Set dimensions
			group_output_1.width, group_output_1.height = 140.0, 100.0
			group_input_1.width, group_input_1.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			group.width, group.height = 197.58424377441406, 100.0
			
			#initialize mn_units links
			#math.Value -> group_output_1.Angstrom
			mn_units.links.new(math.outputs[0], group_output_1.inputs[0])
			#group_input_1.Value -> math.Value
			mn_units.links.new(group_input_1.outputs[0], math.inputs[0])
			#group.world_scale -> math.Value
			mn_units.links.new(group.outputs[0], math.inputs[1])
			#math.Value -> math_001.Value
			mn_units.links.new(math.outputs[0], math_001.inputs[0])
			#math_001.Value -> group_output_1.Nanometre
			mn_units.links.new(math_001.outputs[0], group_output_1.inputs[1])
			return mn_units

		mn_units = mn_units_node_group()

		#initialize topology_break_bonds node group
		def topology_break_bonds_node_group():
			topology_break_bonds = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Topology Break Bonds")

			topology_break_bonds.color_tag = 'GEOMETRY'
			topology_break_bonds.description = ""

			topology_break_bonds.is_modifier = True
			
			#topology_break_bonds interface
			#Socket Atoms
			atoms_socket = topology_break_bonds.interface.new_socket(name = "Atoms", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket.attribute_domain = 'POINT'
			atoms_socket.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Atoms
			atoms_socket_1 = topology_break_bonds.interface.new_socket(name = "Atoms", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			atoms_socket_1.attribute_domain = 'POINT'
			atoms_socket_1.description = "Atomic geometry that contains vertices and edges"
			
			#Socket Selection
			selection_socket = topology_break_bonds.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Cutoff
			cutoff_socket = topology_break_bonds.interface.new_socket(name = "Cutoff", in_out='INPUT', socket_type = 'NodeSocketFloat')
			cutoff_socket.subtype = 'NONE'
			cutoff_socket.default_value = 2.5
			cutoff_socket.min_value = 0.0
			cutoff_socket.max_value = 10000.0
			cutoff_socket.attribute_domain = 'POINT'
			cutoff_socket.description = "Cutoff distance over which to remove bonds (Angstrom)"
			
			
			#initialize topology_break_bonds nodes
			#node Compare
			compare = topology_break_bonds.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'FLOAT'
			compare.mode = 'ELEMENT'
			compare.operation = 'GREATER_THAN'
			
			#node Boolean Math
			boolean_math = topology_break_bonds.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'OR'
			
			#node Vector Math
			vector_math = topology_break_bonds.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'DISTANCE'
			
			#node Edge Vertices
			edge_vertices = topology_break_bonds.nodes.new("GeometryNodeInputMeshEdgeVertices")
			edge_vertices.name = "Edge Vertices"
			
			#node Delete Geometry
			delete_geometry = topology_break_bonds.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry.name = "Delete Geometry"
			delete_geometry.domain = 'EDGE'
			delete_geometry.mode = 'EDGE_FACE'
			
			#node Group Input.001
			group_input_001 = topology_break_bonds.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[0].hide = True
			group_input_001.outputs[1].hide = True
			group_input_001.outputs[3].hide = True
			
			#node Group Input
			group_input_2 = topology_break_bonds.nodes.new("NodeGroupInput")
			group_input_2.name = "Group Input"
			group_input_2.outputs[2].hide = True
			group_input_2.outputs[3].hide = True
			
			#node Group Output
			group_output_2 = topology_break_bonds.nodes.new("NodeGroupOutput")
			group_output_2.name = "Group Output"
			group_output_2.is_active_output = True
			
			#node Group
			group_1 = topology_break_bonds.nodes.new("GeometryNodeGroup")
			group_1.name = "Group"
			group_1.node_tree = mn_units
			
			
			
			
			#Set locations
			compare.location = (220.0, -20.0)
			boolean_math.location = (460.0, 0.0)
			vector_math.location = (60.0, -20.0)
			edge_vertices.location = (-100.0, -20.0)
			delete_geometry.location = (460.0, 160.0)
			group_input_001.location = (-100.0, -160.0)
			group_input_2.location = (220.0, 140.0)
			group_output_2.location = (660.0, 160.0)
			group_1.location = (54.12406921386719, -160.0)
			
			#Set dimensions
			compare.width, compare.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			edge_vertices.width, edge_vertices.height = 140.0, 100.0
			delete_geometry.width, delete_geometry.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			group_input_2.width, group_input_2.height = 140.0, 100.0
			group_output_2.width, group_output_2.height = 140.0, 100.0
			group_1.width, group_1.height = 145.8759307861328, 100.0
			
			#initialize topology_break_bonds links
			#group_input_2.Atoms -> delete_geometry.Geometry
			topology_break_bonds.links.new(group_input_2.outputs[0], delete_geometry.inputs[0])
			#delete_geometry.Geometry -> group_output_2.Atoms
			topology_break_bonds.links.new(delete_geometry.outputs[0], group_output_2.inputs[0])
			#edge_vertices.Position 1 -> vector_math.Vector
			topology_break_bonds.links.new(edge_vertices.outputs[2], vector_math.inputs[0])
			#edge_vertices.Position 2 -> vector_math.Vector
			topology_break_bonds.links.new(edge_vertices.outputs[3], vector_math.inputs[1])
			#vector_math.Value -> compare.A
			topology_break_bonds.links.new(vector_math.outputs[1], compare.inputs[0])
			#group_1.Angstrom -> compare.B
			topology_break_bonds.links.new(group_1.outputs[0], compare.inputs[1])
			#compare.Result -> boolean_math.Boolean
			topology_break_bonds.links.new(compare.outputs[0], boolean_math.inputs[1])
			#boolean_math.Boolean -> delete_geometry.Selection
			topology_break_bonds.links.new(boolean_math.outputs[0], delete_geometry.inputs[1])
			#group_input_001.Cutoff -> group_1.Value
			topology_break_bonds.links.new(group_input_001.outputs[2], group_1.inputs[0])
			#group_input_2.Selection -> boolean_math.Boolean
			topology_break_bonds.links.new(group_input_2.outputs[1], boolean_math.inputs[0])
			return topology_break_bonds

		topology_break_bonds = topology_break_bonds_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Topology Break Bonds", type = 'NODES')
		mod.node_group = topology_break_bonds
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Topology_Break_Bonds.bl_idname)
			
def register():
	bpy.utils.register_class(Topology_Break_Bonds)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Topology_Break_Bonds)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
