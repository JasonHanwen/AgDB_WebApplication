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
    public partial class Login : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
        
        }
        //When the button is clicked, get the linkCode, insert one record into our databse and then send one email to user to verify their identity
        protected void submitButton_Click(object sender, EventArgs e)
        {
            String linkCode = generateNewID();
            String emailAddress = Email.Text;
            insertInTable(emailAddress, linkCode);
            sendEmail(emailAddress, linkCode);
        }

        //Get the Link For User
        public String generateNewID()
        {
            Guid theVerificationCode;
            theVerificationCode = Guid.NewGuid();
            return theVerificationCode.ToString();
        }

        //Insert into database table about this record
        public void insertInTable(string emailAddress, string linkCode){
            
            string ipAddress = Request.UserHostAddress;
            DataTable dataTable = new DataTable();
            string _localConnStr = WebConfigurationManager.ConnectionStrings["LocalConnectionString"].ConnectionString;
            using (SqlConnection conn = new SqlConnection(_localConnStr))
            {   
                //Insert record in the database
                conn.Open();
                StringBuilder StringBuilder = new StringBuilder("INSERT dbo.EmailIpTable (EMAIL, IP, LinkCode Set) VALUES(@EMAIL, @IP, @LinkCode, @Set)");
                string command = StringBuilder.ToString();
                SqlCommand mycommand = new SqlCommand(command);
                mycommand.Connection = conn;
                mycommand.Parameters.AddWithValue("@Email", emailAddress);
                mycommand.Parameters.AddWithValue("@Ip", ipAddress);
                mycommand.Parameters.AddWithValue("@LinkCode", linkCode);
                mycommand.Parameters.AddWithValue("@Set", true);
                SqlDataAdapter sqlDA = new SqlDataAdapter(mycommand);
                sqlDA.SelectCommand.CommandTimeout = 300;
                sqlDA.Fill(dataTable);
                conn.Close();
            }
        }

        //Send Email from preDefined Email address
        public void sendEmail(String emailAddress, String linkCode){
 
            string EmailLink = "http://localhost:56060/Verify.aspx?code=" + linkCode;

            String fromEmail = "agdbofwoodard@gmail.com";

            //and push the link into the database and the email address and the IP of the request
            var client = new SmtpClient("smtp.gmail.com", 587)
            {
                Credentials = new NetworkCredential(fromEmail, "Nankaiee2015"),
                EnableSsl = true
            };
            //client.Send("agdbofwoodard@gmail.com", "hw544@cornell.edu", "test", "testbody");
            String testBody = String.Format("Please verified your EMail Address on AgBD becuase you have hit the limit of query number, Please click here" + EmailLink);
            client.Send(fromEmail, emailAddress, "test", testBody);
            Console.WriteLine("Sent the verify email to" + emailAddress);
        }
    }
}