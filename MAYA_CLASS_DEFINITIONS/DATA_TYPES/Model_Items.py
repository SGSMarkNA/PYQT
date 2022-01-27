from PYQT import BASE_CLASS_DEFINITIONS
from . import Node_Item_Data
from . import Item_Data_Storage
from ..Item_Data_Roles import Maya_Item_Data_Roles
from PYQT import userType_generator
import pymel.core as pm
if False:
	from ..DATA_MODELS.Node_Tree_Model import TreeModel
_class_data_item_Relation = dict()

########################################################################
class Base_Model_Item(BASE_CLASS_DEFINITIONS.DATA_TYPES.Model_Items.Base_Model_Item):
	_Item_Type =  userType_generator()
	#----------------------------------------------------------------------
	def __init__(self, model=None, parent_item=None, items=[], column_count=1):
		self.parentItem          = parent_item
		self._column_items       = Item_Data_Storage.Column_Item_List(self)
		self.childItems          = []
		self._with_Context_Depth = 0
		self._model              = model
		isinstance(self.parentItem, Base_Model_Item)
		
		isinstance(self.column_items, Item_Data_Storage.Column_Item_List)

		if isinstance(items,list) and len(items):
			for i, column_item in enumerate(items):
				if isinstance(column_item, dict ):
					column_item['tree_item']=self
					column_item = Item_Data_Storage.Internal_Item_Data(**column_item)
				elif isinstance(column_item, (Item_Data_Storage.Internal_Item_Data,Item_Data_Storage.Standered_Item_Data)):
					column_item.tree_item = self
				else:
					raise ValueError("index %i in child_items arg must be a instance of Tree_Item and a %r was found" % (i, type(column_item)) )
				self._column_items.items.append(column_item)
		elif isinstance(items,str):
			column_item = Item_Data_Storage.Internal_Item_Data(tree_item=self,display_name=items)
			self._column_items.items.append(column_item)
		else:
			column_items = []
			for i in range(column_count):
				item = Item_Data_Storage.Internal_Item_Data(tree_item = self)
				item.display_name = "column %i" % i
				self._column_items.items.append(item)
		
		if self.parentItem is not None:
			self.parentItem.appendChild(self)
		if False:
			isinstance(self.model, TreeModel)
			isinstance(self.root_item, Base_Model_Item)
			isinstance(self.index, PYQT.QModelIndex)
			isinstance(self.parent, Base_Model_Item)
	#----------------------------------------------------------------------
	def data(self, column=0, role=Maya_Item_Data_Roles.DISPLAY):
		return super(Base_Model_Item,self).data(column,role)
	#----------------------------------------------------------------------
	def setData(self, value, column=0, role=Maya_Item_Data_Roles.DISPLAY):
		return self._column_items.setData(value, column, role)
	#----------------------------------------------------------------------
	def insertChild(self, position, child_Item):
		super(Base_Model_Item,self).insertChildren(position, child_Item)
	#----------------------------------------------------------------------
	def appendChild(self, child_Item):
		super(Base_Model_Item,self).appendChild(child_Item)
	#----------------------------------------------------------------------
	def clone(self, destination):
		super(Base_Model_Item,self).clone(destination)
	#----------------------------------------------------------------------
	def appendColumn(self, item_data):
		res = super(Base_Model_Item,self).appendColumn(destination)
		return res
	#----------------------------------------------------------------------
	def takeChildren(self, items):
		res = super(Base_Model_Item,self).takeChildren(items)
		return res
	#----------------------------------------------------------------------
	def insertColumns(self, position, items):
		res = super(Base_Model_Item,self).insertColumns(position, items)
		return res
	#----------------------------------------------------------------------
	def removeColumns(self, items):
		res = super(Base_Model_Item,self).removeColumns(items)
		return res
	#----------------------------------------------------------------------
	def insertChildren(self, position, items):
		res = super(Base_Model_Item,self).insertChildren(position, items)
		return res
	#----------------------------------------------------------------------
	def moveChildren(self, items, position):
		res = super(Base_Model_Item,self).moveChildren(items, position)
		return res
	#----------------------------------------------------------------------
	def moveChild(self, child, position):
		res = super(Base_Model_Item,self).moveChild(child, position)
		return res
	#----------------------------------------------------------------------
	def removeChild(self, child_item):
		res = super(Base_Model_Item,self).removeChild(child_item)
		return res
	#----------------------------------------------------------------------
	def removeChildren(self, items):
		res = super(Base_Model_Item,self).removeChildren(items)
		return res
	#----------------------------------------------------------------------
	def clear_Children(self):
		""""""
		res = super(Base_Model_Item,self).clear_Children()
		return res
	#----------------------------------------------------------------------
	def child(self, row):
		res = super(Base_Model_Item,self).child(row)
		return res
	#----------------------------------------------------------------------
	def find_child(self, value, column=0, role=Maya_Item_Data_Roles.DISPLAY):
		res = super(Base_Model_Item,self).find_child(value, column=column, role=role)
		return res
	#----------------------------------------------------------------------
	def find_all_children(self, value, column=0, role=Maya_Item_Data_Roles.DISPLAY):
		res = super(Base_Model_Item,self).find_all_children(value, column=column, role=role)
		return res
	#----------------------------------------------------------------------
	def get_internal_Data(self, column=0):
		""""""
		res = self.data(column=column, role=Maya_Item_Data_Roles.INTERNAL_DATA)
		isinstance(res, Item_Data_Storage.Internal_Item_Data)
		return res
	#----------------------------------------------------------------------
	def set_internal_Data(self, value, column=0):
		""""""
		self.setData(value, column=column, role=Maya_Item_Data_Roles.INTERNAL_DATA)
	#----------------------------------------------------------------------
	def _get_Current_State(self):
		""""""
		raise NotImplemented()
	#----------------------------------------------------------------------
	def load_child_data(self, list_of_child_dicts):
		""""""
		raise NotImplemented()
	#----------------------------------------------------------------------
	def get_Current_Tree_State(self, collection={}):
		""""""
		raise NotImplemented()
	#----------------------------------------------------------------------
	@property
	def column_items(self):
		""""""
		res = super(Base_Model_Item,self).column_items
		return res
	#----------------------------------------------------------------------
	@property
	def parent(self):
		res = super(Base_Model_Item,self).parent
		return res
	#----------------------------------------------------------------------
	@property
	def all_parents(self):
		res = super(Base_Model_Item,self).all_parents
		return res
	#----------------------------------------------------------------------
	@property
	def all_childern(self):
		res = super(Base_Model_Item,self).all_childern
		return res
	#----------------------------------------------------------------------
	@property
	def row(self):
		res = super(Base_Model_Item,self).row
		return res
	#----------------------------------------------------------------------
	@property
	def column_Count(self):
		res = super(Base_Model_Item,self).column_Count
		return res
	#----------------------------------------------------------------------
	@property
	def root_item(self):
		res = super(Base_Model_Item,self).root_item
		return res
	#----------------------------------------------------------------------
	@property
	def model(self):
		res = super(Base_Model_Item,self).model
		return res
	#----------------------------------------------------------------------
	@property
	def index(self):
		""""""
		res = super(Base_Model_Item,self).index
		return res
	#----------------------------------------------------------------------
	@property
	def child_Count(self):
		res = super(Base_Model_Item,self).child_Count
		return res
	@property
	#----------------------------------------------------------------------
	def current_context_state(self):
		""""""
		res = super(Base_Model_Item,self).current_context_state
		return res
	@property
	#----------------------------------------------------------------------
	def context_data(self):
		""""""
		res = super(Base_Model_Item,self).context_data
		return res
	@property
	#----------------------------------------------------------------------
	def isRoot(self):
		""""""
		res = super(Base_Model_Item,self).isRoot
		return res
	#----------------------------------------------------------------------
	def __len__(self):
		""""""
		res = super(Base_Model_Item,self).__len__()
		return res
	#----------------------------------------------------------------------
	def _build_Data_items(self,node):
		""""""
		items = _class_data_item_Relation.get(self.__class__.__name__,[])
		res = []
		for item in items:
			data_item = item(node,tree_item=self)
			res.append(data_item)
		return res
########################################################################
class Base_Maya_Node_Item(Base_Model_Item):
	_Item_Type =  userType_generator()
	#----------------------------------------------------------------------
	def __init__(self, model=None, parent_item=None, items=[]):
		super(Base_Maya_Node_Item,self).__init__(model=model, parent_item=parent_item, items=items, column_count=1)
	#----------------------------------------------------------------------
	def get_internal_Data(self, column=0):
		""""""
		res = super(Base_Maya_Node_Item,self).get_internal_Data(column=column)
		## WING IDE CODE COMPLEASHION ##
		if False:
			isinstance(res, Item_Data_Storage.Maya_Node_Data)
		return res
########################################################################
class Base_Maya_Plug_Item(Base_Model_Item):
	_Item_Type =  userType_generator()
	#----------------------------------------------------------------------
	def __init__(self, model=None, parent_item=None, items=[]):
		super(Base_Maya_Plug_Item,self).__init__(model=model, parent_item=parent_item, items=items, column_count=1)
	#----------------------------------------------------------------------
	def get_internal_Data(self, column=0):
		""""""
		res = super(Base_Maya_Plug_Item,self).get_internal_Data(column=column)
		## WING IDE CODE COMPLEASHION ##
		if False:
			isinstance(res, Item_Data_Storage.Maya_Plug_Data)
		return res