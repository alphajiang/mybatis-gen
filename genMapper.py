


class GenRoMapper(object) :
    def __init__(self, entity, outDir):
        self.entity = entity
        self.outDir = outDir

    def gen(self) :
        out = self._genImport()
        out = out + self._genClazz()
        self._writeFile(out)
    


    def _genImport(self):
        out = 'package ' + self.entity.packageName + '.ro.' + self.entity.moduleName + '.mapper;\r\n\r\n\
import ' + self.entity.packageName + '.' + self.entity.moduleName + '.po.' + self.entity.clazzName + 'Po;\r\n\
import io.swagger.annotations.ApiModelProperty;\r\n\
import org.apache.ibatis.annotations.Mapper;\r\n\
import org.apache.ibatis.annotations.Param;\r\n\
import java.math.BigDecimal;\r\n\
import java.util.Date;\r\n\r\n'

        return out


    def _genClazz(self) :
        out = '@Mapper\r\n\
public interface ' + self.entity.clazzName + 'RoMapper {\r\n\r\n'


        if self.entity.keyCol :
            out = out + '\t' + self.entity.poClazz() + ' getById(@Param("id") \
' + self.entity.getColJavaType(self.entity.keyCol) + ' ' + self.entity.keyCol + ');'
        out = out + '\r\n}\r\n'
        return out

    def _writeFile(self, content) :
        fileName = self.outDir + "/ro/" + self.entity.clazzName + "RoMapper.java"
        with open(fileName, 'w') as f :
            f.write(content)



class GenRwMapper(object) :
    def __init__(self, entity, outDir):
        self.entity = entity
        self.outDir = outDir

    def gen(self) :
        out = self._genImport()
        out = out + self._genClazz()
        self._writeFile(out)
    


    def _genImport(self):
        out = 'package ' + self.entity.packageName + '.rw.' + self.entity.moduleName + '.mapper;\r\n\r\n\
import ' + self.entity.packageName + '.' + self.entity.moduleName + '.po.' + self.entity.clazzName + 'Po;\r\n\
import io.swagger.annotations.ApiModelProperty;\r\n\
import org.apache.ibatis.annotations.Mapper;\r\n\
import org.apache.ibatis.annotations.Param;\r\n\
import java.math.BigDecimal;\r\n\
import java.util.Date;\r\n\r\n'

        return out


    def _genClazz(self) :
        out = '@Mapper\r\n\
public interface ' + self.entity.clazzName + 'RwMapper {\r\n'

        # 生成 getById 函数
        if self.entity.keyCol :
            out = out + '\t' + self.entity.poClazz() + ' getById(@Param("id") \
' + self.entity.getColJavaType(self.entity.keyCol) + ' ' + self.entity.keyCol \
 + ', @Param("lock") boolean lock);\r\n\r\n'

        # 生成 insert 函数
        out = out + self._genFunInsert()
        out = out + '\r\n}\r\n'
        return out


    def _genFunInsert(self) :
        out = "\tint insert" + self.entity.clazzName + '('\
            + self.entity.poClazz() + ' ' + self.entity.poProp() + ');\r\n\r\n'
        return out

    def _writeFile(self, content) :
        fileName = self.outDir + "/rw/" + self.entity.clazzName + "RwMapper.java"
        with open(fileName, 'w') as f :
            f.write(content)

