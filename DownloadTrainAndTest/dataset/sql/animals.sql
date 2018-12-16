SELECT price.amount as price,price.currency as currency, category.name, images.filename.text as url, 
FROM 
	announce.annonce 
WHERE
	category.name
IN ("55906718531b3b2b478b456c","5591588e531b3b94438b457e","55915880531b3b2b478b457e","55915899531b3b95438b457f","559158a5531b3b96438b4580","559158f5531b3bab628b457c","55915909531b3b2b478b457f","55915911531b3b94438b457f")
