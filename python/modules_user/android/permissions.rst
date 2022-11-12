.. py:module:: android.permissions

permissions
===========

.. py:class:: Permission

    Права https://developer.android.com/reference/android/Manifest.permission

    .. py:attribute:: CAMERA
    .. py:attribute:: READ_EXTERNAL_STORAGE
    .. py:attribute:: WRITE_EXTERNAL_STORAGE
    

.. py:function:: check_permission(permission)

    * permission - Permission

    Возвращает булево, проверят наличие прав
    

.. py:function:: request_permission(permission, callback=None)

    * permission - Permission
    * callback - callable(permission: Permission, permission_grant: bool)

    Запрос прав на 1 зону


.. py:function:: request_permissions(permissions, callback=None)

    * permissions - List[Permission]
    * callback - callable(permissions: List[Permission], permissions_grant: List[bool])

    Запрос прав 

    .. code-block:: py

        from android.permissions import request_permissions, Permission

        request_permissions(
            [Permission.CAMERA]
        )
