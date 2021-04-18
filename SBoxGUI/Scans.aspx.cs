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
    public partial class Scans : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        protected void run_et_Click(object sender, EventArgs e)
        {
            StringBuilder wfr_txt = new StringBuilder();
            wfr_txt.Append("<th style=\"background-color:lightgray\">");
            wfr_txt.Append("Waiting for Results...");
            wfr_txt.Append("</th>");
            et_wfr.Controls.Add(new Literal { Text = wfr_txt.ToString() });

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
            html.Append("</th>");
            Thread.Sleep(5000);
            et_res.Controls.Add(new Literal { Text = html.ToString() });
        }

        protected void run_mitm_Click(object sender, EventArgs e)
        {
            StringBuilder wfr_txt = new StringBuilder();
            wfr_txt.Append("<th style=\"background-color:lightgray\">");
            wfr_txt.Append("Waiting for Results...");
            wfr_txt.Append("</th>");
            mitm_wfr.Controls.Add(new Literal { Text = wfr_txt.ToString() });

            TcpClient tcpclnt = new TcpClient();
            tcpclnt.Connect("127.0.0.1", 447);

            String str = "5#0";
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
            if (recv_msg.Contains("attack"))
            {
                html.Append("<th style=\"background-color:red\">");
                html.Append(recv_msg);
            }
            else
            {
                html.Append("<th style=\"background-color:springgreen\">");
                html.Append("Everything's OK");
            }
            html.Append("</th>");
            mitm_res.Controls.Add(new Literal { Text = html.ToString() });
        }

        protected void run_dns_Click(object sender, EventArgs e)
        {
            StringBuilder wfr_txt = new StringBuilder();
            wfr_txt.Append("<th style=\"background-color:lightgray\">");
            wfr_txt.Append("Waiting for Results...");
            wfr_txt.Append("</th>");
            dns_wfr.Controls.Add(new Literal { Text = wfr_txt.ToString() });

            TcpClient tcpclnt = new TcpClient();
            tcpclnt.Connect("127.0.0.1", 447);

            String str = "6#0";
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
            if (recv_msg.Contains("DETECT"))
            {
                html.Append("<th style=\"background-color:red\">");
                html.Append(recv_msg);
            }
            else
            {
                html.Append("<th style=\"background-color:springgreen\">");
                html.Append("Everything's OK");
            }
            html.Append("</th>");
            dns_res.Controls.Add(new Literal { Text = html.ToString() });
        }

        protected void run_dhcp_Click(object sender, EventArgs e)
        {
            StringBuilder wfr_txt = new StringBuilder();
            wfr_txt.Append("<th style=\"background-color:lightgray\">");
            wfr_txt.Append("Waiting for Results...");
            wfr_txt.Append("</th>");
            dhcp_wfr.Controls.Add(new Literal { Text = wfr_txt.ToString() });

            TcpClient tcpclnt = new TcpClient();
            tcpclnt.Connect("127.0.0.1", 447);

            String str = "7#0";
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
            if (recv_msg.Contains("WARNING") || recv_msg.Contains("error"))
            {
                if(recv_msg.Contains("error"))
                {
                    html.Append("<th style=\"background-color:red\">");
                    html.Append("Error - detection failed");
                }
                else
                {
                    html.Append("<th style=\"background-color:red\">");
                    html.Append(recv_msg);
                }
            }
            else
            {
                html.Append("<th style=\"background-color:springgreen\">");
                html.Append("Everything's OK");
            }
            html.Append("</th>");
            dhcp_res.Controls.Add(new Literal { Text = html.ToString() });
        }

        protected void run_arp_Click(object sender, EventArgs e)
        {
            StringBuilder wfr_txt = new StringBuilder();
            wfr_txt.Append("<th style=\"background-color:lightgray\">");
            wfr_txt.Append("Waiting for Results...");
            wfr_txt.Append("</th>");
            arp_wfr.Controls.Add(new Literal { Text = wfr_txt.ToString() });

            TcpClient tcpclnt = new TcpClient();
            tcpclnt.Connect("127.0.0.1", 447);

            String str = "8#0";
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
            if (recv_msg.Contains("ok"))
            {
                html.Append("<th style=\"background-color:springgreen\">");
                html.Append("Everything's OK");
            }
            else
            {
                html.Append("<th style=\"background-color:red\">");
                html.Append("unknown error occured: sniff failed");
            }
            html.Append("</th>");
            arp_res.Controls.Add(new Literal { Text = html.ToString() });
        }
    }
}