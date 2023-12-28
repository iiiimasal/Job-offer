from django.http import JsonResponse


def getRoutes(request):
    routes=[
        'GET /api',
        'GET/api/companies',
        'GET /api/companies/:id'
    ]
    return JsonResponse(routes, safe=False)