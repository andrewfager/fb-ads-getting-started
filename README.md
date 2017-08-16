# Getting Started with Facebook Marketing API 
A step-by-step guide to automatically creating Ads in Python with the Facebook Marketing API.

## Create Advert Account
create account at www.facebook.com/ads/manager

## Create App
create a new app at developers.facebook.com

![ScreenShot](images/fb-create-app2.png)

### Allow API access to the App
API access to our new app needs to be enabled.  
developers.facebook.com
settings > advanced

![ScreenShot](images/fb-api-access.png)

### Add Advert account to the App

The app and advert account need to linked. Enter Advert account number under app's advanced settings.
![ScreenShot](images/fb-ad-id.png)

### Access Token
Create user access token to the App. One way to do this is in the graph API explorer.
https://developers.facebook.com/tools/explorer

Select correct app

![ScreenShot](images/fb-access-token1.png)

Select 'create user access token'

![ScreenShot](images/fb-access-token3.png)

Make sure permisions are enabled for: 
ads_management, ads_read, read_insights

![ScreenShot](images/fb-access-token4.png)

## Resources:
github.com/facebook/facebook-python-ads-sdk
www.facebookmarketingdevelopers.com
