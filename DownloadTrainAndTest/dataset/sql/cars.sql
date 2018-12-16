SELECT price.amount as price,price.currency as currency, category.name, images.filename.text as url, 
FROM
  announce.annonce
WHERE
	category.name 
IN ("559066d0531b3b2b478b456b","55914fbe531b3b093e8b4572","55914ff6531b3b93438b4577","55915000531b3b013b8b4574","55915012531b3baa628b4571","55915029531b3b92438b4573","5591503c531b3b94438b457c","55915046531b3b95438b457d","5591504e531b3b96438b457d")

