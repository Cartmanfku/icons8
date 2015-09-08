__author__ = 'cartman'


import os

def modify_icon_file_name(dir_path, icon, prefix, suffix):
    try:
        icon_name = icon.split('.')[0]
        icon_name = icon_name.strip()
        icon_name = icon_name.lower()
        icon_name = icon_name.replace(' ','_')
        icon_name = icon_name.replace('+','plus')
        icon_name = icon_name.replace('-','minus')
        icon_name = prefix + icon_name + suffix
        print icon_name
        os.rename(os.path.join(dir_path,icon), os.path.join(dir_path, icon_name))
    except Exception,e:
        print e.message
        print e.args
    finally:
        pass



root_path = './'
app_icon_prefix = 'app_'
icon_suffix = '.png'
icon_prefix = 'icon_'

files = os.listdir(root_path)
for f in files:
    file_path = os.path.join(root_path, f)
    if os.path.isdir(file_path) and f.startswith(app_icon_prefix):
        icons = os.listdir(file_path)
        for icon in icons:
            icon_path = os.path.join(file_path, icon)
            if os.path.isfile(icon_path) and icon.endswith(icon_suffix):
                modify_icon_file_name(file_path, icon, icon_prefix, icon_suffix)

