#!/usr/bin/env python3


import sys,logging
from optparse import OptionParser
from dataSchema import DataSchema
from genRoot import GenRoot



logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("MyGen")

class MyGen(object) :
    def __init__(self, packageName, moduleName, dataSchema) :
        self.packageName = packageName
        self.moduleName = moduleName
        self.dataSchema = dataSchema

    def gen(self) :
        entityList = self.dataSchema.getTables()
        for entity in entityList :
            #log.debug(entity)
            javaGen = GenRoot(self.packageName, self.moduleName, entity)
            javaGen.genJavaCode()
            



def main() :
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("--host", dest="host", help="数据库地址, 如 127.0.0.1")
    parser.add_option("-d", "--db", dest="db", help="数据库名称如, ehc", default="ehc")
    parser.add_option("-u", "--username", dest="username", help="访问数据库的账号")
    parser.add_option("-p", "--password", dest="password", help="访问数据库密码")
    parser.add_option("-t", "--tables", dest="tables", help="数据库表,使用逗号分隔")
    parser.add_option("--package", dest="packageName", help="java包名")
    parser.add_option("--module", dest="moduleName", help="java模块名称")
    parser.add_option("-v", "--verbose", dest="verbose", help="verbose")
    parser.add_option("--email", dest="email", help="邮件通知")
    (options, args) = parser.parse_args(args=sys.argv)
    #print(options)
    if len(args) < 1:
        parser.error("参数错误")
    if options.verbose:
        print("reading %s..." % options.host)
    if options.host == None :
        print("缺少参数 host")
        return 1
    if options.username == None :
        print("缺少参数 username")
        return 2
    if options.password == None :
        print("缺少参数 -p")
        return 3

    dataSchema = DataSchema(dbHost = options.host,
        dbUsername = options.username,
        dbPassword = options.password,
        dbName = options.db,
        tables = options.tables)
    myGen = MyGen(options.packageName, options.moduleName, dataSchema)
    myGen.gen()
    # result = dbExport.export()
    result = True

    if result == True :
        return 0
    else :
        return 99

if  __name__ =='__main__':
    sys.exit(main())