


import os,logging
from genPo import GenPo
from genMapper import GenRoMapper,GenRwMapper
from genMapperXml import GenRoMapperXml,GenRwMapperXml
from genDs import GenRoDs,GenRwDs


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("GenRoot")



class GenRoot(object) :
    def __init__(self, packageName, moduleName, modelPackage, dsPackage, decimalType, entity) :
        self.packageName = packageName
        self.moduleName = moduleName
        self.modelPackage = modelPackage
        self.dsPackage = dsPackage
        self.decimalType = decimalType

        self.entity = entity
        self.entity.packageName = packageName
        self.entity.moduleName = moduleName
        self.entity.modelPackage = modelPackage
        self.entity.dsPackage = dsPackage
        #self.entity.fullPo()
        self.outDirRoot = "out"
        self.outDirPo = "out/po"
        self.outDirMapper = "out/mapper"
        self.outDirDs = "out/ds"



    def genJavaCode(self):
        log.debug(self.entity)
        self.entity.splitRead(False)
        self._mkdir()
        po = GenPo(self.entity, self.outDirPo)
        po.gen()


        rwMapper = GenRwMapper(self.entity, self.outDirMapper, False)
        rwMapper.gen()
        rwMapperXml = GenRwMapperXml(self.entity, self.outDirMapper, False)
        rwMapperXml.gen()
        rwDs = GenRwDs(entity = self.entity, outDir = self.outDirDs, splitRead = False)
        rwDs.gen()

    def _mkdir(self) :
        if not os.path.isdir(self.outDirRoot) :
            os.mkdir(self.outDirRoot)
        if not os.path.isdir(self.outDirPo) :
            os.mkdir(self.outDirPo)
        if not os.path.isdir(self.outDirMapper) :
            os.mkdir(self.outDirMapper)
        if not os.path.isdir(self.outDirDs) :
            os.mkdir(self.outDirDs)         



class GenSplitRoot(object) :
    def __init__(self, packageName, moduleName, modelPackage, dsPackage, decimalType, entity) :
        self.packageName = packageName
        self.moduleName = moduleName
        self.modelPackage = modelPackage
        self.dsPackage = dsPackage
        self.decimalType = decimalType

        self.entity = entity
        self.entity.packageName = packageName
        self.entity.moduleName = moduleName
        self.entity.modelPackage = modelPackage
        self.entity.dsPackage = dsPackage
        #self.entity.fullPo()
        self.outDirRoot = "out"
        self.outDirPo = "out/po"
        self.outDirMapper = "out/mapper"
        self.outDirDs = "out/ds"



    def genJavaCode(self):
        log.debug(self.entity)
        self.entity.splitRead(True)
        self._mkdir()
        po = GenPo(self.entity, self.outDirPo)
        po.gen()


        roMapper = GenRoMapper(self.entity, self.outDirMapper)
        roMapper.gen()
        roMapperXml = GenRoMapperXml(self.entity, self.outDirMapper)
        roMapperXml.gen()
        roDs = GenRoDs(entity = self.entity, outDir = self.outDirDs)
        roDs.gen()



        rwMapper = GenRwMapper(self.entity, self.outDirMapper, True)
        rwMapper.gen()
        rwMapperXml = GenRwMapperXml(self.entity, self.outDirMapper, True)
        rwMapperXml.gen()
        rwDs = GenRwDs(entity = self.entity, outDir = self.outDirDs, splitRead = True)
        rwDs.gen()

    def _mkdir(self) :
        if not os.path.isdir(self.outDirRoot) :
            os.mkdir(self.outDirRoot)
        if not os.path.isdir(self.outDirPo) :
            os.mkdir(self.outDirPo)
        if not os.path.isdir(self.outDirMapper) :
            os.mkdir(self.outDirMapper)
        if not os.path.isdir(self.outDirMapper + "/ro") :
            os.mkdir(self.outDirMapper + "/ro")
        if not os.path.isdir(self.outDirMapper + "/rw") :
            os.mkdir(self.outDirMapper + "/rw")
        if not os.path.isdir(self.outDirDs) :
            os.mkdir(self.outDirDs)
        if not os.path.isdir(self.outDirDs + "/ro") :
            os.mkdir(self.outDirDs + "/ro")
        if not os.path.isdir(self.outDirDs + "/rw") :
            os.mkdir(self.outDirDs + "/rw")            



