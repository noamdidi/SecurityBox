<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="LandingPage.aspx.cs" Inherits="SBoxGUI.LandingPage" %>

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
            <img src="SecurityBox.png" alt="Logo" style="width:200px;height:100px;">
            <br /><br /><br />
            <table id="menu" width="100%">
                <tr>
                    <th><asp:Button ID="find_devices_1" class="menu_btn" runat="server" Text="Find Devices" OnClick="find_devices_1_Click" /></th>
                    <th><asp:Button ID="scans"          class="menu_btn" runat="server" Text="Scans"        OnClick="scans_Click" /></th>
                    <th><asp:Button ID="user_info"      class="menu_btn" runat="server" Text="User Info"    OnClick="user_info_Click" /></th>
                    <th><asp:Button ID="logs"           class="menu_btn" runat="server" Text="Logs"         OnClick="logs_Click" /></th>
                    <th><asp:Button ID="help"           class="menu_btn" runat="server" Text="Help"         OnClick="help_Click" /></th>
                    <th><asp:Button ID="contact"        class="menu_btn" runat="server" Text="Contact"      OnClick="contact_Click" /></th>
                </tr>
            </table>
            <h1 style="vertical-align:central">Hooray! You have successfully joined the network!</h1>
            <br />

            <table class="table_desg">
                <tr>
                    <td>EVIL TWIN</td>
                    <td><asp:Button ID="run_et" class="btn" runat="server" Text="Detect" OnClick="run_et_Click" /></td>
                    <asp:PlaceHolder ID="waiting_for_results" runat="server"></asp:PlaceHolder>
                    <asp:PlaceHolder ID="et_res" runat="server"></asp:PlaceHolder>
                
                </tr>
                <tr>
                    <%--<td>MAN IN THE MIDDLE</td>
                    <td><asp:Button ID="run_mitm" class="btn" runat="server" Text="Detect" OnClick="run_mitm_Click" /></td>
                    <asp:PlaceHolder ID="mitm_res" runat="server"></asp:PlaceHolder>--%>
                </tr>
            </table>

            <h1 style="text-align:center">Devices</h1>
            <asp:Label ID="user" runat="server"></asp:Label>
            <br />
            <asp:Button ID="find_devices" class="btn" runat="server" Text="Find Devices" OnClick="find_devices_Click" />
            <asp:PlaceHolder ID="devices_tbl" runat="server" />
        </div>
        
    </form>
</body>
</html>
