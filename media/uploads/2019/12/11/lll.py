Access_Key='AKIAI37VVOBFMLGQYA5A'		

Secret_Key='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'		
		
Tag='aggtrends-20'

from amazon.api import AmazonAPI
amazon = AmazonAPI(Access_Key, Secret_Key, Tag)
product = amazon.lookup(ItemId='B01J4MF53Q')
print(product.reviews[1])
print(product.large_image_url)

