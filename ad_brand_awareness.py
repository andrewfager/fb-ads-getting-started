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

my_targeting	= {'geo_locations':{'countries':['US']}}
my_daily_budget	= 1000 # 1000 = $10
img_filename 	= '/path/to/image.jpg'    #local image path to be uploaded by the API.
link_url        = 'http://www.mylink.com' #link to your brand's website.
link_message 	= 'try it out'

# rm before upload
access_token    = 'EAAX6ZA1VtWiIBAPpp6JJrw0iFRNwdPKh5OBSpYeZBhp8m9PEznICIWY44x4lND4PVRQtbUmqWRn6wzxZBGEeHqMLwpysxLk7iho3CzjtL4K9FmWb5ADnKMu7NGHzb69Vg6IpR7vypXBcZAgQbPEiFSGKY5QE4uEZD' # long lived user access token for andrewfager app 2 months from 7/27
ad_account_id   = '10152750485066251'
page_id         = '1897834227096194'

campaign_name   = 'My Campaign4'
campaign_status = 'ACTIVE'
campaign_status = 'PAUSED'

adset_name      = 'My Adset'
adset_status    = 'ACTIVE'
adset_status    = 'PAUSED'

ad_name         = 'My Ad'
ad_status       = 'ACTIVE'
ad_status       = 'PAUSED'

img_filename = '/Users/carolefager/Desktop/rock1.jpg'
link_url = 'http://www.exa.com/digitalrock'

####### Setup ############

FacebookAdsApi.init(access_token=access_token)
my_parent_id = 'act_'+ad_account_id

me = objects.AdUser(fbid='me')
my_accounts = list(me.get_ad_accounts())
my_account = my_accounts[0]

### Campaign ###
print 'Creating Campaign: ',campaign_name

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

# when using parent id get this message: WARNING:root:parent_id as a parameter of constructor is being deprecated.
# need to figure out new approache
campaign = Campaign(parent_id=my_parent_id)
campaign.remote_create(params=params)
campaign_id = campaign.get_id()


### Ad Set ###
print 'Creating Ad Set: ',adset_name

params = {
    'name': adset_name,
    'optimization_goal': 'BRAND_AWARENESS',
    'billing_event': 'IMPRESSIONS',
    'promoted_object': {'page_id': page_id},
    'daily_budget': my_daily_budget,
    'is_autobid':True,
    'campaign_id': campaign_id,
    'targeting': my_targeting,
    'status': adset_status,
}

# if manual bid use:
#'bid_amount': '20',

ad_account = my_account
ad_set = ad_account.create_ad_set(params=params) #could have also used remote_create() method
ad_set_id = ad_set.get_id()

### Ad ###
print 'Creating Ad: ',ad_name

#Image
image = AdImage(parent_id=my_parent_id)
image[AdImage.Field.filename] = img_filename
image.remote_create()


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

creative = AdCreative(parent_id=my_parent_id)
creative[AdCreative.Field.name] = 'AdCreative for Link Ad'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()
creative_id = creative.get_id()

# The Actual Ad
ad = Ad(parent_id=my_parent_id)
# alternate way to specify parameters, could have also used params dictionary like in the Campaign or AdSet creation
ad[Ad.Field.name] = ad_name
ad[Ad.Field.adset_id] = ad_set_id
ad[Ad.Field.creative] = {
    'creative_id':creative_id,
}
ad.remote_create(params={
    'status': ad_status,
})


########### List Campaigns #############

print '\nCurrent Campaigns:'
my_campaigns =  list(my_account.get_campaigns())

for each_campaign in my_campaigns:
	data = each_campaign.remote_read(fields=[objects.Campaign.Field.name,objects.Campaign.Field.status,objects.Campaign.Field.created_time,objects.Campaign.Field.objective,objects.Campaign.Field.effective_status])
	print data




