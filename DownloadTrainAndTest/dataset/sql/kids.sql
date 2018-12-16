SELECT price.amount as price,price.currency as currency, category.name, images.filename.text as url, 
FROM announce.annonce 
WHERE
	category.name
IN ("55906559531b3b093e8b4567","55914dcb531b3b2b478b457a","55914dd7531b3b94438b457b","55914de0531b3b95438b457c","55914deb531b3b96438b457c","55914df3531b3bab628b4578")
