bl_info = {
	"name" : "Style Density Surface",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class Style_Density_Surface(bpy.types.Operator):
	bl_idname = "node.style_density_surface"
	bl_label = "Style Density Surface"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize style_density_surface node group
		def style_density_surface_node_group():
			style_density_surface = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Style Density Surface")

			style_density_surface.color_tag = 'GEOMETRY'
			style_density_surface.description = ""

			style_density_surface.is_modifier = True
			
			#style_density_surface interface
			#Socket Geometry
			geometry_socket = style_density_surface.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Volume
			volume_socket = style_density_surface.interface.new_socket(name = "Volume", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			volume_socket.attribute_domain = 'POINT'
			
			#Socket Threshold
			threshold_socket = style_density_surface.interface.new_socket(name = "Threshold", in_out='INPUT', socket_type = 'NodeSocketFloat')
			threshold_socket.subtype = 'NONE'
			threshold_socket.default_value = 0.800000011920929
			threshold_socket.min_value = -3.4028234663852886e+38
			threshold_socket.max_value = 3.4028234663852886e+38
			threshold_socket.attribute_domain = 'POINT'
			
			#Socket Shade Smooth
			shade_smooth_socket = style_density_surface.interface.new_socket(name = "Shade Smooth", in_out='INPUT', socket_type = 'NodeSocketBool')
			shade_smooth_socket.attribute_domain = 'POINT'
			shade_smooth_socket.description = "Apply smooth shading to the created geometry"
			
			#Socket Hide Dust
			hide_dust_socket = style_density_surface.interface.new_socket(name = "Hide Dust", in_out='INPUT', socket_type = 'NodeSocketFloat')
			hide_dust_socket.subtype = 'NONE'
			hide_dust_socket.default_value = 0.0
			hide_dust_socket.min_value = -10000.0
			hide_dust_socket.max_value = 10000.0
			hide_dust_socket.attribute_domain = 'POINT'
			
			#Panel Material
			material_panel = style_density_surface.interface.new_panel("Material")
			#Socket Color
			color_socket = style_density_surface.interface.new_socket(name = "Color", in_out='INPUT', socket_type = 'NodeSocketColor', parent = material_panel)
			color_socket.attribute_domain = 'POINT'
			
			#Socket Material
			material_socket = style_density_surface.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial', parent = material_panel)
			material_socket.attribute_domain = 'POINT'
			material_socket.description = "Material to apply to the resulting geometry"
			
			
			
			#initialize style_density_surface nodes
			#node Volume to Mesh
			volume_to_mesh = style_density_surface.nodes.new("GeometryNodeVolumeToMesh")
			volume_to_mesh.name = "Volume to Mesh"
			volume_to_mesh.resolution_mode = 'GRID'
			#Adaptivity
			volume_to_mesh.inputs[4].default_value = 0.0
			
			#node Store Named Attribute
			store_named_attribute = style_density_surface.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT_COLOR'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "Color"
			
			#node Set Material
			set_material = style_density_surface.nodes.new("GeometryNodeSetMaterial")
			set_material.name = "Set Material"
			#Selection
			set_material.inputs[1].default_value = True
			
			#node Group Output
			group_output = style_density_surface.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Set Shade Smooth
			set_shade_smooth = style_density_surface.nodes.new("GeometryNodeSetShadeSmooth")
			set_shade_smooth.name = "Set Shade Smooth"
			set_shade_smooth.domain = 'FACE'
			#Selection
			set_shade_smooth.inputs[1].default_value = True
			
			#node Group Input
			group_input = style_density_surface.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Mesh Island
			mesh_island = style_density_surface.nodes.new("GeometryNodeInputMeshIsland")
			mesh_island.name = "Mesh Island"
			
			#node Face Area
			face_area = style_density_surface.nodes.new("GeometryNodeInputMeshFaceArea")
			face_area.name = "Face Area"
			
			#node Accumulate Field
			accumulate_field = style_density_surface.nodes.new("GeometryNodeAccumulateField")
			accumulate_field.name = "Accumulate Field"
			accumulate_field.data_type = 'FLOAT'
			accumulate_field.domain = 'POINT'
			
			#node Compare
			compare = style_density_surface.nodes.new("FunctionNodeCompare")
			compare.name = "Compare"
			compare.data_type = 'FLOAT'
			compare.mode = 'ELEMENT'
			compare.operation = 'LESS_THAN'
			
			#node Delete Geometry
			delete_geometry = style_density_surface.nodes.new("GeometryNodeDeleteGeometry")
			delete_geometry.name = "Delete Geometry"
			delete_geometry.domain = 'POINT'
			delete_geometry.mode = 'ALL'
			
			
			
			
			#Set locations
			volume_to_mesh.location = (-362.1430358886719, 7.630115509033203)
			store_named_attribute.location = (108.04933166503906, 22.085805892944336)
			set_material.location = (306.03485107421875, 6.998895645141602)
			group_output.location = (745.5179443359375, 7.314505577087402)
			set_shade_smooth.location = (525.8917846679688, 32.18394470214844)
			group_input.location = (-575.2391967773438, -60.0)
			mesh_island.location = (-718.2122802734375, 136.0499267578125)
			face_area.location = (-719.6749267578125, 216.50949096679688)
			accumulate_field.location = (-514.8893432617188, 256.0077819824219)
			compare.location = (-332.0450439453125, 241.37879943847656)
			delete_geometry.location = (-112.00000762939453, 21.943641662597656)
			
			#Set dimensions
			volume_to_mesh.width, volume_to_mesh.height = 170.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			set_material.width, set_material.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			mesh_island.width, mesh_island.height = 140.0, 100.0
			face_area.width, face_area.height = 140.0, 100.0
			accumulate_field.width, accumulate_field.height = 140.0, 100.0
			compare.width, compare.height = 140.0, 100.0
			delete_geometry.width, delete_geometry.height = 140.0, 100.0
			
			#initialize style_density_surface links
			#store_named_attribute.Geometry -> set_material.Geometry
			style_density_surface.links.new(store_named_attribute.outputs[0], set_material.inputs[0])
			#delete_geometry.Geometry -> store_named_attribute.Geometry
			style_density_surface.links.new(delete_geometry.outputs[0], store_named_attribute.inputs[0])
			#group_input.Color -> store_named_attribute.Value
			style_density_surface.links.new(group_input.outputs[4], store_named_attribute.inputs[3])
			#group_input.Volume -> volume_to_mesh.Volume
			style_density_surface.links.new(group_input.outputs[0], volume_to_mesh.inputs[0])
			#set_shade_smooth.Geometry -> group_output.Geometry
			style_density_surface.links.new(set_shade_smooth.outputs[0], group_output.inputs[0])
			#group_input.Threshold -> volume_to_mesh.Threshold
			style_density_surface.links.new(group_input.outputs[1], volume_to_mesh.inputs[3])
			#group_input.Material -> set_material.Material
			style_density_surface.links.new(group_input.outputs[5], set_material.inputs[2])
			#set_material.Geometry -> set_shade_smooth.Geometry
			style_density_surface.links.new(set_material.outputs[0], set_shade_smooth.inputs[0])
			#group_input.Shade Smooth -> set_shade_smooth.Shade Smooth
			style_density_surface.links.new(group_input.outputs[2], set_shade_smooth.inputs[2])
			#volume_to_mesh.Mesh -> delete_geometry.Geometry
			style_density_surface.links.new(volume_to_mesh.outputs[0], delete_geometry.inputs[0])
			#face_area.Area -> accumulate_field.Value
			style_density_surface.links.new(face_area.outputs[0], accumulate_field.inputs[0])
			#compare.Result -> delete_geometry.Selection
			style_density_surface.links.new(compare.outputs[0], delete_geometry.inputs[1])
			#accumulate_field.Total -> compare.A
			style_density_surface.links.new(accumulate_field.outputs[2], compare.inputs[0])
			#group_input.Hide Dust -> compare.B
			style_density_surface.links.new(group_input.outputs[3], compare.inputs[1])
			#mesh_island.Island Index -> accumulate_field.Group ID
			style_density_surface.links.new(mesh_island.outputs[0], accumulate_field.inputs[1])
			return style_density_surface

		style_density_surface = style_density_surface_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "Style Density Surface", type = 'NODES')
		mod.node_group = style_density_surface
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(Style_Density_Surface.bl_idname)
			
def register():
	bpy.utils.register_class(Style_Density_Surface)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(Style_Density_Surface)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
