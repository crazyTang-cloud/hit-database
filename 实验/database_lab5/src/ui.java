import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class ui {

    int index = 0;
    JButton btn1 = new JButton("选择");
    JButton btn2 = new JButton("选择");
    JButton btn3 = new JButton("选择");

    JLabel lbl1 = new JLabel("SELECT [ ENAME = ’Mary’ & DNAME = ’Research’ ] ( EMPLOYEE JOIN DEPARTMENT )");
    JLabel lbl2 = new JLabel("PROJECTION [ BDATE ] ( SELECT [ ENAME = ’John’ & DNAME = ’ Research’ ] ( EMPLOYEE JOIN DEPARTMENT ) )");
    JLabel lbl3 = new JLabel("SELECT [ ESSN = ’01’ ] (  PROJECTION [ ESSN, PNAME ] ( WORKS_ON JOIN PROJECT ) )");


    JList jList = new JList();
    JScrollPane jScrollPane = new JScrollPane(jList,ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS,ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
    DefaultListModel<String> defaultListModel = new DefaultListModel<>();

    public void show(){
        JFrame frame = new JFrame();
        JPanel panel;
        panel = (JPanel) frame.getContentPane();
        panel.setLayout(null);

        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        JLabel imageJLabel = new JLabel();
        // 获取屏幕大小
        int screenWidth = Toolkit.getDefaultToolkit().getScreenSize().width;
        int screenHeight = Toolkit.getDefaultToolkit().getScreenSize().height;
        // 设置窗体信息
        int frameWidth = 800;
        int frameHeight = 800;
        int frameX = (screenWidth - frameWidth) / 2;
        int frameY = (screenHeight - frameHeight) / 2;
        // 将窗体设置在屏幕中央
        frame.setBounds(frameX, frameY, frameWidth, frameHeight);
        imageJLabel.setBounds(0, 0, frame.getWidth(), frame.getHeight());
        frame.getLayeredPane().add(imageJLabel, Integer.MIN_VALUE);

        btn1.setFont(new Font("Dialog", Font.BOLD, 12));
        btn1.setBounds(10, 10, 60, 30);
        btn1.setBackground(new Color(224, 255, 255));
        panel.add(btn1);

        btn2.setFont(new Font("Dialog", Font.BOLD, 12));
        btn2.setBounds(10, 50, 60, 30);
        btn2.setBackground(new Color(224, 255, 255));
        panel.add(btn2);

        btn3.setFont(new Font("Dialog", Font.BOLD, 12));
        btn3.setBounds(10, 90, 60, 30);
        btn3.setBackground(new Color(224, 255, 255));
        panel.add(btn3);

        lbl1.setBounds(80, 10, 700, 30);
        lbl1.setFont(new Font("Dialog",Font.PLAIN,12));
        panel.add(lbl1);

        lbl2.setBounds(80, 50, 700, 30);
        lbl2.setFont(new Font("Dialog",Font.PLAIN,12));
        panel.add(lbl2);

        lbl3.setBounds(80, 90, 700, 30);
        lbl3.setFont(new Font("Dialog",Font.PLAIN,12));
        panel.add(lbl3);


        jList.setModel(defaultListModel);
        jList.setFont(new Font("Dialog", Font.BOLD, 24));
        jScrollPane.add(jList);
        jScrollPane.setBounds(10, 150, 760, 600);
        frame.add(jScrollPane);

        btn1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                defaultListModel.addElement("查询语句1：");
                String sql = lbl1.getText();

                analyze analyze = new analyze();

                syntaxTree tree = analyze.syntax(sql);
                printTree(tree);

                defaultListModel.addElement("优化结果：");
                ArrayList<String> cons = new ArrayList<>();
                syntaxTree tree1 = analyze.analyze(tree, cons);
                printTree(tree1);
            }
        });
        btn2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                defaultListModel.addElement("查询语句2：");
                String sql = lbl2.getText();

                analyze analyze = new analyze();

                syntaxTree tree = analyze.syntax(sql);
                printTree(tree);

                defaultListModel.addElement("优化结果：");
                ArrayList<String> cons = new ArrayList<>();
                syntaxTree tree1 = analyze.analyze(tree, cons);
                printTree(tree1);
            }
        });
        btn3.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                defaultListModel.addElement("查询语句3：");
                String sql = lbl3.getText();

                analyze analyze = new analyze();

                syntaxTree tree = analyze.syntax(sql);
                printTree(tree);

                defaultListModel.addElement("优化结果：");
                ArrayList<String> cons = new ArrayList<>();
                syntaxTree tree1 = analyze.analyze(tree, cons);
                printTree(tree1);
            }
        });

        jList.setModel(defaultListModel);
        panel.add(imageJLabel);
        panel.setOpaque(false);    //将内容面板设置为透明；背景图片位于内容面板下方
        jScrollPane.setViewportView(jList);
        frame.setVisible(true);
    }

    public void printTree(syntaxTree tree){
        String str = "";
        for(int i = 0;i < index;i++){
            str +=" ";
        }
        if(tree.getOp()!=null && tree.getOp()!=""){
            if(tree.getCon()!=null)
                defaultListModel.addElement(str+tree.getOp()+" "+tree.getCon());
            else
                defaultListModel.addElement(str+tree.getOp());
            //System.out.println(defaultListModel);
//            jList.setModel(defaultListModel);
        }
        else{
            defaultListModel.addElement(str+tree.getAttr().replace(")",""));
            //System.out.println(defaultListModel);
//            jList.setModel(defaultListModel);
        }
        if(tree.getLeft() != null){
            index += 2;
            printTree(tree.getLeft());
            index -=2;
        }
        if(tree.getRight() != null){
            index += 2;
            printTree(tree.getRight());
            index -=2;
        }
    }

    public static void main(String[] arg0){
        ui ui = new ui();
        ui.show();
    }
}
