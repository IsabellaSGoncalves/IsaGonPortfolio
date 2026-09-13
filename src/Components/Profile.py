from nicegui import ui

from src.Data.Socials import SOCIAL_LINKS
from src.Fragments.Vine_Svg import image_data_uri, svg_corner, svg_divider


def build_profile() -> None:
    with ui.element("section").classes("an-section an-hero border-top-none an-reveal"):
        ui.html(
            f'<div class="an-hero-reveal-layer" '
            f'style="background-image:url({image_data_uri("beach.gif")})"></div>'
        )
        ui.html(svg_corner()).classes("an-corner tl")
        ui.html(svg_corner()).classes("an-corner tr")

        with ui.element("div").classes("an-max-lg").style(
            "position:relative;z-index:10;display:flex;flex-direction:column;align-items:center;"
        ):
            with ui.element("div").classes("an-avatar-wrap"):
                with ui.element("div").classes("an-avatar"):
                    ui.image("Images/profile.jpeg")
                for corner in ("tl", "tr", "bl", "br"):
                    ui.element("div").classes(f"an-avatar-corner {corner}")

            ui.label("Full-Stack Developer").classes("an-eyebrow")
            ui.label("Isabella").classes("an-name")
            ui.label("Gonçalves").classes("an-name last")
            ui.html(svg_divider()).classes("an-divider")
            ui.label(
                "Desenvolvedora de software apaixonada por transformar ideias em experiências digitais"
                " funcionais, intuitivas e visualmente cuidadas."
            ).classes("an-bio")

            with ui.element("div").classes("an-social-row"):
                for link in SOCIAL_LINKS:
                    ui.html(
                        f'<a class="an-social" href="{link["href"]}" target="_blank" '
                        f'rel="noreferrer" title="{link["label"]}">'
                        f'<svg viewBox="0 0 24 24" fill="currentColor">{link["svg"]}</svg></a>'
                    )

        with ui.element("div").classes("an-ticker-bar"):
            items = "".join(
                '<span class="item">Software Designer (também) <span class="dot">✦</span></span>'
                for _ in range(12)
            )
            ui.html(f'<div class="an-ticker-track">{items}{items}</div>')
