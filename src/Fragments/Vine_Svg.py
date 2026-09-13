import base64
from pathlib import Path


def image_data_uri(filename: str) -> str:
    image_path = Path(__file__).resolve().parents[2] / "Images" / filename
    image_data = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{image_data}"


def svg_divider() -> str:
    image_path = Path(__file__).resolve().parents[2] / "Images" / "dot_flower.png"
    image_data = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return (
        '<div style="width:100%;display:flex;align-items:center;gap:1rem">'
        '<span style="height:1px;flex:1;background:rgba(252,232,211,0.5)"></span>'
        f'<img src="data:image/png;base64,{image_data}" alt="" '
        'style="width:2rem;height:2rem;object-fit:contain;display:block;flex:none">'
        '<span style="height:1px;flex:1;background:rgba(252,232,211,0.5)"></span>'
        "</div>"
    )


def svg_corner() -> str:
    return """
    <svg viewBox="0 0 80 80" fill="none" style="width:100%;height:100%">
      <path d="M5 5 L5 40 Q5 75 40 75 L75 75" stroke="#FCE8D3" stroke-width="1" opacity="0.6" stroke-linecap="round"/>
      <path d="M5 5 L30 5 Q50 5 50 25" stroke="#FCE8D3" stroke-width="0.8" opacity="0.4" stroke-linecap="round"/>
      <circle cx="5" cy="5" r="3" fill="#FCE8D3" opacity="0.7"/>
      <ellipse cx="22" cy="18" rx="7" ry="4" transform="rotate(-40 22 18)" fill="#57434F" opacity="0.5"/>
      <ellipse cx="14" cy="45" rx="6" ry="3.5" transform="rotate(10 14 45)" fill="#57434F" opacity="0.45"/>
    </svg>"""


def svg_botanical() -> str:
    image_path = Path(__file__).resolve().parents[2] / "Images" / "carousel_frame.png"
    image_data = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return (
        f'<img src="data:image/png;base64,{image_data}" '
        'alt="" style="width:100%;height:100%;object-fit:contain;object-position:left center;display:block">'
    )


def svg_footer_ornament() -> str:
    image_path = Path(__file__).resolve().parents[2] / "Images" / "dot_flower.png"
    image_data = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return (
        f'<img src="data:image/png;base64,{image_data}" alt="" '
        'style="width:2.5rem;height:2.5rem;object-fit:contain;display:block">'
    )
