import java.util.Arrays;
import java.util.List;

public class analyze {

    database db;

    public analyze() {
        db = new database();
    }

    public syntaxTree syntax(String sql){
        String[] sql_split = sql.split(" ");
        syntaxTree tree = new syntaxTree();
        int i = 0;
        int length = sql_split.length;
        while(i < length){
            if (sql_split[i].equals("SELECT") || sql_split[i].equals("PROJECTION")){
                tree.setOp(sql_split[i]);
                i = i +2;
                String condition = "";
                while(!sql_split[i].equals("]")){
                    condition += sql_split[i];
                    i++;
                }
                tree.setCon(condition);
                i++;
            }
            else if(sql_split[i].equals("JOIN")){
                tree.setOp(sql_split[i]);
                syntaxTree left = new syntaxTree();
                left.setAttr(sql_split[i-1]);
                syntaxTree right = new syntaxTree();
                right.setAttr(sql_split[i+1]);

                tree.setLeft(left);
                tree.setRight(right);

                i = i+2;
            }
            else if(sql_split[i].equals("(")){
                i = i+1;
                String inner_sql = "";
                while(i < length && !sql_split[i].equals(")")){
                    inner_sql += sql_split[i]+" ";
                    i++;
                }
                i++;
                tree.setLeft(syntax(inner_sql));
            }
            else{
                i++;
            }
        }
        return tree;
    }

    public syntaxTree analyze(syntaxTree tree, List<String> cons){
        if(tree.getOp().equals("SELECT")){
            cons = Arrays.asList(tree.getCon().split("&"));
            tree = analyze(tree.getLeft(),cons);
        }
        else if(tree.getOp().equals("JOIN")){
            if(cons.size()==0){
                return tree;
            }
            syntaxTree left = new syntaxTree();
            left.setOp("SELECT");
            left.setCon(cons.get(0));
            List<String> con0 = Arrays.asList(cons.get(0).split("="));
            List<String> s = db.fromWhere(con0.get(0));
            if(tree.getRight().getAttr()!=null&&tree.getRight().getAttr()!=null){
                if(s.contains(tree.getRight().getAttr())&&!s.contains(tree.getLeft().getAttr())){
                    syntaxTree tempTree;
                    tempTree = tree.getRight();
                    tree.setRight(tree.getLeft());
                    tree.setLeft(tempTree);
                }
            }
            left.setLeft(tree.getLeft());
            tree.setLeft(left);
            if(cons.size()==2){
                syntaxTree right = new syntaxTree();
                right.setOp("SELECT");
                right.setCon(cons.get(1));
                List<String> con1 = Arrays.asList(cons.get(1).split("="));
                List<String> s1 = db.fromWhere(con1.get(0));
                if(tree.getLeft().getAttr()!=null&&tree.getRight().getAttr()!=null){
                    if(!s1.contains(tree.getRight().getAttr())&&s1.contains(tree.getLeft().getAttr())){
                        syntaxTree tempTree;
                        tempTree = tree.getRight();
                        tree.setRight(tree.getLeft());
                        tree.setLeft(tempTree);
                    }
                }

                right.setLeft(tree.getRight());
                tree.setRight(right);
            }
        }
        else if(tree.getOp().equals("PROJECTION")){
            tree.setLeft(analyze(tree.getLeft(),cons));
        }
        return tree;
    }

}
