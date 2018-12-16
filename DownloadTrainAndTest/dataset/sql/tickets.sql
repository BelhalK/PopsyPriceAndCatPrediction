SELECT price.amount as price,price.currency as currency, category.name, images.filename.text as url, 
FROM
	announce.annonce 
WHERE
	category.name
IN ("559066c7531b3bab628b4568","55914f59531b3b013b8b4572","55914f63531b3baa628b4570","55914f6e531b3b92438b4572","55914f7b531b3b093e8b4571","55914f85531b3b93438b4576","55914f8e531b3b013b8b4573")
