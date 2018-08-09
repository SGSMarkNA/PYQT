import os
import lxml.etree

def generate_widget_code(tree,QT_modual_prefix="CFQT"):
	code = []  
	#code.append("import AW_Asset_Assembly_System.CFQT")
	#code.append("CFQT = AW_Asset_Assembly_System.CFQT")
	
	#import_code = "from AW_Asset_Assembly_System.Main_Window import"
	#for wig in tree.findall(".//widget"):
		#if not wig.get("name").startswith("Q"):
			#import_code += " %s," % wig.get("name")
	#import_code = import_code[:-1]
	#code.append(import_code)
	
	code.append("########################################################################")
	code.append("class _CODE_COMPLEATION_HELPER(CFQT.QMainWindow):")
	code.append('\t""""""')
	code.append("\t#----------------------------------------------------------------------")
	code.append("\tdef __init__(self,parent=None):")
	code.append("\t\t''''''")
	code.append("\t\tsuper(_CODE_COMPLEATION_HELPER,self).__init__(parent=parent)")
	code.append("\t\tif False:")
	
	for wig in tree.findall(".//widget"):
		if wig.get("class").startswith("Q"):
			code.append("\t\t\tself.%s = %s.%s()" % (wig.get("name"),QT_modual_prefix,wig.get("class")))
		else:
			code.append("\t\t\tself.%s = %s()" % (wig.get("name"),wig.get("class")))
			
	for wig in tree.findall(".//action"):
		code.append("\t\t\tself.%s = %s.QAction()" % (wig.get("name"),QT_modual_prefix))
	print "\n".join(code)

file_directory = os.path.dirname(__file__)
_ui = os.path.join(file_directory,"Simple_Display.ui")	
tree = lxml.etree.parse(r"C:\Users\dloveridge\Documents\maya\scripts\AW_States_Manager.ui")
generate_widget_code(tree,"PYQT")
