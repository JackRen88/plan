# -*- coding: utf-8 -*-

import os
import random
import shutil


def makedir(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)


if __name__ == '__main__':

    random.seed(1)

    dataset_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", "..", "data", "cat_dog")

    #生成cat_dog文件夹
    is_split = True
    if is_split is False:
        makedir(os.path.join(dataset_dir, "cat"))
        makedir(os.path.join(dataset_dir, "dog"))

        imgs = os.listdir(dataset_dir)
        imgs_cat = list(filter(lambda x: x.startswith('cat.'), imgs))
        imgs_dog = list(filter(lambda x: x.startswith('dog.'), imgs))


        for img_cat in imgs_cat:
            target_path = os.path.join(dataset_dir,"cat", img_cat)
            src_path = os.path.join(dataset_dir, img_cat)
            #移动文件到cat文件夹
            shutil.move(src_path, target_path)

        for img_dog in imgs_dog:
            target_path = os.path.join(dataset_dir,"dog", img_dog)
            src_path = os.path.join(dataset_dir, img_dog)

            shutil.move(src_path, target_path)

    else:
        split_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", "..", "data", "cat_dog_split")
        train_dir = os.path.join(split_dir, "train")
        valid_dir = os.path.join(split_dir, "valid")
        test_dir = os.path.join(split_dir, "test")
        train_pct = 0.8
        valid_pct = 0.1
        test_pct = 0.1

        for root, dirs, files in os.walk(dataset_dir):
            for sub_dir in dirs:
                imgs = os.listdir(os.path.join(root, sub_dir))
                imgs = list(filter(lambda x: x.endswith('.jpg'), imgs))
                random.shuffle(imgs)
                img_count = len(imgs)

                train_point = int(img_count * train_pct)
                valid_point = int(img_count * (train_pct + valid_pct))

                for i in range(img_count):
                    if i < train_point:
                        out_dir = os.path.join(train_dir, sub_dir)
                    elif i < valid_point:
                        out_dir = os.path.join(valid_dir, sub_dir)
                    else:
                        out_dir = os.path.join(test_dir, sub_dir)

                    makedir(out_dir)

                    target_path = os.path.join(out_dir, imgs[i])
                    src_path = os.path.join(dataset_dir, sub_dir, imgs[i])

                    shutil.copy(src_path, target_path)

                print('Class:{}, train:{}, valid:{}, test:{}'.format(sub_dir, train_point, valid_point-train_point,
                                                                    img_count-valid_point))
                
