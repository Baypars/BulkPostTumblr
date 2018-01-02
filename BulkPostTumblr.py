#!/usr/bin/python3
#BulkPostTumblr

#Purpose:
#BulkPostTumblr is a script which can be used to post multipe photos on a Tumblr blog.

#Author:Kshithij Iyer
#Email: ahole@disroot.org
#Date of Creation: 2/1/2018


#imports
import sys, getopt, re, pytumblr, os, glob

def main(argv):
    
    blog_name=''
    #Put your tumblr credentials here.
    client = pytumblr.TumblrRestClient(
    '<consumer_key>',
    '<consumer_secret>',
    '<oauth_token>',
    '<oauth_secret>',
    )


    try:
        opts, args = getopt.getopt(argv,"hb:",["blog="])
    except getopt.GetoptError:
        print("Error: Unable to identify the given argument!")
        print('python3 BulkPostTumblr.py -b <blog>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('python3 BulkPostTumblr.py -b <blog>')
            sys.exit(2)
        elif opt in ("-b", "--blog"):
            blog_name = arg
        
        #chaning working dir
        os.chdir("images/")
        
        #Taking the images from images/ dir and posting them on the blog.
        for file in glob.glob("*.jpeg"):
            print(file)
            client.create_photo(blog_name, state="published", data=file)
        for file in glob.glob("*.jpg"):
            print(file)
            client.create_photo(blog_name, state="published", data=file)
        for file in glob.glob("*.png"):
            print(file)
            client.create_photo(blog_name, state="published", data=file)

        #Final termination message
        print("All images posted to your sepecifed blog!")

if __name__ == "__main__":
    main(sys.argv[1:])
