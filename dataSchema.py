#!/usr/bin/env python3

import pymysql.cursors
import re,logging
from dbEntity import DbEntity,DbColumn


log = logging.getLogger("dataSchema")

# 解析数据库create table语句,生成出数据对象
class DataSchema(object) :
    def __init__(self, dbHost, dbPort, dbUsername, dbPassword, dbName, tables) :
        self.dbConn = None
        self.cursor = None
        self.dbHost = dbHost
        self.dbPort = dbPort
        self.dbUsername = dbUsername
        self.dbPassword = dbPassword
        self.dbName = dbName
        self.tables = tables


    def getTables(self) :
        entityList = []
        try :
            self._connect()
            with self.dbConn.cursor() as cursor:
                self.cursor = cursor
                #return self.listValidationSql()
            #    return cursor
                for t in self.tables.split(',') :
                    entity = self._getTable(t)
                    entityList.append(entity)
        finally:
            if self.dbConn != None :
                self.dbConn.close()
        return entityList
        
    def _connect(self) :
        log.debug(">> host = " + self.dbHost + ", port = " + str(self.dbPort) + ", db = " + self.dbName + ", username = " + self.dbUsername)
        self.dbConn = pymysql.connect(host=self.dbHost,
                                 port=self.dbPort,
                                 user=self.dbUsername,
                                 password=self.dbPassword,
                                 db=self.dbName,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)



    def _getTable(self, tableName) :
        log.debug(tableName)
        sql = "show create table " + tableName
        log.debug("sql : " + sql)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result != None and len(result) > 0 :
#            print(result)
            tableSchema = result['Create Table']
            # print(tableSchema)
            dbEntity = self._parseTable(tableName, tableSchema)
            return dbEntity
        else :
            log.error("ERROR: 获取表结构失败!!!!")
#        pass

    def _parseTable(self, tableName, tableSchema) :
        log.debug(tableSchema)
        # 下划线转驼峰
        clazzName = "".join(map(lambda x:x.capitalize(), tableName.lstrip("t_").split("_")))
        clazzComment = ""
        keyCol = None
        colList = []
        for line in tableSchema.splitlines() :
            line = line.strip()
            if line.startswith("CREATE TABLE") :
                pass
            elif line.startswith(")") :
                clazzComment = self._parseEndLine(line)
            elif line.startswith("UNIQUE") :
                pass
            elif line.startswith("KEY") :
                pass
            elif line.startswith("PRIMARY KEY") :
                keyCol = self._parsePrimaryKey(line)
            else :
                col = self._parseTableColumnLine(line)
                colList.append(col)

        dbEntity = DbEntity(tableName, clazzName, clazzComment, keyCol, colList)
        return dbEntity


    def _parseTableColumnLine(self, line) :
        name = None
        items = line.split(" ")
        name = items[0]
        name = name.strip("`")
        jdbcType = items[1]
        javaType = jdbcType
        maxLen = None
        if jdbcType.startswith("int") :
            javaType = "Integer"
            jdbcType = "INTEGER"
        elif jdbcType.startswith("tinyint(1)") :
            javaType = "Boolean"
            jdbcType = "BOOLEAN"
        elif jdbcType.startswith("tinyint") or jdbcType.startswith("smallint") :
            javaType = "Integer"
            jdbcType = "INTEGER"
        elif jdbcType.startswith("bigint") :
            javaType = "Long"
            jdbcType = "BIGINT"
        elif jdbcType.startswith("decimal") :
            javaType = "BigDecimal"
            jdbcType = "DECIMAL"
        elif jdbcType.startswith("varchar") :
            javaType = "String"
            jdbcType = "VARCHAR"
        elif jdbcType.startswith("text") :
            javaType = "String"
            jdbcType = "LONGVARCHAR"
        elif jdbcType.startswith("datetime") :
            javaType = "Date"
            jdbcType = "DATE"
        elif jdbcType.startswith("date") :
            javaType = "Date"
            jdbcType = "DATE"
        elif jdbcType.startswith("timestamp") :
            javaType = "Date"
            jdbcType = "TIMESTAMP"
        
        comment = ""
        for idx in range(len(items)) :
            #print(idx)
            if items[idx] == "COMMENT" :
                pt = re.compile("COMMENT \'(.+)\'")
                comment = pt.findall(line)[0]
                # comment = items[idx +1].strip(",").strip("'")
                # log.debug("xxxxxxxxxxxxxxxxxxx")
                # log.debug(comment)
                break
        #log.debug(name)
        #log.debug(type)
        #log.debug(comment)
        nullable = re.search(r'NOT NULL', line) == None
        if(javaType == 'String') :
            pt = re.compile('varchar\((\d+)\)')
            maxLenRet = pt.findall(line)
            if maxLenRet : 
                maxLen = maxLenRet[0]
        dbCol = DbColumn(name, javaType, jdbcType, comment, nullable, maxLen)
        return dbCol

    def _parsePrimaryKey(self, line):
        key = line.split(' ')[-1]
        key = re.sub('[()\,`]', '', key)
        return key

    def _parseEndLine(self, line) :
        items = line.split(" ")
        for item in items :
            
            if item.startswith("COMMENT=") :
                return item.strip("COMMENT=").strip("'")
        return ""
