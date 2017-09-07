# How to Create a Brand Awareness Ad with the Facebook Marketing API

## Introduction
In this repository ``ad_brand_awareness.py`` creates a Facebook Brand Awareness ad. What follows are the steps I used to setup and use the Marketing API to create the ad. I hope someone finds this helpful for getting starting automatically creating and managing Facebook ads.

## Setup

#### Install API
Install Marketing API for Python with ``pip``, if there are permission issues you may need to use ``sudo``
```
pip install facebookads
```
See <a href="https://github.com/facebook/facebook-python-ads-sdk">github.com/facebook/facebook-python-ads-sdk</a> for more information on the installation process.

#### App
You will need a Facebook App. Create a new app at https://developers.facebook.com

<img src="images/fb-create-app2.png" width="650">


#### Ad Account

If not already setup you will need to create an Ad account. This can be done at: https://www.facebook.com/ads/manager/

#### Page

The brand awareness ad needs to reference a Facebook page. If you do not have a page you can create one here: https://www.facebook.com/pages/create

## User Input

Before running ``ad_awareness.py`` fill out the ``### User Input ###`` section at the top of the code  

#### Access Token

For the API to access your app you will need to enter an access token (as a string). 
```
access_token    = '<ACCESS_TOKEN>'
```

When you're getting started it's simplet to use the graph API explorer to create one.
https://developers.facebook.com/tools/explorer. To do so select app

<img src="images/fb-access-token-1.png" width="650">

Select 'get user access token'

<img src="images/fb-access-token-3.png" width="650">

Make sure permisions are enabled for: 
``ads_management``, ``ads_read``, ``read_insights``

<img src="images/fb-access-token-4.png" width="650">

copy and paste into ```access_token``` variable.  

#### Ad Account ID

You'll also need to enter your ad account ID (as a string). 
```
ad_account_id   = '<AD_ACCOUNT_ID>'
```

You can obtain this from the Ads manager (https://www.facebook.com/ads/manager/).

<img src="images/fb-ad-id3.png" width="400">


#### Page ID

Finally, you will need to input your FB page ID  (again, as a string).
```
page_id         = '<PAGE_ID>'
```

You can find this by going to the page's 'About' section. 

<img src="images/fb-page-id2.png" width="650">


#### Campaign/Adset/Ad Settings
This is where you input settings such as naming, targeting, budget, etc. These Ad Settings are required input:
```
img_filename    = '/path/to/image.jpg'    #local image path to be uploaded by the API.
link_url        = 'http://www.mylink.com' #link to your brand's website.
```

For this example you can keep all the other setting at their defaults and succesfully create an Ad. 

To prevent any charges from being incurred the Campaign, Adset & Ad are all paused when initially created. This is set in the  ```campaign_status```/```adset_status```/```ad_status``` variables.


## Create Your Ad

Now it's time to create an ad using the API
```
python ad_brand_awareness.py
```
Example output:
```
Creating Campaign:  My Campaign
Creating Ad Set:  My Adset
Creating Ad:  My Ad

Current Campaigns:
<Campaign> {
    "created_time": "2017-08-31T07:17:17+0200",
    "effective_status": "PAUSED",
    "id": "6103773787451",
    "name": "My Campaign",
    "objective": "BRAND_AWARENESS",
    "status": "PAUSED"
}
<Campaign> {
    "created_time": "2017-08-31T07:06:50+0200",
    "effective_status": "PAUSED",
    "id": "6103773531251",
    "name": "My Campaign3",
    "objective": "BRAND_AWARENESS",
    "status": "PAUSED"
```
To verify that the ad was created successfully check that it appears in the list of campaigns outputed when running ``ad_brand_awareness.py`` or check the Ads Manager (https://www.facebook.com/ads/manager/).

In this example you can see that the campaign labeled ``My Campaign`` was successfully created as it is found in the list current campaigns. In a similar way we could list all the Ad Sets and Ad associated with our new campaign.

That's it! I hope this is helpful and can be used as a starting point for working with Facebook's Marketing API in Python. 

## Resources
<a href="https://github.com/facebook/facebook-python-ads-sdk/">github.com/facebook/facebook-python-ads-sdk</a>

www.facebookmarketingdevelopers.com

<a href="https://developers.facebook.com/docs/marketing-apis">developers.facebook.com/docs/marketing-apis</a>
