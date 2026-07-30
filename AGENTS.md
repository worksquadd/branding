# Prototype Instructions

This is a deliberately minimal static file listing. Do not add a framework, package manager, build tooling, deployment worker, or generated build directory unless the user explicitly asks for one.

Keep downloadable branding files in `assets/`. The only runtime helper is `serve_assets.py`, which serves that folder directly.

The preferred presentation is a bare directory listing for `assets/`, matching a classic server index: browser-default serif heading, monospace file rows, and only the heading centered.

The production deployment is a Docker container published only on `127.0.0.1:6700` and routed by the project `nginx.conf` fragment at `/branding/`.
