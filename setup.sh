#!/bin/bash
sqlacodegen --outfile=./model/schema.py mysql://root:123456@127.0.0.1:3306/school?charset=utf8
sed -i 's/TAddres(/TAddress(/g' ./model/schema.py
sed -i 's/TUserWithdrawStatu/TUserWithdrawStatus/g' ./model/schema.py
sed -i 's/TPackageExpres/TPackageExpress/g' ./model/schema.py
python tools/generate.py

