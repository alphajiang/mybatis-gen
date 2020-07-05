#!/usr/bin/env python3

import pymysql.cursors
import logging
from dbEntity import DbEntity,DbColumn


log = logging.getLogger("dataSchema")

# 解析数据库create table语句,生成出数据对象
class DataSchema(object) :
    def __init__(self, dbHost, dbUsername, dbPassword, dbName, tables) :
        self.dbConn = None
        self.cursor = None
        self.dbHost = dbHost
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
        log.debug(">> host = " + self.dbHost + ", db = " + self.dbName + ", username = " + self.dbUsername)
        self.dbConn = pymysql.connect(host=self.dbHost,
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
        clazzName = "".join(map(lambda x:x.capitalize(), tableName.strip("t_").split("_")))
        clazzComment = ""
        colList = []
        for line in tableSchema.splitlines() :
            line = line.strip()
            if line.startswith("CREATE TABLE") :
                pass
            elif line.startswith(")") :
                clazzComment = self._parseEndLine(line)
            elif line.startswith("UNIQUE") :
                pass
            elif line.startswith("PRIMARY") :
                pass
            else :
                col = self._parseTableColumnLine(line)
                colList.append(col)

        dbEntity = DbEntity(clazzName, clazzComment, colList)
        return dbEntity


    def _parseTableColumnLine(self, line) :
        name = None
        items = line.split(" ")
        name = items[0]
        name = name.strip("`")
        type = items[1]
        if type.startswith("int") :
            type = "Integer"
        elif type.startswith("tinyint") :
            type = "Integer"
        elif type.startswith("bigint") :
            type = "Long"
        elif type.startswith("decimal") :
            type = "BigDecimal"
        elif type.startswith("varchar") :
            type = "String"
        elif type.startswith("text") :
            type = "String"
        elif type.startswith("datetime") :
            type = "Date"
        elif type.startswith("date") :
            type = "Date"
        elif type.startswith("timestamp") :
            type = "Date"
        
        comment = ""
        for idx in range(len(items)) :
            #print(idx)
            if items[idx] == "COMMENT" :
                comment = items[idx +1].strip(",").strip("'")
                break
        #log.debug(name)
        #log.debug(type)
        #log.debug(comment)
        dbCol = DbColumn(name, type, comment)
        return dbCol

    def _parseEndLine(self, line) :
        items = line.split(" ")
        for item in items :
            
            if item.startswith("COMMENT=") :
                return item.strip("COMMENT=").strip("'")
        return ""