from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from . import models
from user.models import User
import json
import ast

# Create your views here.

@csrf_exempt
def add_app(request):
    request.POST = json.loads(request.body.decode())
    app_type = request.POST.get('app_type')
    catalog_id = request.POST.get('catalog_id')
    mob_url = request.POST.get('mob_url')
    name = request.POST.get('name')
    portal_id = request.POST.get('portal_id')
    run_type = request.POST.get('run_type')
    summary = request.POST.get('summary')
    author_id = request.POST.get('open_uid')

    instance_portalapp = models.Portal_app.objects.get(portal_id=portal_id)
    instance_user = User.objects.get(open_uid=author_id)
    set_mob_log = 'http://hillinsight-image.oss-cn-beijing.aliyuncs.com/open/light_app_logo/61498a62ccc502006d9911de51523502.png'

    models.Light_app.objects.create(author_id=instance_user,app_type=app_type,catalog_id=catalog_id,mob_logo=set_mob_log,mob_url=mob_url,
                              name=name,portal_id=instance_portalapp,run_type=run_type,summary=summary)

    result = {
        'error_code':0,
        'message':'Success',
        'result':790
    }
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_my_apps(request):
    open_uid = request.GET.get('open_uid')
    portal_id = request.GET.get('portal_id')

    user_instance = User.objects.get(open_uid = open_uid)
    portal_instance = models.Portal_app.objects.get(portal_id=portal_id)

    lightapps = portal_instance.portalapp_lightapp.all()

    result = []
    for item in lightapps:
         #判断用户是不是轻应用的创建者
         if item.author_id_id == user_instance.id:
             result.append({'name': item.name, 'mob_logo': item.mob_logo, 'app_id': item.id, 'app_type': item.app_type})
             continue

         #判断用户是不是轻应用的成员
         cc = item.memberlist.filter(open_uid = open_uid)
         if cc:
              result.append({'name':item.name,'mob_logo':item.mob_logo,'app_id':item.id,'app_type':item.app_type})

    response = {
        'error_code': 0,
        'message': 'Success',
        'result': result
    }
    return HttpResponse(json.dumps(response), content_type="application/json")

