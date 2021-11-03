/******************************************************************************
 * Title: 				Login simple
 * Author: 			    Youssif Al-Nashif
 * Email: 				yalnashif@floridapoly.edu
 * Package: 				Login
 * Version: 				0.0.1a
 * Creation Date: 		Oct. 15, 2017 @ 22:07
 * Modification Date: 	Oct. 15, 2017 @ 22:07
 * Description: 			Login class
 ******************************************************************************/

package login;

import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import java.security.SecureRandom;
import java.sql.*;
import java.util.Base64;

public class loginSQLiteDB {
	
	
    /***************************************************
     * Create Database
     ***************************************************/
	public static void createSQLiteDB(String filename) {

		String URL = "jdbc:sqlite:" + filename;
		try {
			Connection conn = DriverManager.getConnection(URL);
			if (conn != null) {
				// DatabaseMetaData meta = conn.getMetaData();
				conn.close();
			}

		} catch (SQLException e) {
			System.out.println("Error creating the database.");
			System.exit(1);
		}
	}

	/***************************************************
     * Create Users table in the database
     ***************************************************/
	public static void createSQLiteLoginTable(String filename) {
		String URL = "jdbc:sqlite:" + filename;
		Connection conn = null;
		Statement stmt = null;
		String sqlcommand = "CREATE TABLE IF NOT EXISTS USERS (" + "FIRST_NAME CHAR(32) NOT NULL,"
				+ "LAST_NAME CHAR(32) NOT NULL," + "USERNAME CHAR(32) NOT NULL," + "SALT CHAR(128) NOT NULL,"
				+ "PASSHASH CHAR(128) NOT NULL)";
		try {
			conn = DriverManager.getConnection(URL);
			stmt = conn.createStatement();
			stmt.executeUpdate(sqlcommand);
			stmt.close();
			conn.close();
		} catch (SQLException e) {
			System.err.println(e.getClass().getName());
			System.out.println("Error opening the database.");
			System.exit(1);
		}
	}

	public static void createSQLiteLoginUser(String filename, String firstName, String lastName, String username,
			String password) {
		String URL = "jdbc:sqlite:" + filename;
		byte[] salt = new byte[16];
		Connection conn = null;
		Statement stmt = null;
		String sqlcommand = "";
		try {
			SecureRandom sr = SecureRandom.getInstance("SHA1PRNG");
			sr.nextBytes(salt);
			conn = DriverManager.getConnection(URL);
			stmt = conn.createStatement();
			PBEKeySpec spec = new PBEKeySpec(password.toCharArray(), salt, 65536, 128);
			SecretKeyFactory skey = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1");
			byte[] hash = skey.generateSecret(spec).getEncoded();
			sqlcommand = "INSERT into users values('" + firstName + "','" + lastName + "','" + username + "','"
					+ Base64.getEncoder().encodeToString(salt) + "', '" + Base64.getEncoder().encodeToString(hash)
					+ "');";
			stmt.executeUpdate(sqlcommand);
			stmt.close();
			conn.close();

		} catch (Exception e) {
			System.out.println("Error opening the database.");
			System.exit(1);
		}
	}

	
    /***************************************************
     * Authentication
     ***************************************************/	
	public static String[] checkSQLiteLoginUser(String filename, String username, String password) {
		// System.out.println(username+" ---- "+password);
		String URL = "jdbc:sqlite:" + filename;
		byte[] salt = new byte[16];
		Connection conn = null;
		Statement stmt = null;
		ResultSet rst = null;
		String sqlcommand = "";
		try {
			conn = DriverManager.getConnection(URL);
			stmt = conn.createStatement();
			sqlcommand = "select * from USERS where USERNAME='" + username + "';";
			rst = stmt.executeQuery(sqlcommand);
			while (rst.next()) {
				salt = Base64.getDecoder().decode(rst.getString("SALT"));
				PBEKeySpec spec = new PBEKeySpec(password.toCharArray(), salt, 65536, 128);
				SecretKeyFactory skey = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1");
				byte[] hash = skey.generateSecret(spec).getEncoded();
				if ((Base64.getEncoder().encodeToString(hash)).equals(rst.getString("PASSHASH"))) {
					String[] myReturnString = new String[2];
					myReturnString[0] = rst.getString("FIRST_NAME");
					myReturnString[1] = rst.getString("LAST_NAME");
					rst.close();
					stmt.close();
					conn.close();
					return myReturnString;
				}
			}
			stmt.close();
			conn.close();

		} catch (Exception e) {
			System.out.println("Error opening the database.");
			System.exit(1);
		}
		return null;
	}

}