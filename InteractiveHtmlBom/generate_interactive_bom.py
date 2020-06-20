#!/usr/bin/python3
from __future__ import absolute_import

import argparse
import os
import sys


# python 2 and 3 compatibility hack
def to_utf(s):
    if isinstance(s, bytes):
        return s.decode('utf-8')
    else:
        return s

# i18n
# method：1 similar to GUN gettext API，2 Python gettext
method = 1
 
if method == 1:
    import gettext
    lang_domain = "wx_i18n"
    lang_localedir = os.path.abspath("i18n")
    gettext.bindtextdomain(lang_domain, lang_localedir)
    gettext.textdomain(lang_domain)
    os.environ['LANGUAGE'] = "zh_CN"
    import builtins
    __builtins__.__dict__['_'] = gettext.gettext

if method == 2:
    import gettext
    lang_domain = "wx_i18n"
    lang_localedir = os.path.abspath("i18n")
    zh_CN = gettext.translation(domain=lang_domain, localedir=lang_localedir, languages=['zh_CN'])
    zh_CN.install(True)
    en_US = gettext.translation(lang_domain, lang_localedir, languages=['en_US'])
    en_US.install(True)


if __name__ == "__main__":
    if '_' in GUI_Frame.__dict__:
        GUI_Frame.__dict__.pop('_')
    # Add ../ to the path
    # Works if this script is executed without installing the module
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(script_dir))
    os.environ['INTERACTIVE_HTML_BOM_CLI_MODE'] = 'True'
    import InteractiveHtmlBom

    from InteractiveHtmlBom.core import ibom
    from InteractiveHtmlBom.core.config import Config
    from InteractiveHtmlBom.ecad import get_parser_by_extension
    from InteractiveHtmlBom.version import version

    create_wx_app = 'INTERACTIVE_HTML_BOM_NO_DISPLAY' not in os.environ
    if create_wx_app:
        import wx
        app = wx.App()

    parser = argparse.ArgumentParser(
            description=_('KiCad InteractiveHtmlBom plugin CLI.'),
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('file',
                        type=lambda s: to_utf(s),
                        help=_("KiCad PCB file"))
    config = Config(version)
    config.add_options(parser, config.FILE_NAME_FORMAT_HINT)
    args = parser.parse_args()
    if not os.path.isfile(args.file):
        print(_("File %s does not exist.") % args.file)
        exit(1)
    print(_("Loading %s") % args.file)
    logger = ibom.Logger(cli=True)
    parser = get_parser_by_extension(os.path.abspath(args.file), config, logger)
    if args.show_dialog:
        if not create_wx_app:
            print(_("Can not show dialog when INTERACTIVE_HTML_BOM_NO_DISPLAY is set."))
            exit(1)
        ibom.run_with_dialog(parser, config, logger)
    else:
        config.set_from_args(args)
        ibom.main(parser, config, logger)
