from django import template

register = template.Library()

@register.filter(name='truncate_words')
def truncate_words(value, count=5):
    words = str(value).split()

    if len(words) <= count:
        return value

    return ' '.join(words[:count]) + '...'