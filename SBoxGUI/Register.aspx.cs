using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data.SqlClient;
using System.Drawing;

namespace SBoxGUI
{
    public partial class Register : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            
        }
        protected void Username_TextChanged(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection(@"Data Source=.\\App_Data\\users.mdf;Integrated Security=True;User Instance=True;");
            con.Open();
            SqlCommand cmd = new SqlCommand("SELECT * FROM usersTable WHERE username='" + username.Text + "'", con);
            SqlDataReader dr = cmd.ExecuteReader();
            if (dr.Read())
            {
                username_label.Text = "Username is Already Exist";
                this.username_label.ForeColor = Color.Red;
            }
            else
            {
                username_label.Text = "Username is Available";
                this.username_label.ForeColor = Color.LightGreen;
            }
            con.Close();
        }
        protected void RegBtn_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection(@"Data Source=C:\\Users\\משתמש\\source\\repos\\SBoxGUI\\App_Data\\users.mdf;Integrated Security=True;User Instance=True;");
            con.Open();
            SqlCommand cmd = new SqlCommand("INSER INTO usersTable VALUES(@usn,@pwd)", con);
            cmd.Parameters.AddWithValue("usn", username.Text);
            cmd.Parameters.AddWithValue("pwd", password.Text);
            cmd.ExecuteNonQuery();
            Session["name"] = username.Text;
            Response.Redirect("LandingPage.aspx");
            con.Close();
            
        }
    }
}