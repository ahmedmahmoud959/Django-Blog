from django import template
from django.template.loader import get_template
from blog.models import Post

t = get_template('parts/side_bar.html')
register = template.Library()

@register.inclusion_tag(t)
def side_bar():
    all_post = Post.objects.all()
    views  = all_post.order_by('views')[0:6]
    context = {
        'side_views' : views
    }
    return context

