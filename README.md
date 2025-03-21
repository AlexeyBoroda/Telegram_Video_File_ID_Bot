# Telegram Video File ID Bot

Этот Telegram-бот предназначен для получения идентификатора файла (file_id) отправленного видео. Бот обрабатывает видео, отправленные как отдельные видеофайлы и как документы (при условии, что MIME-тип документа соответствует видео).

## Функциональность

- **Обработка видео, отправленных как видео:**  
  Бот извлекает `file_id` из объекта `video` и отправляет его пользователю.

- **Обработка видео, отправленных как документ:**  
  Если документ имеет MIME-тип, начинающийся с `video/`, бот извлекает `file_id` из объекта `document` и отправляет его.

- **Отладка:**  
  Универсальный обработчик регистрирует все входящие сообщения и выводит их тип в лог для диагностики.

## Используемые технологии

- **Python 3.7+**
- **aiogram 3.x** – для работы с Telegram Bot API
- **python-dotenv** – для загрузки переменных окружения из файла `.env`
- **asyncio** – для асинхронного выполнения

## Установка

1. **Клонируйте репозиторий или скачайте файлы проекта.**

2. **Установите зависимости:**  
   Выполните команду:
   ```bash
   pip install -r requirements.txt
   ```

3. **Настройте переменные окружения:**

   - Создайте файл `.env` в корне проекта.
   - Добавьте в него следующую строку, заменив `Ваш_Telegram_токен` на реальный токен:
     ```
     TELEGRAM_TOKEN=Ваш_Telegram_токен
     ```

4. **Защитите секретные данные от публикации:**  
   Убедитесь, что файл `.env` добавлен в `.gitignore`, чтобы он не попал в публичный репозиторий.

## Запуск

Запустите скрипт командой:
```bash
python get_video_file_id.py
```

После запуска в терминале появится сообщение о том, что бот запущен и ожидает входящих сообщений. Отправьте видео боту через Telegram – он пришлёт вам `file_id`.

## Логирование

Логи выводятся в консоль с уровнем `INFO`. Они содержат информацию о полученных сообщениях и возможных ошибках, что помогает в отладке работы бота.

## Примечания

- Если бот используется на сервере, убедитесь, что не запущено несколько экземпляров, иначе может возникнуть ошибка конфликта обновлений.
- При форматировании ответа используется HTML-разметка для корректного отображения `file_id`.
- **Важно:** Не публикуйте файл `.env` с секретными данными в публичных репозиториях!

## Контрибьюция

Если у вас есть предложения или исправления, пожалуйста, создайте pull request или откройте issue.

## Лицензия

Этот проект распространяется под лицензией MIT.
```

## Автор
https://github.com/AlexeyBoroda
```
