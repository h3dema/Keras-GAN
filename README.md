<p align="center">
    <img src="assets/keras_gan.png" width="480"\>
</p>

## Keras-GAN
Collection of Keras implementations of Generative Adversarial Networks (GANs) suggested in research papers. These models are in some cases simplified versions of the ones ultimately described in the papers, but I have chosen to focus on getting the core ideas covered instead of getting every layer configuration right. Contributions and suggestions of GAN varieties to implement are very welcomed.

<b>See also:</b> [The original Keras-GAN](https://github.com/eriklindernoren/Keras-GAN)

## Table of Contents
  * [Installation](#installation)
  * [Implementations](#implementations)
    + [Auxiliary Classifier GAN](acgan/README.MD)
    + [Adversarial Autoencoder](aae/README.MD)
    + [Bidirectional GAN](bigan/README.MD)
    + [Boundary-Seeking GAN](bgan/README.MD)
    + [Conditional GAN](cgan/README.MD)
    + [Context-Conditional GAN](ccgan/README.MD)
    + [Context Encoder](context-encoder/README.MD)
    + [Coupled GANs](cogan/README.MD)
    + [CycleGAN](cyclegan/README.MD)
    + [Deep Convolutional GAN](dcgan/README.MD)
    + [DiscoGAN](#discogan)
    + [DualGAN](#dualgan)
    + [Generative Adversarial Network](#gan)
    + [InfoGAN](#infogan)
    + [LSGAN](#lsgan)
    + [Pix2Pix](#pix2pix)
    + [PixelDA](#pixelda)
    + [Semi-Supervised GAN](#sgan)
    + [Super-Resolution GAN](#srgan)
    + [Wasserstein GAN](#wgan)
    + [Wasserstein GAN GP](#wgan-gp)

## Installation
    $ git clone https://github.com/h3dema/Keras-GAN.git
    $ cd Keras-GAN/
    $ sudo pip3 install -r requirements.txt


## Running the code

The code is in the folder indicated above.

```
$ cd Keras-GAN/
$ jupyter notebook
```

In the web page that jupyter opens, you can browser each folder, and run the notebook.
