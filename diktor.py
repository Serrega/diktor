import os


if __name__ == '__main__':
    diktor_variant = '  diktor          ru: diktor\n'
    try:
        with open('/usr/share/X11/xkb/rules/evdev.lst', 'r') as file_r:
            content = file_r.readlines()
    except BaseException as be:
        print('file open error', be)

    if ind := content.index('! variant\n'):
        try: 
            content.index(diktor_variant)
        except ValueError:
            content.insert(ind + 1, diktor_variant)
            try:
                with open('/usr/share/X11/xkb/rules/evdev.tmp', 'a') as file_a:
                    file_a.writelines(content)
            except BaseException as be:
                print('file write error', be)
            os.rename('/usr/share/X11/xkb/rules/evdev.lst', '/usr/share/X11/xkb/rules/evdev.lst.old')
            os.rename('/usr/share/X11/xkb/rules/evdev.tmp', '/usr/share/X11/xkb/rules/evdev.lst')
        else:
            print('diktor_variant just is in evdev.lst')
            
    else:
        print('! variant not found')

    diktor_xml = "        <variant>\n          <configItem>\n            <name>diktor</name>\n            " \
                 "<description>diktor</description>\n            <languageList>\n              " \
                 "<iso639Id>rus</iso639Id>\n            " \
                 "</languageList>\n          </configItem>\n        </variant>\n"
    try:
        with open('/usr/share/X11/xkb/rules/evdev.xml', 'r') as file_r:
            content = file_r.readlines()
    except BaseException as be:
        print('file open error', be)

    if ind := content.index('            <description>Mari</description>\n'):
        if '            <description>diktor</description>\n' in content:
            print('diktor_xml just is in evdev.xml')
        else:
            content.insert(ind + 6, diktor_xml)
            try:
                with open('/usr/share/X11/xkb/rules/evdev.tmp', 'a') as file_a:
                    file_a.writelines(content)
            except BaseException as be:
                print('file write error', be)
            os.rename('/usr/share/X11/xkb/rules/evdev.xml', '/usr/share/X11/xkb/rules/evdev.xml.old')
            os.rename('/usr/share/X11/xkb/rules/evdev.tmp', '/usr/share/X11/xkb/rules/evdev.xml')
    else:
        print('<description>Mari</description> not found')




