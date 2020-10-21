#!/usr/bin/env python3


import sys,logging
from optparse import OptionParser
import configparser
from dataSchema import DataSchema
from genRoot import GenRoot,GenSplitRoot



logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("MyGen")

class MyGen(object) :
    def __init__(self, splitRw, decimalType, packageName, moduleName, modelPackage, dsPackage, dataSchema) :
        self.splitRw = splitRw
        self.decimalType = decimalType
        self.packageName = packageName
        self.moduleName = moduleName
        self.modelPackage = modelPackage
        self.dsPackage = dsPackage
        self.dataSchema = dataSchema

    def gen(self) :
        entityList = self.dataSchema.getTables()
        for entity in entityList :
            #log.debug(entity)
            if self.splitRw == 'true':
                javaGen = GenSplitRoot(self.packageName, self.moduleName, self.modelPackage, self.dsPackage, self.decimalType, entity)
                javaGen.genJavaCode()
            else:
                javaGen = GenRoot(self.packageName, self.moduleName, self.modelPackage, self.dsPackage, self.decimalType, entity)
                javaGen.genJavaCode()
            



def main() :
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-c", "--cfg", dest="cfg", help="配置文件如, my.cfg", default="my.cfg")
    (options, args) = parser.parse_args(args=sys.argv)
    #print(options)

    cfg = configparser.ConfigParser()
    cfg.read(options.cfg)

    dataSchema = DataSchema(dbHost = cfg.get("DB", "ip"),
        dbPort = cfg.getint("DB", "port"),
        dbUsername = cfg.get("DB", "username"),
        dbPassword = cfg.get("DB", "password"),
        dbName = cfg.get("DB", "database"),
        tables = cfg.get("DB", "tables"),
        decimalType = cfg.get("JAVA", "decimalType"))
    myGen = MyGen(splitRw = cfg.get("JAVA", "read_write_splitting"),
        decimalType = cfg.get("JAVA", "decimalType"),
        packageName = cfg.get("JAVA", "package"), 
        moduleName = cfg.get("JAVA", "module"),
        modelPackage = cfg.get("JAVA", "model"), 
        dsPackage = cfg.get("JAVA", "ds"), 
        dataSchema = dataSchema)
    myGen.gen()
    # result = dbExport.export()
    result = True

    if result == True :
        return 0
    else :
        return 99

if  __name__ =='__main__':
    sys.exit(main())