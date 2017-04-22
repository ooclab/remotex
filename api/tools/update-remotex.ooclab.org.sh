#!/bin/sh

# -v, --verbose 详细模式输出
# -q, --quiet 精简输出模式
# -c, --checksum 打开校验开关，强制对文件传输进行校验
# -a, --archive 归档模式，表示以递归方式传输文件，并保持所有文件属性，等于-rlptgoD
# -r, --recursive 对子目录以递归模式处理
# -l, --links 保留软链结
# -L, --copy-links 想对待常规文件一样处理软链结
# --copy-unsafe-links 仅仅拷贝指向SRC路径目录树以外的链结
# --safe-links 忽略指向SRC路径目录树以外的链结
# -H, --hard-links 保留硬链结
# -p, --perms 保持文件权限
# -o, --owner 保持文件属主信息
# -g, --group 保持文件属组信息
# -D, --devices 保持设备文件信息
# -t, --times 保持文件时间信息
# -S, --sparse 对稀疏文件进行特殊处理以节省DST的空间

## 注意: remotex 主机名是我在 ~/.ssh/config 里面配置:
# Host remotex
#     port 22
#     user root
#     Hostname 139.59.103.82
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
rsync -avz --delete --progress --filter='- *.pyc' --filter='- __pycache__' --filter='- .git*' $DIR/../ remotex:/srv/product/api/
