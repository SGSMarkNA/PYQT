import pymel.core as pm
import PYQT.BASE_CLASS_DEFINITIONS.DATA_MODELS
import PYQT.BASE_CLASS_DEFINITIONS.DATA_TYPES
DATA_MODELS = PYQT.BASE_CLASS_DEFINITIONS.DATA_MODELS
DATA_TYPES  = PYQT.BASE_CLASS_DEFINITIONS.DATA_TYPES
from ..DATA_TYPES import Node_Item_Data
import PYQT.MAYA_CLASS_DEFINITIONS.DATA_TYPES
########################################################################
class TreeModel(DATA_MODELS.Tree_Model.TreeModel):
	def __init__(self, parent=None, root_item=None, headers=[]):
		super(TreeModel, self).__init__(parent)
		
		if len(headers) == 0:
			headers.append("First Name")
			headers.append("Last Name")
		if root_item is None:
			root_item = DATA_TYPES.Model_Items.Root_Model_Item(self, headers=headers,column_Count=1)

		self.rootItem = root_item

########################################################################
class DAG_Node_TreeModel(TreeModel):
	def __init__(self, parent=None, root_item=None, headers=[]):
		super(DAG_Node_TreeModel, self).__init__(parent=parent, root_item=root_item, headers=headers)			