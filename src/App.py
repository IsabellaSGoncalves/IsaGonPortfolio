from nicegui import ui

from src.Components.Profile import build_profile
from src.Components.Styles import load_styles
from src.Data.loader import load_portfolio_data
from src.Sections.Carousel import build_carousel_section
from src.Sections.Skills import build_skills_section


def run() -> None:
    projects, skills_data = load_portfolio_data()
    ui.add_head_html(load_styles(), shared=True)

    @ui.page("/")
    def index() -> None:
        with ui.element("div").classes("an-page"):
            build_profile()
            build_carousel_section(projects)
            build_skills_section(skills_data)

    ui.run(title="Isabella Gonçalves ✦ Portfolio", reload=False)
