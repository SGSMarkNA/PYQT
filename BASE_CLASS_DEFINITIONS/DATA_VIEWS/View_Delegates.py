import PYQT
from ..Base_Item_Data_Roles import Base_Item_Data_Roles


class SpinBoxDelegate(PYQT.QItemDelegate):
	def createEditor(self, parent, option, index):
		val = index.data(PYQT.BASE_CLASS_DEFINITIONS.Item_Data_Roles.Base_Item_Data_Roles.USER)
		editor = None
		if hasattr(val,"has_editor"):
			if val.has_editor:
				editor = val.create_editor(parent=parent)
		if editor == None:
			editor = super(SpinBoxDelegate,self).createEditor(parent, option, index)

		return editor

	def setEditorData(self, spinBox, index):
		value = index.model().data(index, PYQT.Qt.EditRole)

		spinBox.setValue(int(value))

	def setModelData(self, spinBox, model, index):
		spinBox.interpretText()
		value = spinBox.value()

		model.setData(index, value, PYQT.Qt.EditRole)

	def updateEditorGeometry(self, editor, option, index):
		editor.setGeometry(option.rect)

class Item_View_Delegate(PYQT.QItemDelegate):

	def paint(self, painter, option, index):
		super(Item_View_Delegate, self).paint(painter, option, index)
	# #----------------------------------------------------------------------
	def drawDisplay(self, painter, option, rect, text):
		if option.widget.underMouse():
			painter.drawRect(rect.adjusted(2, 2, -2, -1))
			painter.drawText(rect, CFQT.AlignmentFlag.Horizontal.Center|CFQT.AlignmentFlag.Vertical.Center, text)
			painter.fillRect(rect, CFQT.Colors.BLUE)
		else:
			super(Item_View_Delegate, self).drawDisplay(painter, option, rect, text)
	#----------------------------------------------------------------------
	def drawFocus(self, painter, option, rect):
		""""""
		isinstance(painter, PYQT.QPainter)
		isinstance(rect, PYQT.QRect)
		if option.widget._item_under_mouse is not None:
			painter.fillRect(option.widget.visualRect(option.widget._item_under_mouse), CFQT.Colors.RED)
			painter.drawText(rect, CFQT.AlignmentFlag.Horizontal.Center|CFQT.AlignmentFlag.Vertical.Center, option.widget._item_under_mouse.data())
		else:
			super(Item_View_Delegate, self).drawFocus(painter, option, rect)
	#----------------------------------------------------------------------
	def drawBackground (self, painter, option, index):
		painter.fillRect(option.widget.visualRect(option.widget.CurrentIndex), CFQT.Colors.BLUE)
		super(Item_View_Delegate, self).drawBackground(painter, option, rect)
	#----------------------------------------------------------------------
	def createEditor(self, parent, option, index):
		# editor = QtGui.QSpinBox(parent)
		# editor.setMinimum(0)
		# editor.setMaximum(100)
		editor = super(Item_View_Delegate, self).createEditor(parent, option, index)
		return editor
	#----------------------------------------------------------------------
	def setEditorData(self, spinBox, index):
		super(Item_View_Delegate, self).setEditorData(spinBox, index)
		# value = index.model().data(index, QtCore.Qt.EditRole)
		# spinBox.setValue(value)
	#----------------------------------------------------------------------
	def setModelData(self, spinBox, model, index):
		# # spinBox.interpretText()
		# # value = spinBox.value()
		super(Item_View_Delegate, self).setModelData(spinBox, model, index)
		# model.setData(index, value, QtCore.Qt.EditRole)
	# #----------------------------------------------------------------------
	# def updateEditorGeometry(self, editor, option, index):
		# super(Item_View_Delegate, self).updateEditorGeometry(editor, option, index)
		# # editor.setGeometry(option.rect)

