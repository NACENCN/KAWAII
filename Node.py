#coding=utf-8
try:
    from importlib import reload
except:
    from imp import reload
finally:
    pass

def run():
    import picker 
    reload (picker) 
    picker.pickerWindow.show() 

def onMayaDroppedPythonFile(param):
    run() 
