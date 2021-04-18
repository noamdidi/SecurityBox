<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Scans.aspx.cs" Inherits="SBoxGUI.Scans" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">

<head runat="server">
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            background-color: lightgrey;
        }

        * {
            box-sizing: border-box;
        }

        /* Add padding to containers */
        .container {
            padding: 16px;
            background-color: white;
        }

        .center {
            margin-left: auto;
            margin-right: auto;
        }

        /* Full-width input fields */
        input[type=text], input[type=password] {
            width: 100%;
            padding: 15px;
            margin: 5px 0 22px 0;
            display: inline-block;
            border: none;
            background: #f1f1f1;
        }

            input[type=text]:focus, input[type=password]:focus {
                background-color: #ddd;
                outline: none;
            }

        /* Overwrite default styles of hr */
        hr {
            border: 1px solid #f1f1f1;
            margin-bottom: 25px;
        }

        /* Set a style for the submit button */
        .btn {
            background-color: #06C258;
            color: white;
            padding: 16px 20px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 100%;
            opacity: 0.9;
        }

            .btn:hover {
                opacity: 1;
            }

        .menu_btn {
            background-color: #29AB87;
            color: white;
            padding: 16px 20px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 100%;
            opacity: 0.9;
        }

            .menu_btn:hover {
                opacity: 1;
            }

        /* Add a blue text color to links */
        a {
            color: dodgerblue;
        }

        /* Set a grey background color and center the text of the "sign in" section */
        .switch {
            background-color: #f1f1f1;
            text-align: center;
        }

        .table_desg {
            font-family: Arial, Helvetica, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }

        .table_desg td, #table_desg th {
            border: 1px solid #ddd;
            padding: 8px;
        }

        .table_desg tr:nth-child(even){background-color: #f2f2f2;}

        .table_desg tr:hover {background-color: #ddd;}

        .table_desg th {
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: left;
            background-color: #4CAF50;
            color: white;
        }
        

        #general_tbl {
            font-family: Arial, Helvetica, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }

        #general_tbl td, #customers th {
            border: 1px solid #ddd;
            padding: 8px;
        }

        #general_tbl tr:nth-child(even){background-color: #f2f2f2;}

        #general_tbl tr:hover {background-color: #ddd;}

        #general_tbl th {
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: left;
            background-color: #4CAF50;
            color: white;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div class="container">
            <table class="table_desg">
                <tr>
                    <td>EVIL TWIN</td>
                    <td width="500px"><asp:Button ID="run_et" class="btn" runat="server" Text="Detect" OnClick="run_et_Click" /></td>
                    <asp:PlaceHolder ID="et_wfr" runat="server"></asp:PlaceHolder>
                    <asp:PlaceHolder ID="et_res" runat="server"></asp:PlaceHolder>
                
                </tr>
            </table>
            <br />

            <table class="table_desg">
                <tr>
                    <td>MAN IN THE MIDDLE</td>
                    <td width="500px"><asp:Button ID="run_mitm" class="btn" runat="server" Text="Detect" OnClick="run_mitm_Click" /></td>
                    <asp:PlaceHolder ID="mitm_wfr" runat="server"></asp:PlaceHolder>
                    <asp:PlaceHolder ID="mitm_res" runat="server"></asp:PlaceHolder>
                </tr>
            </table>
            <br />

            <table class="table_desg">
                <tr>
                    <td>DNS SPOOFING</td>
                    <td width="500px"><asp:Button ID="run_dns" class="btn" runat="server" Text="Detect" OnClick="run_dns_Click" /></td>
                    <asp:PlaceHolder ID="dns_wfr" runat="server"></asp:PlaceHolder>
                    <asp:PlaceHolder ID="dns_res" runat="server"></asp:PlaceHolder>
                </tr>
            </table>
            <br />

            <table class="table_desg">
                <tr>
                    <td>DHCP SPOOFING</td>
                    <td width="500px"><asp:Button ID="run_dhcp" class="btn" runat="server" Text="Detect" OnClick="run_dhcp_Click" /></td>
                    <asp:PlaceHolder ID="dhcp_wfr" runat="server"></asp:PlaceHolder>
                    <asp:PlaceHolder ID="dhcp_res" runat="server"></asp:PlaceHolder>
                </tr>
            </table>
            <br />

            <table class="table_desg">
                <tr>
                    <td>ARP SPOOFING</td>
                    <td width="500px"><asp:Button ID="run_arp" class="btn" runat="server" Text="Detect" OnClick="run_arp_Click" /></td>
                    <asp:PlaceHolder ID="arp_wfr" runat="server"></asp:PlaceHolder>
                    <asp:PlaceHolder ID="arp_res" runat="server"></asp:PlaceHolder>
                </tr>
            </table>
        </div>
    </form>
</body>
</html>
