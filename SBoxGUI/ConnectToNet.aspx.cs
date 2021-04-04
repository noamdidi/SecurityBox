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

namespace SBoxGUI
{
    public partial class ConnectToNet : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            //user.Text = Session["name"].ToString();

            TcpClient tcpclnt = new TcpClient();
            tcpclnt.Connect("127.0.0.1", 447);

            String str = "1#0";
            Stream stm = tcpclnt.GetStream();

            ASCIIEncoding asen = new ASCIIEncoding();
            byte[] ba = asen.GetBytes(str);
            stm.Write(ba, 0, ba.Length);
            byte[] bb = new byte[1000];
            int k = stm.Read(bb, 0, 1000);
            string recv_msg = "";

            for (int j = 0; j < k; j++)
                recv_msg += Convert.ToChar(bb[j]);

            string[] headers = { "SSID Number", "Network Name", "Select" };
            
            string data = recv_msg;
            string[] data_org = data.Split('#');
            
            //Building an HTML string.
            StringBuilder html = new StringBuilder();

            //Table start.
            html.Append("<table id=\"table_desg\">");

            //Building the Header row.
            html.Append("<tr>");
            foreach (string header in headers)
            {
                html.Append("<th>");
                html.Append(header);
                html.Append("</th>");
            }
            html.Append("</tr>");

            //Building the Data rows.
            int i = 1;
            foreach (string word in data_org)
            {
                html.Append("<tr>");
                html.Append("<td>");
                html.Append(i);
                html.Append("</td>");
                html.Append("<td>");
                html.Append(word);
                html.Append("</td>");
                html.Append("<td>");
                html.Append("<input type = \"radio\" id = \"" + word + "\" name = \"" + "network" + "\" value = \"" + i + "\" >");
                html.Append("</td>");
                html.Append("<tr>");
                i++;
            }

            //Table end.
            html.Append("</table>");

            //Append the HTML string to Placeholder.
            NetworksTable.Controls.Add(new Literal { Text = html.ToString() });
        }
        

        protected void connnect_Click(object sender, EventArgs e)
        {
            
            String net = "0";
            if (Request.Form["network"] != null)
            {
                net = Request.Form["network"].ToString();
            }

            TcpClient tcpclnt = new TcpClient();
            tcpclnt.Connect("127.0.0.1", 447);

            String str = "2#";
            str += net;
            Stream stm = tcpclnt.GetStream();

            ASCIIEncoding asen = new ASCIIEncoding();
            byte[] ba = asen.GetBytes(str);
            stm.Write(ba, 0, ba.Length);
            byte[] bb = new byte[1000];
            int k = stm.Read(bb, 0, 1000);
            string recv_msg = "";

            for (int j = 0; j < k; j++)
                recv_msg += Convert.ToChar(bb[j]);

            Response.Redirect("LandingPage.aspx");
            
        }
    }
}