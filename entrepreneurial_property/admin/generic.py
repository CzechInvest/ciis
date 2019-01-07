from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
import nested_admin


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(
                u' <a href="%s" target="_blank"><img src="{}" alt="{}" '
                u'width="150" height="150"  style="object-fit: cover;"/>'
                u'</a> {} '.format(image_url, image_url, file_name, _('')))
            output.append(
                super(
                    AdminFileWidget,
                    self).render(
                    name,
                    value,
                    attrs))
        return mark_safe(u''.join(output))
