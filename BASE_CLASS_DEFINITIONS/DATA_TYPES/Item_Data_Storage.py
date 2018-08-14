import os
import PYQT
import PYQT.BASE_CLASS_DEFINITIONS.QT_SUBCLASS.QItemDelegate
Constants = PYQT.Constants
from ..Item_Data_Roles import Base_Item_Data_Roles

if False:
	from .. import DATA_TYPES

#----------------------------------------------------------------------
def is_Convertable_To_QColor(val):
	""""""
	if isinstance(val, (PYQT.QColor, PYQT.Qt.GlobalColor)):
		return True
	elif isinstance(val, (tuple, list)) and len(val) == 4 and all([isinstance(i, int) for i in val]):
		return True
	return False
#----------------------------------------------------------------------
def convert_To_QColor(val):
	""""""
	if not is_Convertable_To_QColor(val):
		raise ValueError("input is cannot be converted to a QColor")
	else:
		if isinstance(val, PYQT.QColor):
			return val
		elif isinstance(val, PYQT.Qt.GlobalColor):
			return PYQT.QColor(val)
		else:
			return PYQT.QColor(*val)
#----------------------------------------------------------------------
def create_Item_Icon(value):
	if isinstance(value, str):
		if value.startswith(":"):
			pixmap = PYQT.QPixmap(value)
			return PYQT.QIcon(pixmap)
	pixmap = PYQT.QPixmap(16, 16)
	painter = PYQT.QPainter(pixmap)
	painter.setPen(PYQT.Qt.NoPen)
	painter.fillRect(PYQT.QRect(0, 0, 16, 16), color)
	#painter.fillRect(QT.QRect(0, 10, 20, 10), QT.Qt.GlobalColor.green)
	painter.end()
	return PYQT.QIcon(pixmap)
# ======================================================================
# DATA MODEL STANDERD ITEMS TYPES
# ----------------------------------------------------------------------
# Synopsis:
#     Each Items Constains All The Information Needed To Display Itself
#     In A Column for View such as
#     font size, font color, display name ect.
# ======================================================================

########################################################################
class DATA_DEFAULT_VALUES:
	""""""
	class FONT:
		family          = "Arial"
		pointSize       = 8
		weight          = Constants.Font.Weight.Normal
		capitalization  = Constants.Font.Capitalization.MixedCase
	class DISPLAY:
		background_color = PYQT.QColor(Constants.Colors.TRANSPARENT)
		foreground_color = PYQT.QColor(Constants.Colors.BLACK)
		icon_color       = PYQT.QColor(Constants.Colors.RED)
		brush            = PYQT.QBrush(Constants.Colors.RED)
		alignment_V      = Constants.AlignmentFlag.Vertical.Center
		alignment_H      = Constants.AlignmentFlag.Horizontal.Justify
	class BRUSH:
		_brush_val = None
		@classmethod
		def value(cls):
			if cls._brush_val is None:
				cls._brush_val = PYQT.QBrush(Colors.RED)
			return cls._brush_val
	@classmethod
	def update_Font(cls):
		cls.font = PYQT.QFont(FONT.family, FONT.pointSize)
		cls.font.setCapitalization(FONT.capitalization)
		cls.font.setWeight(FONT.weight)

	font             = PYQT.QFont(FONT.family, FONT.pointSize)
	font.setCapitalization(FONT.capitalization)
	font.setWeight(FONT.weight)
	icon             = None



########################################################################
class Item_Data_Editor(object):
	#----------------------------------------------------------------------
	def __init__(self,item_data):
		""""""
		isinstance(item_data,Standered_Item_Data)
		self.item_data = item_data
		self._editor = None
	#----------------------------------------------------------------------
	@property
	def has_editor(self):
		""""""
		return self.createEditor() != None
	#----------------------------------------------------------------------
	def createEditor(self,parent=None):
		""""""
		return None
	#----------------------------------------------------------------------
	def setEditorData(self):
		""""""
		pass
	#----------------------------------------------------------------------
	def setModelData(self):
		""""""
		pass
	
########################################################################
class Spin_Box_Data_Editor(Item_Data_Editor):
	#----------------------------------------------------------------------
	def __init__(self,item_data):
		""""""
		super(Spin_Box_Data_Editor,self).__init__(item_data)
	#----------------------------------------------------------------------
	def createEditor(self,parent=None,index=None):
		""""""
		self._editor = PYQT.QSpinBox(parent=parent)
		return self._editor
	#----------------------------------------------------------------------
	def setEditorData(self):
		""""""
		self._editor.setValue(int(self.item_data.display_name))
	#----------------------------------------------------------------------
	def setModelData(self):
		""""""
		self.item_data.display_name = self._editor.value()
		
########################################################################
class Combo_Box_Data_Editor(Item_Data_Editor):
	#----------------------------------------------------------------------
	def __init__(self,item_data):
		""""""
		super(Combo_Box_Data_Editor,self).__init__(item_data)
	#----------------------------------------------------------------------
	def createEditor(self,parent=None):
		""""""
		self._editor = PYQT.QComboBox(parent=parent)
		return self._editor
	#----------------------------------------------------------------------
	def setEditorData(self):
		""""""
		self._editor.addItems(["New Name One","New Name 2",self.item_data.display_name])
		self._editor.setCurrentIndex(self._editor.findText(self.item_data.display_name))
	#----------------------------------------------------------------------
	def setModelData(self):
		""""""
		self.item_data.display_name = self._editor.currentText()
		
########################################################################
class Item_Data_Delegate(PYQT.QItemDelegate):
	#----------------------------------------------------------------------
	def createEditor(self, parent, option, index):
		editor = index.data(Base_Item_Data_Roles.INTERNAL_EDITOR)
		if not editor == None:
			return editor.createEditor(parent=parent,index=index)
		else:
			return super(Item_Data_Delegate,self).createEditor(parent, option, index)
	#----------------------------------------------------------------------
	def setEditorData(self, editor, index):
		editor = index.data(Base_Item_Data_Roles.INTERNAL_EDITOR)
		if not editor == None:
			return editor.setEditorData()
		else:
			return super(Item_Data_Delegate,self).setEditorData(editor, index)
	#----------------------------------------------------------------------
	def setModelData(self, spinBox, model, index):
		editor = index.data(Base_Item_Data_Roles.INTERNAL_EDITOR)
		if not editor == None:
			return editor.setModelData()
		else:
			return super(Item_Data_Delegate,self).setEditorData(editor, index)

########################################################################
class Standered_Item_Data(object):
	"""This Is The Base Item Data Class It Only Stores Data That Is Needed To Display Itself"""
	DEF_VALS    = DATA_DEFAULT_VALUES
	H_ALIGNMENT = Constants.AlignmentFlag.Horizontal
	V_ALIGNMENT = Constants.AlignmentFlag.Vertical
	ID_ROLE     = Base_Item_Data_Roles

	#----------------------------------------------------------------------
	def __init__(self,
	             tree_item            = None,
	             selectable           = None, enabled             = None, editable     = None,
	             dragable             = None, dropable            = None, checkable    = None, checked = False,
	             tristate             = None, font_family         = None, font_size    = None,
	             size_hint            = None, status_tip          = None, tool_tip     = None,
	             brush                = None, icon_visable        = None, icon_color   = None,
	             font_weight          = None, font_capitalization = None, display_name = None,
	             background_color     = None, foreground_color    = None,
	             horizontal_alignment = None, vertical_alignment  = None):
		""""""
		if False:
			isinstance(tree_item, DATA_TYPES.Model_Items.Base_Model_Item)
			#raise ValueError("tree_item input must be and instance or subclass of Tree_Item and a %r was found" % type(tree_item))

		self.tree_item                  = tree_item
		self._item_selectable           = selectable
		self._item_enabled              = enabled
		self._item_editable             = editable
		self._item_dragable             = dragable
		self._item_dropable             = dropable
		if checkable:
			self._item_checkable        = checkable
		else:
			self._item_checkable        = False
		self._item_tristate             = tristate
		self._item_display_name         = display_name
		self._item_font_family          = font_family
		self._item_font_size            = font_size
		self._item_font_weight          = font_weight
		self._item_font_capitalization  = font_capitalization
		self._item_background_color     = background_color
		self._item_foreground_color     = foreground_color
		self._item_brush                = brush
		self._item_icon_visable         = icon_visable
		self._item_icon_color           = icon_color
		self._item_size_hint            = size_hint
		self._item_status_tip           = status_tip
		self._item_tool_tip             = tool_tip
		self._item_horizontal_alignment = self.H_ALIGNMENT.Values.get(horizontal_alignment,None)
		self._item_vertical_alignment   = self.V_ALIGNMENT.Values.get(vertical_alignment,None)
		self._data_icon                 = None #create_Item_Icon(":/outliner/group")
		self._data_font                 = None
		if checked:
			self._data_checked              = PYQT.Qt.CheckState.Checked
		else:
			self._data_checked              = PYQT.Qt.CheckState.Unchecked
		self._data_foreground_color     = None
		self._data_background_color     = None
		self._data_alignment            = None
		self._data_flags                = PYQT.Qt.ItemFlags()
		self._update_flags()
		self._update_text_alignment()
		self._internal_editor = None
		if False:
			isinstance(self.background_color,PYQT.QColor)
			isinstance(self.foreground_color,PYQT.QColor)
			isinstance(self.brush,PYQT.QBrush)
			isinstance(self.size_hint,PYQT.QSize)
			isinstance(self.status_tip,str)
			isinstance(self.tool_tip,str) 
			isinstance(self.text_font,PYQT.QFont)
	#----------------------------------------------------------------------
	@property
	def has_editor(self):
		""""""
		return self._internal_editor is not None
	#----------------------------------------------------------------------
	@property
	def internal_editor(self):
		""""""
		return self._internal_editor
	#----------------------------------------------------------------------
	@internal_editor.setter
	def internal_editor(self,editor):
		""""""
		self._internal_editor = editor
	#----------------------------------------------------------------------
	def createColorIcon(self, color):
		if isinstance(color, str):
			if color.startswith(":"):
				pixmap = PYQT.QPixmap(color)
				return PYQT.QIcon(pixmap)
			elif os.path.exists(color):
				pixmap = PYQT.PYQT.QPixmap(color)
				return PYQT.QIcon(pixmap)
		else:
			pixmap = PYQT.QPixmap(16, 16)
			painter = PYQT.QPainter(pixmap)
			painter.setPen(PYQT.Qt.NoPen)
			painter.fillRect(PYQT.QRect(0, 0, 16, 16), color)
			#painter.fillRect(QT.QRect(0, 10, 20, 10), QT.Qt.GlobalColor.green)
			painter.end()
			return PYQT.QIcon(pixmap)
	#----------------------------------------------------------------------
	def get_Current_State(self):
		""""""
		state = dict()
		for key in self.__dict__.keys():
			if key.startswith("_item_"):
				val = getattr(self, key)
				if not val is None:
					key = key.replace("_item_", "")
					if hasattr(val, "name"):
						state[key] = val.name
					else:
						state[key] = val
		return state
	#----------------------------------------------------------------------
	def set_Current_State(self, state):
		""""""
		if not isinstance(state,dict):
			raise ValueError("input state must be a dict and a %r was given" % type(state))
		for key, val in state.iteritems():
			if hasattr(self, "_item_"+key):
				if val is not None:
					try:
						setattr(self, key, val)
					except AttributeError:
						pass
	#----------------------------------------------------------------------
	@property
	def icon_visable(self):
		"""Returns Weather Or Not The Icon Is Visable"""
		if self._item_icon_visable is None:
			return False
		else:
			return self._item_icon_visable
	#----------------------------------------------------------------------
	@icon_visable.setter
	def icon_visable(self, value):
		"""Set Weather Or Not The Icon Is Visable"""
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be of type bool or int and a %r was given" % type(value))
		self._item_icon_visable = value
	#----------------------------------------------------------------------
	@property
	def background_color(self):
		"""Get The Backround Color Of A Item"""
		if self._data_background_color is None and not self._item_background_color == None:
			self._update_background_color()
		return self._data_background_color
	#----------------------------------------------------------------------
	@background_color.setter
	def background_color(self, value):
		if value is None:
			self._item_background_color = value
		elif isinstance(value,PYQT.QColor):
			self._item_background_color = value.getRgb()
		else:
			raise ValueError("input value must be an instance of QT.QColor and a %r was given" % type(value))
		self._update_background_color()
	#----------------------------------------------------------------------
	@property
	def foreground_color(self):
		if self._data_foreground_color is None and not self._item_foreground_color == None:
			self._update_foregound_color()
		return self._data_foreground_color
	#----------------------------------------------------------------------
	@foreground_color.setter
	def foreground_color(self, value):
		if value is None:
			self._item_foreground_color = value
		elif isinstance(value,(PYQT.QColor, PYQT.Qt.GlobalColor)):
			if isinstance(value,PYQT.Qt.GlobalColor):
				value = PYQT.QColor(value)
			self._item_foreground_color = value.getRgb()
		else:
			raise ValueError("input value must be an instance of QT.QColor and a %r was given" % type(value))
		self._update_foregound_color()
	#----------------------------------------------------------------------
	@property
	def brush(self):
		if self._item_brush is None:
			return self.DEF_VALS.BRUSH.value()
		else:
			return self._item_brush
	#----------------------------------------------------------------------
	@brush.setter
	def brush(self, value):
		if not isinstance(value,PYQT.QBrush):
			raise ValueError("input value must be an instance of QT.QBrush and a %r was given" % type(value))
		self._item_bush = value
	#----------------------------------------------------------------------
	@property
	def size_hint(self):
		return self._item_size_hint
	#----------------------------------------------------------------------
	@size_hint.setter
	def size_hint(self, value):
		if not isinstance(value,PYQT.QSize):
			raise ValueError("input value must be an instance of QT.QSize and a %r was given" % type(value))
		self._item_size_hint = value	
	#----------------------------------------------------------------------
	@property
	def status_tip(self):
		if self._item_status_tip is None:
			return ""
		else:
			return self._item_status_tip
	#----------------------------------------------------------------------
	@status_tip.setter
	def status_tip(self, value):
		if not isinstance(value,(str,unicode)):
			raise ValueError("input value must be an instance of (str,unicode) and a %r was given" % type(value))
		self._item_status_tip = value
	#----------------------------------------------------------------------
	@property
	def tool_tip(self):
		if self._item_tool_tip is None:
			return ""
		else:
			return self._item_tool_tip
	#----------------------------------------------------------------------
	@tool_tip.setter
	def tool_tip(self, value):
		if not isinstance(value,(str,unicode)):
			raise ValueError("input value must be an instance of (str,unicode) and a %r was given" % type(value))
		self._item_tool_tip = value
	#----------------------------------------------------------------------
	@property
	def vertical_alignment(self):
		if self._item_vertical_alignment is None:
			return self.DEF_VALS.DISPLAY.alignment_V
		return self._item_vertical_alignment
	#----------------------------------------------------------------------
	@vertical_alignment.setter
	def vertical_alignment(self, value):
		""""""
		if value is None:
			self._item_vertical_alignment = value
		elif value in self.V_ALIGNMENT.Values.keys():
			self._item_vertical_alignment = self.V_ALIGNMENT.Values[value]
		else:
			raise ValueError("input value must be one of the fallowing (%s) and a %r was given" % (",".join(self.V_ALIGNMENT.Values.keys()), value))
		self._update_text_alignment()
	#----------------------------------------------------------------------
	@property
	def horizontal_alignment(self):
		if self._item_horizontal_alignment is None:
			return self.DEF_VALS.DISPLAY.alignment_H
		return self._item_horizontal_alignment
	#----------------------------------------------------------------------
	@horizontal_alignment.setter
	def horizontal_alignment(self, value):
		if value is None:
			self._item_horizontal_alignment = value
		elif value in self.H_ALIGNMENT.Values.keys():
			self._item_horizontal_alignment = self.H_ALIGNMENT.Values[value]
		else:
			raise ValueError("input value must be one of the fallowing (%s) and a %r was given" % (",".join(self.H_ALIGNMENT.Values.keys()), value))
		self._update_text_alignment()
	#----------------------------------------------------------------------
	@property
	def text_alignment(self):
		if self._data_alignment is None:
			return PYQT.Qt.AlignmentFlag(self.horizontal_alignment|self.vertical_alignment)
		return self._data_alignment
	#----------------------------------------------------------------------
	@property
	def font_family(self):
		if self._item_font_family is None:
			return False
		else:
			return self._item_font_family
	#----------------------------------------------------------------------
	@font_family.setter
	def font_family(self, value):
		if not isinstance(value,(str, unicode)):
			raise ValueError("input value must be an instance of str, unicode and a %r was given" % type(value))
		self._item_font_family = value
		self._update_font()
	#----------------------------------------------------------------------
	@property
	def font_size(self):
		if self._item_font_size is None:
			return False
		else:
			return self._item_font_size
	#----------------------------------------------------------------------
	@font_size.setter
	def font_size(self, value):
		if not isinstance(value,(int)):
			raise ValueError("input value must be an instance of (int) and a %r was given" % type(value))
		self._item_font_size = value
		self._update_font()
	#----------------------------------------------------------------------
	@property
	def font_weight(self):
		if self._item_font_weight is None:
			return False
		else:
			return self._item_font_weight
	#----------------------------------------------------------------------
	@font_weight.setter
	def font_weight(self, value):

		if not isinstance(value,(int)):
			raise ValueError("input value must be an instance of (int) and a %r was given" % type(value))
		if int(value) == 0:
			value = None
		elif not int(value) in [25, 50, 63, 75, 87]:
			raise ValueError("input value must be one of the fallowing values of 25, 50, 63, 75, 87 and %i was given" % int(value))
		self._item_font_weight = value
		self._update_font()
	#----------------------------------------------------------------------
	@property
	def font_capitalization(self):
		if self._item_font_capitalization is None:
			return False
		else:
			return self._item_font_capitalization
	#----------------------------------------------------------------------
	@font_capitalization.setter
	def font_capitalization(self, value):
		if not isinstance(value,(int)):
			raise ValueError("input value must be an instance of (int) and a %r was given" % type(value))
		self._item_font_capitalization = value
		self._update_font()
	#----------------------------------------------------------------------
	@property
	def selectable(self):
		if self._item_selectable is None:
			return True
		else:
			return self._item_selectable
	#----------------------------------------------------------------------
	@selectable.setter
	def selectable(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_selectable = value
		self._update_flags()
	#----------------------------------------------------------------------
	@property
	def checked(self):
		if self._item_checkable:
			return self._data_checked
		else:
			return None
	#----------------------------------------------------------------------
	@checked.setter
	def checked(self, value):
		if not self._item_checkable is None and self._item_checkable:
			if value is True or value == PYQT.Qt.CheckState.Checked:
				self._data_checked = PYQT.Qt.CheckState.Checked
			else:
				self._data_checked = PYQT.Qt.CheckState.Unchecked
	#----------------------------------------------------------------------
	@property
	def enabled(self):
		if self._item_enabled is None:
			return True
		else:
			return self._item_enabled
	#----------------------------------------------------------------------
	@enabled.setter
	def enabled(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_enabled = value
		self._update_flags()
	#----------------------------------------------------------------------
	@property
	def editable(self):
		if self._item_editable is None:
			return True
		else:
			return self._item_editable 
	#----------------------------------------------------------------------
	@editable.setter
	def editable(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_editable = value
		self._update_flags()
	#----------------------------------------------------------------------
	@property
	def dragable(self):
		if self._item_dragable is None:
			return True
		else:
			return self._item_dragable
	#----------------------------------------------------------------------
	@dragable.setter
	def dragable(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_dragable = value
		self._update_flags()
	#----------------------------------------------------------------------
	@property
	def dropable(self):
		if self._item_dropable is None:
			return True
		else:
			return self._item_dropable 
	#----------------------------------------------------------------------
	@dropable.setter
	def dropable(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_dropable = value
		self._update_flags()
	#----------------------------------------------------------------------
	@property
	def checkable(self):
		if self._item_checkable is None:
			return False
		else:
			return self._item_checkable
	#----------------------------------------------------------------------
	@checkable.setter
	def checkable(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_checkable = value
		self._update_flags()
	#----------------------------------------------------------------------
	@property
	def tristate(self):
		if self._item_tristate is None:
			return False
		else:
			if self.checkable:
				return self._item_tristate
			else:
				return False
	#----------------------------------------------------------------------
	@tristate.setter
	def tristate(self, value):
		if not isinstance(value,(bool, int)):
			raise ValueError("input value must be an instance of (bool, int) and a %r was given" % type(value))
		self._item_tristate = value
		self._update_flags()
	#----------------------------------------------------------------------
	@property
	def display_name(self):
		if self._item_display_name is None:
			return None
		else:
			return self._item_display_name
	#----------------------------------------------------------------------
	@display_name.setter
	def display_name(self, value):
		if not isinstance(value,(str, unicode, bool, int)):
			raise ValueError("input value must be an instance of (str,unicode) and a %r was given" % type(value))
		self._item_display_name = value
	#----------------------------------------------------------------------
	@property
	def icon_color(self):
		if self._item_icon_color is None:
			return self.DEF_VALS.DISPLAY.icon_color
		else:
			return self._item_icon_color
	#----------------------------------------------------------------------
	@icon_color.setter
	def icon_color(self, value):
		if not isinstance(value,(PYQT.QColor, PYQT.Qt.GlobalColor, str, PYQT.QIcon)):
			raise ValueError("input value must be an instance of (QT.QColor, QT.Qt.GlobalColor, str) and a %r was given" % type(value))
		self._item_icon_color = value
		if not isinstance(value,PYQT.QIcon):
			self._data_icon  = self.createColorIcon(self._item_icon_color)
		else:
			self._data_icon = value
	#----------------------------------------------------------------------
	@property
	def font(self):
		""""""
		if any([val is not False for val in self.font_attributes]):
			return self._data_font
		else:
			return None
	#----------------------------------------------------------------------
	@property
	def icon(self):
		""""""
		if self.icon_visable:
			if self._data_icon is None:
				if self._item_icon_color is None:
					if self.DEF_VALS.icon is None:
						self.DEF_VALS.icon = self.createColorIcon(PYQT.QColor(self.DEF_VALS.DISPLAY.icon_color))
					return self.DEF_VALS.icon
			else:
				return self._data_icon
		else:
			return None
	#----------------------------------------------------------------------
	@icon.setter
	def icon(self,value):
		""""""
		self.icon_color = value
	@property
	#----------------------------------------------------------------------
	def column(self):
		""""""
		return self.tree_item._column_items.items.index(self)
	@property
	#----------------------------------------------------------------------
	def index(self):
		""""""
		return self.tree_item.model.indexFromItemData(self)
	#----------------------------------------------------------------------
	@property
	def flags(self):
		""""""
		return self._data_flags
	@property
	def font_attributes(self):
		return [self.font_family, self.font_size, self.font_weight, self.font_capitalization]
	#----------------------------------------------------------------------
	def _update_font(self):
		""""""
		local_font_atts = self.font_attributes
		global_font_attrs = [self.DEF_VALS.FONT.family, self.DEF_VALS.FONT.pointSize, self.DEF_VALS.FONT.weight, self.DEF_VALS.FONT.capitalization]

		if any([val is not False for val in local_font_atts]):
			if self._data_font is None:
				self._data_font = PYQT.QFont(self.DEF_VALS.font)
			fn_list = [self._data_font.setFamily, self._data_font.setPointSize, self._data_font.setWeight, self._data_font.setCapitalization]
			self._data_font.setFamily
			for loc, glob, fn in zip(local_font_atts, global_font_attrs, fn_list):
				if not loc is False:
					fn(loc)
				else:
					fn(glob)
	#----------------------------------------------------------------------
	def _update_flags(self):
		""""""
		flgs = PYQT.Qt.ItemFlags()
		if self.selectable:
			flgs =  flgs | PYQT.Qt.ItemFlag.ItemIsSelectable
		if self.editable:
			flgs =  flgs | PYQT.Qt.ItemFlag.ItemIsEditable
		if self.enabled:
			flgs =  flgs | PYQT.Qt.ItemFlag.ItemIsEnabled
		if self.dragable:
			flgs =  flgs | PYQT.Qt.ItemFlag.ItemIsDragEnabled
		if self.dropable:
			flgs =  flgs | PYQT.Qt.ItemFlag.ItemIsDropEnabled
		if self.checkable:
			flgs =  flgs | PYQT.Qt.ItemFlag.ItemIsUserCheckable
		if self.tristate:
			flgs =  flgs | PYQT.Qt.ItemFlag.ItemIsTristate
		self._data_flags = flgs
	#----------------------------------------------------------------------
	def _update_text_alignment(self):
		""""""
		self._data_alignment = PYQT.Qt.AlignmentFlag(self.horizontal_alignment|self.vertical_alignment)
	#----------------------------------------------------------------------
	def _update_foregound_color(self):
		""""""
		if self._item_foreground_color is None:
			self._data_foreground_color = self.DEF_VALS.DISPLAY.foreground_color
		else:
			if isinstance(self._item_foreground_color, PYQT.Qt.GlobalColor):
				self._data_foreground_color = PYQT.QColor(self._item_foreground_color)
			else:
				if isinstance(self._item_foreground_color,basestring):
					self._data_foreground_color = PYQT.QColor(self._item_foreground_color)
				else:
					self._data_foreground_color = PYQT.QColor(*self._item_foreground_color)
	#----------------------------------------------------------------------
	def _update_background_color(self):
		""""""
		if self._item_background_color is None:
			self._data_background_color = None
		else:
			if isinstance(self._item_background_color,basestring):
				self._data_background_color = PYQT.QColor(self._item_background_color)
			elif isinstance(self._item_background_color,CFQT.Qt.GlobalColor):
				self._data_background_color = PYQT.QColor(self._item_background_color)
			else:
				self._data_background_color = PYQT.QColor(*self._item_background_color)
	#----------------------------------------------------------------------
	def data(self, role=Base_Item_Data_Roles.DISPLAY):
		if role in [Base_Item_Data_Roles.DISPLAY, Base_Item_Data_Roles.EDIT]:
			return self.display_name
		elif role == Base_Item_Data_Roles.FOREGROUND:
			return self.foreground_color
		elif role == Base_Item_Data_Roles.BACKGROUND:
			return self.background_color
		elif role == Base_Item_Data_Roles.SIZEHINT:
			return self.size_hint
		elif role == Base_Item_Data_Roles.TOOLTIP:
			return self.tool_tip
		elif role == Base_Item_Data_Roles.STATUSTIP:
			return self.status_tip
		elif role == Base_Item_Data_Roles.FONT:
			return self.font
		elif role == Base_Item_Data_Roles.TEXT_ALIGNMENT:
			return self.text_alignment
		elif role == Base_Item_Data_Roles.DECORATION:
			if self.icon_visable:
				return self.icon
			else:
				return None
		elif role == Base_Item_Data_Roles.ICON_COLOR:
			return self.icon_color
		elif role == Base_Item_Data_Roles.FONT_SIZE:
			return self.text_size
		elif role == Base_Item_Data_Roles.FONT_WEIGHT:
			return self.font_weight
		elif role == Base_Item_Data_Roles.HORIZONTAL_ALIGNMENT:
			return self.horizontal_alignment
		elif role == Base_Item_Data_Roles.VERTICAL_ALIGNMENT:
			return self.vertical_alignment
		elif role == Base_Item_Data_Roles.CHECKSTATE:
			return self.checked
		elif role == Base_Item_Data_Roles.CHECKABLE:
			return self.checkable
		elif role == Base_Item_Data_Roles.USER:
			return self
		elif role == Base_Item_Data_Roles.TREE_OBJECT:
			return self.tree_item
		elif role == Base_Item_Data_Roles.INTERNAL_EDITOR:
			return self.internal_editor
		return None
	#----------------------------------------------------------------------
	def setData(self, role, value):
		res = False

		if role in [Base_Item_Data_Roles.DISPLAY, Base_Item_Data_Roles.EDIT]:
			self.display_name = value
			res = True
		elif role == Base_Item_Data_Roles.FOREGROUND:
			self.foreground_color = value
			res = True
		elif role == Base_Item_Data_Roles.BACKGROUND:
			self.background_color = value
			res = True
		elif role == Base_Item_Data_Roles.SIZEHINT:
			self.size_hint        = value
			res = True
		elif role == Base_Item_Data_Roles.TOOLTIP:
			self.tool_tip         = value
			res = True
		elif role == Base_Item_Data_Roles.STATUSTIP:
			self.status_tip       = value
			res = True
		elif role == Base_Item_Data_Roles.FONT:
			self.text_font        = value
			res = True
		elif role == Base_Item_Data_Roles.TEXT_ALIGNMENT:
			self.text_alignment   = value
			res = True
		elif role == Base_Item_Data_Roles.DECORATION:
			self.brush            = value
			res = True
		elif role == Base_Item_Data_Roles.ICON_COLOR:
			self.icon_color       = value
			res = True
		elif role == Base_Item_Data_Roles.FONT_SIZE:
			self.text_size        = value
		elif role == Base_Item_Data_Roles.FONT_WEIGHT:
			self.font_weight      = value
			res = True
		elif role == Base_Item_Data_Roles.FONT_FAMILY:
			self.font_family         = value
			res = True
		elif role == Base_Item_Data_Roles.FONT_CAPITALIZATION:
			self.font_capitalization = value
			res = True
		elif role == Base_Item_Data_Roles.SELECTABLE:
			self.selectable        = value
			res = True
		elif role == Base_Item_Data_Roles.ENABLED:
			self.enabled =  value
			res = True
		elif role == Base_Item_Data_Roles.EDITABLE:
			self.editable = value
			res = True
		elif role == Base_Item_Data_Roles.DRAGABLE:
			self.dragable = value
			res = True
		elif role == Base_Item_Data_Roles.DROPABLE:
			self.dropable = value
			res = True
		elif role == Base_Item_Data_Roles.CHECKABLE:
			self.checkable = value
			res = True
		elif role == Base_Item_Data_Roles.CHECKSTATE:
			self.checked = value
		elif role == Base_Item_Data_Roles.TRISTATE:
			self.tristate = value
			res = True
		elif role == Base_Item_Data_Roles.HORIZONTAL_ALIGNMENT:
			self.horizontal_alignment = value
			res = True
		elif role == Base_Item_Data_Roles.VERTICAL_ALIGNMENT:
			self.vertical_alignment = value
			res = True
		return res
	#----------------------------------------------------------------------
	def _update_Changed_Data(self, role):
		""""""
		index =  self.index
		try:
			self.tree_item.model.dataChanged.emit(index, index, role)
		except:
			self.tree_item.model.dataChanged.emit(index, index)

########################################################################
class Internal_Item_Data(Standered_Item_Data):
	"""This Is The Item Data Class For Use If Any Costom Data Needs To Be Accesed This Data Is Contained in the internal_data attribute"""
	#----------------------------------------------------------------------
	def __init__(self,
	             tree_item            = None,
	             selectable           = None, enabled             = None, editable     = None,
	             dragable             = None, dropable            = None, checkable    = None, checked = False,
	             tristate             = None, font_family         = None, font_size    = None,
	             size_hint            = None, status_tip          = None, tool_tip     = None,
	             brush                = None, icon_visable        = None, icon_color   = None,
	             font_weight          = None, font_capitalization = None, display_name = None,
	             background_color     = None, foreground_color    = None,
	             horizontal_alignment = None, vertical_alignment  = None,
	             internal_data = None):
		""" """
		super(Internal_Item_Data, self).__init__(tree_item,
		                                selectable           = selectable          , enabled             = enabled            , editable     = editable,
		                                dragable             = dragable            , dropable            = dropable           , checkable    = checkable, checked=checked,
		                                tristate             = tristate            , font_family         = font_family        , font_size    = font_size,
		                                size_hint            = size_hint           , status_tip          = status_tip         , tool_tip     = tool_tip,
		                                brush                = brush               , icon_visable        = icon_visable       , icon_color   = icon_color,
		                                font_weight          = font_weight         , font_capitalization = font_capitalization, display_name = display_name,
		                                background_color     = background_color    , foreground_color    = foreground_color,
		                                horizontal_alignment = horizontal_alignment, vertical_alignment  = vertical_alignment)
		self._internal_data = internal_data
	#----------------------------------------------------------------------
	def data(self, role=Base_Item_Data_Roles.DISPLAY):
		if role == Base_Item_Data_Roles.INTERNAL_DATA:
			return self._internal_data
		return super(Internal_Item_Data, self).data(role)
	#----------------------------------------------------------------------
	def setData(self, role, value):
		if role == Base_Item_Data_Roles.INTERNAL_DATA:
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
# ======================================================================
# DATA MODEL STANDERD ITEM CONTAINERS
# ----------------------------------------------------------------------
# Synopsis:
#     Like A StanderedItem
# ======================================================================
########################################################################
class Column_Item_List(object):
	#----------------------------------------------------------------------
	def __init__(self, tree_item):
		""" """
		if not hasattr(tree_item, "root_item"):
			raise TypeError("tree_item %r input does not contain a root_item attribute" % type(tree_item))
		self.tree_item = tree_item
		self.items     = []
	#----------------------------------------------------------------------
	def __iter__(self):
		""""""
		for item in self.items:
			yield item
	#----------------------------------------------------------------------
	def data(self, column=0, role=Base_Item_Data_Roles.DISPLAY):
		try:
			item = self.items[column]
			return item.data(role)
		except IndexError:
			return None
	#----------------------------------------------------------------------
	def setData(self, value, column=0, role=Base_Item_Data_Roles.DISPLAY):
		item = self.get_item(column)
		return item.setData(role, value)
	#----------------------------------------------------------------------
	def get_item(self, column=0):
		if column >= self.column_Count:
			return None
		item = self.items[column]
		isinstance(item, Internal_Item_Data)
		return item
	#----------------------------------------------------------------------
	def get_Item_Flags(self, index):
		item = self.get_item(index)
		if item is None:
			res = PYQT.Qt.ItemFlag.NoItemFlags
		else:
			res = item.flags
		return res
	#----------------------------------------------------------------------
	@property
	def column_Count(self):
		""""""
		return len(self.items)
	##----------------------------------------------------------------------
	@property
	def model(self):
		""""""
		return self.tree_item.root_item.model
	#----------------------------------------------------------------------
	def _get_Current_State(self):
		""""""
		state = []
		for column in self:
			isinstance(column, Internal_Item_Data)
			column_state = column.get_Current_State()
			state.append(column_state)
		return state
	#----------------------------------------------------------------------
	def get_Icon_Visable(self,column=0):
		"""Returns Weather Or Not The Icon Is Visable"""
		item = self.get_item(column)
		return False if item is None else item.icon_visable
	#----------------------------------------------------------------------
	def set_icon_visable(self, value, column=0):
		"""Set Weather Or Not The Icon Is Visable"""
		item = self.get_item(column)
		if not item is None:
			item.icon_visable = value
	#----------------------------------------------------------------------
	def get_background_color(self,column=0):
		"""Get The Backround Color Of A Item"""
		item = self.get_item(column)
		return None if item is None else item.background_color
	#----------------------------------------------------------------------
	def set_background_color(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.background_color = value
	#----------------------------------------------------------------------
	def get_foreground_color(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.foreground_color
	#----------------------------------------------------------------------
	def set_foreground_color(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.foreground_color = value
	#----------------------------------------------------------------------
	def get_brush(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.brush
	#----------------------------------------------------------------------
	def set_brush(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.brush = value
	#----------------------------------------------------------------------
	def get_size_hint(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.size_hint
	#----------------------------------------------------------------------
	def set_size_hint(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.size_hint = value
	#----------------------------------------------------------------------
	def get_status_tip(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.status_tip
	#----------------------------------------------------------------------
	def set_status_tip(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.status_tip = value
	#----------------------------------------------------------------------
	def get_tool_tip(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.tool_tip
	#----------------------------------------------------------------------
	def set_tool_tip(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.tool_tip = value
	#----------------------------------------------------------------------
	def get_vertical_alignment(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.vertical_alignment
	#----------------------------------------------------------------------
	def set_vertical_alignment(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.vertical_alignment = value
	#----------------------------------------------------------------------
	def get_horizontal_alignment(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.horizontal_alignment
	#----------------------------------------------------------------------
	def set_horizontal_alignment(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.horizontal_alignment = value
	#----------------------------------------------------------------------
	def get_text_alignment(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.text_alignment
	#----------------------------------------------------------------------
	def get_font_family(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.font_family
	#----------------------------------------------------------------------
	def set_font_family(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.font_family = value
	#----------------------------------------------------------------------
	def get_font_size(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.font_size
	#----------------------------------------------------------------------
	def set_font_size(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.font_size = value
	#----------------------------------------------------------------------
	def get_font_weight(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.font_weight
	#----------------------------------------------------------------------
	def set_font_weight(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.font_weight = value
	#----------------------------------------------------------------------
	def get_font_capitalization(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.font_capitalization
	#----------------------------------------------------------------------
	def set_font_capitalization(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.font_capitalization = value
	#----------------------------------------------------------------------
	def get_selectable(self,column=0):
		item = self.get_item(column)
		return False if item is None else item.selectable
	#----------------------------------------------------------------------
	def set_selectable(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.selectable = value
	#----------------------------------------------------------------------
	def get_enabled(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.enabled
	#----------------------------------------------------------------------
	def set_enabled(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.enabled = value
	#----------------------------------------------------------------------
	def get_editable(self,column=0):
		item = self.get_item(column)
		return False if item is None else item.editable
	#----------------------------------------------------------------------
	def set_editable(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.editable = value
	#----------------------------------------------------------------------
	def get_dragable(self,column=0):
		item = self.get_item(column)
		return False if item is None else item.dragable
	#----------------------------------------------------------------------
	def set_dragable(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.dragable = value
	#----------------------------------------------------------------------
	def get_dropable(self,column=0):
		item = self.get_item(column)
		return False if item is None else item.dropable
	#----------------------------------------------------------------------
	def set_dropable(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.dropable = value
	#----------------------------------------------------------------------
	def get_checkable(self,column=0):
		item = self.get_item(column)
		return False if item is None else item.checkable
	#----------------------------------------------------------------------
	def set_checkable(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.checkable = value
	#----------------------------------------------------------------------
	def get_tristate(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.tristate
	#----------------------------------------------------------------------
	def set_tristate(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.tristate = value
	#----------------------------------------------------------------------
	def get_display_name(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.display_name
	#----------------------------------------------------------------------
	def set_display_name(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.display_name = value
	#----------------------------------------------------------------------
	def get_icon_color(self,column=0):
		item = self.get_item(column)
		return None if item is None else item.icon_color
	#----------------------------------------------------------------------
	def set_icon_color(self, value, column=0):
		item = self.get_item(column)
		if not item is None:
			item.icon_color = value
	#----------------------------------------------------------------------
	def get_font(self,column=0):
		""""""
		item = self.get_item(column)
		return False if item is None else item.font
	#----------------------------------------------------------------------
	def get_icon(self,column=0):
		""""""
		item = self.get_item(column)
		return False if item is None else item.icon
