from collections.abc import Callable
from html import escape
import re

from nicegui import ui


def _project_title(title: str) -> str:
    match = re.fullmatch(r"\s*(.*?)\s*\[(https?://[^\]]+)\]\s*", title)
    if not match:
        return escape(title)

    name, url = match.groups()
    return (
        f'<a href="{escape(url, quote=True)}" target="_blank" '
        f'rel="noreferrer">{escape(name)}</a>'
    )


def project_card(
    project: dict,
    active_index: int,
    total_projects: int,
    go_prev: Callable[[], None],
    go_next: Callable[[], None],
    frame_svg: str | None = None,
) -> None:
    with ui.element("div").classes("an-carousel-card an-reveal"):
        with ui.element("div").classes("an-carousel-grid"):
            with ui.element("div").classes("an-carousel-img-wrap"):
                ui.image(project["img"])
                ui.html('<div class="an-carousel-fade-r"></div>')
                ui.html('<div class="an-carousel-fade-b"></div>')

            with ui.element("div").classes("an-carousel-text"):
                with ui.element("div").classes("an-tag-row"):
                    ui.label(project["tag"]).classes("an-tag")
                    ui.label(project["year"]).classes("an-year")

                ui.html(_project_title(project["title"])).classes("an-proj-title")
                ui.label(project["desc"]).classes("an-proj-desc")

                with ui.element("div").classes("an-tech-row"):
                    for technology in project["tech"]:
                        ui.label(technology).classes("an-tech-chip")

                with ui.element("div").classes("an-carousel-nav"):
                    ui.label(f"{active_index + 1} / {total_projects}").classes(
                        "an-nav-count"
                    )
                    with ui.element("div").classes("an-nav-btns"):
                        ui.button("‹", on_click=go_prev).props("flat").classes(
                            "an-nav-btn"
                        )
                        ui.button("›", on_click=go_next).props("flat").classes(
                            "an-nav-btn"
                        )
