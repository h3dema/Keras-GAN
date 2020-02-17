mkdir datasets

# valid: cityscapes, edges2handbags, edges2shoes
$FILE="edges2shoes"

$URL="https://people.eecs.berkeley.edu/~tinghuiz/projects/pix2pix/datasets/$FILE.tar.gz"
$TAR_FILE="./datasets/$FILE.tar.gz"
$TARGET_DIR="./datasets/"

mkdir $TARGET_DIR
wget --no-check-certificate -N -c $URL -O $TAR_FILE
tar -xvzf $TAR_FILE
rm $TAR_FILE