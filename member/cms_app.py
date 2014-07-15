from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from menu import MemberMenu

class Memberhook(CMSApp):
    name = "Memberhook"
    urls = ["member.urls"]
    app_name = "member"
    menus = [MemberMenu]

apphook_pool.register(Memberhook)
