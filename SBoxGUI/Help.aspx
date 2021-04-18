<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Help.aspx.cs" Inherits="SBoxGUI.Help" %>

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
            <h3><b>Evil Twin</b></h3>
            <h5>
                An evil twin is a fraudulent Wi-Fi access point that appears to be legitimate but is set up to eavesdrop on wireless communications. The evil twin is the wireless LAN equivalent of the phishing scam.
                This type of attack may be used to steal the passwords of unsuspecting users, either by monitoring their connections or by phishing, which involves setting up a fraudulent web site and luring people there.
            </h5>
            <h5>You can learn more about this attack here:</h5><a style=href="https://en.wikipedia.org/wiki/Evil_twin_(wireless_networks)">evil twin attack</a>
            <br />
            <h3><b>Man in the Middle</b></h3>
            <h5>
                Man in the Middle is a cyberattack where the attacker secretly relays and possibly alters the communications between two parties who believe that they are directly communicating with each other. 
                One example of a MITM attack is active eavesdropping, in which the attacker makes independent connections with the victims and relays messages between them to make them believe they are talking directly to each other over a private connection, when in fact the entire conversation is controlled by the attacker.
            </h5>
            <h5>You can learn more about this attack here:</h5><a style=href="https://en.wikipedia.org/wiki/Man-in-the-middle_attack">man in the middle attack</a>
            <br />
            <h3><b>DNS Spoofing</b></h3>
            <h5>
                DNS spoofing is a form of computer security hacking in which corrupt Domain Name System data is introduced into the DNS resolver's cache, causing the name server to return an incorrect result record, e.g. an IP address. 
                This results in traffic being diverted to the attacker's computer (or any other computer).
            </h5>
            <h5>You can learn more about this attack here:</h5><a style=href="https://en.wikipedia.org/wiki/DNS_spoofing">DNS spoofing attack</a>
            <br />
            <h3><b>DHCP Spoofing</b></h3>
            <h5>
                DHCP spoofing occurs when an attacker attempts to respond to DHCP requests and trying to list themselves (spoofs) as the default gateway or DNS server, hence, initiating a man in the middle attack.
            </h5>
            <h5>You can learn more about this attack here:</h5><a style=href="https://he.wikipedia.org/wiki/%D7%94%D7%95%D7%A0%D7%90%D7%AA_DHCP">DHCP spoofing attack</a>
            <br />
            <h3><b>ARP Spoofing</b></h3>
            <h5>
                ARP spoofing is a technique by which an attacker sends (spoofed) Address Resolution Protocol (ARP) messages onto a local area network. 
                Generally, the aim is to associate the attacker's MAC address with the IP address of another host, such as the default gateway, causing any traffic meant for that IP address to be sent to the attacker instead.
            </h5>
            <h5>You can learn more about this attack here:</h5><a style=href="https://en.wikipedia.org/wiki/ARP_spoofing">ARP spoofing attack</a>
            <br />
            
        </div>
    </form>
</body>
</html>
