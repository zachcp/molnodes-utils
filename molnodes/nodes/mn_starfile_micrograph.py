bl_info = {
	"name" : "MN_Starfile_Micrograph",
	"author" : "Brady Johnson",
	"version" : (4, 2, 0),
	"blender" : (4, 2, 0),
	"location" : "Node",
	"category" : "Node",
}

import bpy
import mathutils
import os

class MN_Starfile_Micrograph(bpy.types.Operator):
	bl_idname = "node.mn_starfile_micrograph"
	bl_label = "MN_Starfile_Micrograph"
	bl_options = {'REGISTER', 'UNDO'}
			
	def execute(self, context):
		#initialize mn_starfile_micrograph node group
		def mn_starfile_micrograph_node_group():
			mn_starfile_micrograph = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MN_Starfile_Micrograph")

			mn_starfile_micrograph.color_tag = 'NONE'
			mn_starfile_micrograph.description = ""

			
			#mn_starfile_micrograph interface
			#Socket Output
			output_socket = mn_starfile_micrograph.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
			output_socket.attribute_domain = 'POINT'
			
			#Socket Geometry
			geometry_socket = mn_starfile_micrograph.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
			geometry_socket.attribute_domain = 'POINT'
			
			#Socket Switch
			switch_socket = mn_starfile_micrograph.interface.new_socket(name = "Switch", in_out='INPUT', socket_type = 'NodeSocketBool')
			switch_socket.attribute_domain = 'POINT'
			
			#Socket Image
			image_socket = mn_starfile_micrograph.interface.new_socket(name = "Image", in_out='INPUT', socket_type = 'NodeSocketImage')
			image_socket.attribute_domain = 'POINT'
			
			#Socket A
			a_socket = mn_starfile_micrograph.interface.new_socket(name = "A", in_out='INPUT', socket_type = 'NodeSocketFloat')
			a_socket.subtype = 'NONE'
			a_socket.default_value = 0.0
			a_socket.min_value = -10000.0
			a_socket.max_value = 10000.0
			a_socket.attribute_domain = 'POINT'
			
			#Socket Z
			z_socket = mn_starfile_micrograph.interface.new_socket(name = "Z", in_out='INPUT', socket_type = 'NodeSocketFloat')
			z_socket.subtype = 'NONE'
			z_socket.default_value = 0.0
			z_socket.min_value = -10000.0
			z_socket.max_value = 10000.0
			z_socket.attribute_domain = 'POINT'
			
			#Socket Brightness
			brightness_socket = mn_starfile_micrograph.interface.new_socket(name = "Brightness", in_out='INPUT', socket_type = 'NodeSocketFloat')
			brightness_socket.subtype = 'NONE'
			brightness_socket.default_value = 0.0
			brightness_socket.min_value = -3.4028234663852886e+38
			brightness_socket.max_value = 3.4028234663852886e+38
			brightness_socket.attribute_domain = 'POINT'
			
			#Socket Contrast
			contrast_socket = mn_starfile_micrograph.interface.new_socket(name = "Contrast", in_out='INPUT', socket_type = 'NodeSocketFloat')
			contrast_socket.subtype = 'NONE'
			contrast_socket.default_value = 0.0
			contrast_socket.min_value = -3.4028234663852886e+38
			contrast_socket.max_value = 3.4028234663852886e+38
			contrast_socket.attribute_domain = 'POINT'
			
			
			#initialize mn_starfile_micrograph nodes
			#node Grid
			grid = mn_starfile_micrograph.nodes.new("GeometryNodeMeshGrid")
			grid.name = "Grid"
			#Size X
			grid.inputs[0].default_value = 1.0
			#Size Y
			grid.inputs[1].default_value = 1.0
			#Vertices X
			grid.inputs[2].default_value = 2
			#Vertices Y
			grid.inputs[3].default_value = 2
			
			#node Transform Geometry.006
			transform_geometry_006 = mn_starfile_micrograph.nodes.new("GeometryNodeTransform")
			transform_geometry_006.name = "Transform Geometry.006"
			transform_geometry_006.mode = 'COMPONENTS'
			#Translation
			transform_geometry_006.inputs[1].default_value = (0.5, 0.5, 0.0)
			#Rotation
			transform_geometry_006.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_006.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Transform Geometry.007
			transform_geometry_007 = mn_starfile_micrograph.nodes.new("GeometryNodeTransform")
			transform_geometry_007.name = "Transform Geometry.007"
			transform_geometry_007.mode = 'COMPONENTS'
			#Translation
			transform_geometry_007.inputs[1].default_value = (0.0, 0.0, 0.0)
			#Rotation
			transform_geometry_007.inputs[2].default_value = (0.0, 0.0, 0.0)
			
			#node Transform Geometry.008
			transform_geometry_008 = mn_starfile_micrograph.nodes.new("GeometryNodeTransform")
			transform_geometry_008.name = "Transform Geometry.008"
			transform_geometry_008.mode = 'COMPONENTS'
			#Rotation
			transform_geometry_008.inputs[2].default_value = (0.0, 0.0, 0.0)
			#Scale
			transform_geometry_008.inputs[3].default_value = (1.0, 1.0, 1.0)
			
			#node Image Info
			image_info = mn_starfile_micrograph.nodes.new("GeometryNodeImageInfo")
			image_info.name = "Image Info"
			#Frame
			image_info.inputs[1].default_value = 0
			
			#node Combine XYZ.002
			combine_xyz_002 = mn_starfile_micrograph.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_002.name = "Combine XYZ.002"
			#X
			combine_xyz_002.inputs[0].default_value = 0.0
			#Y
			combine_xyz_002.inputs[1].default_value = 0.0
			
			#node Combine XYZ.001
			combine_xyz_001 = mn_starfile_micrograph.nodes.new("ShaderNodeCombineXYZ")
			combine_xyz_001.name = "Combine XYZ.001"
			#Z
			combine_xyz_001.inputs[2].default_value = 0.0
			
			#node Named Attribute.004
			named_attribute_004 = mn_starfile_micrograph.nodes.new("GeometryNodeInputNamedAttribute")
			named_attribute_004.name = "Named Attribute.004"
			named_attribute_004.data_type = 'FLOAT'
			#Name
			named_attribute_004.inputs[0].default_value = "MNPixelSize"
			
			#node Attribute Statistic.002
			attribute_statistic_002 = mn_starfile_micrograph.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic_002.name = "Attribute Statistic.002"
			attribute_statistic_002.data_type = 'FLOAT'
			attribute_statistic_002.domain = 'POINT'
			#Selection
			attribute_statistic_002.inputs[1].default_value = True
			
			#node Attribute Statistic.001
			attribute_statistic_001 = mn_starfile_micrograph.nodes.new("GeometryNodeAttributeStatistic")
			attribute_statistic_001.name = "Attribute Statistic.001"
			attribute_statistic_001.data_type = 'FLOAT'
			attribute_statistic_001.domain = 'POINT'
			#Selection
			attribute_statistic_001.inputs[1].default_value = True
			
			#node Switch.003
			switch_003 = mn_starfile_micrograph.nodes.new("GeometryNodeSwitch")
			switch_003.name = "Switch.003"
			switch_003.input_type = 'FLOAT'
			#False
			switch_003.inputs[1].default_value = 1.0
			
			#node Compare.002
			compare_002 = mn_starfile_micrograph.nodes.new("FunctionNodeCompare")
			compare_002.name = "Compare.002"
			compare_002.data_type = 'FLOAT'
			compare_002.mode = 'ELEMENT'
			compare_002.operation = 'GREATER_THAN'
			#B
			compare_002.inputs[1].default_value = 0.0
			
			#node Switch.004
			switch_004 = mn_starfile_micrograph.nodes.new("GeometryNodeSwitch")
			switch_004.name = "Switch.004"
			switch_004.input_type = 'FLOAT'
			
			#node Math.001
			math_001 = mn_starfile_micrograph.nodes.new("ShaderNodeMath")
			math_001.name = "Math.001"
			math_001.operation = 'DIVIDE'
			math_001.use_clamp = False
			#Value_001
			math_001.inputs[1].default_value = 100.0
			
			#node Vector Math
			vector_math = mn_starfile_micrograph.nodes.new("ShaderNodeVectorMath")
			vector_math.name = "Vector Math"
			vector_math.operation = 'MULTIPLY'
			
			#node Group Output
			group_output = mn_starfile_micrograph.nodes.new("NodeGroupOutput")
			group_output.name = "Group Output"
			group_output.is_active_output = True
			
			#node Switch.002
			switch_002 = mn_starfile_micrograph.nodes.new("GeometryNodeSwitch")
			switch_002.name = "Switch.002"
			switch_002.input_type = 'GEOMETRY'
			
			#node Set Material
			set_material = mn_starfile_micrograph.nodes.new("GeometryNodeSetMaterial")
			set_material.name = "Set Material"
			#Selection
			set_material.inputs[1].default_value = True
			if "MN_micrograph_material" in bpy.data.materials:
				set_material.inputs[2].default_value = bpy.data.materials["MN_micrograph_material"]
			
			#node Store Named Attribute.001
			store_named_attribute_001 = mn_starfile_micrograph.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute_001.name = "Store Named Attribute.001"
			store_named_attribute_001.data_type = 'FLOAT'
			store_named_attribute_001.domain = 'POINT'
			#Selection
			store_named_attribute_001.inputs[1].default_value = True
			#Name
			store_named_attribute_001.inputs[2].default_value = "MNContrast"
			
			#node Group Input
			group_input = mn_starfile_micrograph.nodes.new("NodeGroupInput")
			group_input.name = "Group Input"
			
			#node Store Named Attribute
			store_named_attribute = mn_starfile_micrograph.nodes.new("GeometryNodeStoreNamedAttribute")
			store_named_attribute.name = "Store Named Attribute"
			store_named_attribute.data_type = 'FLOAT'
			store_named_attribute.domain = 'POINT'
			#Selection
			store_named_attribute.inputs[1].default_value = True
			#Name
			store_named_attribute.inputs[2].default_value = "MNBrightness"
			
			
			
			
			#Set locations
			grid.location = (-999.37109375, 99.62265014648438)
			transform_geometry_006.location = (-818.5869140625, 126.43045806884766)
			transform_geometry_007.location = (-631.0038452148438, 120.99168395996094)
			transform_geometry_008.location = (-280.42913818359375, 127.88481903076172)
			image_info.location = (-1585.4774169921875, -457.0034484863281)
			combine_xyz_002.location = (-463.28271484375, 19.085479736328125)
			combine_xyz_001.location = (-922.6502075195312, -307.76483154296875)
			named_attribute_004.location = (-1683.5006103515625, -1052.9495849609375)
			attribute_statistic_002.location = (-1112.16845703125, -966.6381225585938)
			attribute_statistic_001.location = (-1105.0552978515625, -612.5789184570312)
			switch_003.location = (-887.4561767578125, -835.5484619140625)
			compare_002.location = (-875.1576538085938, -657.2496948242188)
			switch_004.location = (-661.568359375, -714.772216796875)
			math_001.location = (-466.16815185546875, -596.7671508789062)
			vector_math.location = (-592.4921875, -338.4251403808594)
			group_output.location = (754.4419555664062, 429.34814453125)
			switch_002.location = (502.57647705078125, 427.40423583984375)
			set_material.location = (380.0, 200.0)
			store_named_attribute_001.location = (160.0, 140.0)
			group_input.location = (-1467.8316650390625, -14.638721466064453)
			store_named_attribute.location = (-60.0, 160.0)
			
			#Set dimensions
			grid.width, grid.height = 140.0, 100.0
			transform_geometry_006.width, transform_geometry_006.height = 140.0, 100.0
			transform_geometry_007.width, transform_geometry_007.height = 140.0, 100.0
			transform_geometry_008.width, transform_geometry_008.height = 140.0, 100.0
			image_info.width, image_info.height = 240.0, 100.0
			combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
			combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
			named_attribute_004.width, named_attribute_004.height = 140.0, 100.0
			attribute_statistic_002.width, attribute_statistic_002.height = 140.0, 100.0
			attribute_statistic_001.width, attribute_statistic_001.height = 140.0, 100.0
			switch_003.width, switch_003.height = 140.0, 100.0
			compare_002.width, compare_002.height = 140.0, 100.0
			switch_004.width, switch_004.height = 140.0, 100.0
			math_001.width, math_001.height = 140.0, 100.0
			vector_math.width, vector_math.height = 140.0, 100.0
			group_output.width, group_output.height = 140.0, 100.0
			switch_002.width, switch_002.height = 140.0, 100.0
			set_material.width, set_material.height = 140.0, 100.0
			store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
			group_input.width, group_input.height = 140.0, 100.0
			store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
			
			#initialize mn_starfile_micrograph links
			#switch_004.Output -> math_001.Value
			mn_starfile_micrograph.links.new(switch_004.outputs[0], math_001.inputs[0])
			#attribute_statistic_001.Mean -> switch_003.True
			mn_starfile_micrograph.links.new(attribute_statistic_001.outputs[0], switch_003.inputs[2])
			#compare_002.Result -> switch_004.Switch
			mn_starfile_micrograph.links.new(compare_002.outputs[0], switch_004.inputs[0])
			#combine_xyz_001.Vector -> vector_math.Vector
			mn_starfile_micrograph.links.new(combine_xyz_001.outputs[0], vector_math.inputs[0])
			#switch_003.Output -> switch_004.False
			mn_starfile_micrograph.links.new(switch_003.outputs[0], switch_004.inputs[1])
			#set_material.Geometry -> switch_002.True
			mn_starfile_micrograph.links.new(set_material.outputs[0], switch_002.inputs[2])
			#attribute_statistic_002.Mean -> switch_003.Switch
			mn_starfile_micrograph.links.new(attribute_statistic_002.outputs[0], switch_003.inputs[0])
			#math_001.Value -> vector_math.Vector
			mn_starfile_micrograph.links.new(math_001.outputs[0], vector_math.inputs[1])
			#transform_geometry_007.Geometry -> transform_geometry_008.Geometry
			mn_starfile_micrograph.links.new(transform_geometry_007.outputs[0], transform_geometry_008.inputs[0])
			#vector_math.Vector -> transform_geometry_007.Scale
			mn_starfile_micrograph.links.new(vector_math.outputs[0], transform_geometry_007.inputs[3])
			#named_attribute_004.Exists -> attribute_statistic_002.Attribute
			mn_starfile_micrograph.links.new(named_attribute_004.outputs[1], attribute_statistic_002.inputs[2])
			#grid.Mesh -> transform_geometry_006.Geometry
			mn_starfile_micrograph.links.new(grid.outputs[0], transform_geometry_006.inputs[0])
			#transform_geometry_006.Geometry -> transform_geometry_007.Geometry
			mn_starfile_micrograph.links.new(transform_geometry_006.outputs[0], transform_geometry_007.inputs[0])
			#image_info.Width -> combine_xyz_001.X
			mn_starfile_micrograph.links.new(image_info.outputs[0], combine_xyz_001.inputs[0])
			#image_info.Height -> combine_xyz_001.Y
			mn_starfile_micrograph.links.new(image_info.outputs[1], combine_xyz_001.inputs[1])
			#combine_xyz_002.Vector -> transform_geometry_008.Translation
			mn_starfile_micrograph.links.new(combine_xyz_002.outputs[0], transform_geometry_008.inputs[1])
			#named_attribute_004.Attribute -> attribute_statistic_001.Attribute
			mn_starfile_micrograph.links.new(named_attribute_004.outputs[0], attribute_statistic_001.inputs[2])
			#group_input.A -> compare_002.A
			mn_starfile_micrograph.links.new(group_input.outputs[3], compare_002.inputs[0])
			#group_input.A -> switch_004.True
			mn_starfile_micrograph.links.new(group_input.outputs[3], switch_004.inputs[2])
			#group_input.Switch -> switch_002.Switch
			mn_starfile_micrograph.links.new(group_input.outputs[1], switch_002.inputs[0])
			#group_input.Z -> combine_xyz_002.Z
			mn_starfile_micrograph.links.new(group_input.outputs[4], combine_xyz_002.inputs[2])
			#group_input.Image -> image_info.Image
			mn_starfile_micrograph.links.new(group_input.outputs[2], image_info.inputs[0])
			#group_input.Geometry -> attribute_statistic_001.Geometry
			mn_starfile_micrograph.links.new(group_input.outputs[0], attribute_statistic_001.inputs[0])
			#group_input.Geometry -> attribute_statistic_002.Geometry
			mn_starfile_micrograph.links.new(group_input.outputs[0], attribute_statistic_002.inputs[0])
			#switch_002.Output -> group_output.Output
			mn_starfile_micrograph.links.new(switch_002.outputs[0], group_output.inputs[0])
			#store_named_attribute_001.Geometry -> set_material.Geometry
			mn_starfile_micrograph.links.new(store_named_attribute_001.outputs[0], set_material.inputs[0])
			#transform_geometry_008.Geometry -> store_named_attribute.Geometry
			mn_starfile_micrograph.links.new(transform_geometry_008.outputs[0], store_named_attribute.inputs[0])
			#store_named_attribute.Geometry -> store_named_attribute_001.Geometry
			mn_starfile_micrograph.links.new(store_named_attribute.outputs[0], store_named_attribute_001.inputs[0])
			#group_input.Brightness -> store_named_attribute.Value
			mn_starfile_micrograph.links.new(group_input.outputs[5], store_named_attribute.inputs[3])
			#group_input.Contrast -> store_named_attribute_001.Value
			mn_starfile_micrograph.links.new(group_input.outputs[6], store_named_attribute_001.inputs[3])
			return mn_starfile_micrograph

		mn_starfile_micrograph = mn_starfile_micrograph_node_group()

		name = bpy.context.object.name
		obj = bpy.data.objects[name]
		mod = obj.modifiers.new(name = "MN_Starfile_Micrograph", type = 'NODES')
		mod.node_group = mn_starfile_micrograph
		return {'FINISHED'}

def menu_func(self, context):
	self.layout.operator(MN_Starfile_Micrograph.bl_idname)
			
def register():
	bpy.utils.register_class(MN_Starfile_Micrograph)
	bpy.types.NODE_MT_add.append(menu_func)
			
def unregister():
	bpy.utils.unregister_class(MN_Starfile_Micrograph)
	bpy.types.NODE_MT_add.remove(menu_func)
			
if __name__ == "__main__":
	register()
