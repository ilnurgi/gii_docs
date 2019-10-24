.. title:: js puppeteer

.. meta::
    :description:
        Описание js модуля puppeteer.
    :keywords:
        js puppeteer

puppeteer
=========

.. code-block:: sh

    npm install puppeteer


.. code-block:: js

    const puppeteer = require('puppeteer');

    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    var args = process.argv[2]
    await page.goto("ilnurgi.ru");
    await page.click('button.btn-search')
    await page.type('input#', args)
    await page.keyboard.press('Enter');
    await page.screenshot({path: 'sample.png'})

    let urls = await page.evaluate(() = {
        let results = [];
        let items = document.querySelectorAll('li.product__list--item');
        items.forEach((item) = {
                let name = item.querySelector('a.product__list--name').innerText
                let price = item.querySelector('span.pdpPrice').innerText
                let discount = item.querySelector('div.listingDiscnt').innerText
                results.push({
                        prod_name:  name,
                        prod_price: price,
                        prod_discount: discount
                });
            });
        return results;
    })
