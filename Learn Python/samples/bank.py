import concurrent.futures
import threading
from datetime import datetime
import json


"""
The db holds the user's details
the acc.no, username , the cash present 
data visualization:
// add other fields
{acc_no:{username:'', cash_present: '', date_added: ''}}
"""


class DatabaseMock:
    def __init__(self):
        self.db_dict = {}
        self._lock = threading.Lock()

    def add_items(self, username: str, cash_present: float, acc_no: int):
        # you need to add the user's details for a new user
        # to prevent race conditions
        with self._lock:
            # create a local copy rather than modifying the dict directly
            local_copy = self.db_dict
            date_added = datetime.strftime(datetime.now(), "%Y-%d-%b")
            local_copy[acc_no] = {'username': username, 'cash_present': cash_present, 'date_added': date_added}
            # update the dic to the new local copy
            self.db_dict = local_copy

    def get_acc_detail(self, acc_no):
        print('-------------------------------')
        if self.db_dict[acc_no]:
            for k, v in self.db_dict[acc_no].items():
                if k == 'cash_present':
                    v = "Ksh " + str(v)
                    # print(k)
                print(k, ':', v)
        else:
            print(f"The account no: {acc_no} provided does not exist")

    def get_account_details(self):
        if self.db_dict:
            print('-------------------------------')
            for key, value in self.db_dict.items():
                print(f'account no: {key}')
                for k, v in value.items():
                    if k == 'cash_present':
                        v = v * 2
                        v = "ksh " + str(v)
                        print(k)
                    print(k, ':', v)
                print('----------------------')
        else:
            print("Sorry there is no information yet ! ")

    def double_values(self):
        if self.db_dict:
            print('-------------------------------')
            for key, value in self.db_dict.items():
                print(f'account no: {key}')
                for k, v in value.items():
                    if k == 'cash_present':
                        v = v * 2
                        v = "ksh "+ str(v)
                        print(k)
                    print(k, ':', v)
                print('----------------------')
        else:
            print("sorry the db has no values at the moment")


if __name__ == '__main__':
    database = DatabaseMock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executors:
        executors.submit(database.add_items, "Gibson", 14000.00, 1)
        executors.submit(database.add_items, "Joan", 30000.00, 2)
        json.dumps(database.db_dict, indent=2)
        print(database.get_acc_detail(2))
