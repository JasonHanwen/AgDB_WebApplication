using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Net.Mail;
using System.Net;
using System.Web.Configuration;
using System.Data.SqlClient;
using System.Text;
using System.Data;

namespace TestEmail
{
    public partial class verify : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            
        }
        protected void Application_BeginRequest(object sender, EventArgs e)
        {
            String linkCode = Request.QueryString["code"];
            setRecord(linkCode);
            information.InnerText = "your Email address has been verified";
            revert.InnerText = "you will be reqirected in 3 seconds ";
            Response.AddHeader("REFRESH", "5;URL=~/FirstWebPage.aspx");
            //Server.Transfer("FirstWebPage.aspx");
        }

        //set the record to make sure that the IP address has been verified 
        public void setRecord(String linkCode){
            string ipAddress = Request.UserHostAddress;
            DataTable dataTable = new DataTable();
            string _localConnStr = WebConfigurationManager.ConnectionStrings["LocalConnectionString"].ConnectionString;
            using (SqlConnection conn = new SqlConnection(_localConnStr))
            {
                //Insert record in the database
                conn.Open();
                StringBuilder StringBuilder = new StringBuilder("UPDATE dbo.EmailIpTable  SET Set = @Set Where Code = @code");
                string command = StringBuilder.ToString();
                SqlCommand mycommand = new SqlCommand(command);
                mycommand.Connection = conn;
                mycommand.Parameters.AddWithValue("@Code", linkCode);
                mycommand.Parameters.AddWithValue("@Set", true);
                SqlDataAdapter sqlDA = new SqlDataAdapter(mycommand);
                sqlDA.SelectCommand.CommandTimeout = 300;
                sqlDA.Fill(dataTable);
                conn.Close();
            }
            //also we need to update the traffic and IP table
            String IpAddress;

            using (SqlConnection conn = new SqlConnection(_localConnStr)) {
                {
                    //Insert record in the database
                    conn.Open();
                    StringBuilder StringBuilder = new StringBuilder("SELECT * FROM dbo.EmailIpTable WHERE Code = @code");
                    string command = StringBuilder.ToString();
                    SqlCommand mycommand = new SqlCommand(command);
                    mycommand.Connection = conn;
                    mycommand.Parameters.AddWithValue("@code", linkCode);
                    SqlDataAdapter sqlDA = new SqlDataAdapter(mycommand);
                    sqlDA.SelectCommand.CommandTimeout = 300;
                    sqlDA.Fill(dataTable);
                    conn.Close();
                }
            }


            IpAddress = dataTable.Rows[0]["IP"].ToString();

            using (SqlConnection conn = new SqlConnection(_localConnStr))
            {
                //Insert record in the database
                conn.Open();
                StringBuilder StringBuilder = new StringBuilder("UPDATE dbo.IPTrafficTable SET Set = @Set Where Ip = @Ip");
                string command = StringBuilder.ToString();
                SqlCommand mycommand = new SqlCommand(command);
                mycommand.Connection = conn;
                mycommand.Parameters.AddWithValue("@Ip", IpAddress);
                mycommand.Parameters.AddWithValue("@Set", true);
                SqlDataAdapter sqlDA = new SqlDataAdapter(mycommand);
                sqlDA.SelectCommand.CommandTimeout = 300;
                sqlDA.Fill(dataTable);
                conn.Close();
            }

        }
    }
}