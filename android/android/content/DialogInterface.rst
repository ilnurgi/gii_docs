.. title:: android.content.DialogInterface

.. meta::
    :description:
        Справочная информация по android классу android.content.DialogInterface().
    :keywords:
        android content DialogInterface

.. py:currentmodule:: android.content

DialogInterface()
=================

.. py:class:: DialogInterface()

  .. py:class:: OnClickListener()

      .. py:method:: onClick(DialogInterface dialog, int which)

          .. code-block:: java

              OnClickListener myClickListener = new OnClickListener() {

                  public void onClick(DialogInterface dialog, int which) {
                    switch (which) {
                    // положительная кнопка
                    case Dialog.BUTTON_POSITIVE:
                      break;
                    // негаитвная кнопка
                    case Dialog.BUTTON_NEGATIVE:
                      break;
                    // нейтральная кнопка
                    case Dialog.BUTTON_NEUTRAL:
                      break;
                    }
              }
