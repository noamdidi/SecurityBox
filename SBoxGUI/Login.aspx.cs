using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data.SqlClient;
using System.Configuration;
using System.Drawing;

namespace SBoxGUI
{
    public partial class Login : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            
        }

        protected void signin_Click1(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection(@"Data Source=.\SQLEXPRESS;AttachDbFilename=App_Data\users.mdf;Integrated Security=True;User Instance=True;");
            con.Open();
            SqlCommand cmd = new SqlCommand("SELECT COUNT (*) FROM usersTable WHERE username='" + username.Text + "' AND password='" + password.Text + "'");
            cmd.Connection = con;
            int OBJ = Convert.ToInt32(cmd.ExecuteScalar());
            if (OBJ > 0)
            {
                Session["name"] = username.Text;
                Response.Redirect("LandingPage.aspx");
            }
            else
            {
                username.Text = "Invalid username or password";
                this.username.ForeColor = Color.Red;
            }
        }

        //protected void LinkButton2_Click(object sender, EventArgs e)
        //{
        //    Response.Redirect("Registration.aspx");
        //}
    }
    
}