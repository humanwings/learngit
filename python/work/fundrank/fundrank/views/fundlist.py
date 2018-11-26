from datetime import datetime

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import Fund
# from ..models import FundTypeEnum
# from ..models import FundStyleEnum

# from ..spider.spider import get_fund

from ..spider import get_fund

from ..common import utils

@view_config(route_name='fundlist', request_method='GET', renderer='../templates/fundlist.jinja2')
def fundlist_view(request):
    
    print("#################  fundlist_view start #####################")

    print(request)

    try:
        query = request.dbsession.query(Fund).order_by(Fund.code)

        fundlist = []
        
        for one in query :

            fund = Fund()
            
            fund.code = one.code
            fund.name = one.name
            fund.type = utils.get_type_value(one.type)
            fund.style = utils.get_style_value(one.style)
            fund.start_date = str(one.start_date or '')
            fund.manager = str(one.manager or '')
            fund.manager_date = str(one.manager_date or '')
            fund.scale = utils.n2yi(one.scale)
            fund.mng_rate = utils.f2per(one.mng_rate)
            fund.dps_rate = utils.f2per(one.dps_rate)

            fundlist.append(fund)
        
    except DBAPIError:
        return Response(DBAPIError, content_type='text/plain', status=500)
    
    print("#################  fundlist_view end #######################")

    return {'list': fundlist,'project': 'fundrank'}

@view_config(route_name='fundlist', request_param='addmode', renderer='json')
def fundlist_add(request):
    
    print("#################  fundlist_add start #####################")

    print(request)

    result = get_fund(request.params["fundid"])

    try:
        fund = Fund()

        fund.code = result['code']
        fund.name = result['name']
        fund.type = utils.get_type_key(result['type'])
        fund.style = utils.get_style_key(result['style'])
        fund.start_date = datetime.strptime(result['start_date'],"%Y-%m-%d")
        fund.manager = result['manager']
        fund.manager_date = datetime.strptime(result['manager_date'],"%Y-%m-%d")
        fund.scale = result['scale']
        fund.mng_rate = utils.per2f(result['mng_rate'])
        fund.dps_rate = utils.per2f(result['dps_rate'])

        request.dbsession.add(fund)
        
    except DBAPIError as dbe:
        
        print(dbe)
    
    result['scale'] = utils.n2yi(result['scale'])
    print(result['scale'])

    print("#################  fundlist_add end #######################")

    return result

@view_config(route_name='fundlist', request_param='delmode', renderer='json')
def fundlist_del(request):
    
    print("#################  fundlist_del start #####################")

    print(request)

    try:
        request.dbsession.query(Fund).filter(Fund.code == request.params["fundid"] ).delete()

    except DBAPIError as dbe:
        
        print(dbe)
    
    print("#################  fundlist_del end #######################")

    return None
