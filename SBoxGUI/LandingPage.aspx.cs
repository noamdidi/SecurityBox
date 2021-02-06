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
    public partial class LandingPage : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            //user.Text = Session["name"].ToString();

            TcpClient tcpclnt = new TcpClient();
            tcpclnt.Connect("127.0.0.1", 447);

            String str = "3#0";
            Stream stm = tcpclnt.GetStream();

            ASCIIEncoding asen = new ASCIIEncoding();
            byte[] ba = asen.GetBytes(str);
            stm.Write(ba, 0, ba.Length);
            byte[] bb = new byte[1000];
            int k = stm.Read(bb, 0, 1000);
            string recv_msg = "";

            for (int i = 0; i < k; i++)
                recv_msg += Convert.ToChar(bb[i]);

            //Console.WriteLine(recv_msg);
            string[] headers = {"#", "IP Number", "Mac Address", "Manifacturer"};
            string data = recv_msg;
            string[] data_org = data.Split('#');
            //Building an HTML string.
            StringBuilder html = new StringBuilder();

            //Table start.
            html.Append("<table class=\"center\" border = '1'>");

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
            
            int count = 0;
            for(int i=0; i < (data_org.Length)/3; i++)
            {
                html.Append("<tr>");
                html.Append("<td>");
                html.Append(i+1);
                html.Append("</td>");
                html.Append("<td>");
                html.Append(data_org[count]);
                html.Append("</td>");
                html.Append("<td>");
                html.Append(data_org[count + 1]);
                html.Append("</td>");
                html.Append("<td>");
                html.Append(data_org[count + 2]);
                html.Append("</td>");
                html.Append("<tr>");
                
                count += 3;
            }

            //Table end.
            html.Append("</table>");

            //Append the HTML string to Placeholder.
            devices_tbl.Controls.Add(new Literal { Text = html.ToString() });
        }

        protected void run_et_Click(object sender, EventArgs e)
        {
            StringBuilder wfr_txt = new StringBuilder();
            wfr_txt.Append("<th style=\"background-color:lightgray\">");
            wfr_txt.Append("Waiting for Results...");
            wfr_txt.Append("</th>");
            et_res.Controls.Add(new Literal { Text = wfr_txt.ToString() });
            
            TcpClient tcpclnt = new TcpClient();
            tcpclnt.Connect("127.0.0.1", 447);

            String str = "4#0";
            Stream stm = tcpclnt.GetStream();

            ASCIIEncoding asen = new ASCIIEncoding();
            byte[] ba = asen.GetBytes(str);
            stm.Write(ba, 0, ba.Length);
            byte[] bb = new byte[1000];
            int k = stm.Read(bb, 0, 1000);
            string recv_msg = "";

            for (int i = 0; i < k; i++)
                recv_msg += Convert.ToChar(bb[i]);

            StringBuilder html = new StringBuilder();
            if (recv_msg.Contains("OK"))
            {
                html.Append("<th style=\"background-color:springgreen\">");
            }
            else
            {
                html.Append("<th style=\"background-color:red\">");
            }
            html.Append(recv_msg);
            html.Append("</th");
            et_res.Controls.Add(new Literal { Text = html.ToString() });
        }
    }
}