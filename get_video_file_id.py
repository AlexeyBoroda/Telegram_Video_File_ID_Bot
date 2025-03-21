import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение токена из переменных окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TELEGRAM_TOKEN:
    raise ValueError("Не найден токен Telegram. Проверьте, что переменная окружения TELEGRAM_TOKEN задана в файле .env.")

# 🔧 Настройка логирования:
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# 📡 Инициализация бота и диспетчера:
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# ========================================================
# Специализированный обработчик для видео, отправленного как "video"
# ========================================================
@dp.message(F.content_type == "video")
async def get_video_file_id_video(message: types.Message):
    """
    Обрабатывает входящие сообщения, в которых видео отправлено как отдельный объект (video).
    Извлекает file_id видео и отправляет его пользователю.
    Используется HTML-разметка для безопасного форматирования ответа.
    """
    logger.info(f"📥 Получено видео (video) от @{message.from_user.username or message.from_user.id}")
    try:
        file_id = message.video.file_id
        await message.reply(f"📎 Ваш file_id:\n<code>{file_id}</code>", parse_mode="HTML")
        logger.info(f"✅ file_id видео: {file_id}")
    except Exception as e:
        logger.error(f"❌ Ошибка в обработчике видео: {e}")
        await message.reply("Произошла ошибка при обработке видео.")

# ========================================================
# Специализированный обработчик для видео, отправленного как документ
# ========================================================
@dp.message(F.content_type == "document")
async def get_video_file_id_document(message: types.Message):
    """
    Обрабатывает входящие сообщения, где видео отправлено как документ.
    Проверяет MIME-тип документа, чтобы удостовериться, что это видео,
    затем извлекает file_id и отправляет его пользователю с HTML-разметкой.
    """
    if message.document.mime_type and message.document.mime_type.startswith("video/"):
        logger.info(f"📥 Получено видео (документ) от @{message.from_user.username or message.from_user.id}")
        try:
            file_id = message.document.file_id
            await message.reply(f"📎 Ваш file_id:\n<code>{file_id}</code>", parse_mode="HTML")
            logger.info(f"✅ file_id видео (документ): {file_id}")
        except Exception as e:
            logger.error(f"❌ Ошибка в обработчике документа: {e}")
            await message.reply("Произошла ошибка при обработке видео-документа.")
    else:
        logger.warning("❗ Получен документ, но MIME-тип не соответствует видео")
        await message.reply("Документ не является видеофайлом.")

# ========================================================
# Отладочный обработчик для всех входящих сообщений
# ========================================================
@dp.message()
async def debug_message(message: types.Message):
    """
    Универсальный обработчик для отладки.
    Регистрирует тип каждого входящего сообщения.
    Этот обработчик регистрируется после специализированных, чтобы не перехватывать их.
    """
    logger.info(f"DEBUG: Получено сообщение. Тип: {message.content_type}")

# ========================================================
# Функция для запуска бота
# ========================================================
async def main():
    """
    Основная асинхронная функция для запуска бота.
    Запускается polling, который постоянно ожидает входящих обновлений.
    """
    logger.info("🚀 Бот запущен. Отправьте видео, чтобы получить его file_id.")
    await dp.start_polling(bot)

# ========================================================
# Точка входа в программу
# ========================================================
if __name__ == "__main__":
    asyncio.run(main())
