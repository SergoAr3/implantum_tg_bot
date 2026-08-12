from bot.keyboards.main_menu import main_menu_keyboard


def test_main_menu_contains_appointment_button() -> None:
    keyboard = main_menu_keyboard()

    button_texts = [button.text for row in keyboard.keyboard for button in row]
    assert "🦷 Записаться на приём" in button_texts

