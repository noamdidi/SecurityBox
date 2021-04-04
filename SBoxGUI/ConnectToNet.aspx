<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="ConnectToNet.aspx.cs" Inherits="SBoxGUI.ConnectToNet" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Security Box</title>
    <link rel="shortcut icon" type="image/ico" href="App_Data/favicon.ico"/>
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
            background-color: #16B21D;
            color: white;
            padding: 16px 20px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 100%;
            opacity: 0.9;
        }

            .registerbtn:hover {
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

        .loader {  
                    border: 16px solid #f3f3f3;  
                    border-radius: 50%;  
                    border-top: 16px solid #95CE67;  
                    border-bottom: 16px solid #8DBF8B;  
                    width: 120px;  
                    height: 120px;  
                    -webkit-animation: spin 2s linear infinite;  
                    animation: spin 2s linear infinite;  
                }  
  
        @-webkit-keyframes spin {  
            0% { -webkit-transform: rotate(0deg); }  
            100% { -webkit-transform: rotate(360deg); }  
        }  
  
        @keyframes spin {  
            0% { transform: rotate(0deg); }  
            100% { transform: rotate(360deg); }  
        }  

        #table_desg {
            font-family: Arial, Helvetica, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }

        #table_desg td, #table_desg th {
            border: 1px solid #ddd;
            padding: 8px;
        }

        #table_desg tr:nth-child(even){background-color: #f2f2f2;}

        #table_desg tr:hover {background-color: #ddd;}

        #table_desg th {
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
            <h1 style="text-align:center">Available Networks</h1>
            <asp:PlaceHolder ID="NetworksTable" runat="server" />
            <h5 style="color:red; text-align:center" >Note: connecting might take a while, we need to get all the information on the network</h5>
            <hr />
            <asp:Button ID="connect" class="btn" runat="server" Text="Connect" OnClick="connnect_Click" />
          
        </div>
    </form>
</body>
</html>
