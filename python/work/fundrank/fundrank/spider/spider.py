import requests
from pyquery import PyQuery as pq

from ..common import utils

def get_fund(fund_id) :
    print("#################  get_fund start #####################")

    print(fund_id)

    print(utils.get_style_key("1"))

    result = {}

    try:
        url = "http://jingzhi.funds.hexun.com/database/openjjgk.aspx?fundcode=" + fund_id

        print(url)

        r = requests.get(url)

        doc = pq(r.text)

        result['code'] = fund_id

        result['name'] = doc("#gaikuang tr").eq(0)("td").eq(1).text()

        result['type'] = doc("#gaikuang tr").eq(1)("td").eq(3).text()

        result['style'] = doc("#gaikuang tr").eq(1)("td").eq(1).text()

        result['start_date'] = doc("#gaikuang tr").eq(3)("td").eq(1).text()

        result['manager'] = doc("#gaikuang tr").eq(3)("td").eq(3).text()

        result['scale'] = doc("#gaikuang tr").eq(2)("td").eq(3).text()

        url = "http://jingzhi.funds.hexun.com/database/sgfl.aspx?fundcode=" + fund_id

        print(url)

        r = requests.get(url)

        doc = pq(r.text)

        result['mng_rate'] = doc("#fundData tr").eq(-2)("td").eq(4).text()

        result['dps_rate'] = doc("#fundData tr").eq(-1)("td").eq(4).text()

        url = "http://jingzhi.funds.hexun.com/"  + fund_id +"/jingli.shtml"

        print(url)

        r = requests.get(url)

        doc = pq(r.text)

        result['manager_date'] = doc("h6:eq(0)").text()[-10:]
    
    except Exception as e:
        print(e)
        result = {
            'code': '000000',
        }

    print("#################  get_fund end #####################")

    return result