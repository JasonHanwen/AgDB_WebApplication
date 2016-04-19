using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.Configuration;
using System.Data.SqlClient;
using System.Text;
using System.Data;

namespace TestEmail
{
    public partial class welcome : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        public void page_Load(){

            DataTable dataTable = new DataTable();

            int queryNum = 0;
            Boolean set = false;

            String IpAddress = Request.UserHostAddress;
  
            string _localConnStr = WebConfigurationManager.ConnectionStrings["LocalConnectionString"].ConnectionString;
            using (SqlConnection conn = new SqlConnection(_localConnStr))
            {
                //Insert record in the database
                conn.Open();
                StringBuilder StringBuilder = new StringBuilder("SELECT * FRPM dbo.IPTrafficTable Where IP = @Ip");
                string command = StringBuilder.ToString();
                SqlCommand mycommand = new SqlCommand(command);
                mycommand.Connection = conn;
                mycommand.Parameters.AddWithValue("@Ip", IpAddress);
                SqlDataAdapter sqlDA = new SqlDataAdapter(mycommand);
                sqlDA.SelectCommand.CommandTimeout = 300;
                sqlDA.Fill(dataTable);
                conn.Close();
            }
            queryNum = (int)dataTable.Rows[0]["Traffic"];

            set=(Boolean)dataTable.Rows[0]["Set"];

            if (queryNum > 10)
            {
                //Turn to the loginTable
                if (set)
                {
                    //run the query
                    Console.WriteLine("the user has been verified, so now run the query");
                }
                else
                {
                    //redircted to the verified page
                    Console.WriteLine("the user read the query limit, and now we need to turn to the logIn page");
                    //let the user to register its IP address.
                    Response.AddHeader("REFRESH", "2;URL=~/Login.aspx");
                }
            }
            else{ 
                //add the number to 1
                //and run the query

                using (SqlConnection conn = new SqlConnection(_localConnStr))
                {
                    conn.Open();
                    StringBuilder StringBuilder = new StringBuilder("SET dbo.IPTrafficTable Traffic = @traffic Where IP = @IP");
                    string command = StringBuilder.ToString();
                    SqlCommand mycommand = new SqlCommand(command);
                    mycommand.Connection = conn;
                    mycommand.Parameters.AddWithValue("@traffic", queryNum + 1);
                    mycommand.Parameters.AddWithValue("@Ip", IpAddress);
                    SqlDataAdapter sqlDA = new SqlDataAdapter(mycommand);
                    sqlDA.SelectCommand.CommandTimeout = 300;
                    sqlDA.Fill(dataTable);
                    conn.Close();
                }
            }
        }
    }
}