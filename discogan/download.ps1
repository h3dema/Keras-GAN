mkdir datasets

# valid: cityscapes, edges2handbags, edges2shoes
$FILE="edges2shoes"

$URL="https://people.eecs.berkeley.edu/~tinghuiz/projects/pix2pix/datasets/$FILE.tar.gz"
$ZIP_FILE="./datasets/$FILE.zip"
$TARGET_DIR="./datasets/"

mkdir $TARGET_DIR

wget --no-check-certificate -N -c $URL -O $ZIP_FILE

Expand-Archive -Path $ZIP_FILE -DestinationPath $TARGET_DIR
rm $ZIP_FILE