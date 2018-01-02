# BulkPostTumblr
This is a command-line python script which can be used to upload multipe images on Tumblr blogs.
## Prerequisites
* Python 3.x
* Python pytumblr module

## Installation and Usage
1. Download the project files from github.
```
git clone https://github.com/kshithijiyer/BulkPostTumblr.git
```
2. Change directory to the project directory. 
```
cd BulkPostTumblr

```
And Create a application in https://api.tumblr.com/console/calls/user/info  and modify the credentails as show below on ```BulkPostTumblr.py``` file.
```
client = pytumblr.TumblrRestClient(
    '<consumer_key>',
    '<consumer_secret>',
    '<oauth_token>',
    '<oauth_secret>',
)

```
3. To post the images on your tumblr blog copy paste the images to ```/images``` folder 
```
python3 BulkPostTumblr.py -b <blog_url>
```
    or 
```
python3 linkExtract.py --blog=<blog_url> 
```
4. For displaying the help menu use the following command.
```
python3 BulkPostTumblr.py -h
```


## Built with 
[IDLE 3](https://www.python.org/downloads/)


## Author
[Kshithij Iyer](https://www.linkedin.com/in/kshithij-iyer/)

## Licence 
The project is released under Apache 2.0 licence.
