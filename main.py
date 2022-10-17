import win32com.client as win32
from treelib import Tree
import re

sw_edition = 2019
swApp = win32.Dispatch('SldWorks.Application.{}'.format(sw_edition - 1992))
swApp.Visible = True

swModel = swApp.ActiveDoc
swConfMgr = swModel.ConfigurationManager
swConf = swConfMgr.ActiveConfiguration
swRoot = swConf.GetRootComponent

print(swRoot.ComponentReference)

py_tree = Tree()
py_tree.create_node(swRoot.name,swRoot.Name2)

def find_child(parent_comp, py_tree):
    tmp = parent_comp.GetChildren
    if tmp != None:
        for i in tmp:
            if not parent_comp.IsRoot:
                child_name = i.Name2[len(parent_comp.Name2)+1:]
            else:
                child_name = i.Name2
            py_tree.create_node(re.match(r'(.*)-(\d*)',child_name).group(1),i.Name2,parent=parent_comp.Name2,data=i)
            find_child(i,py_tree)

# find_child(swRoot,py_tree)

# py_tree.show()


