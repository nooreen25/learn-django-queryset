from django.conf.urls import include, url
from django.contrib import admin

# from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    # Examples:
    url(r'^$', RedirectView.as_view(url=reverse_lazy('admin:index'),
        permanent=False)),
    # url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
