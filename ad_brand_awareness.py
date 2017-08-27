from facebookads import objects
from facebookads.api import FacebookAdsApi
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.adpreview import AdPreview
from facebookads.adobjects.adcreativelinkdata import AdCreativeLinkData
from facebookads.adobjects.adcreativeobjectstoryspec import AdCreativeObjectStorySpec
from facebookads.adobjects.adimage import AdImage

### User Input ###

access_token 	= '<ACCESS_TOKEN>'
ad_account_id 	= '<AD_ACCOUNT_ID>'
page_id 	= '<PAGE_ID>'

campaign_name   = 'My Campaign2'
campaign_status = 'ACTIVE'
campaign_status = 'PAUSED'

adset_name      = 'My Adset'
adset_status    = 'ACTIVE'
adset_status    = 'PAUSED'

ad_name         = 'My Ad'
ad_status       = 'ACTIVE'
ad_status       = 'PAUSED'

img_filename 	= '/path/to/image.jpg'
link_url 	= 'http://www.mylink.com'
link_message 	= 'try it out'

###################

FacebookAdsApi.init(access_token=access_token)
my_parent_id = 'act_'+ad_account_id

### Campaign ###

#Use one of these campaign objectives: 
#EVENT_RESPONSES, LINK_CLICKS, OFFER_CLAIMS, PAGE_LIKES, 
#POST_ENGAGEMENT, PRODUCT_CATALOG_SALES, VIDEO_VIEWS, 
#LEAD_GENERATION, LOCAL_AWARENESS, BRAND_AWARENESS, 
#REACH, APP_INSTALLS, CONVERSIONS

params = {
    'name': campaign_name,
    'objective': 'BRAND_AWARENESS',
    'status': campaign_status,
}

campaign = Campaign(parent_id=my_parent_id)
campaign.remote_create(params=params)
campaign_id = campaign.get_id()

#print 'campaign', campaign
#print 'campaign_id:', campaign_id, '\n'

### Ad Set ###

me = objects.AdUser(fbid='me')
my_accounts = list(me.get_ad_accounts())
my_account = my_accounts[0]

#print(my_accounts)
#print type(my_accounts[0])

params = {
    'name': adset_name,
    'optimization_goal': 'BRAND_AWARENESS',
    'billing_event': 'IMPRESSIONS',
    'promoted_object': {'page_id': page_id},
    'daily_budget': '1000',
    'is_autobid':True,
    'campaign_id': campaign_id,
    'targeting': {'geo_locations':{'countries':['US']}},
    'status': adset_status,
}

# if manual bid use:
#'bid_amount': '20',

ad_account = my_account
ad_set = ad_account.create_ad_set(params=params)
ad_set_id = ad_set.get_id()

#print 'ad_set', ad_set
#print 'ad_set_id:', ad_set_id, '\n'

### Ad ###

#Image

image = AdImage(parent_id=my_parent_id)
image[AdImage.Field.filename] = img_filename
image.remote_create()

# Output image Hash
#print(image[AdImage.Field.hash])


#Creative

link_data = AdCreativeLinkData()
link_data[AdCreativeLinkData.Field.message] = link_message
link_data[AdCreativeLinkData.Field.link] = link_url
link_data[AdCreativeLinkData.Field.image_hash] = image[AdImage.Field.hash]

object_story_spec = AdCreativeObjectStorySpec()
object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = page_id
object_story_spec[AdCreativeObjectStorySpec.Field.link_data] = link_data

creative = AdCreative(parent_id=my_parent_id)
creative[AdCreative.Field.name] = 'AdCreative for Link Ad'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()

#print(creative)

creative = AdCreative(parent_id=my_parent_id)
creative[AdCreative.Field.name] = 'AdCreative for Link Ad'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()

#print 'creative', creative

creative_id = creative.get_id()
#print 'creative_id:', creative_id, '\n'


# The Actual Ad
ad = Ad(parent_id=my_parent_id)
ad[Ad.Field.name] = ad_name
ad[Ad.Field.adset_id] = ad_set_id
ad[Ad.Field.creative] = {
    'creative_id':creative_id,
}
ad.remote_create(params={
    'status': ad_status,
})


