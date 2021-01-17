<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Register.aspx.cs" Inherits="SBoxGUI.Register" %>

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
    </style>
</head>
<body>
    <form id="register_form" runat="server">
        <asp:ScriptManager ID="registersm" runat="server"></asp:ScriptManager>
        <div class="container">
            <h1>Register</h1>
            <p>Please fill in this form to create an account.</p>
            <hr />

            <asp:Label ID="username_label" runat="server" Text="Username"><b>Username</b></asp:Label>
            <br />
            <asp:TextBox ID="username" runat="server"></asp:TextBox>

            <asp:Label ID="password_label" runat="server" Text="Password"><b>Password</b></asp:Label>
            <br />
            <asp:TextBox ID="password" runat="server"></asp:TextBox>

            <asp:Label ID="rpassword_label" runat="server" Text="Repeat Password"><b>Repeat Password</b></asp:Label>
            <br />
            <asp:TextBox ID="rpassword" runat="server"></asp:TextBox>
            
            <hr />
            <p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p>

            <hr />

            <asp:Button ID="register" class="btn" runat="server" Text="Register" />

            <div class="container switch">
            <p>Already Have an Account? <a href="Login.aspx">Sign In</a>.</p>
        </div>
    </form>
</body>
</html>
