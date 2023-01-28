from django import template


register = template.Library()


@register.filter()
def word_changer(value):
    value = str(value).lower()
    if value == "python":
        return "Java"
    elif value == "java":
        return "Python"
    return value
