from django.core.urlresolvers import reverse

from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu


class MemberMenu(CMSAttachMenu):

    name = 'Members'

    def get_nodes(self, request):
        nodes = []
        if request.user.is_active:
            if request.user.first_name or request.user.last_name:
                name = u'{0} {1}'.format(request.user.first_name, request.user.last_name)
            else:
                name = request.user.username
            # if request.user.profile.account_verified:
            #     name += u'(verified)'
            # else:
            #     name += u'(unverified)'
            me_node = NavigationNode(
                name,
                reverse('member:my_detail'),
                2,
            )
            nodes.append(me_node)
            logout_node = NavigationNode(
                'Logout',
                '/accounts/logout',
                1,
            )
            nodes.append(logout_node)
        else:
            login_node = NavigationNode(
                'Login',
                '/accounts/login',
                0,
            )
            nodes.append(login_node)
        return nodes

menu_pool.register_menu(MemberMenu)
