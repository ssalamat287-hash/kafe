import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8838436380:AAGCHrR5G3nnkJcJC57vMPF7PmWbrnS1_LE"
ADMIN_PHONE = "+998 90 881 4949"

dp = Dispatcher()


def get_main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 Kafe menyusi", callback_data="cafe_menu")],
        [InlineKeyboardButton(text="📞 Admin menen baylanıs", callback_data="contact_admin")]
    ])


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Assalawma áleykum, {message.from_user.first_name}!\n"
        "Kafeimizge xosh kelibsiz. Tómendegi bólimlerdiń birin tańlań:",
        reply_markup=get_main_menu()
    )


# --- KAFE MENYUSI ---
@dp.callback_query(F.data == "cafe_menu")
async def show_menu(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🍲 Milliy taǵamlar hám Sorbalar", callback_data="menu_dishes")],
        [InlineKeyboardButton(text="🍢 Shashlıklar", callback_data="menu_shashlik")],
        [InlineKeyboardButton(text="🥗 Salatlar", callback_data="menu_salads")],
        [InlineKeyboardButton(text="🥤 Ishimlikler", callback_data="menu_drinks")],
        [InlineKeyboardButton(text="🔙 Artqa", callback_data="back_to_main")]
    ])
    await callback.message.edit_text(
        "📋 **Kafe menyusi:**\n\nKategoriya tańlań:",
        reply_markup=keyboard
    )
    await callback.answer()


@dp.callback_query(F.data == "menu_dishes")
async def menu_dishes(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Menyuǵa qaytıw", callback_data="cafe_menu")]
    ])
    await callback.message.edit_text(
        "🍲 **Milliy taǵamlar hám Sorbalar:**\n\n"
        "• Tashkent palaw (órt.) - 35,000 sum\n"
        "• Tashkent palaw (komplekt) - 43,000 sum\n"
        "• Samarkand palaw (órt.) - 40,000 sum\n"
        "• Samarkand palaw (komplekt) - 48,000 sum\n"
        "• Djiz (0.5 kg / 1 kg) - 110,000 / 220,000 sum\n"
        "• Chayxana palaw (zakaz) - 140,000 / 280,000 sum\n"
        "• Uygur lagman - 30,000 sum\n"
        "• Quwırma lagman - 30,000 sum\n"
        "• Karma - 60,000 sum\n"
        "• Xe - 60,000 sum\n"
        "• Gurtik (zakaz)\n"
        "• Kazan kebab - 60,000 sum\n"
        "• Bayır quwdak (250 gr) - 40,000 sum\n"    
        "• Mantı uygur (5 sht) - 30,000 sum\n"
        "• Balık kotlet - 30,000 sum\n"
        "• Balık quwırdak (kg) - 35,000 - 100,000 sum\n"
        "• Borsh ukrainskiy - 30,000 sum\n"
        "• Uxa - 30,000 sum\n"
        "• Mastava - 30,000 sum",
        reply_markup=keyboard
    )
    await callback.answer()


@dp.callback_query(F.data == "menu_shashlik")
async def menu_shashlik(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Menyuǵa qaytıw", callback_data="cafe_menu")]
    ])
    await callback.message.edit_text(
        "🍢 **Shashlıklar:**\n\n"
        "• Shashlık farsh - 12,000 sum\n"
        "• Shashlık utka - 10,000 sum\n"
        "• Balık shashlık - 20,000 sum\n"
        "• Shashlık kuskovoy - 22,000 sum\n"
        "• Shashlık okorochka - 24,000 sum\n"
        "• Shashlık baranina - 24,000 sum\n"
        "• Shashlık Napoleon - 24,000 sum\n"
        "• Shashlık assorti (2 personı) - 80,000 sum\n"
        "• Shashlık assorti (3 personı) - 170,000 sum\n"
        "• Shashlık assorti (4 personı) - 250,000 sum",
        reply_markup=keyboard
    )
    await callback.answer()


@dp.callback_query(F.data == "menu_salads")
async def menu_salads(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Menyuǵa qaytıw", callback_data="cafe_menu")]
    ])
    await callback.message.edit_text(
        "🥗 **Salatlar:**\n\n"
        "• Suzbe - 8,000 sum\n"
        "• Chimchi - 10,000 sum\n"
        "• Svejiy salat - 12,000 sum\n"
        "• Okroshka - 10,000 sum\n"
        "• Achik-chukuk - 14,000 sum\n"
        "• Solenya assorti - 12,000 sum\n"
        "• Chirokchi salat - 20,000 sum\n"
        "• Balık xe - 28,000 sum\n"
        "• Jareniy trebuxa - 30,000 sum\n"
        "• Kitayskiy salat - 30,000 sum\n"
        "• Cezar salat - 35,000 sum\n"
        "• Xrustyaşie baklajanı - 40,000 sum\n"
        "• Ovoşnoy assorti - 35,000 sum\n"
        "• Fruktoviy assorti - 90,000 sum\n"
        "• Myasnoy assorti - 120,000 sum",
        reply_markup=keyboard
    )
    await callback.answer()


@dp.callback_query(F.data == "menu_drinks")
async def menu_drinks(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Menyuǵa qaytıw", callback_data="cafe_menu")]
    ])
    await callback.message.edit_text(
        "🥤 **Ishimlikler:**\n\n"
        "• Nan 0.5 / Nan - 3,000 / 6,000 sum\n"
        "• Chay - 5,000 sum\n"
        "• Chay s limonom - 10,000 sum\n"
        "• Chay s molokom (1 L) - 15,000 sum\n"
        "• Kofe 3 v 1 / Çernıy kofe - 5,000 sum\n"
        "• Moxito (stakan / grafin) - 20,000 / 45,000 sum\n"
        "• Kompot (bokal / grafin) - 8,000 / 24,000 sum\n"
        "• Ayran (bokal / grafin) - 8,000 / 24,000 sum\n"
        "• Şubat - 10,000 sum\n"
        "• Coca-Cola / Fanta 1.5 L - 19,000 sum\n"
        "• Coca-Cola 0.5 L / 1 L - 9,000 / 15,000 sum\n"
        "• Voda (s gazom / bez gaza) 1.5 L - 8,000 sum\n"
        "• Çortok - 13,000 sum\n"
        "• Sok - 15,000 sum",
        reply_markup=keyboard
    )
    await callback.answer()


# --- ADMIN MENEN BAYLANIS ---
@dp.callback_query(F.data == "contact_admin")
async def contact_admin(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Artqa", callback_data="back_to_main")]
    ])
    await callback.message.edit_text(
        f"📞 **Admin menen baylanıs:**\n\n"
        f"Sorawlarınız yamasa zakazlar boyınsha tómendegi nomerge xabar alsańız boladı:\n\n"
        f"📱 Telefon: `{ADMIN_PHONE}`",
        reply_markup=keyboard
    )
    await callback.answer()


@dp.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text("Bas menyu:", reply_markup=get_main_menu())
    await callback.answer()


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
