#!/bin/bash
#脚本sh和py放到bupt-rtos根目录前一级
cd ./RTOS # 替换为bupt-rtos根目录名字
make LLVM=1 -j80 2> t1
mv t1 ../
cd ..
python3 ./finderr.py t1
cat ./result
rm ./t1
echo "finish"