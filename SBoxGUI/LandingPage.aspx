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
            background-color: #16B21D;
            color: white;
            padding: 16px 20px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 50%;
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
                    border-radius: 100%;  
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
    </style>
</head>
    
<body>
    <form id="form1" runat="server">
        <div class="container">
            <h1>Hooray! You have successfully joined the network!</h1>
            <br />

            <h4>Run Evil Twin Detection:</h4>
            <table class="center" border = '1' width="50%">
                <tr>
                    <th><asp:Button ID="run_et" class="btn" runat="server" Text="Run" OnClick="run_et_Click" /></th>
                    <asp:PlaceHolder ID="et_res" runat="server"></asp:PlaceHolder>
                </tr>
            </table>

            <h1 style="text-align:center">Devices</h1>
            <asp:Label ID="user" runat="server"></asp:Label>
            <br />
            <asp:PlaceHolder ID="devices_tbl" runat="server" />
        </div>
        
    </form>
</body>
</html>
