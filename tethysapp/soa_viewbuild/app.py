from tethys_sdk.base import TethysAppBase, url_map_maker


class SoaViewbuild(TethysAppBase):
    """
    Tethys app class for Soa Viewbuild.
    """

    name = 'Soa Viewbuild'
    index = 'soa_viewbuild:home'
    icon = 'soa_viewbuild/images/icon.gif'
    package = 'soa_viewbuild'
    root_url = 'soa-viewbuild'
    color = '#27ae60'
    description = '"This is an app to simulate the function viewshed in the city of New York"'
    tags = '"Viewshed", "CE 514" , "BYU", "Corona Virus"'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='soa-viewbuild',
                controller='soa_viewbuild.controllers.home'
            ),
        )

        return url_maps