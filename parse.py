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
    exit("use parse.py filename")

if not os.path.exists(sys.argv[1]):
    exit(sys.argv[1] + " file not found")

blank = "1:<br>2:<br>3:<br>4:<br>5:<br>"
blank_len = len(blank)


with open(sys.argv[1], "r") as dict:
    for word in dict:
        word = word.rstrip()
        resp = get_resp_by(word)
        if resp:
            check = check_for_result(resp, blank_len)
            if check:
                out = resp.replace("<br>", " ")
                print(out)
                result_file = open('parsepy_out.txt', 'a')
                result_file.write("key: " + word + " \t" + out + "\n")
                result_file.close()
            else:
                print(word + " : False")
        else:
            exit("Alert! error on key " + word + ", script stopped")
