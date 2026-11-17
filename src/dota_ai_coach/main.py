"""Launch the Dota AI Coach desktop prototype.

This first version is a UI shell with clearly labelled sample content.
It does not connect to Dota 2 or make live-match claims.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class DotaAICoachApp(tk.Tk):
    """Main application window."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Dota AI Coach")
        self.geometry("900x620")
        self.minsize(720, 500)
        self.configure(bg="#11131b")

        self._configure_style()
        self._build_ui()

    def _configure_style(self) -> None:
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(
            "TFrame",
            background="#11131b",
        )
        style.configure(
            "Panel.TFrame",
            background="#1b1e2a",
        )
        style.configure(
            "Title.TLabel",
            background="#11131b",
            foreground="#f3f4f8",
            font=("Segoe UI", 22, "bold"),
        )
        style.configure(
            "Subtitle.TLabel",
            background="#11131b",
            foreground="#a5a9ba",
            font=("Segoe UI", 10),
        )
        style.configure(
            "PanelTitle.TLabel",
            background="#1b1e2a",
            foreground="#f3f4f8",
            font=("Segoe UI", 12, "bold"),
        )
        style.configure(
            "PanelText.TLabel",
            background="#1b1e2a",
            foreground="#c7cada",
            font=("Segoe UI", 10),
            wraplength=700,
        )
        style.configure(
            "Status.TLabel",
            background="#252a39",
            foreground="#f0c674",
            padding=(10, 6),
            font=("Segoe UI", 9, "bold"),
        )
        style.configure(
            "Accent.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(12, 8),
        )

    def _build_ui(self) -> None:
        outer = ttk.Frame(self, padding=24)
        outer.pack(fill="both", expand=True)

        header = ttk.Frame(outer)
        header.pack(fill="x", pady=(0, 22))

        ttk.Label(header, text="Dota AI Coach", style="Title.TLabel").pack(
            anchor="w"
        )
        ttk.Label(
            header,
            text="Your personal, player-controlled Dota 2 coaching companion",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(5, 0))

        ttk.Label(
            outer,
            text="PROTOTYPE · NOT CONNECTED TO A LIVE MATCH",
            style="Status.TLabel",
        ).pack(anchor="w", pady=(0, 18))

        overview = ttk.Frame(outer, style="Panel.TFrame", padding=18)
        overview.pack(fill="x", pady=(0, 14))
        ttk.Label(
            overview,
            text="Welcome",
            style="PanelTitle.TLabel",
        ).pack(anchor="w")
        ttk.Label(
            overview,
            text=(
                "This is the first desktop shell. Live game-data integration "
                "and AI recommendations are not implemented yet. We will only "
                "consider documented, permitted data sources."
            ),
            style="PanelText.TLabel",
        ).pack(anchor="w", pady=(8, 0))

        recommendation = ttk.Frame(outer, style="Panel.TFrame", padding=18)
        recommendation.pack(fill="both", expand=True)
        ttk.Label(
            recommendation,
            text="Example coaching card",
            style="PanelTitle.TLabel",
        ).pack(anchor="w")
        ttk.Label(
            recommendation,
            text="SAMPLE — NOT A REAL-TIME GAME ANALYSIS",
            foreground="#e6b86b",
            background="#1b1e2a",
            font=("Segoe UI", 8, "bold"),
        ).pack(anchor="w", pady=(12, 4))
        ttk.Label(
            recommendation,
            text="Check the minimap before moving into an unobserved area.",
            style="PanelText.TLabel",
        ).pack(anchor="w")

        footer = ttk.Frame(outer)
        footer.pack(fill="x", pady=(18, 0))
        ttk.Label(
            footer,
            text="No game input automation · No memory reading · No account credentials",
            style="Subtitle.TLabel",
        ).pack(side="left")


def main() -> None:
    app = DotaAICoachApp()
    app.mainloop()


if __name__ == "__main__":
    main()
