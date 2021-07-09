public class syntaxTree {
    private syntaxTree left;
    private syntaxTree right;
    private String op;//SELECT PROJECTION JOIN
    private String con;//条件
    private String attr;//二元运算的左右属性

    public syntaxTree getLeft() {
        return left;
    }

    public void setLeft(syntaxTree left) {
        this.left = left;
    }

    public syntaxTree getRight() {
        return right;
    }

    public void setRight(syntaxTree right) {
        this.right = right;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public String getCon() {
        return con;
    }

    public void setCon(String con) {
        this.con = con;
    }

    public String getAttr() {
        return attr;
    }

    public void setAttr(String attr) {
        this.attr = attr;
    }
}
