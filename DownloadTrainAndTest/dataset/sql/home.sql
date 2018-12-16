SELECT price.amount as price,price.currency as currency, category.name, images.filename.text as url, 
FROM
  announce.annonce
WHERE
	category.name
IN ("5590654d531b3b92438b4568","55906ccd531b3b94438b4570","55906d84531b3b95438b456e","55906d90531b3b96438b456e","55906d9a531b3bab628b456d","55906da5531b3b2b478b4570","55906db5531b3b94438b4571","55906dc3531b3b95438b456f","55906dd3531b3b96438b456f","55906ddf531b3b92438b456a","55906caf531b3bab628b456c","55906cc3531b3b2b478b456f")
