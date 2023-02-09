from fastcampus_note.settings import DEBUG


def renderer(request):
    path = ""
    if not DEBUG:
        path = "/production"
    return {"path": path}
