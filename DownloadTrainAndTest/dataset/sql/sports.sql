SELECT price.amount as price,price.currency as currency, category.name, images.filename.text as url, 
FROM announce.annonce 
WHERE
	category.name
IN ("5590653b531b3b013b8b456a","5590751d531b3b2b478b4573","55907526531b3b94438b4574","5590752f531b3b95438b4571","5590753e531b3b96438b4572","55907545531b3bab628b4570","5590754f531b3b2b478b4574","55907556531b3b94438b4575","55907579531b3b95438b4572","5590759a531b3b96438b4573","5590774b531b3bab628b4571","55907794531b3b2b478b4575")