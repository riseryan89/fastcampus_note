from django.http import JsonResponse


def test_api(reqeust):
    return JsonResponse(status=200, data=dict(result="ok"))