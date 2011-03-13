# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 Pierre Raybaut
# Licensed under the terms of the MIT License
# (see spyderlib/__init__.py for details)

from guidata.gettext_helpers import do_rescan, do_rescan_files

if __name__ == "__main__":
    do_rescan("spyderlib")
    do_rescan_files(["spyderplugins/p_pylint.py",
                     "spyderplugins/widgets/pylintgui.py"],
                     "p_pylint", "spyderplugins")