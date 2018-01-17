import cgitb

cgitb.enable()

import cgi
import common_html
import testWeb_01_datasl

webdata = testWeb_01_datasl.get_web_data()

form_data = cgi.FieldStorage()

r_name = form_data["runner"].value

print(common_html.start_response())
print(common_html.include_header("wujian's web test 01"))

print(common_html.header("Runner: " + r_name + "'s top times are :"))

print(common_html.u_list(webdata[r_name].getTop3()))

print(common_html.include_footer({"Home":"/index.html","Select another runner":"testWeb_01_runnerlist.py","Add a timing data":"testWeb_01_timinginput.py"}))