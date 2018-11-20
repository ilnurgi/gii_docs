grid-template-columns
---------------------

.. code-block:: css
	
	.wrappper {
		grid-template-columns: repeat(4, 1fr);
		grid-template-columns: repeat(4, min-content);
		grid-template-columns: repeat(4, max-content);
		grid-template-columns: minmax(200px, 1fr) minmax(350px, 1fr);
	}