"""Bygg AI-kursens A4-formelblad med pdfLaTeX."""

import os
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory

source = Path(__file__).resolve().parents[1] / "formelblad" / "ai.tex"
with TemporaryDirectory() as output:
    run(
        [
            "pdflatex",
            "-halt-on-error",
            "-interaction=batchmode",
            "-output-directory",
            output,
            source.name,
        ],
        cwd=source.parent,
        check=True,
        env={**os.environ, "SOURCE_DATE_EPOCH": "1795737600", "FORCE_SOURCE_DATE": "1"},
    )
    source.with_suffix(".pdf").write_bytes((Path(output) / "ai.pdf").read_bytes())
