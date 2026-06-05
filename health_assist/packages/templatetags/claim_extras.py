from django import template

register = template.Library()


@register.filter
def get_claim(uploaded_map, doc_id):
    return uploaded_map.get(doc_id)
