# Handoff

Недавняя работа: проект упрощён до простой файловой витрины `assets/` без React, Vite, сборки и зависимостей. Локальный сервер показывает папку сразу в стиле directory listing; постоянный центрированный заголовок — `Worksquad Branding`. Добавлены Dockerfile, docker-compose.yml и nginx.conf для маршрута `/branding/` с localhost-портом 6700.

Последний запрос пользователя: создать публичный `worksquadd/branding` и настроить CI/CD на сервер `worksquad` через организационные SSH-секреты. Репозиторий создан и опубликован: https://github.com/worksquadd/branding.

Дальше: материалы складывать в `assets/`; `serve_assets.py` покажет их автоматически. Правила скрытия находятся в `assets/.ignore` (сейчас `.*`, `.` и `..`). В listing отображаются только названия; файлы скачиваются по клику, папки открываются. GitHub CLI авторизован, но аккаунт не имеет прав на просмотр имён org Actions secrets или variables; нужны их точные имена для workflow.
