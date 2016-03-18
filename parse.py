import base64
import os.path

import requests
import sys


def get_resp_by(key):
    path = "http://enter.seclab.stepic.org/getdata.php?req="
    resp = requests.get(path + base64.b64encode(key.encode('ascii')).decode('ascii'))
    if resp.status_code == 200:
        return resp.text
    else:
        return False


def check_for_result(string, len_blank):
    if len(string) == len_blank:
        return False
    else:
        return True

if len(sys.argv) < 2:
    print("use parse.py filename")
    exit(1)

if not os.path.exists(sys.argv[1]):
    print(sys.argv[0] + " file not found")
    exit(1)

blank = "1:<br>2:<br>3:<br>4:<br>5:<br>"
blank_len = len(blank)


with open(sys.argv[1], "r") as dict:
    for item in dict:
        item = item.rstrip()
        resp = get_resp_by(item)
        if resp:
            check = check_for_result(resp, blank_len)
            if check:
                out = resp.replace("<br>", " ")
                print(out)
                result_file = open('parsepy_out.txt', 'a')
                result_file.write("key: " + item + " \t" + out + "\n")
                result_file.close()
            else:
                print(item + " : False")
        else:
            print("Alert! error on key " + item + ", script stopped")
            exit(1)
