import os
import sys
sys.path.append(os.path.join(os.path.abspath('.'), 'lib'))

from flask import Flask
import settings

app = Flask('application')
app.config.from_object('application.settings')

import views