import os
import sys
"""

This script allows to listen every n seconds to http public info of the project scratch.
It checkf for new value and realy it to Udp local port.

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
