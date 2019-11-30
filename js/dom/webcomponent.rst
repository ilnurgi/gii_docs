.. title:: js.webcomponents

.. meta::
    :description: js.webcomponents
    :keywords: js.webcomponents

webcomponents
=============

.. code-block:: html

    <body>
        <my-webcomp
            id="myWebComp"
            onclick="rgis.showMessage(event)"
            name="ilnurgi"
        ></my-webcomp>

        <template id="myWebCompTemplate">
            <div>Hello</div>
        </template>

        <script type="module">
            class MyWebComp extends HTMLElement {
                connectedCallback() {
                    this.insertAdjacentHTML('beforeEnd', '<div>Hello</div>')

                    let html = document.importNode(myWebCompTemplate.content, true);
                    this.appendChild(html)
                }
                showMessage(event) {
                    console.log(event);
                    console.log(this.getAttribute('name'));
                }
            }
            customElement.define('my-webcomp', MyWebComp)
        </script>

    </body>
