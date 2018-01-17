import cgitb

cgitb.enable()

import os
import time
import sys
import cgi
import common_html
import commondist
import testWeb_01_datasl


print(common_html.start_response())

print(common_html.include_header("wujian's web test 01"))

form_data = cgi.FieldStorage()

webdata = testWeb_01_datasl.get_web_data()

#commondist.printDict(os.environ,sys.stderr)

#commondist.printDict(form_data)

for each_key in form_data.keys():
    print(each_key + '=>' + form_data[each_key].value + '<br/>')

print(file=sys.stderr)


print(common_html.include_footer({"Home":"/index.html","Select another runner":"testWeb_01_runnerlist.py","Add a timing data":"testWeb_01_timinginput.py"}))