from plugin import InvenTreePlugin
from plugin.mixins import EventMixin

from build.models import Build
from order.models import SalesOrderAllocation, SalesOrderLineItem, SalesOrderShipment
from stock.models import StockItem

class AutoAllocateBuildToSales(EventMixin, InvenTreePlugin):
    NAME = "Auto allocate build to sales order"
    SLUG = "inventree_autoallocate_build_to_sales"
    TITLE = "Auto Allocate Build-Sales"
    DESCRIPTION = "Auto allocate build order to sales order"
    VERSION = "0.0.1"

    def wants_process_event(self, event):
        """Here you can decide if this event should be send to `process_event` or not."""
        return event == "build.completed"

    def process_event(self, event, *args, **kwargs):
        build = Build.objects.get(pk=kwargs['id'])
        if build.sales_order is None:
            return

        shipment = SalesOrderShipment.objects.get(order=build.sales_order)
        if shipment is None:
            return

        items = StockItem.objects.filter(
            build=build,
        )
        part = items[0].part

        sales_lines = SalesOrderLineItem.objects.get(
            order=build.sales_order,
            part=part.pk
        )

        for item in items:
            SalesOrderAllocation.objects.create(
                line=sales_lines,
                item=item,
                quantity=1,
                shipment=shipment
            )
