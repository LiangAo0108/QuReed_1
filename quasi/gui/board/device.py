"""
This file implements gui functionality for the
device component
"""
import flet as ft

from .ports import Ports
from .chart import Chart
from .base_device_component import BaseDeviceComponent

class Device(BaseDeviceComponent):
    """
    Device class, handles the device gui visualiztaion and
    control
    """
    def __init__(self, *args, **kwargs):

        # Simulation Connection Components
        self.device_instance = kwargs["device_instance"]
        self.sim_gui_coordinator = DeviceSimGuiCoordinator(self)
        self.device_instance.set_coordinator(
            self.sim_gui_coordinator
        )

        print(kwargs["top"], kwargs["left"])

        # Gui Components
        width = 50
        self.ports_out = None
        self.ports_in = None
        self.page = kwargs["page"]

        self._compute_ports()
        self._ports_width = 10
        self._body_controls = []
        if len(self.ports_in.ports) > 0:
            width += 10
        if len(self.ports_out.ports) > 0:
            width += 10

        super().__init__(
            height=50,
            width=width,
            *args,
            **kwargs)

        self.image = ft.Image(
            src=self.device_instance.gui_icon,
            width=self.content_width - 2 * self._ports_width,
            height=self.content_height - self.header_height
        )

        if len(self.ports_in.ports) > 0:
            self._body_controls.append(self.ports_in)
        self._body_controls.append(self.image)
        if len(self.ports_out.ports) > 0:
            self._body_controls.append(self.ports_out)





        self.set_contents(
            ft.Container(
                top=0,
                left=0,
                right=0,
                bottom=0,
                bgcolor="#3f3e42",
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    spacing=0,
                    controls=self._body_controls
                    )
            )
        )

        self.has_chart = False
        if "chart" in self.device_instance.gui_tags:
            self.has_chart = True



    def _compute_ports(self) -> None:
        """
        Create the port component
        """
        self.ports_in = Ports(
            device=self,
            page=self.page,
            device_cls=self.device_instance,
            direction="input")
        self.ports_out = Ports(
            device=self,
            page=self.page,
            device_cls=self.device_instance,
            direction="output")


    def display_chart(self,chart):
        self.board.content.controls.append(
            Chart(
                chart=chart,
                page=self.page,
                top=self.top,
                left=self.left,
                board=self.board))
        self.board.content.update()
        self.page.update()

class DeviceSimGuiCoordinator():
    """
    Manages the coordination between the
    simulated device and the display device
    """

    def __init__(self, gui_device: Device):
        self.device = gui_device
        self.has_chart = False
        self.chart = None
    
    def start_processing(self):
        self.device.start_processing()

    def processing_finished(self):
        self.device.stop_processing()
        if self.device.has_chart and self.has_chart:
            self.device.display_chart(self.chart)


    def set_chart(self, chart):
        self.has_chart = True
        self.chart = chart
