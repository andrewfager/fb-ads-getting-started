#derived from SAMPLE_CODE1_mod.py

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

access_token = '<ACCESS_TOKEN>'

ad_account_id = '10152750485066251'
page_id = '1897834227096194'

FacebookAdsApi.init(access_token=access_token)

### Campaign ###

#Use one of these campaign objectives: 
#EVENT_RESPONSES, LINK_CLICKS, OFFER_CLAIMS, PAGE_LIKES, 
#POST_ENGAGEMENT, PRODUCT_CATALOG_SALES, VIDEO_VIEWS, 
#LEAD_GENERATION, LOCAL_AWARENESS, BRAND_AWARENESS, 
#REACH, APP_INSTALLS, CONVERSIONS

params = {
    'name': 'My Campaign',
    'objective': 'BRAND_AWARENESS',
    'status': 'PAUSED',
}

campaign = Campaign(parent_id='act_10152750485066251')
campaign.remote_create(params=params)
campaign_id = campaign.get_id()

print 'campaign', campaign
print 'campaign_id:', campaign_id, '\n'

### Ad Set ###

me = objects.AdUser(fbid='me')
my_accounts = list(me.get_ad_accounts())
my_account = my_accounts[0]

print(my_accounts)
print type(my_accounts[0])

params = {
    'name': 'My AdSet',
    'optimization_goal': 'BRAND_AWARENESS',
    'billing_event': 'IMPRESSIONS',
    'promoted_object': {'page_id': page_id},
    'daily_budget': '1000',
    'is_autobid':True,
    'campaign_id': campaign_id,
    'targeting': {'geo_locations':{'countries':['US']}},
    'status': 'PAUSED',
}

# if manual bid use:
#'bid_amount': '20',

ad_account = my_account
ad_set = ad_account.create_ad_set(params=params)
ad_set_id = ad_set.get_id()

print 'ad_set', ad_set
print 'ad_set_id:', ad_set_id, '\n'

### Ad ###
params = {
    'name': 'My Creative',
    'object_id': page_id,
    'title': 'My Page Like Ad',
    'body': 'Like My Page',
    'image_url': 'http://www.facebookmarketingdevelopers.com/static/images/resource_1.jpg',
}

#https://developers.facebook.com/docs/marketing-api/buying-api

#Image

image = AdImage(parent_id='act_10152750485066251')
image[AdImage.Field.filename] = '/Users/carolefager/Desktop/rock1.jpg' #can this be on the internet?
image.remote_create()

# Output image Hash
print(image[AdImage.Field.hash])


#Creative

link_data = AdCreativeLinkData()
link_data[AdCreativeLinkData.Field.message] = 'try it out'
link_data[AdCreativeLinkData.Field.link] = 'http://www.exa.com/exa-digitalrock'
#link_data[AdCreativeLinkData.Field.link] = 'http://www.facebookmarketingdevelopers.com/static/images/resource_1.jpg'
link_data[AdCreativeLinkData.Field.image_hash] = image[AdImage.Field.hash]

object_story_spec = AdCreativeObjectStorySpec()
object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = page_id
object_story_spec[AdCreativeObjectStorySpec.Field.link_data] = link_data

creative = AdCreative(parent_id='act_10152750485066251')
creative[AdCreative.Field.name] = 'AdCreative for Link Ad'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()

print(creative)

creative = AdCreative(parent_id='act_10152750485066251')
creative[AdCreative.Field.name] = 'AdCreative for Link Ad'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()

print 'creative', creative

creative_id = creative.get_id()
print 'creative_id:', creative_id, '\n'


# The Actual Ad


ad = Ad(parent_id='act_10152750485066251')
ad[Ad.Field.name] = 'My Ad'
ad[Ad.Field.adset_id] = ad_set_id
ad[Ad.Field.creative] = {
    'creative_id':creative_id,
}
ad.remote_create(params={
    'status': Ad.Status.paused,
})


