#!/bin/bash
cd /opt/webapps/mayan-edms/
source bin/activate
python mayan/bin/mayan-edms.py pickup
python mayan/bin/mayan-edms.py run_processes