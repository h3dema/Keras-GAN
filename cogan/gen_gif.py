import imageio
import glob

images = []
filenames = glob.glob("images/*.png")
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('cogan.gif', images)
