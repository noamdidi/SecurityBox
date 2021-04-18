<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Devices.aspx.cs" Inherits="SBoxGUI.devices" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
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
            <h1 style="text-align:center">Devices</h1>
            <asp:Label ID="user" runat="server"></asp:Label>
            <br />
            <asp:Button ID="find_devices" class="btn" runat="server" Text="Find Devices" OnClick="find_devices_Click" />
            <asp:PlaceHolder ID="devices_tbl" runat="server" />
        </div>
        
    </form>
</body>
</html>
