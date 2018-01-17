import cgitb

cgitb.enable()

import common_html

print(common_html.start_response())

print(common_html.include_header("wujian's web test 01"))

print(common_html.do_form('templates/testWeb_01_form.html', 'testWeb_01_addtime.py',3, text='send'))

print(common_html.include_footer({"Home":"/index.html","Select another runner":"testWeb_01_runnerlist.py"}))