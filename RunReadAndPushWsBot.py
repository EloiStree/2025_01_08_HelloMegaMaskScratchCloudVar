import os
import sys

"""
Thie Script is aim to read and push integer from local UDP to Scratch Websocket

Not coded yet.
"""


username_password_path = "/token/scratch_log_in.txt"
if not os.path.exists(username_password_path):
    print("No file found at: " + username_password_path)
    sys.exit()


with open(username_password_path, "r") as file:
    username = file.readline().strip()
    password = file.readline().strip()


class ScratchCloudVarToInteger:
    def __init__(self,project_id, cloud_var_name):
        self.project_id = project_id
        self.cloud_var_name = cloud_var_name
    def __str__(self):
        return "Cloud var name: {0}, cloud var value: {1}".format(self.cloud_var_name, self.cloud_var_value)
