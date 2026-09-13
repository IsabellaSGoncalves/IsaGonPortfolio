from collections.abc import Sequence

from nicegui import ui

from src.Components.Card import project_card
from src.Fragments.Vine_Svg import svg_botanical


def build_carousel(projects: Sequence[dict]) -> None:
    state = {"active": 0}

    def go_prev() -> None:
        state["active"] = (state["active"] - 1) % len(projects)
        carousel_card.refresh()
        carousel_dots.refresh()

    def go_next() -> None:
        state["active"] = (state["active"] + 1) % len(projects)
        carousel_card.refresh()
        carousel_dots.refresh()

    def go_to(index: int) -> None:
        state["active"] = index
        carousel_card.refresh()
        carousel_dots.refresh()

    @ui.refreshable
    def carousel_card() -> None:
        with ui.element("div").classes("an-carousel-frame"):
            ui.html(svg_botanical()).classes("an-botanical")
            project_card(
                projects[state["active"]],
                state["active"],
                len(projects),
                go_prev,
                go_next,
            )

    @ui.refreshable
    def carousel_dots() -> None:
        with ui.element("div").classes("an-dots"):
            for index in range(len(projects)):
                active = index == state["active"]
                scale = "1.3" if active else "1"
                ui.button("✦", on_click=lambda index=index: go_to(index)).props(
                    "flat"
                ).classes(f'an-dot{" active" if active else ""}').style(
                    f"transform:scale({scale})"
                )

    carousel_card()
    carousel_dots()
