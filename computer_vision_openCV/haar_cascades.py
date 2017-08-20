import urllib
import cv2
import numpy as np
import os


def store_raw_images():
    #http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152 - people
    #http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513 - athletes
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
    neg_image_urls = urllib.urlopen(neg_images_link).read().decode()
    pic_num = 1
    if not os.path.exists('neg'):
        os.makedirs('neg')
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.urlretrieve(i, "neg/" + str(pic_num) + ".jpg")
            img = cv2.imread("neg/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (400, 400)) # Choose negative image size
            cv2.imwrite("neg/" + str(pic_num) + ".jpg", resized_image)
            pic_num += 1
        except Exception as e:
            print(str(e))

# Find unwanted images that would effect the haar cascade.
def find_uglies():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('haar_cascades/uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('haar_cascades/uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('dayyyummm girl you ugly!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))

# 
def create_pos_n_neg():
    for file_type in ['neg_200px']:
        for img in os.listdir(file_type):
            if file_type[0] == 'p':
                line = file_type + '/' + img + ' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)
            elif file_type[0] == 'n':
                line = file_type + '/' + img + '\n'
                with open('bg_200px.txt', 'a') as f:
                    f.write(line)

# Simple image resizing. Indicate file path, width, and height.
def resize_image(img, w=50, h=50):
    pic = cv2.imread(img)
    pic = cv2.resize(pic, (w,h))
    cv2.imwrite('images/'+img, pic)

# Run functions in here.
def main():
    #store_raw_images()
    #find_uglies()
    #create_pos_n_neg()
    # for i in range(12):
    #     nm = 'pic%i.jpg' % (i+1)
    resize_image("battery_icon.jpg", w=32, h=22)
    #resize_image('pic.jpg')
    print "SUCCESS!!"

if __name__ == "__main__":
    main()
