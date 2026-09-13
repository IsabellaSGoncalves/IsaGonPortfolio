from collections.abc import Sequence

from nicegui import ui

from src.Components.Carousel import build_carousel


def build_carousel_section(projects: Sequence[dict]) -> None:
    with ui.element("section").classes("an-section border-top an-reveal"):
        with ui.element("div").classes("an-max-6xl"):
            with ui.element("div").classes("an-carousel-header"):
                with ui.column().style("gap:0"):
                    ui.label("Selected Work").classes("an-carousel-eyebrow")
                    ui.label("Projects").classes("an-carousel-title")

            build_carousel(projects)
