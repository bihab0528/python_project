from django import template

register = template.Library()
@register.filter

def show(dic,key):
    int_key = int(key)
    value = dic[int_key]
    return value
