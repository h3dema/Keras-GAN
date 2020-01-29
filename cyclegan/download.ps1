mkdir datasets

$FILE="apple2orange"

$URL="https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/$FILE.zip"
$ZIP_FILE="./datasets/$FILE.zip"
$TARGET_DIR="./datasets/"

mkdir $TARGET_DIR

wget --no-check-certificate -N -c $URL -O $ZIP_FILE

Expand-Archive -Path $ZIP_FILE -DestinationPath $TARGET_DIR
rm $ZIP_FILE