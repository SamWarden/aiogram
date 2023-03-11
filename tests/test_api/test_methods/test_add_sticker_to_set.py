from aiogram.methods import AddStickerToSet, Request
from aiogram.types import InputSticker
from tests.mocked_bot import MockedBot


class TestAddStickerToSet:
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(AddStickerToSet, ok=True, result=True)

        response: bool = await AddStickerToSet(
            user_id=42,
            name="test stickers pack",
            sticker=InputSticker(sticker="file id", emoji_list=[":)"]),
        )
        request: Request = bot.get_request()
        assert request.method == "addStickerToSet"
        assert response == prepare_result.result

    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(AddStickerToSet, ok=True, result=True)

        response: bool = await bot.add_sticker_to_set(
            user_id=42,
            name="test stickers pack",
            sticker=InputSticker(sticker="file id", emoji_list=[":)"]),
        )
        request: Request = bot.get_request()
        assert request.method == "addStickerToSet"
        assert response == prepare_result.result
