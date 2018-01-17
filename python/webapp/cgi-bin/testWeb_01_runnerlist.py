import testWeb_01_datasl
import common_html
import glob

webdata = testWeb_01_datasl.init_web_data()

print(common_html.start_response())
print(common_html.include_header("wujian's web test 01"))
print(common_html.start_form("testWeb_01_timingdata.py"))
print(common_html.para("select an runner from the list:"))

for each_runner in webdata:
    print(common_html.radio_button("runner",webdata[each_runner].name))

print(common_html.end_form("Select"))

print(common_html.include_footer({"Home":"/index.html"}))

