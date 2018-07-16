#!/usr/bin/env python3

import tensorflow as tf
from tensorflow.python.saved_model import tag_constants
import numpy as np
import argparse
import librosa
import os


x = None
y = None
y_ = None
graph = None
sess = None


def load_model(model_dir):
    global x, y, y_, graph, sess
    if sess is not None:
        return

    graph = tf.Graph()
    graph.as_default()
    sess = tf.Session(graph=graph)

    tf.saved_model.loader.load(sess, [tag_constants.SERVING], model_dir)
    x = graph.get_tensor_by_name('x:0')
    y = graph.get_tensor_by_name('y:0')
    y_ = graph.get_tensor_by_name('Softmax:0')


def extract_feature(file_name):
    audio, sample_rate = librosa.load(file_name)
    stft = np.abs(librosa.stft(audio))
    mfccs = np.mean(librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40).T, axis=0)
    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
    mel = np.mean(librosa.feature.melspectrogram(audio, sr=sample_rate).T, axis=0)
    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T, axis=0)
    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(audio), sr=sample_rate).T, axis=0)
    return mfccs, chroma, mel, contrast, tonnetz


def classify(audio_path):
    if not os.path.exists(audio_path):
        print('Sample file does not exist')
        return

    global x, y, y_, graph, sess
    ft = extract_feature(audio_path)
    features = []
    for f in ft:
        features.extend(f)

    if sess is None:
        print('Model not loaded, please use load_model function before')
        return

    features = np.array([features], dtype=np.float32)
    res = sess.run(tf.argmax(y_, 1), feed_dict={x: features})
    return res[0]


def load_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_dir', '-md', type=str, help='Model directory', default='./model')
    parser.add_argument('sample', type=str, help='Sample file to classify')
    return parser.parse_args()


def main():
    args = load_args()

    print('Loading model...')
    load_model(args.model_dir)
    print('Running classification')
    c = classify(args.sample)
    print('Sample classified as', c)


if __name__ == "__main__":
    main()
