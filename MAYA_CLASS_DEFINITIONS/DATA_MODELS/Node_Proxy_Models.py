import PYQT
import PYQT.BASE_CLASS_DEFINITIONS
Constants = PYQT.Constants
BASE_CLASS_DEFINITIONS = PYQT.BASE_CLASS_DEFINITIONS

from ..Item_Data_Roles import Maya_Item_Data_Roles
from ..DATA_MODELS import Node_Tree_Model

########################################################################
class BASE_SORT_FILTER_PROXY_MODEL(BASE_CLASS_DEFINITIONS.DATA_MODELS.Proxy_Models.Sort_Filter_Proxy_Model):
	#----------------------------------------------------------------------
	def __init__(self,parent=None):
		super(BASE_SORT_FILTER_PROXY_MODEL,self).__init__(parent=parent)
	#----------------------------------------------------------------------
	def sourceModel(self):
		""""""
		res = super(BASE_SORT_FILTER_PROXY_MODEL,self).sourceModel()
		return res

########################################################################
class COLOR_IMPORTANT_ITEMS_PROXY_MODEL(BASE_SORT_FILTER_PROXY_MODEL):
	#----------------------------------------------------------------------
	color_levels = [PYQT.QBrush(Constants.Colors.GREEN),PYQT.QBrush(Constants.Colors.DARK_GREEN),PYQT.QBrush(Constants.Colors.YELLOW),PYQT.QBrush(Constants.Colors.DARK_YELLOW)]
	def __init__(self,parent=None):
		super(COLOR_IMPORTANT_ITEMS_PROXY_MODEL,self).__init__(parent=parent)
	#----------------------------------------------------------------------
	def sourceModel(self):
		""""""
		res = super(COLOR_IMPORTANT_ITEMS_PROXY_MODEL,self).sourceModel()
		isinstance(res,Node_Tree_Model.TreeModel)
		return res
	#----------------------------------------------------------------------
	def is_Item_Important(self,index,level=0):
		""""""
		return False
	#----------------------------------------------------------------------
	def data(self,index,role=None):
		"""
		data(index,role=None)
			index=CFQT.QModelIndex
			role=CFQT.int
		"""
		if role == PYQT.Qt.ItemDataRole.ForegroundRole:
			for level,color in enumerate(self.color_levels):
				if self.is_Item_Important(index, level=level):
					return color
		res = super(COLOR_IMPORTANT_ITEMS_PROXY_MODEL,self).data(index,role)
		return res