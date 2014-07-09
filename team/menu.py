from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu
from team.models import Team


class TeamMenu(CMSAttachMenu):

    name = 'Teams'

    def get_nodes(self, request):
        nodes = []
        for team in Team.objects.all().order_by("name"):
            node = NavigationNode(
                team.name,
                team.get_absolute_url(),
                team.pk,
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(TeamMenu)
