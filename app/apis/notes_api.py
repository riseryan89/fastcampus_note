import json

from django.db import models
from django.db.models import Value, F
from django.http import JsonResponse

from app.apis.serializers import CustomJSONEncoder
from app.models import Category, Note


def get_or_create_categories(request):
    if request.method == "GET":
        categories = Category.objects.filter(user=request.user).all().values("id", "name")
        return JsonResponse(
            status=200,
            data=list(categories),
            encoder=CustomJSONEncoder,
            json_dumps_params={"ensure_ascii": False},
            safe=False,
        )
    elif request.method == "POST":
        name = json.loads(request.body).get("name")
        if not name:
            return JsonResponse(status=400, data=dict(error="name is required"))
        category, created = Category.objects.get_or_create(user=request.user, name=name)
        if created:
            return JsonResponse(status=201, data=dict(id=category.id, name=category.name))
        else:
            return JsonResponse(status=409, data=dict(error="category already exists"))
    else:
        return JsonResponse(status=405, data=dict(error="method not allowed"))


def get_or_create_notes(request):
    if request.method == "GET":
        category = request.GET.get("category_id")
        base_qs = Note.objects.filter(user=request.user, is_deleted=False)
        if category:
            base_qs = base_qs.filter(category__id=int(category))
        notes = (
            base_qs.all()
            .values("id", "title", "content", "image", "category_id", "created_at", "category__name")
            .order_by("-id")
        )
        return JsonResponse(
            status=200,
            data=list(notes),
            encoder=CustomJSONEncoder,
            json_dumps_params={"ensure_ascii": False},
            safe=False,
        )
    elif request.method == "POST":
        body = json.loads(request.body)
        get_category, _ = Category.objects.get_or_create(user=request.user, name="미설정")
        if not get_category:
            Category.objects.create(user=request.user, name="미설정")
        new_note = Note.objects.create(category=get_category, user=request.user, **body)
        note = Note.objects.filter(id=new_note.id).values(
            "id", "title", "content", "image", "category_id", "created_at", "category__name"
        )
        return JsonResponse(
            status=201, data=note[0], encoder=CustomJSONEncoder, json_dumps_params={"ensure_ascii": False}
        )
    else:
        return JsonResponse(status=405, data=dict(error="method not allowed"))


def update_or_delete_note(request, note_id):
    if request.method == "PUT":
        body = json.loads(request.body)
        Note.objects.filter(id=note_id, user=request.user).update(**body)
        return JsonResponse(status=200, data=dict(result="ok"))
    elif request.method == "DELETE":
        Note.objects.filter(id=note_id, user=request.user).update(is_deleted=True)
        return JsonResponse(status=200, data=dict(result="ok"))
    else:
        return JsonResponse(status=405, data=dict(error="method not allowed"))
