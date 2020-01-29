#
# This class was adapted to implement imread and imresize
# because these functions were deprecated !
#
from glob import glob
import numpy as np


class DataLoader():
    def __init__(self, dataset_name, img_res=(128, 128)):
        self.dataset_name = dataset_name
        self.img_res = img_res

    def load_data(self, domain, batch_size=1, is_testing=False):
        data_type = "train%s" % domain if not is_testing else "test%s" % domain
        path = glob('./datasets/%s/%s/*' % (self.dataset_name, data_type))

        batch_images = np.random.choice(path, size=batch_size)

        imgs = []
        for img_path in batch_images:
            img = self.imread(img_path)
            if not is_testing:
                img = self.imresize(img, self.img_res)

                if np.random.random() > 0.5:
                    img = np.fliplr(img)
            else:
                img = self.imresize(img, self.img_res)
            imgs.append(img)
        imgs = np.array(imgs) / 127.5 - 1.

        return imgs

    def load_batch(self, batch_size=1, is_testing=False):
        data_type = "train" if not is_testing else "val"
        path_A = glob('./datasets/%s/%sA/*' % (self.dataset_name, data_type))
        path_B = glob('./datasets/%s/%sB/*' % (self.dataset_name, data_type))

        self.n_batches = int(min(len(path_A), len(path_B)) / batch_size)
        total_samples = self.n_batches * batch_size

        # Sample n_batches * batch_size from each path list so that model
        # sees all samples from both domains
        path_A = np.random.choice(path_A, total_samples, replace=False)
        path_B = np.random.choice(path_B, total_samples, replace=False)

        for i in range(self.n_batches - 1):
            batch_A = path_A[i * batch_size:(i + 1) * batch_size]
            batch_B = path_B[i * batch_size:(i + 1) * batch_size]
            imgs_A, imgs_B = [], []
            for img_A, img_B in zip(batch_A, batch_B):
                img_A = self.imread(img_A)
                img_B = self.imread(img_B)

                img_A = self.imresize(img_A, self.img_res)
                img_B = self.imresize(img_B, self.img_res)

                if not is_testing and np.random.random() > 0.5:
                        img_A = np.fliplr(img_A)
                        img_B = np.fliplr(img_B)

                imgs_A.append(img_A)
                imgs_B.append(img_B)

            imgs_A = np.array(imgs_A) / 127.5 - 1.
            imgs_B = np.array(imgs_B) / 127.5 - 1.

            yield imgs_A, imgs_B

    def imresize(self, img, size):
        """workaroung imresize"""
        from PIL import Image
        im = Image.fromarray(np.asarray(img).astype(np.uint8))
        new_image = np.array(im.resize(size, Image.BICUBIC))
        return new_image

    def load_img(self, path):
        print("load_img")
        img = self.imread(path)
        print(type(img), img.shape)

        # scipy.misc.imresize is deprecated!
        # imresize is deprecated in SciPy 1.0.0, and will be removed in 1.3.0
        # img = scipy.misc.imresize(img, self.img_res)
        img = self.imresize(img, self.img_res)
        img = img / 127.5 - 1.
        return img[np.newaxis, :, :, :]

    def imread(self, path):
        # imread is deprecated!
        # imread is deprecated in SciPy 1.0.0, and will be removed in 1.2.0.
        # return scipy.misc.imread(path, mode='RGB').astype(np.float)

        import imageio
        return imageio.imread(path, pilmode='RGB').astype(np.float)
