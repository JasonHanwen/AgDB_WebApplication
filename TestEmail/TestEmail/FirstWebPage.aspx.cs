using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Net.Mail;
using System.Net;

namespace TestEmail
{
    public partial class FirstWebPage : System.Web.UI.Page
    {   //This is to to send a email
        protected void Page_Load(object sender, EventArgs e)
        {
            SendEmailtoContacts();
        }


        protected void SendEmailtoContacts()
        {

            var fromAddress = new MailAddress("agdbofwoodard@gmail.com", "From Name");
            var toAddress = new MailAddress("hw544@cornell.edu", "To Name");
            const string fromPassword = "Nankaiee2015";
            const string subject = "test";
            const string body = "Hey now!!";

            var smtp = new SmtpClient
            {
                Host = "smtp.gmail.com",
                Port = 587,
                EnableSsl = true,
                DeliveryMethod = SmtpDeliveryMethod.Network,
                Credentials = new NetworkCredential(fromAddress.Address, fromPassword),
                Timeout = 20000
            };
            using (var message = new MailMessage(fromAddress, toAddress)
            {
                Subject = subject,
                Body = body
            })
            {
                try
                {
                    smtp.Send(message);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.ToString());
                }
            }
            var client = new SmtpClient("smtp.gmail.com", 587)
            {
                Credentials = new NetworkCredential("agdbofwoodard@gmail.com", "Nankaiee2015"),
                EnableSsl = true
            };
            client.Send("agdbofwoodard@gmail.com", "hw544@cornell.edu", "test", "testbody");
            Console.WriteLine("Sent");
            Console.ReadLine();
        }

        public void generateNewID() {
            Guid theVerificationCode;
            theVerificationCode = Guid.NewGuid();
            
            //public the email in the database
            string theEmailLink = "http://localhost:56060/Verify.aspx?code=" + theVerificationCode;
        }
    }
}