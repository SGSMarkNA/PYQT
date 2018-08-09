import pymel.core as pm
import pymel.core.nodetypes as pm_nt
import maya.cmds as cmds
from ..DATA_TYPES import Item_Data_Storage

########################################################################
class Base_Maya_Node_Data(Item_Data_Storage.Maya_Node_Icon_Data):
	""""""
	#----------------------------------------------------------------------
	def _get_display_name(self):
		return super(Base_Maya_Node_Data,self)._get_display_name()
		
	#----------------------------------------------------------------------
	def _set_display_name(self, value):
		super(Base_Maya_Node_Data,self)._set_display_name(value)
		
	display_name = property(_get_display_name,_set_display_name)
		
########################################################################
class Base_Maya_Plug_Data(Item_Data_Storage.Maya_Plug_Data):
	""""""
	#----------------------------------------------------------------------
########################################################################
class Base_Maya_Plug_Uneditalbe_Data(Item_Data_Storage.Maya_Plug_Uneditalbe_Data):
	""""""
	#----------------------------------------------------------------------

