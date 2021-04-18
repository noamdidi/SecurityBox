using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data;
using System.Text;
using System.Configuration;
using System.Data.SqlClient;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace SBoxGUI
{
    public partial class LandingPage : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            //user.Text = Session["name"].ToString();

        }

        protected void find_devices_redirect_Click(object sender, EventArgs e)
        {
            Response.Redirect("Devices.aspx");
        }

        protected void scans_redirect_Click(object sender, EventArgs e)
        {
            Response.Redirect("Scans.aspx");
        }

        protected void help_redirect_Click(object sender, EventArgs e)
        {
            Response.Redirect("Help.aspx");
        }

        protected void contact_redirect_Click(object sender, EventArgs e)
        {
            Response.Redirect("Contact.aspx");
        }

    }
}