SELECT price.amount as price,price.currency as currency, category.name, images.filename.text as url, 
FROM
  announce.annonce
WHERE 
	category.name
IN ("55906545531b3baa628b4568","55906905531b3b93438b456e","559068f8531b3b093e8b4568","559069a5531b3bab628b456b","5590691b531b3b92438b4569")
LIMIT 30