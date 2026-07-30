# Handoff

Недавняя работа: проект упрощён до простой файловой витрины `assets/` без React, Vite, сборки и зависимостей. Локальный сервер показывает папку сразу в стиле directory listing; постоянный центрированный заголовок — `Worksquad Branding`. Добавлены Dockerfile, docker-compose.yml и nginx.conf для маршрута `/branding/` с localhost-портом 6700. Добавлен GitHub Actions workflow для копирования кода и деплоя на `worksquad`.

Последний запрос пользователя: создать публичный `worksquadd/branding` и настроить CI/CD на сервер `worksquad` через организационные SSH-секреты. Репозиторий создан и опубликован: https://github.com/worksquadd/branding.

Дальше: материалы складывать в `assets/`; `serve_assets.py` покажет их автоматически. Правила скрытия находятся в `assets/.ignore` (сейчас `.*`, `.` и `..`). В listing отображаются только названия; файлы скачиваются по клику, папки открываются. Workflow использует org secret `WS_SERVER_SSH_RIFTY_1_PRIVATE_KEY`, org variable `WS_SERVER_RIFTY_1_HOST` и подключается к серверу как `root`.
