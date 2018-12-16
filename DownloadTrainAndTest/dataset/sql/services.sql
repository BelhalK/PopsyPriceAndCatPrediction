SELECT price.amount as price,price.currency as currency, category.name, images.filename.text as url, 
FROM announce.annonce 
WHERE
	category.name
IN ("559066e7531b3b96438b456c","559156b0531b3b96438b457e","559156bc531b3bab628b4579","559156c8531b3b2b478b457b","559156d9531b3b94438b457d","559156e5531b3b95438b457e","559156f1531b3b96438b457f","559156ff531b3bab628b457a","5591570e531b3b2b478b457c")

