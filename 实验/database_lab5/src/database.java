import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class database {
    private List<String> employee = Arrays.asList(new String[]{"ESSN", "ENAME", "DNO"});
    private List<String> department = Arrays.asList(new String[]{"DNO", "DNAME"});
    private List<String> project = Arrays.asList(new String[]{"PNAME", "PNO","DNO"});
    private List<String> works_on = Arrays.asList(new String[]{"ESSN", "PNO"});


    public List<String> fromWhere(String str){
        List<String> list = new ArrayList<>();
        if(employee.contains(str)){
            list.add("EMPLOYEE");
        }
        if(department.contains(str)){
            list.add("DEPARTMENT");
        }
        if(project.contains(str)){
            list.add("PROJECT");
        }
        if(works_on.contains(str)){
            list.add("WORKS_ON");
        }
        return list;
    }
}
