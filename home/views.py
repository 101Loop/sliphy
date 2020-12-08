from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home/index.html"


home_page_view = HomePageView.as_view()
