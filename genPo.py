


class GenPo(object) :
    def __init__(self, entity, outDir):
        self.entity = entity
        self.outDir = outDir

    def gen(self) :
        out = self._genImport()
        out = out + self._genClazz()
        self._writeFile(out)
    


    def _genImport(self):
        out = 'package ' + self.entity.modelPackage + '.' + self.entity.moduleName + '.po;\r\n\r\n\
import io.swagger.annotations.ApiModel;\r\n\
import io.swagger.annotations.ApiModelProperty;\r\n\
import javax.validation.constraints.NotNull;\r\n\
import javax.validation.constraints.Size;\r\n\
import lombok.Data;\r\n\
import lombok.experimental.Accessors;\r\n\
import java.math.BigDecimal;\r\n\
import java.util.Date;\r\n\r\n'

        return out


    def _genClazz(self) :
        out = '@Data\r\n\
@Accessors(chain = true)\r\n\
@ApiModel(value = "' + self.entity.clazzComment + '")\r\n\
public class ' + self.entity.poClazz() + ' {\r\n\r\n'
        for col in self.entity.colList :
            if col.comment != '' :
                out = out + '\t@ApiModelProperty(value = "' + col.comment.replace('"', '\\"') + '")\r\n'
            if col.nullable == False :
                out = out + '\t@NotNull(message = "' + col.name + ' 不能为 null")\r\n'
            if col.maxLen :
                out = out + '\t@Size(max = ' + col.maxLen + ', message = "' + col.name + ' 长度不能超过 ' + col.maxLen + '")\r\n'
            out = out + '\tprivate ' + col.javaType + ' ' + col.name + ';\r\n\r\n'
        out = out + '\r\n}\r\n'
        return out

    def _writeFile(self, content) :
        fileName = self.outDir + "/" + self.entity.clazzName + "Po.java"
        with open(fileName, 'w') as f :
            f.write(content)