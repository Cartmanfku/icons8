__author__ = 'cartman'


import os

def modify_icon_file_name(dir_path, icon, prefix, suffix, color=None):
    try:
        if icon.startswith(prefix):
            if color is not None and not icon.startswith(prefix + color):
                icon_name = icon.replace(prefix, prefix + color + '_')
            else:
                return
        else:

            icon_name = icon.split('.')[0]
            icon_name = icon_name.strip()
            icon_name = icon_name.lower()
            icon_name = icon_name.replace(' ','_')
            icon_name = icon_name.replace('+','plus')
            icon_name = icon_name.replace('-','minus')
            if color is not None:
                icon_name = prefix + color + '_' + icon_name + suffix
            else:
                icon_name = prefix + icon_name + suffix

        print icon_name
        os.rename(os.path.join(dir_path,icon), os.path.join(dir_path, icon_name))

    except Exception,e:
        print e.message
        print e.args
    finally:
        pass

def match_app_dir_pattern(dir_name, prefix, colored=False):

    if not dir_name.startswith(prefix):
        return None

    temp = dir_name.split('_')
    if colored:
        if len(temp) < 3:
            return None
        else:
            return temp[0],temp[1]
    else:
        return temp[0],None

root_path = './'
app_icon_prefix = 'app_'
icon_suffix = '.png'
icon_prefix = 'icon_'

files = os.listdir(root_path)
for f in files:
    file_path = os.path.join(root_path, f)
    if os.path.isdir(file_path):
        ret = match_app_dir_pattern(f, app_icon_prefix, True)
        print ret
        if ret is not None:
            icons = os.listdir(file_path)
            for icon in icons:
                icon_path = os.path.join(file_path, icon)
                if os.path.isfile(icon_path) and icon.endswith(icon_suffix):
                    modify_icon_file_name(file_path, icon, icon_prefix, icon_suffix, ret[1])
        else:
            print 'not match app icon directory name pattern: app_[color]_'

