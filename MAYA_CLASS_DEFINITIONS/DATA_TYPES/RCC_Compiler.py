import os
from AW_Asset_Assembly_System.GENERAL_TOOLS.pathlib2 import Path

def compile_rcc_file(rcc_file, dest_foulder=None, dest_name=None):
	rcc_file = Path(rcc_file)
	if not rcc_file.exists:
		raise IOError("File %r Does Not Exist" % str(rcc_file))
	
	if dest_foulder is None:
		dest_foulder = rcc_file.parent
	else:
		dest_foulder = Path(dest_foulder)
		
	if dest_name is None:
		dest_name = rcc_file.with_suffix(".py")
		dest_name =  os.path.splitext(os.path.basename(str(rcc_file)))[0] + ".py"
	dest_path =  os.path.join(str(dest_foulder), str(dest_name))

	command = 'C:/Python27/Lib/site-packages/PySide/pyside-rcc.exe -o "%s" -py2 -name runit "%s"' % (dest_path, rcc_file)
	os.system(command)

if __name__ == "__main__":
	compile_rcc_file(os.path.join(os.path.dirname(__file__), "Outline_Icons\outliner_icons.qrc") , dest_foulder=os.path.dirname(__file__) )
