使用数据库的create table语句生成出mybatis相关代码

需要安装pymysql
```
pip3 install pymysql
```

使用示例
```
rm -rf out
python3 myGen.py --host=127.0.0.1 -u user -p password -d db_abcd -t "t_table_name" --package="com.aaa.bbb" --module="bbb" \
    --modelPackage="com.aaa.bbb.model.aaa" --dsPackage='com.aaa.bbb.ds.aaa'
```