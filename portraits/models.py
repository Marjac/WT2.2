from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Portrait(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=100, blank=True, default='')
    title = models.CharField(max_length=1000, blank=True, default='')
    when = models.TextField(max_length=1000, blank=True, default='')
    what = models.TextField(max_length=1000, blank=True, default='')
    credits = models.TextField(max_length=1000, blank=True, default='')
    description = models.TextField(max_length=1000, blank=True, default='')
    class Meta:
        ordering = ('created',)