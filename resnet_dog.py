# import skimage.io  # bug. need to import this before tensorflow
# import skimage.transform  # bug. need to import this before tensorflow
from resnet_train import train
from resnet import *
import tensorflow as tf
import time
import os
import sys
import re
import numpy as np
import csv

from image_processing import image_preprocessing

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('data_dir', 'D:\works\python\doggie\data',
                           'doggie dir')


# def loadfile(path):
#     file = open(path+"\data_train_image.csv")
#     filenames = []
#     labels = []
#     f_csv = csv.reader(file)
#     headers = next(f_csv)
#     for row in f_csv:
#         index = str(row[1]).rindex("/")
#         filenames.append(FLAGS.data_dir + "\img\\" + str(row[1])[index + 1:])
#         labels.append(int(row[0]))
#     return filenames, labels

def loadfile(path):
    file = open(path+"\data_train_image_tp.txt")
    filenames = []
    labels = []
    while True:
        lines = file.readlines(1000)
        if not lines:
            break
        for line in lines:
            arr = line.split(",")
            filenames.append(FLAGS.data_dir + "\img\\" + arr[1] + "," + arr[2][0:-1]+".jpg")
            labels.append(int(arr[0]))
    return filenames, labels


def distorted_inputs():
    filenames,label_indexes = loadfile(FLAGS.data_dir)

    filename, label_index = tf.train.slice_input_producer([filenames, label_indexes], shuffle=True)

    num_preprocess_threads = 4
    images_and_labels = []
    for thread_id in range(num_preprocess_threads):
        image_buffer = tf.read_file(filename)

        bbox = []
        train = True
        image = image_preprocessing(image_buffer, bbox, train, thread_id)
        images_and_labels.append([image, label_index])

    images, label_index_batch = tf.train.batch_join(
        images_and_labels,
        batch_size=FLAGS.batch_size,
        capacity=2 * num_preprocess_threads * FLAGS.batch_size)

    height = FLAGS.input_size
    width = FLAGS.input_size
    depth = 3

    images = tf.cast(images, tf.float32)
    label_index_batch = tf.cast(label_index_batch, tf.int32)
    images = tf.reshape(images, shape=[FLAGS.batch_size, height, width, depth])

    return images, tf.reshape(label_index_batch, [FLAGS.batch_size])


def main(_):
    images, labels = distorted_inputs()

    logits = inference(images,
                       num_classes=1000,
                       is_training=True,
                       bottleneck=False,
                       num_blocks=[2, 2, 2, 2])
    train(is_training=True, logits=logits, images=images, labels=labels)


if __name__ == '__main__':
    tf.app.run()
