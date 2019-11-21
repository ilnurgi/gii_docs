.. title:: android.webkit.WebView

.. meta::
    :description:
        Справочная информация по android классу android.webkit.WebView.
    :keywords:
        android webkit WebView

.. py:currentmodule:: android.webkit

WebView()
=========

.. code-block:: xml

    <WebView

        android:layout_width= "match_parent"
        android:layout_height= "match_parent"

        android:id= "@+id/webView" />

.. py:class:: WebView()

    Элемент типа браузера

    .. code-block:: java

        WebView webView = (WebView) findViewById(R.id.webView);


    .. py:method:: loadUrl(String url)

        Загружает указанную страницу.

        .. code-block:: java

            webView.loadUrl("http://ilnurgi1.ru");
