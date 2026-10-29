# Image Processing laboratories

Optional, ungraded laboratory material for lectures 3–7. Each lab can be used
on its own or alongside the others in one shared project. Complete solutions
are provided under `solutions/`.

## Setup and running a script

1. Install [uv](https://docs.astral.sh/uv/) and clone the repository or extract a lab ZIP.
2. Open the folder containing `pyproject.toml` in Visual Studio Code.
3. In that folder, run:

   ```text
   uv sync
   ```

4. Accept the workspace extension recommendations and select the root `.venv`
   as the Python interpreter if VS Code does not select it automatically.
5. Open the Python file specified by the lab README and use **Run Python
   File** or **Debug Python File** in the top-right menu.

The setup installs `labs` as an editable local package. Scripts can import the
supplied helpers when launched directly as files, without configuring
`PYTHONPATH`. OpenCV windows require a graphical desktop; camera exercises
also require a webcam. Close each exercise using its documented keys.


## Labs

This authoring repository includes all five labs. An individual ZIP includes
only its selected lab; use the matching README below when that folder is present.

| Folder | Lecture and topic |
| --- | --- |
| `labs/lab03/` | 3 — OpenCV acquisition |
| `labs/lab04/` | 4 — Edges, thresholding, morphology, and contours |
| `labs/lab05/` | 5 — Components, shapes, template matching, and color |
| `labs/lab06/` | 6 — Hough voting and RANSAC |
| `labs/lab07/` | 7 — Camera calibration and homographies |

Each lab's `README.md` explains its exercises and self-checks.

## Layout

```text
image-processing-labs/
├── pyproject.toml         # Shared dependencies and editable package
├── uv.lock               # Reproducible dependency versions
├── .python-version
├── .vscode/              # Run/debug and interpreter settings
├── labs/
    ├── __init__.py
    ├── common/           # Fully supplied helpers; included in every lab ZIP
    ├── lab03/
    │   ├── __init__.py
    │   ├── README.md
    │   ├── exercises/    # Runnable ex01 and draft ex02-ex03 starters
    │   ├── outputs/      # Created by your captures and processing
    │   └── solutions/    # All solutions, also for ex04-ex05
    |── lab04/
    |── lab05/
    |── lab06/
    └── lab07/
```

## Using one lab or combining labs

Every standalone lab ZIP includes the root setup files, VS Code configuration,
`labs/__init__.py`, `labs/common/`, and one complete lab. Extract it and follow
the setup above; earlier labs are not required.

Student ZIPs include `.vscode/extensions.json` and `.vscode/launch.json`.
The maintainer `.vscode/settings.json` stays in the authoring repository.

To add another lab to an existing project, copy only its `labNN/` folder into
the existing `labs/` directory. Keep your existing lab folders and work. The
course ZIPs share the same environment configuration and supplied helpers, so
there is no need for one environment per lab. If a release explicitly updates
shared files or dependencies, follow its update instructions and rerun
`uv sync`.

Nothing has to be submitted and won't be graded.
