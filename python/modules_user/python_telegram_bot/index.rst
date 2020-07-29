.. title:: python telegram bot

.. meta::
    :description:
        Справочная информация python библиотеке python-telegram-bot.
    :keywords:
        python telegram bot

python-telegram-bot
===================

.. code-block:: sh

    pip install python-telegram-bot

.. code-block:: py

    from telegram import (
        Update,
        KeyboardButton,
        ReplyKeyboardMarkup,
        ReplyKeyboardRemove,
    )
    from telegram.ext import (
        Updater,
        CallbackContext,
        Filters,
        MessageHandler,
    )

    button_help = 'Помощь'


    def button_help_handler(update: Updater, context: CallbackContext):
        update.message.reply_text(
            text='Помощь',
            reply_markup=ReplyKeyboardRemove(),
        )


    def message_handler(update: Updater, context: CallbackContext):
        text = update.message.text
        if text == button_help:
            return button_help_handler(update, context)

        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=button_help),
                ]
            ],
            resize_keyboard=True,
        )
        update.message.reply_text(
            text='тект',
            reply_markup=reply_markup,
        )


    def main():
        updater = Updater(
            token=token,
            use_context=True,
        )
        print(updater.bot.get_me())
        updater.dispatcher.add_handler(
            MessageHandler(
                filters=Filters.all,
                callback=message_handler
        ))
        updater.start_polling()
        updater.idle()

    main()
