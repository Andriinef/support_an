from customusers.constants import Role
from tickets.models import Ticket


class PermissionsMixin:
    def _get_tickets(self):
        # The OR SQL processing
        # from django.db.models import Q
        # tickets = Ticket.objects.filter(
        #     Q(manager=self.request.user) | Q(customer=self.request.user)
        # )

        role: Role = self.request.user.role

        if role == Role.ADMIN:
            return Ticket.objects.all()
        elif role == Role.MANAGER:
            return Ticket.objects.filter(manager=self.request.user)

        return Ticket.objects.filter(customer=self.request.user)
