import bpy
from ._atoms_to_curves import _atoms_to_curves
from ._base_align import _Base_align
from ._bs_smooth import _bs_smooth
from ._cartoon_arrow_primitive import _cartoon_arrow_primitive
from ._cartoon_arrow_instance import _cartoon_arrow_instance
from ._cartoon_arrows_scale import _cartoon_arrows_scale
from ._curve_custom_profile import _curve_custom_profile
from ._curve_end_fix_color import _curve_end_fix_color
from ._curve_ends_adjust_angle import _curve_ends_adjust_angle
from ._curve_profile_backup import _curve_profile_backup
from ._curve_to_mesh import _curve_to_mesh
from ._debug_arrows import _DEBUG_arrows
from ._dssp_sheet_checks import _DSSP_Sheet_Checks
from ._expand_selection import _expand_selection
from ._field_offset import _field_offset
from ._field_offset_bool import _field_offset_bool
from ._field_offset_vec import _field_offset_vec
from ._guide_rotation import _guide_rotation
from ._hbond_i___1__j___1__and_hbond_j___1__i___1_ import (
    _HBond_i___1__j___1__and_HBond_j___1__i___1_,
)
from ._hbond_i___1_j__and_hbond_j_i___1_ import _Hbond_i___1_j__and_Hbond_j_i___1_
from ._hbond_i__j__and_hbond_j__i_ import _HBond_i__j__and_HBond_j__i_
from ._hbond_j___1_i_and_hbond_i_j___1_ import _Hbond_j___1_i_and_Hbond_i_j___1_
from ._is_odd import _is_odd
from ._mn_animate_falloff_empty import _MN_animate_falloff_empty
from ._mn_animate_falloff_points import _MN_animate_falloff_points
from ._mn_animate_field import _MN_animate_field
from ._mn_animate_wiggle_mask_length import _MN_animate_wiggle_mask_length
from ._mn_animate_wiggle_mask_res import _MN_animate_wiggle_mask_res
from ._mn_assembly_instance_chains import _MN_assembly_instance_chains
from ._mn_assembly_rotate import _MN_assembly_rotate
from ._mn_cartoon_bs_alternate_axis import _MN_cartoon_bs_alternate_axis
from ._mn_cartoon_smooth_handles import _MN_cartoon_smooth_handles
from ._mn_constants_atom_name_nucleic import _MN_constants_atom_name_nucleic
from ._mn_constants_atom_name_peptide import _MN_constants_atom_name_peptide
from ._mn_point_curve_trails import _MN_point_curve_trails
from ._mn_select_attribute import _MN_select_attribute
from ._mn_select_nucleic import _MN_select_nucleic
from ._mn_select_peptide import _MN_select_peptide
from ._mn_select_res_name_peptide import _MN_select_res_name_peptide
from ._mn_select_sec_struct import _MN_select_sec_struct
from ._mn_select_sec_struct_id import _MN_select_sec_struct_id
from ._mn_surface_smooth_bumps import _MN_surface_smooth_bumps
from ._mn_topo_assign_backbone import _MN_topo_assign_backbone
from ._mn_topo_calc_helix import _MN_topo_calc_helix
from ._mn_topo_calc_sheet import _MN_topo_calc_sheet
from ._mn_topo_phi_psi import _MN_topo_phi_psi
from ._mn_utils_aa_atom_pos import _MN_utils_aa_atom_pos
from ._mn_utils_bio_assembly import _MN_utils_bio_assembly
from ._mn_utils_int_multiply import _MN_utils_int_multiply
from ._mn_utils_rotate_res import _MN_utils_rotate_res
from ._mn_utils_split_instance import _MN_utils_split_instance
from ._mn_utils_style_cartoon import _MN_utils_style_cartoon
from ._mn_utils_style_old_ball_and_stick import _MN_utils_style_old_ball_and_stick
from ._mn_utils_style_ribbon_nucleic import _MN_utils_style_ribbon_nucleic
from ._mn_utils_style_ribbon_peptide import _MN_utils_style_ribbon_peptide
from ._mn_utils_style_spheres_icosphere import _MN_utils_style_spheres_icosphere
from ._mn_utils_style_spheres_points import _MN_utils_style_spheres_points
from ._mn_utils_style_sticks import _MN_utils_style_sticks
from ._mn_utils_style_surface_new import _MN_utils_style_surface_new
from ._mn_utils_style_surface_old import _MN_utils_style_surface_old
from ._mn_utils_to_instance_centred import _MN_utils_to_instance_centred
from ._mn_world_scale import _MN_world_scale
from ._sampleatomvalue import _SampleAtomValue
from ._sec_struct_counter import _sec_struct_counter
from ._selective_scale import _selective_scale
from ._surface_blur_color import _surface_blur_color
from ._surface_blur_postion import _surface_blur_postion
from ._surface_compute_density_from_points import _surface_compute_density_from_points
from ._surface_sample_color import _surface_sample_color
from ._topo_count_atoms import _Topo_Count_Atoms
from ._topo_count_residues import _Topo_Count_Residues
from ._utils_bounding_box import _utils_bounding_box
from ._utils_group_field_at_selection import _utils_group_field_at_selection
from ._utils_oxdna_base import _utils_oxdna_base
from ._2_point_angle import _2_Point_Angle
from ._3_point_angle import _3_Point_Angle
from ._curve_ends_adjust_position import _curve_ends_adjust_position
from .animate_collection_pick import Animate_Collection_Pick
from .animate_fraction import Animate_Fraction
from .animate_frames import Animate_Frames
from .animate_peptide_to_curve import Animate_Peptide_to_Curve
from .animate_trails import Animate_Trails
from .animate_value import Animate_Value
from .animate_wiggle import Animate_Wiggle
from .attribute_map import Attribute_Map
from .backbone_nh import Backbone_NH
from .backbone_position import Backbone_Position
from .backbone_positions import Backbone_Positions
from .between_float import Between_Float
from .between_integer import Between_Integer
from .between_vector import Between_Vector
from .bond_count import Bond_Count
from .boolean_run_fill import Boolean_Run_Fill
from .boolean_run_mask import Boolean_Run_Mask
from .centre_on_selection import Centre_on_Selection
from .centroid import Centroid
from .chain_info import Chain_Info
from .color_atomic_number import Color_Atomic_Number
from .color_attribute_map import Color_Attribute_Map
from .color_attribute_random import Color_Attribute_Random
from .color_backbone import Color_Backbone
from .color_chain_ import Color_Chain_
from .color_common import Color_Common
from .color_element import Color_Element
from .color_entity_ import Color_Entity_
from .color_goodsell import Color_Goodsell
from .color_ligand_ import Color_Ligand_
from .color_plddt import Color_pLDDT
from .color_rainbow import Color_Rainbow
from .color_res_name import Color_Res_Name
from .color_res_name_nucleic import Color_Res_Name_Nucleic
from .color_sec_struct import Color_Sec_Struct
from .color_segment_ import Color_Segment_
from .dihedral_angle import Dihedral_Angle
from .dihedral_phi import Dihedral_Phi
from .dihedral_psi import Dihedral_Psi
from .edge_info import Edge_Info
from .ensemble_instance import Ensemble_Instance
from .fallback_boolean import Fallback_Boolean
from .fallback_color import Fallback_Color
from .fallback_float import Fallback_Float
from .fallback_integer import Fallback_Integer
from .fallback_vector import Fallback_Vector
from .group_info import Group_Info
from .group_pick import Group_Pick
from .group_pick_vector import Group_Pick_Vector
from .hbond_backbone_check import HBond_Backbone_Check
from .hbond_backbone_check_backup import HBond_Backbone_Check_backup
from .hbond_energy import HBond_Energy
from .helix_detect import Helix_Detect
from .is_alpha_carbon import Is_Alpha_Carbon
from .is_backbone import Is_Backbone
from .is_helix import Is_Helix
from .is_lipid import Is_Lipid
from .is_loop import Is_Loop
from .is_nucleic import Is_Nucleic
from .is_peptide import Is_Peptide
from .is_sheet import Is_Sheet
from .is_side_chain import Is_Side_Chain
from .is_solvent import Is_Solvent
from .mn_units import MN_Units
from .mn_animate_noise_field import MN_animate_noise_field
from .mn_animate_noise_position import MN_animate_noise_position
from .mn_animate_noise_repeat import MN_animate_noise_repeat
from .mn_assembly_ import MN_assembly_
from .mn_assembly_center import MN_assembly_center
from .mn_dna_bases import MN_dna_bases
from .mn_dna_double_helix import MN_dna_double_helix
from .mn_dna_style_ball_and_stick import MN_dna_style_ball_and_stick
from .mn_dna_style_spheres_cycles import MN_dna_style_spheres_cycles
from .mn_dna_style_spheres_eevee import MN_dna_style_spheres_eevee
from .mn_dna_style_surface import MN_dna_style_surface
from .mn_oxdna_style_ribbon import MN_oxdna_style_ribbon
from .mn_select_distance_empty import MN_select_distance_empty
from .mn_select_nucleic_type import MN_select_nucleic_type
from .mn_starfile_micrograph import MN_Starfile_Micrograph
from .mn_style_surface_old import MN_style_surface_old
from .mn_topo_backbone import MN_topo_backbone
from .mn_utils_curve_resample import MN_utils_curve_resample
from .mn_utils_extend_curve import MN_utils_extend_curve
from .mn_utils_helix import MN_utils_helix
from .mn_utils_primitive_atom import MN_utils_primitive_atom
from .nodegroup_001 import NodeGroup_001
from .nodestorage import NodeStorage
from .offset_boolean import Offset_Boolean
from .offset_color import Offset_Color
from .offset_float import Offset_Float
from .offset_integer import Offset_Integer
from .offset_vector import Offset_Vector
from .point_distance import Point_Distance
from .point_edge_angle import Point_Edge_Angle
from .points_of_edge import Points_of_Edge
from .res_group_id import Res_Group_ID
from .res_info import Res_Info
from .residue_mask import Residue_Mask
from .sample_mix_float import Sample_Mix_Float
from .sample_mix_vector import Sample_Mix_Vector
from .sample_nearest_atoms import Sample_Nearest_Atoms
from .select_atomic_number import Select_Atomic_Number
from .select_attribute import Select_Attribute
from .select_bonded import Select_Bonded
from .select_chain_ import Select_Chain_
from .select_cube import Select_Cube
from .select_element import Select_Element
from .select_entity_ import Select_Entity_
from .select_ligand_ import Select_Ligand_
from .select_proximity import Select_Proximity
from .select_res_id import Select_Res_ID
from .select_res_id_range import Select_Res_ID_Range
from .select_res_id_ import Select_Res_ID_
from .select_res_name import Select_Res_Name
from .select_res_whole import Select_Res_Whole
from .select_segment_ import Select_Segment_
from .select_sphere import Select_Sphere
from .self_sample_proximity import Self_Sample_Proximity
from .separate_atoms import Separate_Atoms
from .separate_polymers import Separate_Polymers
from .set_color import Set_Color
from .starfile_instances import Starfile_Instances
from .style_ball_and_stick import Style_Ball_and_Stick
from .style_cartoon import Style_Cartoon
from .style_density_surface import Style_Density_Surface
from .style_density_wire import Style_Density_Wire
from .style_preset_1 import Style_Preset_1
from .style_preset_2 import Style_Preset_2
from .style_preset_3 import Style_Preset_3
from .style_preset_4 import Style_Preset_4
from .style_ribbon import Style_Ribbon
from .style_spheres import Style_Spheres
from .style_sticks import Style_Sticks
from .style_surface import Style_Surface
from .topology_break_bonds import Topology_Break_Bonds
from .topology_dssp import Topology_DSSP
from .topology_find_bonds import Topology_Find_Bonds
from .utils_zyz_to_rotation import Utils_ZYZ_to_Rotation
from .vector_angle import Vector_Angle
from .world_to_angstrom import World_to_Angstrom

__all__ = [
    "_atoms_to_curves",
    "_Base_align",
    "_bs_smooth",
    "_cartoon_arrow_primitive",
    "_cartoon_arrow_instance",
    "_cartoon_arrows_scale",
    "_curve_custom_profile",
    "_curve_end_fix_color",
    "_curve_ends_adjust_angle",
    "_curve_profile_backup",
    "_curve_to_mesh",
    "_DEBUG_arrows",
    "_DSSP_Sheet_Checks",
    "_expand_selection",
    "_field_offset",
    "_field_offset_bool",
    "_field_offset_vec",
    "_guide_rotation",
    "_HBond_i___1__j___1__and_HBond_j___1__i___1_",
    "_Hbond_i___1_j__and_Hbond_j_i___1_",
    "_HBond_i__j__and_HBond_j__i_",
    "_Hbond_j___1_i_and_Hbond_i_j___1_",
    "_is_odd",
    "_MN_animate_falloff_empty",
    "_MN_animate_falloff_points",
    "_MN_animate_field",
    "_MN_animate_wiggle_mask_length",
    "_MN_animate_wiggle_mask_res",
    "_MN_assembly_instance_chains",
    "_MN_assembly_rotate",
    "_MN_cartoon_bs_alternate_axis",
    "_MN_cartoon_smooth_handles",
    "_MN_constants_atom_name_nucleic",
    "_MN_constants_atom_name_peptide",
    "_MN_point_curve_trails",
    "_MN_select_attribute",
    "_MN_select_nucleic",
    "_MN_select_peptide",
    "_MN_select_res_name_peptide",
    "_MN_select_sec_struct",
    "_MN_select_sec_struct_id",
    "_MN_surface_smooth_bumps",
    "_MN_topo_assign_backbone",
    "_MN_topo_calc_helix",
    "_MN_topo_calc_sheet",
    "_MN_topo_phi_psi",
    "_MN_utils_aa_atom_pos",
    "_MN_utils_bio_assembly",
    "_MN_utils_int_multiply",
    "_MN_utils_rotate_res",
    "_MN_utils_split_instance",
    "_MN_utils_style_cartoon",
    "_MN_utils_style_old_ball_and_stick",
    "_MN_utils_style_ribbon_nucleic",
    "_MN_utils_style_ribbon_peptide",
    "_MN_utils_style_spheres_icosphere",
    "_MN_utils_style_spheres_points",
    "_MN_utils_style_sticks",
    "_MN_utils_style_surface_new",
    "_MN_utils_style_surface_old",
    "_MN_utils_to_instance_centred",
    "_MN_world_scale",
    "_SampleAtomValue",
    "_sec_struct_counter",
    "_selective_scale",
    "_surface_blur_color",
    "_surface_blur_postion",
    "_surface_compute_density_from_points",
    "_surface_sample_color",
    "_Topo_Count_Atoms",
    "_Topo_Count_Residues",
    "_utils_bounding_box",
    "_utils_group_field_at_selection",
    "_utils_oxdna_base",
    "_2_Point_Angle",
    "_3_Point_Angle",
    "_curve_ends_adjust_position",
    "Animate_Collection_Pick",
    "Animate_Fraction",
    "Animate_Frames",
    "Animate_Peptide_to_Curve",
    "Animate_Trails",
    "Animate_Value",
    "Animate_Wiggle",
    "Attribute_Map",
    "Backbone_NH",
    "Backbone_Position",
    "Backbone_Positions",
    "Between_Float",
    "Between_Integer",
    "Between_Vector",
    "Bond_Count",
    "Boolean_Run_Fill",
    "Boolean_Run_Mask",
    "Centre_on_Selection",
    "Centroid",
    "Chain_Info",
    "Color_Atomic_Number",
    "Color_Attribute_Map",
    "Color_Attribute_Random",
    "Color_Backbone",
    "Color_Chain_",
    "Color_Common",
    "Color_Element",
    "Color_Entity_",
    "Color_Goodsell",
    "Color_Ligand_",
    "Color_pLDDT",
    "Color_Rainbow",
    "Color_Res_Name",
    "Color_Res_Name_Nucleic",
    "Color_Sec_Struct",
    "Color_Segment_",
    "Dihedral_Angle",
    "Dihedral_Phi",
    "Dihedral_Psi",
    "Edge_Info",
    "Ensemble_Instance",
    "Fallback_Boolean",
    "Fallback_Color",
    "Fallback_Float",
    "Fallback_Integer",
    "Fallback_Vector",
    "Group_Info",
    "Group_Pick",
    "Group_Pick_Vector",
    "HBond_Backbone_Check",
    "HBond_Backbone_Check_backup",
    "HBond_Energy",
    "Helix_Detect",
    "Is_Alpha_Carbon",
    "Is_Backbone",
    "Is_Helix",
    "Is_Lipid",
    "Is_Loop",
    "Is_Nucleic",
    "Is_Peptide",
    "Is_Sheet",
    "Is_Side_Chain",
    "Is_Solvent",
    "MN_Units",
    "MN_animate_noise_field",
    "MN_animate_noise_position",
    "MN_animate_noise_repeat",
    "MN_assembly_",
    "MN_assembly_center",
    "MN_dna_bases",
    "MN_dna_double_helix",
    "MN_dna_style_ball_and_stick",
    "MN_dna_style_spheres_cycles",
    "MN_dna_style_spheres_eevee",
    "MN_dna_style_surface",
    "MN_oxdna_style_ribbon",
    "MN_select_distance_empty",
    "MN_select_nucleic_type",
    "MN_Starfile_Micrograph",
    "MN_style_surface_old",
    "MN_topo_backbone",
    "MN_utils_curve_resample",
    "MN_utils_extend_curve",
    "MN_utils_helix",
    "MN_utils_primitive_atom",
    "NodeGroup_001",
    "NodeStorage",
    "Offset_Boolean",
    "Offset_Color",
    "Offset_Float",
    "Offset_Integer",
    "Offset_Vector",
    "Point_Distance",
    "Point_Edge_Angle",
    "Points_of_Edge",
    "Res_Group_ID",
    "Res_Info",
    "Residue_Mask",
    "Sample_Mix_Float",
    "Sample_Mix_Vector",
    "Sample_Nearest_Atoms",
    "Select_Atomic_Number",
    "Select_Attribute",
    "Select_Bonded",
    "Select_Chain_",
    "Select_Cube",
    "Select_Element",
    "Select_Entity_",
    "Select_Ligand_",
    "Select_Proximity",
    "Select_Res_ID",
    "Select_Res_ID_Range",
    "Select_Res_ID_",
    "Select_Res_Name",
    "Select_Res_Whole",
    "Select_Segment_",
    "Select_Sphere",
    "Self_Sample_Proximity",
    "Separate_Atoms",
    "Separate_Polymers",
    "Set_Color",
    "Starfile_Instances",
    "Style_Ball_and_Stick",
    "Style_Cartoon",
    "Style_Density_Surface",
    "Style_Density_Wire",
    "Style_Preset_1",
    "Style_Preset_2",
    "Style_Preset_3",
    "Style_Preset_4",
    "Style_Ribbon",
    "Style_Spheres",
    "Style_Sticks",
    "Style_Surface",
    "Topology_Break_Bonds",
    "Topology_DSSP",
    "Topology_Find_Bonds",
    "Utils_ZYZ_to_Rotation",
    "Vector_Angle",
    "World_to_Angstrom",
]


def register():
    bpy.utils.register_class(_atoms_to_curves)
    bpy.utils.register_class(_Base_align)
    bpy.utils.register_class(_bs_smooth)
    bpy.utils.register_class(_cartoon_arrow_primitive)
    bpy.utils.register_class(_cartoon_arrow_instance)
    bpy.utils.register_class(_cartoon_arrows_scale)
    bpy.utils.register_class(_curve_custom_profile)
    bpy.utils.register_class(_curve_end_fix_color)
    bpy.utils.register_class(_curve_ends_adjust_angle)
    bpy.utils.register_class(_curve_profile_backup)
    bpy.utils.register_class(_curve_to_mesh)
    bpy.utils.register_class(_DEBUG_arrows)
    bpy.utils.register_class(_DSSP_Sheet_Checks)
    bpy.utils.register_class(_expand_selection)
    bpy.utils.register_class(_field_offset)
    bpy.utils.register_class(_field_offset_bool)
    bpy.utils.register_class(_field_offset_vec)
    bpy.utils.register_class(_guide_rotation)
    bpy.utils.register_class(_HBond_i___1__j___1__and_HBond_j___1__i___1_)
    bpy.utils.register_class(_Hbond_i___1_j__and_Hbond_j_i___1_)
    bpy.utils.register_class(_HBond_i__j__and_HBond_j__i_)
    bpy.utils.register_class(_Hbond_j___1_i_and_Hbond_i_j___1_)
    bpy.utils.register_class(_is_odd)
    bpy.utils.register_class(_MN_animate_falloff_empty)
    bpy.utils.register_class(_MN_animate_falloff_points)
    bpy.utils.register_class(_MN_animate_field)
    bpy.utils.register_class(_MN_animate_wiggle_mask_length)
    bpy.utils.register_class(_MN_animate_wiggle_mask_res)
    bpy.utils.register_class(_MN_assembly_instance_chains)
    bpy.utils.register_class(_MN_assembly_rotate)
    bpy.utils.register_class(_MN_cartoon_bs_alternate_axis)
    bpy.utils.register_class(_MN_cartoon_smooth_handles)
    bpy.utils.register_class(_MN_constants_atom_name_nucleic)
    bpy.utils.register_class(_MN_constants_atom_name_peptide)
    bpy.utils.register_class(_MN_point_curve_trails)
    bpy.utils.register_class(_MN_select_attribute)
    bpy.utils.register_class(_MN_select_nucleic)
    bpy.utils.register_class(_MN_select_peptide)
    bpy.utils.register_class(_MN_select_res_name_peptide)
    bpy.utils.register_class(_MN_select_sec_struct)
    bpy.utils.register_class(_MN_select_sec_struct_id)
    bpy.utils.register_class(_MN_surface_smooth_bumps)
    bpy.utils.register_class(_MN_topo_assign_backbone)
    bpy.utils.register_class(_MN_topo_calc_helix)
    bpy.utils.register_class(_MN_topo_calc_sheet)
    bpy.utils.register_class(_MN_topo_phi_psi)
    bpy.utils.register_class(_MN_utils_aa_atom_pos)
    bpy.utils.register_class(_MN_utils_bio_assembly)
    bpy.utils.register_class(_MN_utils_int_multiply)
    bpy.utils.register_class(_MN_utils_rotate_res)
    bpy.utils.register_class(_MN_utils_split_instance)
    bpy.utils.register_class(_MN_utils_style_cartoon)
    bpy.utils.register_class(_MN_utils_style_old_ball_and_stick)
    bpy.utils.register_class(_MN_utils_style_ribbon_nucleic)
    bpy.utils.register_class(_MN_utils_style_ribbon_peptide)
    bpy.utils.register_class(_MN_utils_style_spheres_icosphere)
    bpy.utils.register_class(_MN_utils_style_spheres_points)
    bpy.utils.register_class(_MN_utils_style_sticks)
    bpy.utils.register_class(_MN_utils_style_surface_new)
    bpy.utils.register_class(_MN_utils_style_surface_old)
    bpy.utils.register_class(_MN_utils_to_instance_centred)
    bpy.utils.register_class(_MN_world_scale)
    bpy.utils.register_class(_SampleAtomValue)
    bpy.utils.register_class(_sec_struct_counter)
    bpy.utils.register_class(_selective_scale)
    bpy.utils.register_class(_surface_blur_color)
    bpy.utils.register_class(_surface_blur_postion)
    bpy.utils.register_class(_surface_compute_density_from_points)
    bpy.utils.register_class(_surface_sample_color)
    bpy.utils.register_class(_Topo_Count_Atoms)
    bpy.utils.register_class(_Topo_Count_Residues)
    bpy.utils.register_class(_utils_bounding_box)
    bpy.utils.register_class(_utils_group_field_at_selection)
    bpy.utils.register_class(_utils_oxdna_base)
    bpy.utils.register_class(_2_Point_Angle)
    bpy.utils.register_class(_3_Point_Angle)
    bpy.utils.register_class(_curve_ends_adjust_position)
    bpy.utils.register_class(Animate_Collection_Pick)
    bpy.utils.register_class(Animate_Fraction)
    bpy.utils.register_class(Animate_Frames)
    bpy.utils.register_class(Animate_Peptide_to_Curve)
    bpy.utils.register_class(Animate_Trails)
    bpy.utils.register_class(Animate_Value)
    bpy.utils.register_class(Animate_Wiggle)
    bpy.utils.register_class(Attribute_Map)
    bpy.utils.register_class(Backbone_NH)
    bpy.utils.register_class(Backbone_Position)
    bpy.utils.register_class(Backbone_Positions)
    bpy.utils.register_class(Between_Float)
    bpy.utils.register_class(Between_Integer)
    bpy.utils.register_class(Between_Vector)
    bpy.utils.register_class(Bond_Count)
    bpy.utils.register_class(Boolean_Run_Fill)
    bpy.utils.register_class(Boolean_Run_Mask)
    bpy.utils.register_class(Centre_on_Selection)
    bpy.utils.register_class(Centroid)
    bpy.utils.register_class(Chain_Info)
    bpy.utils.register_class(Color_Atomic_Number)
    bpy.utils.register_class(Color_Attribute_Map)
    bpy.utils.register_class(Color_Attribute_Random)
    bpy.utils.register_class(Color_Backbone)
    bpy.utils.register_class(Color_Chain_)
    bpy.utils.register_class(Color_Common)
    bpy.utils.register_class(Color_Element)
    bpy.utils.register_class(Color_Entity_)
    bpy.utils.register_class(Color_Goodsell)
    bpy.utils.register_class(Color_Ligand_)
    bpy.utils.register_class(Color_pLDDT)
    bpy.utils.register_class(Color_Rainbow)
    bpy.utils.register_class(Color_Res_Name)
    bpy.utils.register_class(Color_Res_Name_Nucleic)
    bpy.utils.register_class(Color_Sec_Struct)
    bpy.utils.register_class(Color_Segment_)
    bpy.utils.register_class(Dihedral_Angle)
    bpy.utils.register_class(Dihedral_Phi)
    bpy.utils.register_class(Dihedral_Psi)
    bpy.utils.register_class(Edge_Info)
    bpy.utils.register_class(Ensemble_Instance)
    bpy.utils.register_class(Fallback_Boolean)
    bpy.utils.register_class(Fallback_Color)
    bpy.utils.register_class(Fallback_Float)
    bpy.utils.register_class(Fallback_Integer)
    bpy.utils.register_class(Fallback_Vector)
    bpy.utils.register_class(Group_Info)
    bpy.utils.register_class(Group_Pick)
    bpy.utils.register_class(Group_Pick_Vector)
    bpy.utils.register_class(HBond_Backbone_Check)
    bpy.utils.register_class(HBond_Backbone_Check_backup)
    bpy.utils.register_class(HBond_Energy)
    bpy.utils.register_class(Helix_Detect)
    bpy.utils.register_class(Is_Alpha_Carbon)
    bpy.utils.register_class(Is_Backbone)
    bpy.utils.register_class(Is_Helix)
    bpy.utils.register_class(Is_Lipid)
    bpy.utils.register_class(Is_Loop)
    bpy.utils.register_class(Is_Nucleic)
    bpy.utils.register_class(Is_Peptide)
    bpy.utils.register_class(Is_Sheet)
    bpy.utils.register_class(Is_Side_Chain)
    bpy.utils.register_class(Is_Solvent)
    bpy.utils.register_class(MN_Units)
    bpy.utils.register_class(MN_animate_noise_field)
    bpy.utils.register_class(MN_animate_noise_position)
    bpy.utils.register_class(MN_animate_noise_repeat)
    bpy.utils.register_class(MN_assembly_)
    bpy.utils.register_class(MN_assembly_center)
    bpy.utils.register_class(MN_dna_bases)
    bpy.utils.register_class(MN_dna_double_helix)
    bpy.utils.register_class(MN_dna_style_ball_and_stick)
    bpy.utils.register_class(MN_dna_style_spheres_cycles)
    bpy.utils.register_class(MN_dna_style_spheres_eevee)
    bpy.utils.register_class(MN_dna_style_surface)
    bpy.utils.register_class(MN_oxdna_style_ribbon)
    bpy.utils.register_class(MN_select_distance_empty)
    bpy.utils.register_class(MN_select_nucleic_type)
    bpy.utils.register_class(MN_Starfile_Micrograph)
    bpy.utils.register_class(MN_style_surface_old)
    bpy.utils.register_class(MN_topo_backbone)
    bpy.utils.register_class(MN_utils_curve_resample)
    bpy.utils.register_class(MN_utils_extend_curve)
    bpy.utils.register_class(MN_utils_helix)
    bpy.utils.register_class(MN_utils_primitive_atom)
    bpy.utils.register_class(NodeGroup_001)
    bpy.utils.register_class(NodeStorage)
    bpy.utils.register_class(Offset_Boolean)
    bpy.utils.register_class(Offset_Color)
    bpy.utils.register_class(Offset_Float)
    bpy.utils.register_class(Offset_Integer)
    bpy.utils.register_class(Offset_Vector)
    bpy.utils.register_class(Point_Distance)
    bpy.utils.register_class(Point_Edge_Angle)
    bpy.utils.register_class(Points_of_Edge)
    bpy.utils.register_class(Res_Group_ID)
    bpy.utils.register_class(Res_Info)
    bpy.utils.register_class(Residue_Mask)
    bpy.utils.register_class(Sample_Mix_Float)
    bpy.utils.register_class(Sample_Mix_Vector)
    bpy.utils.register_class(Sample_Nearest_Atoms)
    bpy.utils.register_class(Select_Atomic_Number)
    bpy.utils.register_class(Select_Attribute)
    bpy.utils.register_class(Select_Bonded)
    bpy.utils.register_class(Select_Chain_)
    bpy.utils.register_class(Select_Cube)
    bpy.utils.register_class(Select_Element)
    bpy.utils.register_class(Select_Entity_)
    bpy.utils.register_class(Select_Ligand_)
    bpy.utils.register_class(Select_Proximity)
    bpy.utils.register_class(Select_Res_ID)
    bpy.utils.register_class(Select_Res_ID_Range)
    bpy.utils.register_class(Select_Res_ID_)
    bpy.utils.register_class(Select_Res_Name)
    bpy.utils.register_class(Select_Res_Whole)
    bpy.utils.register_class(Select_Segment_)
    bpy.utils.register_class(Select_Sphere)
    bpy.utils.register_class(Self_Sample_Proximity)
    bpy.utils.register_class(Separate_Atoms)
    bpy.utils.register_class(Separate_Polymers)
    bpy.utils.register_class(Set_Color)
    bpy.utils.register_class(Starfile_Instances)
    bpy.utils.register_class(Style_Ball_and_Stick)
    bpy.utils.register_class(Style_Cartoon)
    bpy.utils.register_class(Style_Density_Surface)
    bpy.utils.register_class(Style_Density_Wire)
    bpy.utils.register_class(Style_Preset_1)
    bpy.utils.register_class(Style_Preset_2)
    bpy.utils.register_class(Style_Preset_3)
    bpy.utils.register_class(Style_Preset_4)
    bpy.utils.register_class(Style_Ribbon)
    bpy.utils.register_class(Style_Spheres)
    bpy.utils.register_class(Style_Sticks)
    bpy.utils.register_class(Style_Surface)
    bpy.utils.register_class(Topology_Break_Bonds)
    bpy.utils.register_class(Topology_DSSP)
    bpy.utils.register_class(Topology_Find_Bonds)
    bpy.utils.register_class(Utils_ZYZ_to_Rotation)
    bpy.utils.register_class(Vector_Angle)
    bpy.utils.register_class(World_to_Angstrom)


def unregister():
    bpy.utils.unregister_class(_atoms_to_curves)
    bpy.utils.unregister_class(_Base_align)
    bpy.utils.unregister_class(_bs_smooth)
    bpy.utils.unregister_class(_cartoon_arrow_primitive)
    bpy.utils.unregister_class(_cartoon_arrow_instance)
    bpy.utils.unregister_class(_cartoon_arrows_scale)
    bpy.utils.unregister_class(_curve_custom_profile)
    bpy.utils.unregister_class(_curve_end_fix_color)
    bpy.utils.unregister_class(_curve_ends_adjust_angle)
    bpy.utils.unregister_class(_curve_profile_backup)
    bpy.utils.unregister_class(_curve_to_mesh)
    bpy.utils.unregister_class(_DEBUG_arrows)
    bpy.utils.unregister_class(_DSSP_Sheet_Checks)
    bpy.utils.unregister_class(_expand_selection)
    bpy.utils.unregister_class(_field_offset)
    bpy.utils.unregister_class(_field_offset_bool)
    bpy.utils.unregister_class(_field_offset_vec)
    bpy.utils.unregister_class(_guide_rotation)
    bpy.utils.unregister_class(_HBond_i___1__j___1__and_HBond_j___1__i___1_)
    bpy.utils.unregister_class(_Hbond_i___1_j__and_Hbond_j_i___1_)
    bpy.utils.unregister_class(_HBond_i__j__and_HBond_j__i_)
    bpy.utils.unregister_class(_Hbond_j___1_i_and_Hbond_i_j___1_)
    bpy.utils.unregister_class(_is_odd)
    bpy.utils.unregister_class(_MN_animate_falloff_empty)
    bpy.utils.unregister_class(_MN_animate_falloff_points)
    bpy.utils.unregister_class(_MN_animate_field)
    bpy.utils.unregister_class(_MN_animate_wiggle_mask_length)
    bpy.utils.unregister_class(_MN_animate_wiggle_mask_res)
    bpy.utils.unregister_class(_MN_assembly_instance_chains)
    bpy.utils.unregister_class(_MN_assembly_rotate)
    bpy.utils.unregister_class(_MN_cartoon_bs_alternate_axis)
    bpy.utils.unregister_class(_MN_cartoon_smooth_handles)
    bpy.utils.unregister_class(_MN_constants_atom_name_nucleic)
    bpy.utils.unregister_class(_MN_constants_atom_name_peptide)
    bpy.utils.unregister_class(_MN_point_curve_trails)
    bpy.utils.unregister_class(_MN_select_attribute)
    bpy.utils.unregister_class(_MN_select_nucleic)
    bpy.utils.unregister_class(_MN_select_peptide)
    bpy.utils.unregister_class(_MN_select_res_name_peptide)
    bpy.utils.unregister_class(_MN_select_sec_struct)
    bpy.utils.unregister_class(_MN_select_sec_struct_id)
    bpy.utils.unregister_class(_MN_surface_smooth_bumps)
    bpy.utils.unregister_class(_MN_topo_assign_backbone)
    bpy.utils.unregister_class(_MN_topo_calc_helix)
    bpy.utils.unregister_class(_MN_topo_calc_sheet)
    bpy.utils.unregister_class(_MN_topo_phi_psi)
    bpy.utils.unregister_class(_MN_utils_aa_atom_pos)
    bpy.utils.unregister_class(_MN_utils_bio_assembly)
    bpy.utils.unregister_class(_MN_utils_int_multiply)
    bpy.utils.unregister_class(_MN_utils_rotate_res)
    bpy.utils.unregister_class(_MN_utils_split_instance)
    bpy.utils.unregister_class(_MN_utils_style_cartoon)
    bpy.utils.unregister_class(_MN_utils_style_old_ball_and_stick)
    bpy.utils.unregister_class(_MN_utils_style_ribbon_nucleic)
    bpy.utils.unregister_class(_MN_utils_style_ribbon_peptide)
    bpy.utils.unregister_class(_MN_utils_style_spheres_icosphere)
    bpy.utils.unregister_class(_MN_utils_style_spheres_points)
    bpy.utils.unregister_class(_MN_utils_style_sticks)
    bpy.utils.unregister_class(_MN_utils_style_surface_new)
    bpy.utils.unregister_class(_MN_utils_style_surface_old)
    bpy.utils.unregister_class(_MN_utils_to_instance_centred)
    bpy.utils.unregister_class(_MN_world_scale)
    bpy.utils.unregister_class(_SampleAtomValue)
    bpy.utils.unregister_class(_sec_struct_counter)
    bpy.utils.unregister_class(_selective_scale)
    bpy.utils.unregister_class(_surface_blur_color)
    bpy.utils.unregister_class(_surface_blur_postion)
    bpy.utils.unregister_class(_surface_compute_density_from_points)
    bpy.utils.unregister_class(_surface_sample_color)
    bpy.utils.unregister_class(_Topo_Count_Atoms)
    bpy.utils.unregister_class(_Topo_Count_Residues)
    bpy.utils.unregister_class(_utils_bounding_box)
    bpy.utils.unregister_class(_utils_group_field_at_selection)
    bpy.utils.unregister_class(_utils_oxdna_base)
    bpy.utils.unregister_class(_2_Point_Angle)
    bpy.utils.unregister_class(_3_Point_Angle)
    bpy.utils.unregister_class(_curve_ends_adjust_position)
    bpy.utils.unregister_class(Animate_Collection_Pick)
    bpy.utils.unregister_class(Animate_Fraction)
    bpy.utils.unregister_class(Animate_Frames)
    bpy.utils.unregister_class(Animate_Peptide_to_Curve)
    bpy.utils.unregister_class(Animate_Trails)
    bpy.utils.unregister_class(Animate_Value)
    bpy.utils.unregister_class(Animate_Wiggle)
    bpy.utils.unregister_class(Attribute_Map)
    bpy.utils.unregister_class(Backbone_NH)
    bpy.utils.unregister_class(Backbone_Position)
    bpy.utils.unregister_class(Backbone_Positions)
    bpy.utils.unregister_class(Between_Float)
    bpy.utils.unregister_class(Between_Integer)
    bpy.utils.unregister_class(Between_Vector)
    bpy.utils.unregister_class(Bond_Count)
    bpy.utils.unregister_class(Boolean_Run_Fill)
    bpy.utils.unregister_class(Boolean_Run_Mask)
    bpy.utils.unregister_class(Centre_on_Selection)
    bpy.utils.unregister_class(Centroid)
    bpy.utils.unregister_class(Chain_Info)
    bpy.utils.unregister_class(Color_Atomic_Number)
    bpy.utils.unregister_class(Color_Attribute_Map)
    bpy.utils.unregister_class(Color_Attribute_Random)
    bpy.utils.unregister_class(Color_Backbone)
    bpy.utils.unregister_class(Color_Chain_)
    bpy.utils.unregister_class(Color_Common)
    bpy.utils.unregister_class(Color_Element)
    bpy.utils.unregister_class(Color_Entity_)
    bpy.utils.unregister_class(Color_Goodsell)
    bpy.utils.unregister_class(Color_Ligand_)
    bpy.utils.unregister_class(Color_pLDDT)
    bpy.utils.unregister_class(Color_Rainbow)
    bpy.utils.unregister_class(Color_Res_Name)
    bpy.utils.unregister_class(Color_Res_Name_Nucleic)
    bpy.utils.unregister_class(Color_Sec_Struct)
    bpy.utils.unregister_class(Color_Segment_)
    bpy.utils.unregister_class(Dihedral_Angle)
    bpy.utils.unregister_class(Dihedral_Phi)
    bpy.utils.unregister_class(Dihedral_Psi)
    bpy.utils.unregister_class(Edge_Info)
    bpy.utils.unregister_class(Ensemble_Instance)
    bpy.utils.unregister_class(Fallback_Boolean)
    bpy.utils.unregister_class(Fallback_Color)
    bpy.utils.unregister_class(Fallback_Float)
    bpy.utils.unregister_class(Fallback_Integer)
    bpy.utils.unregister_class(Fallback_Vector)
    bpy.utils.unregister_class(Group_Info)
    bpy.utils.unregister_class(Group_Pick)
    bpy.utils.unregister_class(Group_Pick_Vector)
    bpy.utils.unregister_class(HBond_Backbone_Check)
    bpy.utils.unregister_class(HBond_Backbone_Check_backup)
    bpy.utils.unregister_class(HBond_Energy)
    bpy.utils.unregister_class(Helix_Detect)
    bpy.utils.unregister_class(Is_Alpha_Carbon)
    bpy.utils.unregister_class(Is_Backbone)
    bpy.utils.unregister_class(Is_Helix)
    bpy.utils.unregister_class(Is_Lipid)
    bpy.utils.unregister_class(Is_Loop)
    bpy.utils.unregister_class(Is_Nucleic)
    bpy.utils.unregister_class(Is_Peptide)
    bpy.utils.unregister_class(Is_Sheet)
    bpy.utils.unregister_class(Is_Side_Chain)
    bpy.utils.unregister_class(Is_Solvent)
    bpy.utils.unregister_class(MN_Units)
    bpy.utils.unregister_class(MN_animate_noise_field)
    bpy.utils.unregister_class(MN_animate_noise_position)
    bpy.utils.unregister_class(MN_animate_noise_repeat)
    bpy.utils.unregister_class(MN_assembly_)
    bpy.utils.unregister_class(MN_assembly_center)
    bpy.utils.unregister_class(MN_dna_bases)
    bpy.utils.unregister_class(MN_dna_double_helix)
    bpy.utils.unregister_class(MN_dna_style_ball_and_stick)
    bpy.utils.unregister_class(MN_dna_style_spheres_cycles)
    bpy.utils.unregister_class(MN_dna_style_spheres_eevee)
    bpy.utils.unregister_class(MN_dna_style_surface)
    bpy.utils.unregister_class(MN_oxdna_style_ribbon)
    bpy.utils.unregister_class(MN_select_distance_empty)
    bpy.utils.unregister_class(MN_select_nucleic_type)
    bpy.utils.unregister_class(MN_Starfile_Micrograph)
    bpy.utils.unregister_class(MN_style_surface_old)
    bpy.utils.unregister_class(MN_topo_backbone)
    bpy.utils.unregister_class(MN_utils_curve_resample)
    bpy.utils.unregister_class(MN_utils_extend_curve)
    bpy.utils.unregister_class(MN_utils_helix)
    bpy.utils.unregister_class(MN_utils_primitive_atom)
    bpy.utils.unregister_class(NodeGroup_001)
    bpy.utils.unregister_class(NodeStorage)
    bpy.utils.unregister_class(Offset_Boolean)
    bpy.utils.unregister_class(Offset_Color)
    bpy.utils.unregister_class(Offset_Float)
    bpy.utils.unregister_class(Offset_Integer)
    bpy.utils.unregister_class(Offset_Vector)
    bpy.utils.unregister_class(Point_Distance)
    bpy.utils.unregister_class(Point_Edge_Angle)
    bpy.utils.unregister_class(Points_of_Edge)
    bpy.utils.unregister_class(Res_Group_ID)
    bpy.utils.unregister_class(Res_Info)
    bpy.utils.unregister_class(Residue_Mask)
    bpy.utils.unregister_class(Sample_Mix_Float)
    bpy.utils.unregister_class(Sample_Mix_Vector)
    bpy.utils.unregister_class(Sample_Nearest_Atoms)
    bpy.utils.unregister_class(Select_Atomic_Number)
    bpy.utils.unregister_class(Select_Attribute)
    bpy.utils.unregister_class(Select_Bonded)
    bpy.utils.unregister_class(Select_Chain_)
    bpy.utils.unregister_class(Select_Cube)
    bpy.utils.unregister_class(Select_Element)
    bpy.utils.unregister_class(Select_Entity_)
    bpy.utils.unregister_class(Select_Ligand_)
    bpy.utils.unregister_class(Select_Proximity)
    bpy.utils.unregister_class(Select_Res_ID)
    bpy.utils.unregister_class(Select_Res_ID_Range)
    bpy.utils.unregister_class(Select_Res_ID_)
    bpy.utils.unregister_class(Select_Res_Name)
    bpy.utils.unregister_class(Select_Res_Whole)
    bpy.utils.unregister_class(Select_Segment_)
    bpy.utils.unregister_class(Select_Sphere)
    bpy.utils.unregister_class(Self_Sample_Proximity)
    bpy.utils.unregister_class(Separate_Atoms)
    bpy.utils.unregister_class(Separate_Polymers)
    bpy.utils.unregister_class(Set_Color)
    bpy.utils.unregister_class(Starfile_Instances)
    bpy.utils.unregister_class(Style_Ball_and_Stick)
    bpy.utils.unregister_class(Style_Cartoon)
    bpy.utils.unregister_class(Style_Density_Surface)
    bpy.utils.unregister_class(Style_Density_Wire)
    bpy.utils.unregister_class(Style_Preset_1)
    bpy.utils.unregister_class(Style_Preset_2)
    bpy.utils.unregister_class(Style_Preset_3)
    bpy.utils.unregister_class(Style_Preset_4)
    bpy.utils.unregister_class(Style_Ribbon)
    bpy.utils.unregister_class(Style_Spheres)
    bpy.utils.unregister_class(Style_Sticks)
    bpy.utils.unregister_class(Style_Surface)
    bpy.utils.unregister_class(Topology_Break_Bonds)
    bpy.utils.unregister_class(Topology_DSSP)
    bpy.utils.unregister_class(Topology_Find_Bonds)
    bpy.utils.unregister_class(Utils_ZYZ_to_Rotation)
    bpy.utils.unregister_class(Vector_Angle)
    bpy.utils.unregister_class(World_to_Angstrom)
