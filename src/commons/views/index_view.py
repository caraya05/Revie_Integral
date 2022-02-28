from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutUsView(TemplateView):
    template_name = "about-us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MapSiteView(TemplateView):
    template_name = "map_site.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
