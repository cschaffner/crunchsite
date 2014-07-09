from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from team.menu import TeamMenu

class Teamhook(CMSApp):
    name = "Teamhook"
    urls = ["team.urls"]
    app_name = "team"
    menus = [TeamMenu]

# class Historyhook(CMSApp):
#     name = "Historyhook"
#     urls = ["team.history_urls"]
#     app_name = "history"
#
# class Pickuphook(CMSApp):
#     name = "Pickuphook"
#     urls = ["team.pickup_urls"]
#     app_name = "pickup"
#
apphook_pool.register(Teamhook)
