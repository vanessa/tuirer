from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def liked_tuite_heart_icon(context):
    """
    Mostra o ícone correto dependendo se o usuário
    deu like (ou não) no Tuite
    """
    user = context.get('user')
    tuite = context.get('tuite')
    solid_icon = "fas fa-heart"
    empty_icon = "far fa-heart"

    if not user.pk:
        return empty_icon
    if not user.liked_tuites.filter(id__in=[tuite.id]).exists():
        return solid_icon

    return empty_icon