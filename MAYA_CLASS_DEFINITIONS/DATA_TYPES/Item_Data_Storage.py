import PYQT
from PYQT.BASE_CLASS_DEFINITIONS.DATA_TYPES import Item_Data_Storage
from outliner_icons import *
from ..Item_Data_Roles import Maya_Item_Data_Roles
import maya.api.OpenMaya as OM
import maya.cmds as cmds
import pymel.core as pm
from xml.etree import ElementTree as etree
import os
#----------------------------------------------------------------------
def _build_Outliner_Icon_Dict_Lookup():
	""""""
	res = {}
	file_path = os.path.join(os.path.dirname(__file__),"Outline_Icons","outliner_icons.qrc")
	tree = etree.parse(file_path)
	root = tree.getroot()
	child = root.getchildren()[0]	
	for elem in child.getchildren():
		res[elem.attrib["alias"]] = ":/out/"+elem.attrib["alias"]
	return res

_Global_Outline_Icon_Lookup = _build_Outliner_Icon_Dict_Lookup()

#----------------------------------------------------------------------
def create_Outline_Icon(node_type_name):
	global _Global_Outline_Icon_Lookup
	if not node_type_name in _Global_Outline_Icon_Lookup.keys():
		node_type_name = "default"
	lookup_val = _Global_Outline_Icon_Lookup[node_type_name]
	if isinstance(lookup_val, str):
		pixmap       = PYQT.QPixmap(lookup_val)
		lookup_val   = PYQT.QIcon(pixmap)
		_Global_Outline_Icon_Lookup[node_type_name] = lookup_val
	return lookup_val

#----------------------------------------------------------------------
def name_To_MObject(name):
	""""""
	if not cmds.objExists(name):
		raise LookupError("'{}' Can Not Be Converted To an MObject Becasue It Does Not Exist".format(name))
	sel_list = OM.MSelectionList()
	sel_list.add(name)
	res = sel_list.getDependNode(0)
	isinstance(res,OM.MObject)
	return res

#----------------------------------------------------------------------
def get_Node_MFn_Set(mobject):
	""""""
	if mobject.hasFn(OM.MFn.kDagNode):
		return OM.MFnDagNode(mobject)
	elif mobject.hasFn(OM.MFn.kDependencyNode):
		return OM.MFnDependencyNode(mobject)
	else:
		raise LookupError("Could Not Find A Vaild Function Set For The Input MObject")

########################################################################
class Standered_Item_Data(Item_Data_Storage.Standered_Item_Data):
	"""This Is The Base Item Data Class It Only Stores Data That Is Needed To Display Itself"""
	#----------------------------------------------------------------------
	def __init__(self,**kwargs):
		super(Standered_Item_Data,self).__init__(tree_item       = kwargs.get("tree_item"),
	                                        selectable           = kwargs.get("selectable"),           enabled             = kwargs.get("enabled"),            editable     = kwargs.get("editable"),
	                                        dragable             = kwargs.get("dragable"),             dropable            = kwargs.get("dropable"),
	                                        checkable            = kwargs.get("checkable"),            tristate            = kwargs.get("tristate"),
	                                        font_family          = kwargs.get("font_family"),          font_size           = kwargs.get("font_size"),
	                                        size_hint            = kwargs.get("size_hint"),            status_tip          = kwargs.get("status_tip"),          tool_tip     = kwargs.get("tool_tip"),
	                                        brush                = kwargs.get("brush"),                icon_visable        = kwargs.get("icon_visable"),        icon_color   = kwargs.get("icon_color"),
	                                        font_weight          = kwargs.get("font_weight"),          font_capitalization = kwargs.get("font_capitalization"), display_name = kwargs.get("display_name"),
	                                        background_color     = kwargs.get("background_color"),     foreground_color    = kwargs.get("foreground_color"),
	                                        horizontal_alignment = kwargs.get("horizontal_alignment"), vertical_alignment  = kwargs.get("vertical_alignment"))

########################################################################
class Internal_Item_Data(Standered_Item_Data):
	"""This Is The Item Data Class For Use If Any Costom Data Needs To Be Accesed This Data Is Contained in the internal_data attribute"""
	#----------------------------------------------------------------------
	def __init__(self,**kwargs):
		""" """
		super(Internal_Item_Data, self).__init__(**kwargs)
		self._internal_data = kwargs.get("internal_data")
	#----------------------------------------------------------------------
	def data(self, role=Maya_Item_Data_Roles.DISPLAY):
		if role == Maya_Item_Data_Roles.INTERNAL_DATA:
			return self._internal_data
		return super(Internal_Item_Data, self).data(role)
	#----------------------------------------------------------------------
	def setData(self, role, value):
		if role == Maya_Item_Data_Roles.INTERNAL_DATA:
			self.internal_data = value
			res = True
		else:
			res = super(Internal_Item_Data, self).setData(role, value)
		if res:
			self._update_Changed_Data(role)
		return res
	#----------------------------------------------------------------------
	@property
	def internal_data(self):
		""""""
		return self._internal_data
	#----------------------------------------------------------------------
	@internal_data.setter
	def internal_data(self, value):
		""""""
		self._internal_data = value

########################################################################
class Maya_Plug_Data(Internal_Item_Data):
	"""This Is The Base Item Data Class It Only Stores Data That Is Needed To Display Itself"""
	#----------------------------------------------------------------------
	def __init__(self, plug,**kwargs):
		self._py_node = None
		if isinstance(plug,pm.Attribute):
			self._py_node = plug
		elif isinstance(plug,basestring):
			self._py_node = pm.PyNode(plug)
		else:
			raise ValueError("Invalid input type given")
		if not isinstance(self._py_node,pm.Attribute):
			raise TypeError("The Input Plug {} Was Not A Attribute".format(self._py_node.name()))
		kwargs["internal_data"] = self._py_node
		super(Maya_Plug_Data,self).__init__(**kwargs)
		## WING IDE CODE COMPLEASHION ##
		if False:
			isinstance(self.internal_data,pm.Attribute)
	#----------------------------------------------------------------------
	def data(self, role=Maya_Item_Data_Roles.DISPLAY):
		if role in Maya_Item_Data_Roles.DP_ED:
			return self.display_value
		return super(Maya_Plug_Data, self).data(role)
	#----------------------------------------------------------------------
	def setData(self, role, value):
		if role == Maya_Item_Data_Roles.EDIT:
			self.display_value = value
			res = True
		else:
			res = super(Maya_Plug_Data, self).setData(role, value)
		if res:
			self._update_Changed_Data(role)
		return res
	#----------------------------------------------------------------------
	def _get_display_name(self):
		if self.internal_data.exists():
			return self.internal_data.name(includeNode=False, longName=True)
		else:
			return "unknown"
	#----------------------------------------------------------------------
	def _set_display_name(self, value):
		pass
	#----------------------------------------------------------------------
	display_name = property(_get_display_name,_set_display_name)
	#----------------------------------------------------------------------
	def _get_display_value(self):
		if self.internal_data.exists():
			return self.internal_data.get()
		else:
			return "unknown"
	#----------------------------------------------------------------------
	def _set_display_value(self, value):
		if self.internal_data.exists():
			return self.internal_data.set(value)
		else:
			return "unknown"
	#----------------------------------------------------------------------
	display_value = property(_get_display_value,_set_display_value)
#----------------------------------------------------------------------
########################################################################
class Maya_Plug_Uneditalbe_Data(Maya_Plug_Data):
	"""This Is The Base Item Data Class It Only Stores Data That Is Needed To Display Itself"""
	#----------------------------------------------------------------------
	def __init__(self, plug,**kwargs):
		kwargs["editable"]=False
		super(Maya_Plug_Uneditalbe_Data,self).__init__(plug,**kwargs)
########################################################################
class Maya_Node_Data(Internal_Item_Data):
	"""This Is The Base Item Data Class It Only Stores Data That Is Needed To Display Itself"""
	#----------------------------------------------------------------------
	def __init__(self, node,**kwargs):
		self._py_node = None
		if isinstance(node,pm.PyNode):
			mobject = name_To_MObject(node.name())
			self._py_node = node
		elif isinstance(node,basestring):
			mobject = name_To_MObject(str(node))
		elif isinstance(node,OM.MObject):
			mobject = node
		else:
			raise ValueError("Invalid input type given")
		
		self._Mobject_handle = OM.MObjectHandle(mobject)
		self._MFn_set        = get_Node_MFn_Set(mobject)
		if self._py_node is None:
			if mobject.hasFn(OM.MFn.kDagNode):
				self._py_node = pm.PyNode(self._MFn_set.fullPathName())
			else:
				self._py_node = pm.PyNode(self._MFn_set.name())
		kwargs["internal_data"] = self._py_node
		super(Maya_Node_Data,self).__init__(**kwargs)
		## WING IDE CODE COMPLEASHION ##
		if False:
			isinstance(self.internal_data,pm.nodetypes.Transform)
	#----------------------------------------------------------------------
	def _get_display_name(self):
		if self.internal_data.exists():
			return self.internal_data.nodeName()
		else:
			return "unknown"
	#----------------------------------------------------------------------
	def _set_display_name(self, value):
		if self._Mobject_handle.isValid():
			if not isinstance(value,(str, unicode)):
				raise ValueError("input value must be an instance of (str,unicode) and a %r was given" % type(value))
			self.internal_data.rename(value)
	#----------------------------------------------------------------------
	display_name = property(_get_display_name,_set_display_name)
#----------------------------------------------------------------------

########################################################################
class Maya_Node_Icon_Data(Maya_Node_Data):
	"""This Is The Base Item Data Class It Only Stores Data That Is Needed To Display Itself"""
	#----------------------------------------------------------------------
	def __init__(self, node,**kwargs):
		
		super(Maya_Node_Icon_Data,self).__init__(node,**kwargs)
		if self.internal_data.type() == "transform":
			shapes = self.internal_data.getShapes()
			if len(shapes):
				shape = shapes[0]
			self.icon = create_Outline_Icon(shape.type())
		else:
			self.icon = create_Outline_Icon(self.internal_data.type())
		self.icon_visable = True

########################################################################
class Maya_Node_Uneditalbe_Data(Maya_Node_Data):
	"""This Is The Base Item Data Class It Only Stores Data That Is Needed To Display Itself"""
	#----------------------------------------------------------------------
	def __init__(self, node,**kwargs):
		kwargs["editable"]=False
		super(Maya_Node_Uneditalbe_Data,self).__init__(node,**kwargs)	
########################################################################
class Maya_Node_Type_Data(Maya_Node_Uneditalbe_Data):
	"""This Is The Base Item Data Class It Only Stores Data That Is Needed To Display Itself"""
	#----------------------------------------------------------------------
	def _get_display_name(self):
		if self.internal_data.exists():
			return self.internal_data.type()
		else:
			return "unknown"
	#----------------------------------------------------------------------
	def _set_display_name(self, value):
		pass
	display_name = property(_get_display_name)
########################################################################
class Maya_Node_Uuid_Data(Maya_Node_Uneditalbe_Data):
	"""This Is The Base Item Data Class It Only Stores Data That Is Needed To Display Itself"""
	#----------------------------------------------------------------------
	def _get_display_name(self):
		if self._Mobject_handle.isValid():
			return self._MFn_set.uuid().asString()
		else:
			return "unknown"
	display_name = property(_get_display_name)

########################################################################
class Column_Item_List(Item_Data_Storage.Column_Item_List):
	#----------------------------------------------------------------------
	def __init__(self, tree_item):
		""" """
		super(Column_Item_List,self).__init__(tree_item)