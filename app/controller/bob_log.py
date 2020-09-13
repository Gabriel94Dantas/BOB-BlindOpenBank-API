"""
    The module is responsible for control actions when the model domain will be a bob_log
"""

from app.model.bob_log import BobLog
from app.constants import constants
from app.util import date

"""
    The class is responsible for control actions when the model domain will be a bob_log
"""


class BobLogController:
    bob_log_class = BobLog()

    def find_all_bob_log(self, adm_token):
        """
        This method is responsible to control find_all bob_log
        endpoint
        :param: None
        :return: bob_log_array_json if exists logs. If log doesn't
        exists to return not found
        """
        if adm_token != constants.ADM_TOKEN:
            return constants.UNAUTHORIZED
        bob_logs = self.bob_log_class.find_all()
        bob_log_array_json = []
        if bob_logs:
            for bob_log in bob_logs:
                bob_log_json = self.bob_log_class.bob_log_to_json(bob_log)
                bob_log_array_json.append(bob_log_json)
            return bob_log_array_json
        else:
            return constants.NOT_FOUND

    def insert_bob_log(self, bob_log):
        """
        This method is responsible to control insert of bob_log
        """
        self.bob_log_class.insert_bob_log(bob_log)

    def set_bob_log(self, client_json, operation_type, description):
        """
        This method is responsible to set bob_log
        :param client_json: JSON
        :param operation_type: String
        :param description: String
        :return: bob_log
        """
        bob_log = BobLog()
        bob_log.operation_type = operation_type
        bob_log.operation_time = date.current_time()
        bob_log.user_id = client_json['user_id']
        bob_log.device_id = client_json['device_id']
        bob_log.description = description

        return bob_log
