myloc=$(realpath "$0" | sed 's|\(.*\)/.*|\1|')
source $myloc/env/bin/activate
python3 $myloc/SQLsuma.py -i 1 -n QN
