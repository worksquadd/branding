"""Serve the `assets` directory as a plain directory listing.

Usage example: `python3 serve_assets.py`.
"""

from fnmatch import fnmatch
from html import escape
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import io
import os
from pathlib import Path
from urllib.parse import quote


class AssetsHandler(SimpleHTTPRequestHandler):
    """Render files in `assets` as an Apache-style directory listing.

    Usage example: `ThreadingHTTPServer(("127.0.0.1", 4173), AssetsHandler)`.
    """

    def list_directory(self, path):
        """Return an HTML directory listing for a filesystem path.

        Args:
            path: Absolute directory path requested by the browser.
        Returns:
            A byte stream containing the directory-listing document.
        """
        directory = Path(path)
        rows = []
        ignored = self.read_ignore_patterns()

        for entry in sorted(directory.iterdir(), key=lambda item: (not item.is_dir(), item.name.lower())):
            if any(fnmatch(entry.name, pattern) for pattern in ignored):
                continue

            label = f"{entry.name}/" if entry.is_dir() else entry.name
            href = quote(entry.name) + ("/" if entry.is_dir() else "")
            download = "" if entry.is_dir() else f' download="{escape(entry.name)}"'
            rows.append(f'<a href="{href}"{download}>{escape(label)}</a>')

        listing = "\n".join(rows)
        document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Worksquad Branding</title>
  <style>h1 {{ text-align: center; }}</style>
</head>
<body>
  <h1>Worksquad Branding</h1>
  <hr>
  <pre>{listing}</pre>
  <hr>
</body>
</html>
"""
        encoded = document.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        return io.BytesIO(encoded)

    def read_ignore_patterns(self):
        """Read non-empty ignore patterns from the root assets ignore file.

        Args:
            None.
        Returns:
            A list of filename patterns excluded from the listing.
        """
        ignore_file = Path(self.directory) / ".ignore"
        if not ignore_file.is_file():
            return []

        return [
            line.strip()
            for line in ignore_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]


def run_server():
    """Start the local assets directory server on port 4173.

    Returns:
        None after the server is stopped.
    """
    assets = Path(__file__).parent / "assets"
    handler = lambda *args, **kwargs: AssetsHandler(*args, directory=assets, **kwargs)
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "4173"))
    server = ThreadingHTTPServer((host, port), handler)
    print(f"Serving assets at http://{host}:{port}/")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
