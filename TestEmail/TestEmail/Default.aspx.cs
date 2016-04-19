using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace TestEmail
{
    public partial class _Default : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            //check the database 
            String localConnection = new String();
            int number = 0;
            using (localConnection)
            {
                //connect read the records from database
            }

            if (number < 5)
            {
                //run the query
            }
            else { 
                //verify if the user has been verified

                Boolean ifVerified = false;
                using (localConnection) { 
                   //check if the user has been verified
                    if (ifVerified)
                    {
                        //run the Query
                    }
                    else { 
                        //jump to the sendEmail Page, redirect the request to the verified page.s
                        Response.Redirect("/login", true);
                    }
                }
            }
           
        }

        protected void Application_BeginRequest(object sender, EventArgs e) {
            this.Response.Write("hello user, this is your first request");
            this.Response.StatusCode = 200;
            this.Response.ContentType = "text/plain";

            this.Response.End();
        }

    }
}