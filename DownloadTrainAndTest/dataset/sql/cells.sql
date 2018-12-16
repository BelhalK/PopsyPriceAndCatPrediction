SELECT price.amount as price,price.currency as currency, category.name, images.filename.text as url, 
FROM
  announce.annonce
WHERE
	category.name
IN ("5590670f531b3bab628b4569","5590695b531b3b96438b456d","55906962531b3bab628b456a","5590696a531b3b2b478b456d","559069b2531b3b2b478b456e")

