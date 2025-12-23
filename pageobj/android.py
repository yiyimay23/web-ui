# -*- coding: utf-8 -*-
# @File: android.py.py

import os
import sys

sys.path.append(os.pardir)

from public import App




class OpenWeChatPage(App):

    def click_login_button(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)
