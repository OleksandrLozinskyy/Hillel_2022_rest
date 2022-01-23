from django.http import JsonResponse


def posts(request):
    return JsonResponse(
        {
            "result": [
                {"title": "Title for test post1"},
                {"title": "Title for test post2"},
                {"title": "Title for test post3"},
            ]
        }
    )
