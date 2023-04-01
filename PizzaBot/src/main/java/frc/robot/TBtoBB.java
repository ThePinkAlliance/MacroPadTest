package frc.robot;

import edu.wpi.first.networktables.GenericEntry;
import edu.wpi.first.wpilibj.shuffleboard.BuiltInWidgets;
import edu.wpi.first.wpilibj.shuffleboard.Shuffleboard;
import edu.wpi.first.wpilibj.shuffleboard.ShuffleboardTab;
import edu.wpi.first.wpilibj.shuffleboard.SimpleWidget;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;

public class TBtoBB {

    private ShuffleboardTab tab;
   
    private GenericEntry tb1;
    private GenericEntry tb2;
    
    public TBtoBB(){
       
        ShuffleboardTab tab = Shuffleboard.getTab("ChargeUp");
    
        tb1 = tab.add("tb1", false)
        .withWidget(BuiltInWidgets.kToggleButton)
        .getEntry();
        tb2 = tab.add("tb2", false)
        .withWidget(BuiltInWidgets.kToggleButton)
        .getEntry();
        System.out.println("TBtoBB run");
    }    

    public void putStuff(){
        tb1.setBoolean(false);
        tb2.setBoolean(false);
        System.out.println("PutStuff run");
    }
    
    public void periodic(){
        boolean tb1IsToggled = tb1.getBoolean(false);
        boolean tb2IsToggled = tb2.getBoolean(false);
        SmartDashboard.putBoolean("bb1", tb1IsToggled);
        SmartDashboard.putBoolean("bb2", tb2IsToggled);
    }
}
