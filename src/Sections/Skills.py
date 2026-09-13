from collections.abc import Mapping

from nicegui import ui

from src.Fragments.Vine_Svg import svg_divider, svg_footer_ornament


def _skill_card(group: Mapping) -> None:
    with ui.element("div").classes("an-card an-reveal"):
        ui.label(group["label"]).classes("an-card-title")
        with ui.element("ul").classes("an-list"):
            for item in group["items"]:
                ui.html(f'<li><span class="bullet">◆</span>{item}</li>')


def _info_card(group: Mapping) -> None:
    with ui.element("div").classes("an-card an-reveal"):
        ui.label(group["label"]).classes("an-card-title")
        list_class = "an-list lang" if group["is_lang"] else "an-list"
        with ui.element("ul").classes(list_class):
            for item in group["items"]:
                level_html = (
                    f'<span class="an-lang-level">{item["level"]}</span>'
                    if group["is_lang"]
                    else ""
                )
                ui.html(
                    f'<li><span style="display:flex;align-items:center;gap:0.5rem">'
                    f'<span class="bullet">◆</span>{item["name"]}</span>{level_html}</li>'
                )


def _experience_card(experience: list[Mapping]) -> None:
    with ui.element("div").classes("an-exp-card an-reveal"):
        ui.label("Experience").classes("an-card-title")
        with ui.element("div").classes("an-exp-list"):
            for job in experience:
                with ui.element("div").classes("an-exp-item"):
                    ui.html('<div class="an-exp-dot"></div>')
                    ui.label(job["period"]).classes("an-exp-period")
                    ui.label(job["role"]).classes("an-exp-role")
                    ui.label(job["company"]).classes("an-exp-company")
                    ui.label(job["desc"]).classes("an-exp-desc")


def build_skills_section(data: Mapping) -> None:
    skills = {group["label"]: group for group in data["skills"]}
    info = {group["label"]: group for group in data["right_column"]}

    with ui.element("section").classes(
        "an-section an-skills-section border-top an-reveal"
    ):
        with ui.element("div").classes("an-max-5xl"):
            with ui.element("div").classes("an-skills-title-wrap"):
                ui.label("Expertise").classes("an-carousel-eyebrow")
                ui.label("Skills & Experience").classes("an-carousel-title")
                ui.html(svg_divider()).classes("an-divider").style("margin-top:1rem")

            with ui.element("div").classes("an-skills-grid"):
                with ui.element("div").classes("an-col"):
                    _skill_card(skills["Frontend"])
                    _skill_card(skills["Backend"])

                with ui.element("div").classes("an-col"):
                    _skill_card(skills["Cloud & DevOps"])
                    _info_card(info["Languages"])
                    _info_card(info["Technologies"])

                with ui.element("div").classes("an-col"):
                    _experience_card(data["experience"])
                    _info_card(info["Education"])

            with ui.element("div").classes("an-footer-ornament"):
                ui.html(svg_footer_ornament())
            ui.label("ISABELLA GONÇALVES · MMXXIV").classes("an-footer-sign").style(
                "text-align:center;width:100%"
            )
