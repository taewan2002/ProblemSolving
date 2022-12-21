package HW_4;

public class Staff extends Employee{
    public int payGrade;

    public Staff(){
        super();
        payGrade = 0;
    }

    public Staff(String newName, String newDepartment, int newId, int newPayGrade){
        super(newName, newDepartment, newId);
        payGrade = newPayGrade;
    }

    public void reset(int newPayGrade){
        /** reset */
        payGrade = newPayGrade;
    }

    public void setPayGrade(int newPayGrade){
        /** set Paygrade */
        payGrade = newPayGrade;
    }

    public int getPayGrade(){
        /** get Paygrade */
        return payGrade;
    }
    
    public void writeOutput(){
        super.writeOutput(); // print name, department, id
        System.out.println("pay grade: " + getPayGrade());
    }
}
