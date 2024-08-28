bl_info = {
	"name" : "Ensemble Instance",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Ensemble_Instance(bpy.types.Operator):
	bl_idname = "node.ensemble_instance"
	bl_label = "Ensemble Instance"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize ensemble_instance node group
		def ensemble_instance_node_group():
			ensemble_instance = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Ensemble Instance")

			ensemble_instance.color_tag = 'GEOMETRY'
			ensemble_instance.description = ""

			ensemble_instance.is_modifier = True
			
			#ensemble_instance interface
			#Socket Instances
			instances_socket = ensemble_instance.interface.new_socket(name = "Instances", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			instances_socket.attribute_domain = 'POINT'
			
			#Socket Points
			points_socket = ensemble_instance.interface.new_socket(name = "Points", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			points_socket.attribute_domain = 'POINT'
			
			#Socket Selection
			selection_socket = ensemble_instance.interface.new_socket(name = "Selection", in_out='INPUT', socket_type = 'NodeSocketBool')
			selection_socket.default_value = True
			selection_socket.attribute_domain = 'POINT'
			selection_socket.hide_value = True
			selection_socket.description = "Selection of atoms to apply this node to"
			
			#Socket Instances
			instances_socket_1 = ensemble_instance.interface.new_socket(name = "Instances", in_out='INPUT', socket_type = 'NodeSocketCollection')
			instances_socket_1.attribute_domain = 'POINT'
			
			#Socket Fraction
			fraction_socket = ensemble_instance.interface.new_socket(name = "Fraction", in_out='INPUT', socket_type = 'NodeSocketFloat')
			fraction_socket.default_value = 1.0
			fraction_socket.min_value = 0.0
			fraction_socket.max_value = 1.0
			fraction_socket.subtype = 'FACTOR'
			fraction_socket.attribute_domain = 'POINT'
			
			#Socket As Points
			as_points_socket = ensemble_instance.interface.new_socket(name = "As Points", in_out='INPUT', socket_type = 'NodeSocketBool')
			as_points_socket.default_value = True
			as_points_socket.attribute_domain = 'POINT'
			
			#Panel Point
			point_panel = ensemble_instance.interface.new_panel("Point")
			point_panel.description = "Points"
			#Socket Point Radius
			point_radius_socket = ensemble_instance.interface.new_socket(name = "Point Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = point_panel)
			point_radius_socket.default_value = 0.10000000149011612
			point_radius_socket.min_value = 0.0
			point_radius_socket.max_value = 3.4028234663852886e+38
			point_radius_socket.subtype = 'DISTANCE'
			point_radius_socket.attribute_domain = 'POINT'
			
			#Socket Point Material
			point_material_socket = ensemble_instance.interface.new_socket(name = "Point Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = point_panel)
			point_material_socket.attribute_domain = 'POINT'
			
			
			
			#initialize ensemble_instance nodes
			#node Instance on Points
			instance_on_points = ensemble_instance.nodes.new("GeometryNodeInstanceOnPoints")
			instance_on_points.name = "Instance on Points"
			#Pick Instance
			instance_on_points.inputs[3].default_value = True
			#Scale
			instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)
			
			#node Random Value
			random_value = ensemble_instance.nodes.new("FunctionNodeRandomValue")
			random_value.name = "Random Value"
			random_value.data_type = 'BOOLEAN'
			#ID
			random_value.inputs[7].default_value = 0
			#Seed
			random_value.inputs[8].default_value = 0
			
			#node Boolean Math
			boolean_math = ensemble_instance.nodes.new("FunctionNodeBooleanMath")
			boolean_math.name = "Boolean Math"
			boolean_math.operation = 'AND'
			
			#node Separate Geometry
			separate_geometry = ensemble_instance.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry.name = "Separate Geometry"
			separate_geometry.domain = 'POINT'
			
			#node Separate Geometry.001
			separate_geometry_001 = ensemble_instance.nodes.new("GeometryNodeSeparateGeometry")
			separate_geometry_001.name = "Separate Geometry.001"
			separate_geometry_001.domain = 'POINT'
			
			#node Mesh to Points
			mesh_to_points = ensemble_instance.nodes.new("GeometryNodeMeshToPoints")
			mesh_to_points.name = "Mesh to Points"
			mesh_to_points.mode = 'VERTICES'
			#Selection
			mesh_to_points.inputs[1].default_value = True
			#Position
			mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Set Material
			set_material = ensemble_instance.nodes.new("GeometryNodeSetMaterial")
			set_material.name = "Set Material"
			#Selection
			set_material.inputs[1].default_value = True
			
			#node Join Geometry
			join_geometry = ensemble_instance.nodes.new("GeometryNodeJoinGeometry")
			join_geometry.name = "Join Geometry"
			
			#node Group Output
			group_output = ensemble_instance.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Group Input
			group_input = ensemble_instance.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Collection Info
			collection_info = ensemble_instance.nodes.new("GeometryNodeCollectionInfo")
			collection_info.name = "Collection Info"
			collection_info.transform_space = 'ORIGINAL'
			#Separate Children
			collection_info.inputs[1].default_value = True
			#Reset Children
			collection_info.inputs[2].default_value = False
			
			#node Group Input.001
			group_input_001 = ensemble_instance.nodes.new("NodeGroupInput")
			group_input_001.name = "Group Input.001"
			group_input_001.outputs[0].hide = True
			group_input_001.outputs[1].hide = True
			group_input_001.outputs[2].hide = True
			group_input_001.outputs[3].hide = True
			group_input_001.outputs[7].hide = True
			
			#node Named Attribute
			named_attribute = ensemble_instance.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute.name = "Named Attribute"
			named_attribute.data_type = 'INT'
			#Name
			named_attribute.inputs[0].default_value = "chain_id"
			
			#node Named Attribute.001
			named_attribute_001 = ensemble_instance.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_001.name = "Named Attribute.001"
			named_attribute_001.data_type = 'QUATERNION'
			#Name
			named_attribute_001.inputs[0].default_value = "rotation"
			
			
			
			
			#Set locations
			instance_on_points.location = (78.4000015258789, 352.79998779296875)
			random_value.location = (-420.0, 180.0)
			boolean_math.location = (-420.0, 320.0)
			separate_geometry.location = (-420.0, 480.0)
			separate_geometry_001.location = (-212.1615447998047, 464.0)
			mesh_to_points.location = (77.33333587646484, 541.3333129882812)
			set_material.location = (251.3333282470703, 541.3333129882812)
			join_geometry.location = (444.6666564941406, 541.3333129882812)
			group_output.location = (618.6666870117188, 541.3333129882812)
			group_input.location = (-896.1963500976562, 358.5467529296875)
			collection_info.location = (-200.0, 240.0)
			group_input_001.location = (-212.6666717529297, 580.0)
			named_attribute.location = (-200.0, 80.0)
			named_attribute_001.location = (-200.0, -60.0)
			
			#Set dimensions
			instance_on_points.width, instance_on_points.height = 140.0, 100.0
			random_value.width, random_value.height = 140.0, 100.0
			boolean_math.width, boolean_math.height = 140.0, 100.0
			separate_geometry.width, separate_geometry.height = 140.0, 100.0
			separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
			mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
			set_material.width, set_material.height = 140.0, 100.0
			join_geometry.width, join_geometry.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			collection_info.width, collection_info.height = 140.0, 100.0
			group_input_001.width, group_input_001.height = 140.0, 100.0
			named_attribute.width, named_attribute.height = 140.0, 100.0
			named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
			
			#initialize ensemble_instance links
			#collection_info.Instances -> instance_on_points.Instance
			ensemble_instance.links.new(collection_info.outputs[0], instance_on_points.inputs[2])
			#named_attribute.Attribute -> instance_on_points.Instance Index
			ensemble_instance.links.new(named_attribute.outputs[0], instance_on_points.inputs[4])
			#group_input.Selection -> boolean_math.Boolean
			ensemble_instance.links.new(group_input.outputs[1], boolean_math.inputs[0])
			#random_value.Value -> boolean_math.Boolean
			ensemble_instance.links.new(random_value.outputs[3], boolean_math.inputs[1])
			#group_input.Fraction -> random_value.Probability
			ensemble_instance.links.new(group_input.outputs[3], random_value.inputs[6])
			#boolean_math.Boolean -> instance_on_points.Selection
			ensemble_instance.links.new(boolean_math.outputs[0], instance_on_points.inputs[1])
			#group_input.Instances -> collection_info.Collection
			ensemble_instance.links.new(group_input.outputs[2], collection_info.inputs[0])
			#group_input.Points -> separate_geometry.Geometry
			ensemble_instance.links.new(group_input.outputs[0], separate_geometry.inputs[0])
			#boolean_math.Boolean -> separate_geometry.Selection
			ensemble_instance.links.new(boolean_math.outputs[0], separate_geometry.inputs[1])
			#separate_geometry.Selection -> separate_geometry_001.Geometry
			ensemble_instance.links.new(separate_geometry.outputs[0], separate_geometry_001.inputs[0])
			#separate_geometry_001.Inverted -> instance_on_points.Points
			ensemble_instance.links.new(separate_geometry_001.outputs[1], instance_on_points.inputs[0])
			#separate_geometry_001.Selection -> mesh_to_points.Mesh
			ensemble_instance.links.new(separate_geometry_001.outputs[0], mesh_to_points.inputs[0])
			#mesh_to_points.Points -> set_material.Geometry
			ensemble_instance.links.new(mesh_to_points.outputs[0], set_material.inputs[0])
			#instance_on_points.Instances -> join_geometry.Geometry
			ensemble_instance.links.new(instance_on_points.outputs[0], join_geometry.inputs[0])
			#join_geometry.Geometry -> group_output.Instances
			ensemble_instance.links.new(join_geometry.outputs[0], group_output.inputs[0])
			#group_input_001.As Points -> separate_geometry_001.Selection
			ensemble_instance.links.new(group_input_001.outputs[4], separate_geometry_001.inputs[1])
			#group_input_001.Point Radius -> mesh_to_points.Radius
			ensemble_instance.links.new(group_input_001.outputs[5], mesh_to_points.inputs[3])
			#group_input_001.Point Material -> set_material.Material
			ensemble_instance.links.new(group_input_001.outputs[6], set_material.inputs[2])
			#named_attribute_001.Attribute -> instance_on_points.Rotation
			ensemble_instance.links.new(named_attribute_001.outputs[0], instance_on_points.inputs[5])
			#set_material.Geometry -> join_geometry.Geometry
			ensemble_instance.links.new(set_material.outputs[0], join_geometry.inputs[0])
			return ensemble_instance

		ensemble_instance = ensemble_instance_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Ensemble Instance", type = 'NODES')
		mod.node_group = ensemble_instance
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Ensemble_Instance.bl_idname)
			
def register():
	bpy.utils.register_class(Ensemble_Instance)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Ensemble_Instance)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
