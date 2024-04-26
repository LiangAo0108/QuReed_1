"""
QuaSi Gui program.

This file contains the initialization code for the QuaSi Quantum Simulator.
"""
import logging

import flet as ft
import os

from quasi.gui.panels.main_panel import MainPanel
from quasi.gui.panels.side_panel import SidePanel
from quasi.gui.menus.menu_bar import MenuBar

#  logging.basicConfig(level=logging.DEBUG)



def main(page: ft.Page):
    """Initialize the QuaSi GUI Program."""
    page.padding = 0
    page.window_height = 800
    page.window_width = 900
    page.window_frameless = True

    menu_bar = MenuBar(page)
    side_panel = SidePanel(offset_top=menu_bar.height)
    main_panel = MainPanel(page)

    container = ft.Container(
        expand=True,
        content=ft.Stack(
              [
                  main_panel,
                  side_panel,
                  menu_bar,
              ]
        )
    )

    page.add(container)

def start():
    gui_path = os.path.abspath(__file__)
    gui_dir = os.path.dirname(gui_path)
    assets = os.path.join(gui_dir, "assets")
    ft.app(target=main, assets_dir=assets)

if __name__ == "__main__":
    start()
