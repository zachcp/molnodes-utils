bl_info = {
	"name" : "Style Density Wire",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Style_Density_Wire(bpy.types.Operator):
	bl_idname = "node.style_density_wire"
	bl_label = "Style Density Wire"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize style_density_wire node group
		def style_density_wire_node_group():
			style_density_wire = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Style Density Wire")

			style_density_wire.color_tag = 'GEOMETRY'
			style_density_wire.description = ""

			style_density_wire.is_modifier = True
			
			#style_density_wire interface
			#Socket Geometry
			geometry_socket = style_density_wire.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Volume
			volume_socket = style_density_wire.interface.new_socket(name = "Volume", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			volume_socket.attribute_domain = 'POINT'
			
			#Socket Threshold
			threshold_socket = style_density_wire.interface.new_socket(name = "Threshold", in_out='INPUT', socket_type = 'NodeSocketFloat')
			threshold_socket.subtype = 'NONE'
			threshold_socket.default_value = 0.800000011920929
			threshold_socket.min_value = -3.4028234663852886e+38
			threshold_socket.max_value = 3.4028234663852886e+38
			threshold_socket.attribute_domain = 'POINT'
			
			#Socket Hide Dust
			hide_dust_socket = style_density_wire.interface.new_socket(name = "Hide Dust", in_out='INPUT', socket_type = 'NodeSocketFloat')
			hide_dust_socket.subtype = 'NONE'
			hide_dust_socket.default_value = 20.0
			hide_dust_socket.min_value = -10000.0
			hide_dust_socket.max_value = 10000.0
			hide_dust_socket.attribute_domain = 'POINT'
			
			#Panel Wire
			wire_panel = style_density_wire.interface.new_panel("Wire")
			#Socket Wire Radius
			wire_radius_socket = style_density_wire.interface.new_socket(name = "Wire Radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = wire_panel)
			wire_radius_socket.subtype = 'NONE'
			wire_radius_socket.default_value = 1.0
			wire_radius_socket.min_value = 0.0
			wire_radius_socket.max_value = 3.4028234663852886e+38
			wire_radius_socket.attribute_domain = 'POINT'
			wire_radius_socket.description = "Radius of the created wire (in relative nm)"
			
			#Socket Wire Resolution
			wire_resolution_socket = style_density_wire.interface.new_socket(name = "Wire Resolution", in_out='INPUT', socket_type = 'NodeSocketInt', parent = wire_panel)
			wire_resolution_socket.subtype = 'NONE'
			wire_resolution_socket.default_value = 3
			wire_resolution_socket.min_value = 3
			wire_resolution_socket.max_value = 512
			wire_resolution_socket.attribute_domain = 'POINT'
			
			
			#Panel Material
			material_panel = style_density_wire.interface.new_panel("Material")
			#Socket Color
			color_socket = style_density_wire.interface.new_socket(name = "Color", in_out='INPUT', socket_type = 'NodeSocketColor', parent = material_panel)
			color_socket.attribute_domain = 'POINT'
			
			#Socket Material
			material_socket = style_density_wire.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = material_panel)
			material_socket.attribute_domain = 'POINT'
			material_socket.description = "Material to apply to the resulting geometry"
			
			
			
			#initialize style_density_wire nodes
			#node Group Output
			group_output = style_density_wire.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Set Material
			set_material = style_density_wire.nodes.new("GeometryNodeSetMaterial")
			set_material.name = "Set Material"
			#Selection
			set_material.inputs[1].default_value = True
			
			#node Store Named Attribute
			store_named_attribute = style_density_wire.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_COLOR'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "Color"
			
			#node Mesh to Curve
			mesh_to_curve = style_density_wire.nodes.new("GeometryNodeMeshToCurve")
			mesh_to_curve.name = "Mesh to Curve"
			#Selection
			mesh_to_curve.inputs[1].default_value = True
			
			#node Curve to Mesh
			curve_to_mesh = style_density_wire.nodes.new("GeometryNodeCurveToMesh")
			curve_to_mesh.name = "Curve to Mesh"
			#Fill Caps
			curve_to_mesh.inputs[2].default_value = True
			
			#node Curve Circle
			curve_circle = style_density_wire.nodes.new("GeometryNodeCurvePrimitiveCircle")
			curve_circle.name = "Curve Circle"
			curve_circle.mode = 'RADIUS'
			
			#node Math
			math = style_density_wire.nodes.new("ShaderNodeMath")
			math.name = "Math"
			math.operation = 'DIVIDE'
			math.use_clamp = False
			#Value_001
			math.inputs[1].default_value = 1000.0
			
			#node Mesh Island
			mesh_island = style_density_wire.nodes.new("GeometryNodeInputMeshIsland")
			mesh_island.name = "Mesh Island"
			
			#node Face Area
			face_area = style_density_wire.nodes.new("GeometryNodeInputMeshFaceArea")
			face_area.name = "Face Area"
			
			#node Accumulate Field
			accumulate_field = style_density_wire.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'FLOAT'
			accumulate_field.domain = 'POINT'
			
			#node Compare
			compare = style_density_wire.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'FLOAT'
			compare.mode = 'ELEMENT'
			compare.operation = 'LESS_THAN'
			
			#node Group Input
			group_input = style_density_wire.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Volume to Mesh
			volume_to_mesh = style_density_wire.nodes.new("GeometryNodeVolumeToMesh")
			volume_to_mesh.name = "Volume to Mesh"
			volume_to_mesh.resolution_mode = 'GRID'
			#Adaptivity
			volume_to_mesh.inputs[4].default_value = 0.0
			
			#node Delete Geometry
			delete_geometry = style_density_wire.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry.name = "Delete Geometry"
			delete_geometry.domain = 'POINT'
			delete_geometry.mode = 'ALL'
			
			
			
			
			#Set locations
			group_output.location = (387.14306640625, 0.0)
			set_material.location = (197.14306640625, -7.630115509033203)
			store_named_attribute.location = (-360.0, 60.0)
			mesh_to_curve.location = (-157.53106689453125, 102.452392578125)
			curve_to_mesh.location = (13.590629577636719, 121.26826477050781)
			curve_circle.location = (-160.0, -20.0)
			math.location = (-360.0, -160.0)
			mesh_island.location = (-1117.136474609375, 390.44488525390625)
			face_area.location = (-1118.59912109375, 470.9044494628906)
			accumulate_field.location = (-913.8134765625, 510.4027404785156)
			compare.location = (-730.9691772460938, 495.7737731933594)
			group_input.location = (-942.8719482421875, -125.95775604248047)
			volume_to_mesh.location = (-749.5906372070312, -26.41063690185547)
			delete_geometry.location = (-547.6565551757812, 47.350433349609375)
			
			#Set dimensions
			group_output.width, group_output.height = 140.0, 100.0
			set_material.width, set_material.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
			curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
			curve_circle.width, curve_circle.height = 140.0, 100.0
			math.width, math.height = 140.0, 100.0
			mesh_island.width, mesh_island.height = 140.0, 100.0
			face_area.width, face_area.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			volume_to_mesh.width, volume_to_mesh.height = 170.0, 100.0
			delete_geometry.width, delete_geometry.height = 140.0, 100.0
			
			#initialize style_density_wire links
			#group_input.Color -> store_named_attribute.Value
			style_density_wire.links.new(group_input.outputs[5], store_named_attribute.inputs[3])
			#group_input.Volume -> volume_to_mesh.Volume
			style_density_wire.links.new(group_input.outputs[0], volume_to_mesh.inputs[0])
			#set_material.Geometry -> group_output.Geometry
			style_density_wire.links.new(set_material.outputs[0], group_output.inputs[0])
			#group_input.Threshold -> volume_to_mesh.Threshold
			style_density_wire.links.new(group_input.outputs[1], volume_to_mesh.inputs[3])
			#group_input.Material -> set_material.Material
			style_density_wire.links.new(group_input.outputs[6], set_material.inputs[2])
			#store_named_attribute.Geometry -> mesh_to_curve.Mesh
			style_density_wire.links.new(store_named_attribute.outputs[0], mesh_to_curve.inputs[0])
			#mesh_to_curve.Curve -> curve_to_mesh.Curve
			style_density_wire.links.new(mesh_to_curve.outputs[0], curve_to_mesh.inputs[0])
			#curve_circle.Curve -> curve_to_mesh.Profile Curve
			style_density_wire.links.new(curve_circle.outputs[0], curve_to_mesh.inputs[1])
			#curve_to_mesh.Mesh -> set_material.Geometry
			style_density_wire.links.new(curve_to_mesh.outputs[0], set_material.inputs[0])
			#group_input.Wire Radius -> math.Value
			style_density_wire.links.new(group_input.outputs[3], math.inputs[0])
			#math.Value -> curve_circle.Radius
			style_density_wire.links.new(math.outputs[0], curve_circle.inputs[4])
			#group_input.Wire Resolution -> curve_circle.Resolution
			style_density_wire.links.new(group_input.outputs[4], curve_circle.inputs[0])
			#face_area.Area -> accumulate_field.Value
			style_density_wire.links.new(face_area.outputs[0], accumulate_field.inputs[0])
			#compare.Result -> delete_geometry.Selection
			style_density_wire.links.new(compare.outputs[0], delete_geometry.inputs[1])
			#accumulate_field.Total -> compare.A
			style_density_wire.links.new(accumulate_field.outputs[2], compare.inputs[0])
			#mesh_island.Island Index -> accumulate_field.Group ID
			style_density_wire.links.new(mesh_island.outputs[0], accumulate_field.inputs[1])
			#volume_to_mesh.Mesh -> delete_geometry.Geometry
			style_density_wire.links.new(volume_to_mesh.outputs[0], delete_geometry.inputs[0])
			#delete_geometry.Geometry -> store_named_attribute.Geometry
			style_density_wire.links.new(delete_geometry.outputs[0], store_named_attribute.inputs[0])
			#group_input.Hide Dust -> compare.B
			style_density_wire.links.new(group_input.outputs[2], compare.inputs[1])
			return style_density_wire

		style_density_wire = style_density_wire_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Style Density Wire", type = 'NODES')
		mod.node_group = style_density_wire
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Style_Density_Wire.bl_idname)
			
def register():
	bpy.utils.register_class(Style_Density_Wire)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Style_Density_Wire)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
