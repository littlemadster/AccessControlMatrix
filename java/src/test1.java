/******************************************************************************
 * Title: 				Login driver
 * Author: 				Youssif Al-Nashif
 * Email: 				yalnashif@floridapoly.edu
 * Package: 				N/A
 * Version: 				0.0.1a
 * Creation Date: 		Oct. 15, 2017 @ 22:10
 * Modification Date: 	Oct. 15, 2017 @ 22:10
 * Description:
 ******************************************************************************/

import login.*;

public class test1 {

    public static void main(String[] args) {


        /***************************************************
         * Always have one of the following two lines commented
         ***************************************************/
//        String[] roles = {"Admin", "User"};
        String[] roles = {};

        /***************************************************
         * Create Database ./test.sqlite
         ***************************************************/
//        loginSQLiteDB.createSQLiteDB("./test.sqlite");

        /***************************************************
         * Create User Table in database ./test.sqlite
         ***************************************************/
//        loginSQLiteDB.createSQLiteLoginTable("./test.sqlite");

        /***************************************************
         * Create Sample User John Smith in the table
         ***************************************************/
//        loginSQLiteDB.createSQLiteLoginUser("./test.sqlite","John" ,"Smith", "jsmith","test123");



        /***************************************************
         * Login Dialog. return null: cancel clicked in login dialog
         ***************************************************/
        String[] returned = loginDialog.loginDialogOpen("Login", roles);

        /***************************************************
         * Uncomment the if-block below to check returned value
         ***************************************************/
//        if (returned != null) {
//            if (returned.length == 3) {
//                System.out.println(returned[0]);
//                System.out.println(returned[1]);
//                System.out.println(returned[2]);
//            } else if (returned.length == 2) {
//                System.out.println(returned[0]);
//                System.out.println(returned[1]);
//            }
//
//        }


        /***************************************************
         * Check if user exist in table. return null: user not found
         ***************************************************/
        String[] userInfo = loginSQLiteDB.checkSQLiteLoginUser("./test.sqlite", returned[0], returned[1]);


        /***************************************************
         * Uncomment the following if-block below to check returned value
         ***************************************************/
//		if (userInfo != null) {
//			System.out.println(userInfo[0]);
//			System.out.println(userInfo[1]);
//		} else {
//			System.out.println("User not found");
//		}
        return;
    }
}
