from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class Memberhook(CMSApp):
    name = "Memberhook"
    urls = ["member.urls"]
    app_name = "member"
    # menus = [TeamMenu]

apphook_pool.register(Memberhook)
