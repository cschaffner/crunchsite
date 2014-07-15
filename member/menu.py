from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu


class MemberMenu(CMSAttachMenu):

    name = 'Members'

    def get_nodes(self, request):
        nodes = []
        login_node = NavigationNode(
            'Login',
            '/accounts/login',
            0,
        )
        logout_node = NavigationNode(
            'Logout',
            '/accounts/logout',
            1,
        )
        return [login_node, logout_node]

menu_pool.register_menu(MemberMenu)
