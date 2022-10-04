.. py:module:: android.storage

storage
=======

.. py:function:: app_storage_path()

    Возвращает строку, путь до папки приложения. Папка не доступна для других приложений.

    .. code-block:: py

        app_storage_path()
        # /data/user/0/ru.ilnurgi.agiicamera/files


.. py:function:: primary_external_storage_path()

    Возвращает строку, путь до папки основного хранилища устройства. Папка доступна для всех. Требует прав:  Permission.READ_EXTERNAL_STORAGE и Permission.WRITE_EXTERNAL_STORAGE.

    .. code-block:: py

        primary_external_storage_path()
        # /storage/emulated/0


.. py:function:: secondary_external_storage_path()

    Возвращает строку, путь до папки внешнего хранилища устройства, флешки. Папка доступна для всех. Требует прав:  Permission.READ_EXTERNAL_STORAGE и Permission.WRITE_EXTERNAL_STORAGE.

    .. code-block:: py

        secondary_external_storage_path()
        # None