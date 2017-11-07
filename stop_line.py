#!/usr/bin/env python3

import line_api
import json
import setting
import sys
import signal
import processing_input

line_api.push_message(setting.ID, ['停止'])
