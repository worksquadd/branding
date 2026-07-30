# Worksquad Branding

Прямая файловая витрина бренд-материалов Worksquad, доступная по `/branding/`.

Для добавления материалов положите файлы в `assets/`. Локальный сервер показывает содержимое этой папки сразу, без стартовой страницы.
Имена, которые не нужно показывать, задаются в `assets/.ignore`; по умолчанию скрываются все файлы и папки, начинающиеся с точки, а также `.` и `..`.
Клик по файлу скачивает его, а клик по папке открывает её содержимое.

## Структура

- `assets/` — брендовые материалы для скачивания.
- `serve_assets.py` — минимальный локальный сервер с directory listing.
- `docker-compose.yml` — контейнер, доступный только на `127.0.0.1:6700`.
- `nginx.conf` — фрагмент маршрута `/branding/` для общего Nginx-сервера.
- `.github/workflows/deploy.yml` — деплой после каждого push в `main`.

## Деплой

Workflow использует repo-level GitHub Actions secrets `WORKSQUAD_HOST`, `WORKSQUAD_USER` и `WORKSQUAD_SSH_PRIVATE_KEY`, соответствующие SSH-конфигурации `worksquad`. Он копирует проект в `/srv/worksquad/deploy_projects/branding`, поднимает контейнер и создаёт только `/etc/nginx/worksquad.d/branding.conf`.
